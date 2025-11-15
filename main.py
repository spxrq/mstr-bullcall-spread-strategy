import yfinance as yf
import pandas as pd
import os
from typing import List, Dict

# Start Date of MSTR's Treasury Strategy
START_DATE = "2018-08-11"


def download_and_save_tickers(tickers: List[str], start: str = START_DATE, data_path: str = "data") -> Dict[str, pd.DataFrame]:
    os.makedirs(data_path, exist_ok=True)
    results: Dict[str, pd.DataFrame] = {}
    for ticker in tickers:
        df = yf.download(ticker, start=start, auto_adjust=True)
        filename = f"{ticker}.csv"
        if df is not None and not df.empty:
            df.to_csv(os.path.join(data_path, filename))
        results[ticker] = df
    return results

if __name__ == "__main__":
    tickers = ["BTC-USD", "MSTR"]
    downloaded = download_and_save_tickers(tickers)
    for ticker, df in downloaded.items():
        if df is None:
            print(f"{ticker}: download returned None")
        elif df.empty:
            print(f"{ticker}: downloaded but df is empty")
        else:
            print(f"{ticker} saved {len(df)} rows to data/{ticker}.csv")