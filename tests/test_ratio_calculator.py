import pytest

from app.tools.ratio_calculator import (
    current_ratio,
    quick_ratio,
    cash_ratio,
    working_capital,
    debt_to_equity_ratio,
    debt_to_asset_ratio,
    interest_coverage_ratio,
    equity_multiplier,
    return_on_assets,
    return_on_equity,
    net_profit_margin,
    gross_profit_margin,
    operating_margin,
)

# Test for current ratio


def test_current_ratio_nomral_case():
    result = current_ratio(current_assets=500000, current_liabilities=100000)
    assert result == 5.0


def test_current_ratio_zero_liabilities():
    with pytest.raises(ValueError):
        current_ratio(current_assets=200000, current_liabilities=0)


# Test for quick ratio


def test_quick_ratio_normal_case():
    result = quick_ratio(
        current_assets=200000, inventory=100000, current_liabilities=50000
    )
    assert result == 2.0


def test_quick_ratio_negative_inventory():
    with pytest.raises(ValueError):
        quick_ratio(current_assets=20000, inventory=-10000, current_liabilities=50000)


def test_quick_ratio_zero_liabilities():
    with pytest.raises(ValueError):
        quick_ratio(current_assets=20000, inventory=10000, current_liabilities=0)


def test_quick_ratio_inventory_exceeds_current_assets():
    with pytest.raises(ValueError):
        quick_ratio(current_assets=20000, inventory=50000, current_liabilities=10000)


# Test for cash ratio


def test_cash_ratio_normal_case():
    result = cash_ratio(cash_and_cash_equivalents=50000, current_liabilities=25000)
    assert result == 2.0


def test_cash_ratio_zero_liabilities_raises():
    with pytest.raises(ValueError):
        cash_ratio(cash_and_cash_equivalents=50000, current_liabilities=0)


# Test for working capital (no validation, so only a normal case)


def test_working_capital_normal_case():
    result = working_capital(current_assets=200000, current_liabilities=100000)
    assert result == 100000


# Test for debt to equity ratio


def test_debt_to_equity_ratio_normal_case():
    result = debt_to_equity_ratio(total_liabilities=400000, total_equity=200000)
    assert result == 2.0


def test_debt_to_equity_ratio_zero_equity_raises():
    with pytest.raises(ValueError):
        debt_to_equity_ratio(total_liabilities=400000, total_equity=0)


# Test for debt to asset ratio


def test_debt_to_asset_ratio_normal_case():
    result = debt_to_asset_ratio(total_liabilities=300000, total_assets=1000000)
    assert result == 0.3


def test_debt_to_asset_ratio_zero_assets_raises():
    with pytest.raises(ValueError):
        debt_to_asset_ratio(total_liabilities=300000, total_assets=0)


# Test for interest coverage ratio


def test_interest_coverage_ratio_normal_case():
    result = interest_coverage_ratio(ebit=100000, interest_expenses=20000)
    assert result == 5.0


def test_interest_coverage_ratio_zero_interest_raises():
    with pytest.raises(ValueError):
        interest_coverage_ratio(ebit=100000, interest_expenses=0)


# Test for equity multiplier


def test_equity_multiplier_normal_case():
    result = equity_multiplier(total_equity=200000, total_assets=1000000)
    assert result == 5.0


def test_equity_multiplier_zero_assets_raises():
    with pytest.raises(ValueError):
        equity_multiplier(total_equity=200000, total_assets=0)


# Test for return on assets


def test_return_on_assets_normal_case():
    result = return_on_assets(net_income=50000, total_assets=500000)
    assert result == 0.1


def test_return_on_assets_zero_assets_raises():
    with pytest.raises(ValueError):
        return_on_assets(net_income=50000, total_assets=0)


# Test for return on equity


def test_return_on_equity_normal_case():
    result = return_on_equity(net_income=50000, total_equity=250000)
    assert result == 0.2


def test_return_on_equity_zero_equity_raises():
    with pytest.raises(ValueError):
        return_on_equity(net_income=50000, total_equity=0)


# Test for net profit margin


def test_net_profit_margin_normal_case():
    result = net_profit_margin(net_income=40000, total_revenue=400000)
    assert result == 0.1


def test_net_profit_margin_zero_revenue_raises():
    with pytest.raises(ValueError):
        net_profit_margin(net_income=40000, total_revenue=0)


# Test for gross profit margin


def test_gross_profit_margin_normal_case():
    result = gross_profit_margin(total_revenue=500000, cogs=300000)
    assert result == 0.4


def test_gross_profit_margin_zero_revenue_raises():
    with pytest.raises(ValueError):
        gross_profit_margin(total_revenue=0, cogs=300000)


# Test for operating margin


def test_operating_margin_normal_case():
    result = operating_margin(operating_income=60000, total_revenue=400000)
    assert result == 0.15


def test_operating_margin_zero_revenue_raises():
    with pytest.raises(ValueError):
        operating_margin(operating_income=60000, total_revenue=0)
