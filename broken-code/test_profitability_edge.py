"""Edge-case tests for calculate_load, each on a boundary of the README contract."""
import math
import unittest
from decimal import Decimal

from profitability import calculate_load

PARAMS = ["revenue", "miles", "fuel_price", "mpg", "driver_pay", "tolls",
          "dispatch_pct", "other_expenses", "desired_margin_pct"]
BASE = dict(revenue=2000, miles=500, fuel_price=4, mpg=10, driver_pay=400, tolls=50,
            dispatch_pct=10, other_expenses=100, desired_margin_pct=20)
KEYS = {"fuel_cost", "dispatch_fee", "total_cost", "profit", "margin_pct",
        "break_even_rate", "suggested_rate"}


def calc(**overrides):
    return calculate_load(**{**BASE, **overrides})


class SecondScenario(unittest.TestCase):
    def test_non_round_inputs(self):
        # fuel  = 321 * 3.879 / 6.5            = 1245.159 / 6.5 = 191.56292... -> 191.56
        # disp  = 1234.56 * 8.5 / 100          = 104.9376                       -> 104.94
        # fixed = 191.56292 + 385.25 + 17.4 + 42.1 = 636.31292
        # total = 636.31292 + 104.9376         = 741.25052                      -> 741.25
        # profit= 1234.56 - 741.25052          = 493.30948                      -> 493.31
        # margin= 493.30948 / 1234.56 * 100    = 39.9583                        -> 39.96
        # BE    = 636.31292 / (1 - 0.085)      = 695.42396                      -> 695.42
        # sugg  = 636.31292 / (1 - 0.235)      = 831.78160                      -> 831.78
        r = calculate_load(1234.56, 321, 3.879, 6.5, 385.25, 17.4, 8.5, 42.1, 15)
        self.assertEqual(r, {"fuel_cost": 191.56, "dispatch_fee": 104.94, "total_cost": 741.25,
                             "profit": 493.31, "margin_pct": 39.96,
                             "break_even_rate": 695.42, "suggested_rate": 831.78})

    def test_result_shape(self):
        r = calc()
        self.assertEqual(set(r), KEYS)
        for k, v in r.items():
            self.assertIs(type(v), float, k)
            self.assertEqual(v, round(v, 2), k)


class Properties(unittest.TestCase):
    CASES = [BASE, dict(revenue=1234.56, miles=321, fuel_price=3.879, mpg=6.5, driver_pay=385.25,
                        tolls=17.4, dispatch_pct=8.5, other_expenses=42.1, desired_margin_pct=15)]

    def test_break_even_rate_gives_zero_profit(self):
        for case in self.CASES:
            with self.subTest(case=case):
                be = calculate_load(**case)["break_even_rate"]
                # rate is rounded to the cent, so profit is off by at most ~1 cent
                self.assertLessEqual(abs(calculate_load(**{**case, "revenue": be})["profit"]), 0.01)

    def test_suggested_rate_hits_target_margin(self):
        for case in self.CASES:
            with self.subTest(case=case):
                s = calculate_load(**case)["suggested_rate"]
                m = calculate_load(**{**case, "revenue": s})["margin_pct"]
                self.assertAlmostEqual(m, case["desired_margin_pct"], delta=0.01)


class Percentages(unittest.TestCase):
    def test_zero_dispatch_and_zero_margin(self):
        r = calc(dispatch_pct=0, desired_margin_pct=0)
        self.assertEqual(r["dispatch_fee"], 0.0)
        self.assertEqual(r["break_even_rate"], 750.0)  # 200 fuel + 400 + 50 + 100
        self.assertEqual(r["suggested_rate"], r["break_even_rate"])

    def test_sum_boundary(self):
        r = calc(dispatch_pct=50, desired_margin_pct=49.99)  # 750 / 0.0001
        self.assertEqual(r["suggested_rate"], 7500000.0)
        with self.assertRaises(ValueError):
            calc(dispatch_pct=50, desired_margin_pct=50)

    def test_each_percent_at_100_or_negative_rejected(self):
        for name in ("dispatch_pct", "desired_margin_pct"):
            for bad in (100, -0.01):
                with self.subTest(name=name, value=bad), self.assertRaises(ValueError):
                    # keep the other percent at 0 so only this one is out of range
                    calc(**{"dispatch_pct": 0, "desired_margin_pct": 0, name: bad})


class MilesAndMpg(unittest.TestCase):
    def test_mpg_zero_or_negative_rejected(self):
        for bad in (0, 0.0, -1):
            with self.subTest(mpg=bad), self.assertRaises(ValueError):
                calc(mpg=bad)

    def test_tiny_mpg_accepted(self):
        self.assertEqual(calc(miles=10, mpg=0.5)["fuel_cost"], 80.0)  # 10 / 0.5 * 4

    def test_zero_miles_zero_fuel(self):
        self.assertEqual(calc(miles=0)["fuel_cost"], 0.0)


class InvalidInputs(unittest.TestCase):
    def test_each_param_negative_rejected(self):
        for name in PARAMS:
            with self.subTest(name), self.assertRaises(ValueError):
                calc(**{name: -1})

    def test_non_finite_and_wrong_types_rejected(self):
        for name in PARAMS:
            for bad in (math.nan, math.inf, -math.inf, Decimal("NaN"), True, False, "100", None):
                with self.subTest(name=name, value=bad), self.assertRaises(ValueError):
                    calc(**{name: bad})


class Margins(unittest.TestCase):
    def test_zero_revenue_with_costs_is_minus_100(self):
        r = calc(revenue=0)
        self.assertEqual(r["profit"], -750.0)
        self.assertEqual(r["margin_pct"], -100.0)

    def test_zero_revenue_zero_costs_is_0(self):
        r = calculate_load(0, 0, 0, 1, 0, 0, 0, 0, 0)
        self.assertEqual((r["profit"], r["margin_pct"]), (0.0, 0.0))

    def test_loss_making_load(self):
        r = calc(revenue=500)  # fixed 750 + dispatch 50 = 800 cost
        self.assertEqual(r["profit"], -300.0)
        self.assertEqual(r["margin_pct"], -60.0)


class Rounding(unittest.TestCase):
    def test_half_up_where_float_round_fails(self):
        self.assertEqual(round(2.675, 2), 2.67)  # float binary 2.67499..., the trap
        r = calculate_load(0, 1, 2.675, 1, 0, 0, 0, 0, 0)
        self.assertEqual(r["fuel_cost"], 2.68)
        self.assertEqual(r["total_cost"], 2.68)

    def test_negative_half_rounds_away_from_zero(self):
        # profit = 1 - 1.005 = -0.005 exactly. ROUND_HALF_UP in Decimal is half away
        # from zero, so -0.01: the loss is not understated, and matches |+0.005| -> 0.01.
        r = calculate_load(1, 0, 0, 1, 0, 0, 0, 1.005, 0)
        self.assertEqual(r["profit"], -0.01)
        self.assertEqual(r["total_cost"], 1.01)  # 1.005 -> 1.01, symmetric with profit


    def test_tiny_loss_shows_zero_not_negative_zero(self):
        # Charging the displayed break-even 833.33 loses 0.003: shown as 0.0, never -0.0 (JSON "-0.0").
        r = calc(revenue=833.33)
        self.assertEqual(math.copysign(1, r["profit"]), 1.0)
        self.assertEqual(math.copysign(1, r["margin_pct"]), 1.0)


class InputTypes(unittest.TestCase):
    def test_decimal_int_float_agree(self):
        ints = calc()
        floats = calc(**{k: float(v) for k, v in BASE.items()})
        decimals = calc(**{k: Decimal(v) for k, v in BASE.items()})
        self.assertEqual(ints, floats)
        self.assertEqual(ints, decimals)

    def test_decimal_cents_not_float_noise(self):
        # 0.1 + 0.2 as floats is 0.30000000000000004; Decimal path must give 0.30 exactly
        r = calculate_load(Decimal("0.30"), 0, 0, 1, Decimal("0.1"), Decimal("0.2"), 0, 0, 0)
        self.assertEqual((r["total_cost"], r["profit"]), (0.3, 0.0))

    def test_large_revenue_exact_to_cent(self):
        r = calculate_load(999999999.99, 0, 0, 1, 0, 0, 0, 0.01, 0)
        self.assertEqual(r["profit"], 999999999.98)
        r = calculate_load(1e9, 0, 0, 1, 0, 0, 10, 0, 0)
        self.assertEqual((r["dispatch_fee"], r["profit"]), (100000000.0, 900000000.0))


    def test_amount_beyond_decimal_precision_is_value_error(self):
        # 1e27 cannot be held to the cent in 28 digits; reject cleanly instead of decimal.InvalidOperation.
        with self.assertRaises(ValueError):
            calc(revenue=10**27)


if __name__ == "__main__":
    unittest.main()
