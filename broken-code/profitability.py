"""FDL fictional load profitability service.
No external dependencies. Monetary inputs are USD.

Money is computed in Decimal and each displayed field is rounded once, from the
unrounded value, to two decimal places with halves away from zero (ROUND_HALF_UP).
Fields are rounded independently, so a displayed sum can differ from a displayed
total by 0.01. Results are returned as floats for JSON compatibility.

Zero-revenue convention: profit margin is undefined when revenue is 0. For this
exercise it is reported as -100 when profit is negative (a pure loss) and 0 when
profit is also 0 (nothing earned, nothing spent).
"""
from decimal import Decimal, DecimalException, ROUND_HALF_UP

_HUNDRED = Decimal(100)
_CENT = Decimal("0.01")
ZERO_REVENUE_LOSS_MARGIN = -100


def _number(name, value):
    # JSON numbers arrive as int or float; bool is an int subclass but never a valid amount.
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        raise ValueError(f"{name} must be a number")
    # str() keeps the value as written (0.1, not its binary expansion).
    number = Decimal(str(value))
    if not number.is_finite():
        raise ValueError(f"{name} must be finite")
    if number < 0:
        raise ValueError(f"{name} must not be negative")
    return number


def _percent(name, value):
    number = _number(name, value)
    if number >= _HUNDRED:
        raise ValueError(f"{name} must be below 100")
    return number


def _display(value):
    try:
        cents = value.quantize(_CENT, rounding=ROUND_HALF_UP)
    except DecimalException:
        # shortcut: amounts of 1e26 and up exceed Decimal's 28-digit precision; raise prec if ever needed.
        raise ValueError("amount too large to represent to the cent") from None
    return float(cents) + 0.0  # + 0.0 turns -0.0 into 0.0


def calculate_load(revenue, miles, fuel_price, mpg, driver_pay, tolls, dispatch_pct, other_expenses, desired_margin_pct):
    revenue = _number("revenue", revenue)
    miles = _number("miles", miles)
    fuel_price = _number("fuel_price", fuel_price)
    mpg = _number("mpg", mpg)
    if mpg == 0:
        raise ValueError("mpg must be greater than 0")
    driver_pay = _number("driver_pay", driver_pay)
    tolls = _number("tolls", tolls)
    other_expenses = _number("other_expenses", other_expenses)
    dispatch_pct = _percent("dispatch_pct", dispatch_pct)
    desired_margin_pct = _percent("desired_margin_pct", desired_margin_pct)
    if dispatch_pct + desired_margin_pct >= _HUNDRED:
        raise ValueError("dispatch_pct + desired_margin_pct must be below 100")

    fuel_cost = miles * fuel_price / mpg
    dispatch_fee = revenue * dispatch_pct / _HUNDRED
    # Costs that do not scale with the rate; the dispatch fee does, so pricing grosses it up.
    fixed_cost = fuel_cost + driver_pay + tolls + other_expenses
    total_cost = fixed_cost + dispatch_fee
    profit = revenue - total_cost

    if revenue > 0:
        margin_pct = profit / revenue * _HUNDRED
    else:
        margin_pct = Decimal(ZERO_REVENUE_LOSS_MARGIN) if profit < 0 else Decimal(0)

    # Rate R where R - fixed - R*d = 0, and where (R - fixed - R*d) / R = m.
    break_even_rate = fixed_cost / (1 - dispatch_pct / _HUNDRED)
    suggested_rate = fixed_cost / (1 - (dispatch_pct + desired_margin_pct) / _HUNDRED)

    return {
        "fuel_cost": _display(fuel_cost),
        "dispatch_fee": _display(dispatch_fee),
        "total_cost": _display(total_cost),
        "profit": _display(profit),
        "margin_pct": _display(margin_pct),
        "break_even_rate": _display(break_even_rate),
        "suggested_rate": _display(suggested_rate),
    }
