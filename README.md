# Stock Range Calculator

A web-based tool designed to estimate the next day's price range for stocks using implied volatility (IV) or VIX.

## Features

- Calculate expected price ranges based on standard deviations
- Educational insights on volatility and price movements
- Simple, intuitive interface for both novice and experienced investors
- Feedback mechanism for continuous improvement

## Installation

1. Clone this repository:
```
git clone <repository-url>
cd stock-range-calculator
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```
streamlit run app.py
```

2. Open your web browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

3. Enter the required information:
   - Stock name (optional)
   - Previous day's stock price
   - Implied volatility (IV/VIX)

4. Click "Calculate" to see the estimated price ranges

## How It Works

The tool uses the following formula to calculate the standard deviation move:

```
SD Move = Current Stock Price × Implied Volatility × √(Time Period / 252)
```

Where:
- Time Period is set to 1 day for next-day estimation
- 252 represents the standard number of trading days per year

The tool then calculates the price ranges for 1st, 2nd, and 3rd standard deviations:
- 1 SD: Stock Price ± (1 × SD Move)
- 2 SD: Stock Price ± (2 × SD Move)
- 3 SD: Stock Price ± (3 × SD Move)

## Example

For a stock "ABC" with:
- Stock Price = $100
- IV = 0.20 (20%)

The calculation would be:
- SD Move ≈ 100 × 0.20 × √(1/252) ≈ 1.26

Resulting in the following ranges:
- 1 SD: 100 ± 1.26 (i.e., 98.74 to 101.26)
- 2 SD: 100 ± 2.52 (i.e., 97.48 to 102.52)
- 3 SD: 100 ± 3.78 (i.e., 96.22 to 103.78)

## Feedback

We welcome your feedback! Please use the feedback form in the application to submit suggestions or report issues. 