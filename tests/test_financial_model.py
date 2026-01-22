import pytest
import pandas as pd
import sys
from pathlib import Path

# Add src to path so we can import the modules
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from financial_model import FinancialModel

@pytest.fixture
def model():
    """Fixture to create a fresh model instance for each test"""
    return FinancialModel()

def test_user_growth_projection(model):
    """Test that user growth projection returns valid data"""
    months = 12
    df = model.project_user_growth(months=months)
    
    # Assertions
    assert isinstance(df, pd.DataFrame)
    assert len(df) == months
    assert 'total_users' in df.columns
    assert 'mrr' in df.columns
    assert df['total_users'].iloc[-1] > 0  # Users should grow

def test_break_even_calculation(model):
    """Test break-even analysis"""
    # First ensure we have projections
    model.project_user_growth(months=24)
    
    breakeven = model.calculate_break_even()
    
    assert isinstance(breakeven, dict)
    assert 'month' in breakeven
    assert 'is_reached' in breakeven