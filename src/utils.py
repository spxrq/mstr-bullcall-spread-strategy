import pandas as pd

def rolling_correlation(series1: pd.Series, series2: pd.Series, window: int = 20) -> pd.Series:
    """
    Compute rolling correlation between two aligned price series.
    """
    return series1.rolling(window=window).corr(series2)
