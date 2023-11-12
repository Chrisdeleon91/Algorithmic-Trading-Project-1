import streamlit as st
import pandas as pd

# Define a simple moving average (SMA) function
def calculate_sma(data, window):
    return data['Close'].rolling(window=window).mean()

# Streamlit UI
st.title('Cryptocurrency Price Analysis')

# List of cryptocurrency CSV files
crypto_files = {
    'Bitcoin (BTC)': 'BTC-USD.csv',
    'Ethereum (ETH)': 'ETH-USD.csv',
    'Cardano (ADA)': 'ADA-USD.csv',
    'Polygon (MATIC)': 'MATIC-USD.csv',
    'Solana (SOL)': 'SOL-USD.csv',
}

# Sidebar for user input
st.sidebar.header('Algorithm Parameters')
window_size = st.sidebar.slider('SMA Window Size', min_value=1, max_value=365, value=50)

# Analyze and display data for each cryptocurrency
for crypto_name, csv_file in crypto_files.items():
    st.write(f'## {crypto_name} Price Analysis')

    # Read cryptocurrency price data from the CSV file
    data = pd.read_csv(csv_file)

    # Display the data
    st.write(f'{crypto_name} Price Data (Last 5 Years)')
    st.write(data)

    # Calculate and display the SMA
    sma = calculate_sma(data, window_size)
    st.write(f'Simple Moving Average (SMA-{window_size})')
    st.line_chart(sma)

    # Trading signals based on SMA
    data['Signal'] = data['Close'] > sma
    st.write(f'Trading Signals (Buy/Sell) for {crypto_name}')
    st.write(data[['Date', 'Signal']])

    # Performance Metrics
    total_trades = len(data) - 1
    winning_trades = sum(data['Signal'].shift(-1))
    winning_percentage = (winning_trades / total_trades) * 100
    st.write(f'Performance Metrics for {crypto_name}')
    st.write(f'Total Trades: {total_trades}')
    st.write(f'Winning Trades: {winning_trades}')
    st.write(f'Winning Percentage: {winning_percentage:.2f}%')