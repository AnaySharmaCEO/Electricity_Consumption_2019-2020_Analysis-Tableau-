## Data Preparation and Validation

This document describes how the raw POSOCO‑derived dataset is validated, cleaned, and prepared for downstream analysis and visualization.

---

### 1. Input and Output Files

- **Raw input**:  
  `data/Consumption.csv`

- **Prepared output**:  
  `data/prepared_consumption.csv`

Both files are maintained within the `electricity-consumption-analysis` project so that the entire pipeline is reproducible.

---

### 2. Preparation Script – `scripts/data_preparation.py`

The `data_preparation.py` script performs the following steps:

1. **Read the raw CSV**:
   - Uses `pandas.read_csv` to load `Consumption.csv`.
   - The first column in the CSV has an empty header; the script renames it to `datetime`.

2. **Initial inspection**:
   - Prints the raw dataset shape (rows, columns).
   - Prints the count of missing values per column.
   - Counts duplicate rows with `df.duplicated().sum()`.

3. **De‑duplication**:
   - Drops exact duplicate rows using `drop_duplicates()`.

4. **Datetime parsing**:
   - Converts the `datetime` column from string to pandas `datetime64` using:
     - `pd.to_datetime(..., dayfirst=True, errors="coerce")`
   - The `dayfirst=True` flag matches the source format: `DD/MM/YYYY HH:MM:SS`.
   - Any unparsable values become `NaT` and are removed in the next step.

5. **Invalid date handling**:
   - Drops rows where `datetime` is null after parsing.
   - Reports how many rows were removed at this stage.

6. **Descriptive statistics**:
   - Outputs `df_clean.describe().T` to summarize distribution of consumption values across states (count, mean, min/max, quartiles).

7. **Persist cleaned data**:
   - Writes the cleaned dataset to `data/prepared_consumption.csv` without the pandas index.

---

### 3. Prepared Dataset Characteristics

After preparation:

- **Datetime column**:
  - Is guaranteed to be a proper datetime type.
  - No invalid or missing datetime rows remain.

- **Consumption columns**:
  - Remain numeric float columns representing daily usage in MU.
  - Any obvious structural duplicates or corrupt rows have been removed.

- **Shape**:
  - Rows: Same as or slightly fewer than the raw file, depending on duplicates and parsing errors.
  - Columns: 1 datetime column (`datetime`) + 34 state/UT consumption columns.

This “prepared” file is suitable both for:

- Direct use in Tableau (for quick prototypes).
- Further transformation into a long analytical format for the database layer.

---

### 4. Relationship to Database Ingestion

The ingestion script (`scripts/load_to_db.py`) can operate on either:

- The original `Consumption.csv`, or
- The cleaned `prepared_consumption.csv` (recommended for strict pipelines).

In both cases, the target structure in SQLite is a **long format** table:

- One row per (`state`, `date`), with:
  - `state`, `region`, `latitude`, `longitude`, `date`, `usage`.

Ensuring the datetime column is properly parsed and the dataset is free from duplicates significantly simplifies this reshaping step and reduces the risk of subtle time‑series errors later in analysis.

