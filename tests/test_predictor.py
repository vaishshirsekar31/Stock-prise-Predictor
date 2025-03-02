"""Unit tests for Stock Price Predictor"""
import pytest
import numpy as np
from src.predictor import fetch_data, prepare_data, build_model, predict

def test_fetch_data():
    """Test data fetching with a valid ticker."""
    data = fetch_data('AAPL', '2023-01-01', '2023-01-10')
    assert len(data) > 0
    assert data.shape[1] == 1

def test_fetch_data_invalid_ticker():
    """Test data fetching with an invalid ticker."""
    with pytest.raises(ValueError):
        fetch_data('INVALID', '2023-01-01', '2023-01-10')

def test_prepare_data():
    """Test data preparation for LSTM."""
    data = np.array([[100], [101], [102], [103], [104], [105]])
    X, y, scaler = prepare_data(data, look_back=3)
    assert X.shape == (3, 3)  # 6 - 3 = 3 samples
    assert y.shape == (3,)
    assert scaler is not None

def test_build_model():
    """Test model creation."""
    model = build_model(look_back=60)
    assert len(model.layers) == 3  # LSTM, LSTM, Dense
    assert model.input_shape == (None, 60, 1)