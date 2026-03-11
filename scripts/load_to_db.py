import sqlite3
from pathlib import Path

import pandas as pd


def get_project_root() -> Path:
    """
    Return the project root directory (the folder containing this script's parent).
    """
    return Path(__file__).resolve().parents[1]


def load_schema(conn: sqlite3.Connection, schema_path: Path) -> None:
    """
    Execute the SQL schema file to create the required tables and indexes.
    """
    with schema_path.open("r", encoding="utf-8") as f:
        schema_sql = f.read()
    conn.executescript(schema_sql)


def transform_wide_to_long(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform the wide-format consumption dataframe into a long analytical format.

    Input format (wide):
        - First column: datetime string (no header in raw CSV)
        - Remaining columns: one column per state/UT with numeric usage values

    Output format (long):
        - Columns: state, region, latitude, longitude, date, usage
    """
    # The first column in the raw CSV header is empty, pandas will name it something like 'Unnamed: 0'
    datetime_col = df.columns[0]
    df = df.rename(columns={datetime_col: "datetime"})

    # Melt wide state columns into a single 'state' dimension
    long_df = df.melt(
        id_vars=["datetime"],
        var_name="state",
        value_name="usage",
    )

    # Parse datetime; the source uses day-first format like '02/01/2019 00:00:00'
    long_df["date"] = pd.to_datetime(long_df["datetime"], dayfirst=True, errors="coerce")

    # Optional attributes – left NULL for now but included for schema compatibility
    long_df["region"] = pd.NA
    long_df["latitude"] = pd.NA
    long_df["longitude"] = pd.NA

    # Reorder columns to match the database schema
    long_df = long_df[["state", "region", "latitude", "longitude", "date", "usage"]]

    # Drop rows where date or usage is missing after parsing
    long_df = long_df.dropna(subset=["date", "usage"])

    return long_df


def main() -> None:
    project_root = get_project_root()

    csv_path = project_root / "data" / "Consumption.csv"
    db_path = project_root / "database" / "electricity.db"
    schema_path = project_root / "database" / "schema.sql"

    if not csv_path.exists():
        raise FileNotFoundError(f"Input CSV not found at {csv_path}")

    # Load the raw CSV
    df_raw = pd.read_csv(csv_path)

    # Transform into long analytical format
    df_long = transform_wide_to_long(df_raw)

    # Connect to SQLite and apply schema
    conn = sqlite3.connect(db_path)
    try:
        load_schema(conn, schema_path)

        # Insert data into the electricity_consumption table
        df_long.to_sql(
            "electricity_consumption",
            conn,
            if_exists="append",
            index=False,
        )

        # Confirm number of rows inserted
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM electricity_consumption;")
        (row_count,) = cur.fetchone()
        print(f"Total rows in electricity_consumption: {row_count}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()

