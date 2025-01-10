import streamlit as st
import matplotlib.pyplot as plt

from requestdata import fetch_stock_data

st.title("Finance Dashboard")

# Sidebar input for stock symbol
stock_symbol = st.sidebar.text_input("Enter Stock Symbol", "SPY")

# Fetch data
data = fetch_stock_data(stock_symbol)
if data is not None:
    st.write(f"Stock Data for {stock_symbol}")
    st.dataframe(data)

    # Plot stock closing prices
    st.write("Closing Prices")
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data["close"], label="Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"{stock_symbol} Closing Prices")
    plt.legend()
    st.pyplot(plt.gcf())
else:
    st.error("Failed to fetch data. Check the stock symbol.")
