
import numpy as np
import pandas as pd


def build_features(df, amount_median=None):
    """Создает дополнительные признаки для обнаружения мошеннических операций."""
    df = df.copy()

    df["amount_log1p"] = np.log1p(df["Amount"].clip(lower=0))
    df["time_hour_approx"] = (df["Time"] // 3600).astype(int)

    if amount_median is None:
        amount_median = df["Amount"].median()

    df["amount_vs_median"] = df["Amount"] / (amount_median + 1e-6)

    return df
