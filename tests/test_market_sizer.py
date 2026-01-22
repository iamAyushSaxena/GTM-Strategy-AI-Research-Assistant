import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from market_sizer import MarketSizer

@pytest.fixture
def sizer():
    return MarketSizer()

def test_tam_calculation(sizer):
    """Test Total Addressable Market calculation"""
    tam = sizer.calculate_tam()
    
    assert isinstance(tam, dict)
    # FIX: The key is 'final', not 'total_users'
    assert 'final' in tam 
    assert 'confidence' in tam
    assert tam['final'] > 0

def test_som_calculation(sizer):
    """Test Serviceable Obtainable Market calculation"""
    # SOM depends on TAM and SAM, so we run them all
    sizer.calculate_tam()
    sizer.calculate_sam()
    som = sizer.calculate_som()
    
    assert isinstance(som, dict)
    assert 'final' in som
    assert som['final'] > 0
    # FIX: Compare against 'final' key in TAM data
    assert som['final'] < sizer.tam_data['final']