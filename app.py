import streamlit as st
import numpy as np
import pandas as pd

# Header
st.title("Stock Range Calculator")
st.write("Estimate the next day's price range for stocks using implied volatility.")

# How to Use Section
st.markdown("""
### How to Use
This tool estimates the next day's price range for a stock based on its previous day's price and implied volatility (IV or VIX).

- **Standard Deviation (SD)**: A measure of how much the stock price is expected to fluctuate.
  - **1st SD**: Approximately 68% probability that the stock price will be within this range.
  - **2nd SD**: Approximately 95% probability.
  - **3rd SD**: Approximately 99.7% probability.

These calculations use the implied volatility to estimate expected price movement without revealing the proprietary formula.
""")

# Input Section
stock_name = st.text_input("Stock Name (optional)", "", help="Enter the stock ticker or name (e.g., ABC).")
stock_price = st.number_input(
    "Previous Day's Stock Price", 
    min_value=0.0, 
    step=0.01, 
    help="Enter the closing price of the stock from the previous day."
)

# Volatility input type selection
volatility_type = st.radio(
    "Select Volatility Input Type",
    ["IV (as decimal)", "VIX (as index value)"],
    help="Choose whether to enter implied volatility as a decimal (e.g., 0.20) or VIX as an index value (e.g., 20)."
)

# Adjust label and help text based on selection
if volatility_type == "IV (as decimal)":
    volatility_label = "Implied Volatility (IV)"
    volatility_help = "Enter the implied volatility as a decimal (e.g., 0.20 for 20%)."
    step_value = 0.01
else:
    volatility_label = "VIX Value"
    volatility_help = "Enter the VIX index value (e.g., 20)."
    step_value = 0.1

volatility = st.number_input(
    volatility_label, 
    min_value=0.0, 
    step=step_value, 
    help=volatility_help
)

# Information about Sensibull for individual stock VIX
st.info("You can get individual stock VIX values from [Sensibull](https://sensibull.com) for Indian stocks.")

# Calculation and Output
if st.button("Calculate"):
    if stock_price <= 0 or volatility <= 0:
        st.error("Please enter positive values for stock price and volatility.")
    else:
        try:
            # Constants
            time_period = 1  # 1 day
            trading_days = 252  # Standard trading days per year
            
            # Convert VIX to decimal if needed
            iv_value = volatility if volatility_type == "IV (as decimal)" else volatility / 100
            
            # Calculate SD Move
            sd_move = stock_price * iv_value * np.sqrt(time_period / trading_days)
            
            # Calculate ranges for 1, 2, and 3 SD
            sd1_lower = round(stock_price - (1 * sd_move), 2)
            sd1_upper = round(stock_price + (1 * sd_move), 2)
            sd2_lower = round(stock_price - (2 * sd_move), 2)
            sd2_upper = round(stock_price + (2 * sd_move), 2)
            sd3_lower = round(stock_price - (3 * sd_move), 2)
            sd3_upper = round(stock_price + (3 * sd_move), 2)
            
            # Determine stock name for display
            stock_display_name = stock_name if stock_name else "Stock"
            
            # Create table data
            data = {
                "Stock Name": [stock_display_name],
                "1st SD Lower": [sd1_lower],
                "1st SD Upper": [sd1_upper],
                "2nd SD Lower": [sd2_lower],
                "2nd SD Upper": [sd2_upper],
                "3rd SD Lower": [sd3_lower],
                "3rd SD Upper": [sd3_upper]
            }
            df = pd.DataFrame(data)
            
            # Display table
            st.table(df)
            
            # Display the volatility value used in calculation
            st.info(f"Calculation used volatility value of {iv_value:.4f} (as decimal)")
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Sample Calculation
if st.checkbox("Show Sample Calculation"):
    st.write("For a stock 'ABC':")
    
    sample_tab1, sample_tab2 = st.tabs(["Using IV (decimal)", "Using VIX (index)"])
    
    with sample_tab1:
        st.write("- Input: Stock Price = $100, IV = 0.20 (as decimal)")
        st.write("- Calculation: SD Move ≈ 100 × 0.20 × √(1/252) ≈ 1.26")
        st.write("- Ranges:")
        st.write("  - 1 SD: 100 ± 1.26 (i.e., 98.74 to 101.26)")
        st.write("  - 2 SD: 100 ± 2.52 (i.e., 97.48 to 102.52)")
        st.write("  - 3 SD: 100 ± 3.78 (i.e., 96.22 to 103.78)")
    
    with sample_tab2:
        st.write("- Input: Stock Price = $100, VIX = 20 (as index value)")
        st.write("- Conversion: VIX 20 → 0.20 (divide by 100)")
        st.write("- Calculation: SD Move ≈ 100 × 0.20 × √(1/252) ≈ 1.26")
        st.write("- Ranges:")
        st.write("  - 1 SD: 100 ± 1.26 (i.e., 98.74 to 101.26)")
        st.write("  - 2 SD: 100 ± 2.52 (i.e., 97.48 to 102.52)")
        st.write("  - 3 SD: 100 ± 3.78 (i.e., 96.22 to 103.78)")

# Footer with "Made with love" message
st.markdown("""
---
<div style="text-align: center; margin-top: 20px;">
    Made with ❤️ by Raj
</div>
""", unsafe_allow_html=True) 