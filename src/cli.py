"""CLI for Stock Price Predictor"""
import argparse
from predictor import run_prediction

def main():
    parser = argparse.ArgumentParser(description="Predict stock prices using LSTM.")
    parser.add_argument('--ticker', default='AAPL', help='Stock ticker symbol (e.g., AAPL)')
    parser.add_argument('--start', default='2023-01-01', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end', default='2025-02-28', help='End date (YYYY-MM-DD)')
    parser.add_argument('--look-back', type=int, default=60, help='Number of days to look back')
    parser.add_argument('--epochs', type=int, default=10, help='Number of training epochs')
    args = parser.parse_args()

    try:
        actual, predicted = run_prediction(
            ticker=args.ticker,
            start=args.start,
            end=args.end,
            look_back=args.look_back,
            epochs=args.epochs
        )
        print(f"Prediction completed for {args.ticker}. Check docs/prediction.png for visualization.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()