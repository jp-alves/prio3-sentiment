import yfinance as yf, pandas as pd

df = (yf.Ticker("PRIO3.SA")          
        .history(start="2015-01-01", end="2024-12-31")
        .reset_index())

df.to_csv("data/raw/prio3_prices.csv", index=False)