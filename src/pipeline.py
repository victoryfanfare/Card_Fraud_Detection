
from data_quality import check_quality
from data_preprocessing import clean
from feature_engineering import build_features


def run_pipeline(df, amount_median=None):
    """Проверяет, очищает и преобразует данные."""

    clean_df, removed_duplicates = clean(df)

    quality_issues = check_quality(clean_df)

    if quality_issues:
        raise ValueError(
            "Обнаружены проблемы с качеством данных: "
            + "; ".join(quality_issues)
        )

    featured_df = build_features(
        clean_df,
        amount_median=amount_median
    )

    return featured_df, removed_duplicates
