import requests
import pandas as pd

# parameters
API_KEY = "YY2Q36V806T22YJX"
BASE_URL = "https://www.alphavantage.co/query"
HIST_LENGHT = "full"

def fetch_stock_data(symbol):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY,
        "outputsize": HIST_LENGHT
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if "Time Series (Daily)" in data:
        df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
        df.columns = ["open", "high", "low", "close", "volume"]
        df.index = pd.to_datetime(df.index)
        return df.astype(float)
    else:
        print("Error fetching data:", data)
        return None