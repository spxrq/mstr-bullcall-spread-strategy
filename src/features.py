import pandas as pd
import numpy as np

class SignalFeatures:
    "Indicators for daily price closes"

    def __init__(self, df: pd.DataFrame, price_col: str = "Close"):
        df = df.copy()
        self.df = df
        self.price_col = price_col

    def add_ema(self, span: int = 21):
        self.df[f"EMA_{span}"] = self.df[self.price_col].ewm(span=span, adjust=False).mean()
        return self.df

    def add_standardized_return(self, window: int = 30):
        ret = self.df[self.price_col].pct_change()
        rolling_std = ret.rolling(window=window).std()
        self.df[f"z_{window}"] = ret / rolling_std
        return self.df

