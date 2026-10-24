# Candidate Submission: FDL Broken-Code Challenge

Hours spent: about 2.5 hours for the whole assessment, this challenge and the platform plan together (details in the root `README.md`)
AI tools used: Claude Code (Anthropic, Claude Opus) as pair programmer and reviewer. See "How AI was used and how I checked it" below.

**Result:** 8 defects fixed in `profitability.py`. The 5 supplied tests went from **1 passing to 5 passing**, with the
supplied test file left exactly as given (`diff` against the original zip shows no change). I added 22 edge-case
tests, so there are **27 tests and all pass**. Raw output: [test-results-before.txt](test-results-before.txt) and
[test-results-after.txt](test-results-after.txt).

## Defects

Baseline input from the supplied test: revenue 2000, miles 500, fuel $4/gal, 10 mpg, driver pay 400, tolls 50,
dispatch 10%, other 100, target margin 20%.

| ID | Observed failure | Root cause | Fix | Verification |
|---|---|---|---|---|
| D1 | Fuel cost 20,000 instead of 200 | `miles * mpg * fuel_price`: multiplied by mpg instead of dividing | `miles * fuel_price / mpg` | `test_normal_load` fuel = 200 |
| D2 | Dispatch fee 20,000 instead of 200 | `revenue * dispatch_pct`: the contract says the percent is 0-100, so the `/ 100` was missing | `revenue * dispatch_pct / 100` | `test_normal_load` fee = 200 |
| D3 | Margin was profit / total cost (a markup), not profit / revenue | Wrong denominator | `profit / revenue * 100` | `test_normal_load` margin = 52.5 |
| D4 | At zero revenue, margin is undefined; with D3 fixed it becomes `ZeroDivisionError` | No zero-revenue branch | Revenue 0: margin -100 when profit < 0 (contract sentinel), 0 when profit is also 0. Documented in the module docstring | `test_zero_revenue_margin`, `Margins.*` |
| D5 | Break-even 750 instead of 833.33 | It summed fixed costs but ignored the dispatch fee, which grows with the rate itself | Solve R - fixed - R*d = 0: `fixed / (1 - d/100)` | `test_normal_load` = 833.33; property test: charging the break-even rate gives profit within 0.01 of 0 |
| D6 | Suggested rate 937.50 (from the buggy break-even 750 / 0.8) instead of 1071.43; the target margin was not net of the dispatch fee | Grossed up only by the margin and did not take the dispatch % into account | Solve (R - fixed - R*d) / R = m: `fixed / (1 - (d + m)/100)`. Built from fixed costs, not from break-even, so the dispatch fee is not counted twice | `test_normal_load` = 1071.43; property test: charging it gives the target margin within 0.01 points |
| D7 | `mpg=0` accepted; negative driver pay/tolls/other accepted; margin 100 raised `ZeroDivisionError` instead of `ValueError`; percent > 100 gave negative rates; NaN passed every `< 0` check; `"100"` raised `TypeError`; `True` was treated as 1 | The validation only checked 4 of the 9 inputs, and only for `< 0` | One `_number` check on every input (real number, not bool, finite, not negative); mpg > 0; each percent < 100; dispatch + margin < 100. Everything invalid raises `ValueError` as the contract asks | `test_zero_mpg_rejected`, `test_negative_expense_rejected`, `test_invalid_margin_rejected`, `InvalidInputs.*` (all 9 params × negative, NaN, ±inf, bool, str, None), `Percentages.*` |
| D8 | Money rounding was off by a cent on some values: `round(2.675, 2)` gives 2.67 | `round()` on binary floats rounds half-to-even, and 2.675 is stored as 2.67499999... | Compute in `Decimal` (inputs converted through `str()` so 0.1 stays 0.1), round each output once to cents with halves away from zero. Values are still returned as floats so the supplied tests and JSON keep working | `Rounding.*`, `InputTypes.test_decimal_cents_not_float_noise` |

D1 to D7 break the written contract. D8 is a judgement call: the contract says "two decimal places" without naming a
rounding mode. I treated it as a defect because this is money, and the FDL master sheet asks for "decimal-safe money
handling, and explicit rounding rules". The owner should confirm half-up.

Two more hardening fixes came out of the independent review:
- A tiny loss (charging exactly the displayed 833.33 break-even loses $0.003) printed `-0.0`, which is confusing in
  a UI and in JSON. It now prints `0.0`.
- An amount of about 1e27 or more can't be held to the cent in Decimal's 28 digits. That raised an internal
  `decimal.InvalidOperation`. It now raises a clear `ValueError`.

## Test execution

```
$ python -m unittest -v        # original code, supplied tests
Ran 5 tests in 0.003s
FAILED (failures=3, errors=1)  # only test_zero_revenue_margin passed, and only by accident (it divided by cost)

$ python -m unittest -v        # fixed code, supplied tests unchanged + test_profitability_edge.py
Ran 27 tests in 0.004s
OK
```

Python 3.15.0, standard library only. Full verbose output is in the two `test-results-*.txt` files.

Correctness proof for the baseline load (hand-checked, matches the supplied expected values):

| Field | Working | Result |
|---|---|---|
| Fuel | 500 / 10 × 4 | 200.00 |
| Dispatch fee | 2000 × 10 / 100 | 200.00 |
| Fixed costs | 200 + 400 + 50 + 100 | 750.00 |
| Total cost | 750 + 200 | 950.00 |
| Profit | 2000 − 950 | 1050.00 |
| Margin | 1050 / 2000 × 100 | 52.50 |
| Break-even | 750 / (1 − 0.10) | 833.33 |
| Suggested (20% net) | 750 / (1 − 0.10 − 0.20) | 1071.43 |

Check of the suggested rate: at $1071.43 the fee is 107.14, so profit = 1071.43 − 750 − 107.14 = 214.29, and
214.29 / 1071.43 = 20.0%. A second non-round scenario is worked by hand in the comment of
`SecondScenario.test_non_round_inputs`, and I checked it separately.

## Edge cases and remaining limitations

Covered by the added tests:
- the 0 and just-under-100 boundaries of both percentages and of their sum
- tiny mpg and zero miles
- every input negative, NaN, ±inf, bool, string and None
- zero revenue with and without costs
- loss-making loads
- half-up rounding where float `round()` fails, and a negative half
- Decimal/int/float inputs giving the same result
- revenue around $1 billion staying exact to the cent

Known limitations, left as they are on purpose and flagged for the owner:
1. **Displayed rates can be up to half a cent below the true minimum.** Break-even is 833.333..., shown as 833.33.
   For a "minimum rate" I'd round up (ceiling). The supplied test pins 833.33, so I kept half-up, as the README forbids
   changing expected values.
2. **Fields are rounded independently.** For sub-cent inputs, displayed revenue minus displayed total can differ from
   displayed profit by 0.01. This is documented in the module.
3. **The -100 zero-revenue sentinel is a convention, not a floor.** Revenue $100 against $500 cost gives -400%.
   The contract asks for it, so I implemented and documented it as written.
4. Numeric strings such as `"100"` are rejected rather than parsed. The README says only "reject invalid inputs with
   ValueError", and JSON numbers arrive as numbers.
5. The real FDL product charges the 10% dispatch fee on **linehaul revenue only** (master sheet). This function takes
   one revenue figure. If this logic moves into the product, accessorials need their own input.

## How AI was used and how I checked it

- I read the contract and the code myself first and listed the suspected defects before asking AI for anything.
- Claude Code helped draft the fix and the edge-case tests. A **separate AI review pass** was given only the code and
  the contract, not my conclusions, so it couldn't simply agree with me. It confirmed D1-D8 and found the `-0.0` and
  overflow cases, which I then fixed and covered with tests.
- Checking didn't rest on the AI saying "it passes":
  - Every expected value in the new tests was checked by hand (tables above).
  - The supplied test file was diffed against the zip to prove it is untouched.
  - The two property tests (break-even gives profit 0, suggested rate gives the target margin) check the formulas
    against their definitions rather than against numbers copied from the code.
- One AI-written test was wrong at first: its value still fitted in 28 digits after costs were subtracted. I caught it
  because the test failed, worked out why, and corrected the test, not the code.

## GitHub / Replit links

Repository: _add link after pushing_. The project is plain Python with no install step. It runs anywhere with
`python -m unittest -v`, including a Replit Python repl.
