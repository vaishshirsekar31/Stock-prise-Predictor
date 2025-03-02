# Stock Price Predictor

![Build Status](https://github.com/rafael-fuentes/stock-price-predictor/actions/workflows/ci.yml/badge.svg)
![Code Coverage](https://img.shields.io/badge/coverage-90%25-green)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

A machine learning tool to predict stock prices using historical data and LSTM models, with visualizations.

## Project Overview
Stock Price Predictor is a Python-based application that fetches historical stock data from Yahoo Finance, processes it through an ETL pipeline, trains a Long Short-Term Memory (LSTM) neural network using TensorFlow, and generates visualizations of actual vs. predicted prices with Matplotlib. Designed to showcase advanced skills in data science and automation, this project is ideal for roles such as Software Engineer or Data Scientist.

### Key Features
- **ETL Pipeline**: Fetches and cleans stock data from Yahoo Finance.
- **Machine Learning**: Uses an LSTM model to predict future stock prices.
- **Data Visualization**: Generates plots comparing actual and predicted prices.
- **CLI Interface**: Flexible command-line options for customization.

### Technologies
- Python: Pandas, NumPy, TensorFlow, Matplotlib
- Testing: Pytest with coverage
- Deployment: Docker, AWS ECR (via CI/CD)

## Installation Guide
Follow these steps to set up and run the project locally.

### Prerequisites
- Python 3.9 or higher
- Docker (optional, for containerized deployment)
- Git (for cloning the repository)

### Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rafael-fuentes/stock-price-predictor.git
   cd stock-price-predictor
   ```
2. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   - This installs Pandas, NumPy, TensorFlow, Matplotlib, and testing tools.
3. **Verify Installation**:
   Run a simple test to ensure dependencies are installed:
   ```bash
   python -c "import tensorflow; print(tensorflow.__version__)"
   ```

## Usage Examples
Here are practical examples of how to use the Stock Price Predictor.

### Default Prediction (Apple Stock)
Run the predictor with default settings:
```bash
python src/cli.py
```
- Output: A prediction graph saved as `docs/prediction.png`.

### Custom Prediction (Tesla Stock)
Predict Tesla stock prices with custom parameters:
```bash
python src/cli.py --ticker TSLA --start 2024-01-01 --end 2025-02-28 --look-back 30 --epochs 20
```
- Output: A graph for TSLA in `docs/prediction.png`.

### Dockerized Run
Build and run the predictor in a Docker container:
```bash
docker build -t stock-price-predictor .
docker run -v $(pwd)/docs:/app/docs stock-price-predictor
```
- The `-v` flag mounts the `docs/` directory to save the output plot locally.

## CLI Documentation
The command-line interface (`src/cli.py`) provides flexible options for running predictions.

### Command
```bash
python src/cli.py [options]
```

### Options
- `--ticker`: Stock ticker symbol (default: `AAPL`)
  - Example: `--ticker MSFT` for Microsoft.
- `--start`: Start date in YYYY-MM-DD format (default: `2023-01-01`)
- `--end`: End date in YYYY-MM-DD format (default: `2025-02-28`)
- `--look-back`: Number of past days to use for prediction (default: `60`)
  - Example: `--look-back 90` for a 90-day window.
- `--epochs`: Number of training epochs for the LSTM model (default: `10`)
  - Example: `--epochs 50` for more training iterations.

### Example
```bash
python src/cli.py --ticker GOOGL --start 2023-06-01 --end 2024-06-01 --look-back 45 --epochs 15
```

## Tutorial: Predicting Stock Prices
This section walks you through using the Stock Price Predictor step-by-step.

### Step 1: Set Up the Environment
- Follow the installation guide above to clone the repo and install dependencies.

### Step 2: Run a Prediction
- Predict Google stock prices:
  ```bash
  python src/cli.py --ticker GOOGL
  ```
- The script will:
  1. Fetch historical data from Yahoo Finance.
  2. Train an LSTM model on the data.
  3. Generate a prediction plot saved as `docs/prediction.png`.

### Step 3: Interpret the Results
- Open `docs/prediction.png` to view:
  - Blue line: Actual stock prices.
  - Orange line: Predicted stock prices.
- The model uses the last `look-back` days to forecast future prices.

### Step 4: Experiment
- Try different tickers (e.g., `AMZN`, `FB`) or adjust `--look-back` and `--epochs` to see how predictions change.

### Deployment Option
- **Docker**: Run locally with the Docker commands above.
- **AWS**: Configure an ECR repository and deploy via the CI/CD pipeline (see Contributing Guidelines).

## Contributing Guidelines
Contributions are welcome to enhance this project! Here’s how to contribute:

### Workflow
1. **Fork and Branch**:
   ```bash
   git checkout -b feature/add-model-save
   ```
2. **Code Standards**:
   - Adhere to PEP8 (run `flake8 src/` to check).
   - Write clean, documented code with docstrings.
3. **Testing**:
   - Add tests in `tests/` using Pytest.
   - Run `pytest tests/ --cov=src` to verify ≥85% coverage.
   - Example test command:
     ```bash
     pytest --cov=src --cov-report=html
     ```
4. **Commit and Push**:
   - Use clear commit messages following conventional commits (e.g., `feat: add CLI option for saving models`).
   - Push your branch:
     ```bash
     git push origin feature/add-model-save
     ```
5. **Submit a Pull Request**:
   - Open a PR on GitHub with a detailed description of your changes.
   - Ensure the CI pipeline (`ci.yml`) passes.

### CI/CD Pipeline
- **Triggers**: Runs on push or pull request to `main`.
- **Steps**: Installs dependencies, runs tests with coverage, builds a Docker image, and deploys to AWS ECR (if configured).
- **AWS Deployment**: Replace `<your-aws-ecr-repo>` in `ci.yml` and set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in GitHub Secrets.

## License Information
MIT License

Copyright (c) 2025 Rafael Fuentes

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

---

### Notes on the README
- **Sections**: Includes all required sections (Project Overview, Installation Guide, Usage Examples, CLI Documentation, Tutorial, Contributing Guidelines, License Information) as per `readme_specs`.
- **Badges**: Build Status, Code Coverage, and Version badges are present at the top.
- **Clarity**: Each section is concise yet detailed, with practical examples and commands.
- **Deployment**: Instructions for both local Docker and AWS deployment are included.
- **Alignment**: Reflects the project's focus on data science and automation, meeting Rafael Fuentes' portfolio goals.

This `README.md` serves as a standalone, comprehensive guide for users and contributors. Let me know if you'd like adjustments or the next repository!