
import numpy as np
import pandas as pd


def check_quality(df):
    """Проверяет качество данных и возвращает список найденных проблем."""
    issues = []

    if df.isna().any().any():
        issues.append(f"Пропуски: {int(df.isna().sum().sum())}")

    duplicates = int(df.duplicated().sum())
    if duplicates:
        issues.append(f"Полные дубликаты: {duplicates}")

    if "Class" not in df.columns:
        issues.append("Отсутствует целевой столбец Class")
    elif not df["Class"].isin([0, 1]).all():
        issues.append("Class содержит значения, отличные от 0 и 1")

    if "Amount" in df.columns and (df["Amount"] < 0).any():
        issues.append("Amount содержит отрицательные значения")

    numeric = df.select_dtypes(include="number")
    if np.isinf(numeric.to_numpy()).any():
        issues.append("Числовые столбцы содержат бесконечные значения")

    return issues
