# FDL Final Assessment: Lead Developer Candidate Submission

This is the final-stage assessment for the Lead Developer role at Family Dispatch & Logistics. It has two parts:

1. **The broken-code challenge.** A fictional load-profitability calculator had intentional defects. I found and
   fixed them, explained each one, proved the results, and added tests.
2. **The full-platform plan.** A timeline and cost assessment for the whole FDL platform, plus how I would lead the
   technical work.

All data is fictional. I didn't touch the existing FDL project, production systems or live accounts. This work is
not affiliated with any real FDL system.

## Where to find each deliverable

| Requested | Where |
|---|---|
| Corrected broken-code project | [broken-code/](broken-code/): `profitability.py` (fixed), `test_profitability.py` (supplied, unchanged), `test_profitability_edge.py` (22 added tests) |
| Debugging explanation and test results | [broken-code/SUBMISSION.md](broken-code/SUBMISSION.md), [test-results-before.txt](broken-code/test-results-before.txt), [test-results-after.txt](broken-code/test-results-after.txt) |
| Complete FDL timeline and cost estimate | [docs/fdl-development-plan.md](docs/fdl-development-plan.md) (also as Word: `docs/FDL-Development-Plan.docx`) |
| Estimating model (every row and assumption, rerunnable) | [docs/estimate/estimate.py](docs/estimate/estimate.py), output in [docs/estimate/estimate-output.md](docs/estimate/estimate-output.md), per-workstream table in [docs/estimate/workstreams.md](docs/estimate/workstreams.md) (also the appendix of the plan) |
| Technical leadership and AI development approach | [docs/technical-leadership.md](docs/technical-leadership.md) |
| Approximate total assessment hours | See below |

## Results at a glance

**Broken-code challenge**

- Found 8 defects:
  - wrong fuel formula
  - dispatch percent not divided by 100
  - margin divided by cost instead of revenue
  - no zero-revenue rule
  - break-even and suggested rate both ignored the dispatch fee
  - incomplete validation
  - float rounding wrong on money
- Supplied tests went from **1/5 passing to 5/5**, with the test file unchanged.
- **27/27 pass** with the added edge-case tests.

**Platform estimate**

| Item | Estimate |
|---|---|
| Total effort | **~11,200 h** realistic (9,150 to 13,250), testing and contingency included |
| Internal pilot on FDL's own operation | Dispatch about month 9; money and profitability about month 12 |
| First outside paying carrier | About **month 17** (month 11 with a second developer from month 2) |
| Full platform | About **month 31** with the recommended team (24 to 40) |
| Monthly technical cost | About $250-350 while building, $450-750 after launch, $1,350-5,400 at full scale, plus usage and quoted licences |

## Run the tests

Needs Python 3.10+ and no packages.

```bash
cd broken-code
python -m unittest -v
```

Rerun the estimate:

```bash
python docs/estimate/estimate.py
```

## Assessment hours

About **2.5 hours** for this final assessment, in one sitting on 25 October 2026 (about 1:40 to 4:15 AM Philippine
time). That covers reading both documents, debugging and testing, building and reviewing the estimating model,
writing the plan and leadership documents, and a final review of everything against the requirements.

## AI disclosure

I used Claude Code (Anthropic) throughout, as pair programmer, researcher and reviewer:

- **Debugging.** I listed the suspected defects from the contract first, then used AI to draft the fix and the tests.
  A separate AI pass reviewed the code without my conclusions. Every expected value was checked by hand.
- **Estimate.** I built the hour model myself. An AI "skeptical tech lead" review found missing scope and factors that
  were too generous, and the numbers went up as a result.
- **Pricing.** AI research gathered current published prices. Unpublished prices are marked as unknown rather than
  guessed.

I can explain and defend every part of this submission.
