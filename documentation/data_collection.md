## Data Collection – Electricity Consumption Dataset

### 1. Project Context

This project, **“Plugging into the Future: An Exploration of Electricity Consumption Patterns”**, analyses electricity usage across Indian states between **January 2019 and December 2020**. The underlying dataset is derived from POSOCO weekly energy reports and structured into a daily, state‑level time series.

---

### 2. Source and Acquisition

- **Primary source**:  
  Power System Operation Corporation Limited (POSOCO) weekly energy reports for India.

- **Data captured**:
  - Daily energy consumption for each major Indian state and union territory.
  - Values expressed in **Mega Units (MU)**.

- **Extraction process (conceptual)**:
  1. Download weekly energy reports from the POSOCO website.
  2. Parse daily consumption records for each state/UT.
  3. Normalize all values to a consistent unit (MU).
  4. Aggregate weekly files into a single consolidated CSV.

The consolidated dataset is made available in the repository as `data/Consumption.csv`.

---

### 3. File Structure – `Consumption.csv`

- **Location**: `electricity-consumption-analysis/data/Consumption.csv`
- **Shape**:
  - **Rows**: 503 data rows (one per date) plus header.
  - **Columns**: 35 total
    - 1 datetime column (first column, unnamed in the raw file).
    - 34 numeric columns, one per state/UT:
      - `Punjab, Haryana, Rajasthan, Delhi, UP, Uttarakhand, HP, J&K, Chandigarh, Chhattisgarh, Gujarat, MP, Maharashtra, Goa, DNH, Andhra Pradesh, Telangana, Karnataka, Kerala, Tamil Nadu, Pondy, Bihar, Jharkhand, Odisha, West Bengal, Sikkim, Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Tripura`.

- **Date/time format**:
  - Values like `02/01/2019 00:00:00`.
  - Interpreted as **day‑first**: `DD/MM/YYYY HH:MM:SS`.

---

### 4. Assumptions and Limitations

- **Temporal coverage**:
  - The dataset spans from early **January 2019** to **December 2020**, but exact start/end points are governed by available POSOCO reports.
  - Each row represents a single day; missing days (if any) should be handled as gaps during analysis.

- **Geographic coverage**:
  - Includes major Indian states and union territories represented in POSOCO reports.
  - Some smaller UTs or special regions may be aggregated or absent.

- **Quality assumptions**:
  - Values are assumed to be validated by POSOCO at source.
  - No manual editing of consumption figures is performed in this project; all transformations are structural (reshaping, type conversions, aggregations).

---

### 5. Usage in the Project Workflow

The raw CSV is the starting point for the rest of the analytics stack:

1. **Data preparation**:
   - `scripts/data_preparation.py` reads `Consumption.csv`, cleans it, and writes `prepared_consumption.csv`.
2. **Database ingestion**:
   - `scripts/load_to_db.py` reshapes the dataset into a long analytical format and loads it into `database/electricity.db`.
3. **Analytics and visualization**:
   - SQL queries in `scripts/sql_queries.sql` read from the SQLite database.
   - Tableau dashboards connect to the prepared analytical view for interactive exploration.

This separation between raw collection, preparation, and analysis helps keep the project maintainable, auditable, and easy to extend as new POSOCO data becomes available.

