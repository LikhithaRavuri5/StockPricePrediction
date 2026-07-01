import yfinance as yf
import pandas as pd

STOCK_SYMBOL = "TSLA"
START_DATE = "2020-01-01"
END_DATE = "2024-01-01"

def load_stock_data():
    print(f"Downloading {STOCK_SYMBOL} stock data...")
    
    stock = yf.download(STOCK_SYMBOL, start=START_DATE, end=END_DATE)
    
    stock = stock[['Close']]
    
    stock = stock.dropna()
    
    print(f"Downloaded {len(stock)} days of data!")
    print(stock.head())
    
    return stock

if __name__ == "__main__":
    data = load_stock_data()