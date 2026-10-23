
import numpy as np
import pandas as pd


def clean(df):
    """Очищает данные и возвращает очищенный DataFrame и число удаленных дубликатов."""
    df = df.copy()

    numeric_columns = [
        "Time",
        *[f"V{i}" for i in range(1, 29)],
        "Amount",
        "Class"
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.dropna(subset=numeric_columns)
    df = df[df["Class"].isin([0, 1])]

    before = len(df)
    df = df.drop_duplicates()
    removed_duplicates = before - len(df)

    return df.reset_index(drop=True), removed_duplicates
