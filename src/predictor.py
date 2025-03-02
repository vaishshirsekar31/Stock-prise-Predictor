"""Stock Price Predictor using LSTM"""
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

def fetch_data(ticker='AAPL', start='2023-01-01', end='2025-02-28'):
    """Fetch historical stock data from Yahoo Finance."""
    try:
        stock_data = yf.download(ticker, start=start, end=end)
        if stock_data.empty:
            raise ValueError(f"No data found for ticker {ticker}")
        return stock_data['Close'].values.reshape(-1, 1)
    except Exception as e:
        raise RuntimeError(f"Error fetching data: {e}")

def prepare_data(data, look_back=60):
    """Prepare data for LSTM model."""
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)
    X, y = [], []
    for i in range(look_back, len(scaled_data)):
        X.append(scaled_data[i - look_back:i, 0])
        y.append(scaled_data[i, 0])
    return np.array(X), np.array(y), scaler

def build_model(look_back=60):
    """Build and return an LSTM model."""
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(look_back, 1)))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

def train_model(model, X, y, epochs=10, batch_size=32):
    """Train the LSTM model."""
    model.fit(X, y, epochs=epochs, batch_size=batch_size, verbose=1)
    return model

def predict(model, X, scaler):
    """Make predictions and inverse transform them."""
    predicted = model.predict(X)
    return scaler.inverse_transform(predicted.reshape(-1, 1))

def plot_predictions(actual, predicted, ticker='AAPL'):
    """Visualize actual vs predicted prices."""
    plt.figure(figsize=(10, 6))
    plt.plot(actual, label='Actual Prices')
    plt.plot(predicted, label='Predicted Prices')
    plt.title(f'{ticker} Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig('docs/prediction.png')
    plt.close()

def run_prediction(ticker='AAPL', start='2023-01-01', end='2025-02-28', look_back=60, epochs=10):
    """Run the full prediction pipeline."""
    data = fetch_data(ticker, start, end)
    X, y, scaler = prepare_data(data, look_back)
    X = X.reshape((X.shape[0], X.shape[1], 1))
    model = build_model(look_back)
    model = train_model(model, X, y, epochs=epochs)
    predicted = predict(model, X, scaler)
    actual = scaler.inverse_transform(y.reshape(-1, 1))
    plot_predictions(actual, predicted, ticker)
    return actual, predicted

if __name__ == '__main__':
    actual, predicted = run_prediction()