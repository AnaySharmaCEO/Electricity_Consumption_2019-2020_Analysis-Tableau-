from pathlib import Path

import pandas as pd


def get_project_root() -> Path:
    """
    Return the project root directory (the folder containing this script's parent).
    """
    return Path(__file__).resolve().parents[1]

def main() -> None:
    project_root = get_project_root()
    raw_path = project_root / "data" / "Consumption.csv"
    prepared_path = project_root / "data" / "prepared_consumption.csv"

    if not raw_path.exists():
        raise FileNotFoundError(f"Input CSV not found at {raw_path}")

    df = pd.read_csv(raw_path)

    # Normalise column names: first unnamed column is the datetime
    datetime_col = df.columns[0]
    df = df.rename(columns={datetime_col: "datetime"})

    # Basic data quality checks
    print("=== Raw dataset shape ===")
    print(df.shape)

    print("\n=== Missing values per column ===")
    print(df.isna().sum())

    duplicate_count = df.duplicated().sum()
    print(f"\n=== Duplicate rows ===\n{duplicate_count}")

    # Drop duplicate rows
    df_clean = df.drop_duplicates()

    # Convert datetime column to proper pandas datetime (day-first)
    df_clean["datetime"] = pd.to_datetime(df_clean["datetime"], dayfirst=True, errors="coerce")

    # Remove rows where datetime could not be parsed
    before_drop = len(df_clean)
    df_clean = df_clean.dropna(subset=["datetime"])
    after_drop = len(df_clean)
    print(f"\nDropped {before_drop - after_drop} rows with invalid datetime values.")

    print("\n=== Cleaned dataset shape ===")
    print(df_clean.shape)

    print("\n=== Descriptive statistics (numeric columns) ===")
    print(df_clean.describe().T)

    # Save cleaned dataset
    df_clean.to_csv(prepared_path, index=False)
    print(f"\nCleaned dataset written to {prepared_path}")


if __name__ == "__main__":
    main()