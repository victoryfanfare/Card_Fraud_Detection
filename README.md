# Card Fraud Detection

Проект обнаружения мошеннических операций по банковским транзакциям.

- Целевая переменная: `Class` (0 - легитимная операция, 1 - мошенническая).
- Исходный набор: Kaggle Credit Card Fraud Detection (`creditcard.csv`).
- Данные и обученные модели не хранятся в Git; они находятся на Google Drive.
- Начальная выборка: `data/processed/initial_train.csv`.
- Новые порции: `data/incoming/batch_01.csv` - `batch_04.csv`.

## Структура
- `data/raw/` - исходный CSV
- `data/incoming/` - порции для обработки
- `data/processed/` - подготовленные данные
- `notebooks/` - анализ и моделирование
- `src/` - исходный код
- `models/` - обученные модели
- `api/` - API приложения
