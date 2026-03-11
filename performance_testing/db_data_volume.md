## Database Data Volume and Table Information

### 1. Source Dataset

- **File**: `data/Consumption.csv`  
- **Rows**: 503 daily records (from 02/01/2019 to 05/12/2020).  
- **Columns**:
  - 1 datetime column (daily timestamp).
  - 34 state/UT usage columns (Punjab, Haryana, Rajasthan, Delhi, UP, Uttarakhand, HP, J&K, Chandigarh, Chhattisgarh, Gujarat, MP, Maharashtra, Goa, DNH, Andhra Pradesh, Telangana, Karnataka, Kerala, Tamil Nadu, Pondy, Bihar, Jharkhand, Odisha, West Bengal, Sikkim, Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Tripura).

The raw CSV is therefore relatively small, on the order of a few hundred kilobytes, which is ideal for rapid prototyping and Tableau exploration.

---

### 2. Database Design

- **Database**: `database/electricity.db` (SQLite)  
- **Primary table**: `electricity_consumption`

**Schema**:

- `id` – INTEGER, primary key, auto‑incremented.
- `state` – TEXT, name of the Indian state/UT.
- `region` – TEXT, regional grouping (optional, can be populated for advanced analytics).
- `latitude` – REAL, latitude of state centroid or representative point (optional).
- `longitude` – REAL, longitude of state centroid or representative point (optional).
- `date` – DATE, parsed from the datetime in the CSV (day‑first).
- `usage` – REAL, electricity consumption in Mega Units (MU).

Indexes:

- `idx_electricity_consumption_state_date` on (`state`, `date`).
- `idx_electricity_consumption_region_date` on (`region`, `date`).

These indexes are chosen to accelerate the most common analytical patterns: time‑series by state and region, year/quarter aggregations, and before/after lockdown comparisons.

---

### 3. Row Volume in the Analytical Table

The ingestion script (`scripts/load_to_db.py`) reshapes the wide CSV into a **long** table:

- For each date row, there is one record per state/UT.
- Approximate row count:
  - 503 daily rows × 34 states ≈ **17,102 rows**.

This row volume is modest for SQLite and for Tableau extracts:

- **SQLite performance**:
  - Full table scans and grouped aggregations (by state, region, year, or quarter) are effectively instantaneous on typical hardware.
  - Indexes further reduce query time for date‑filtered and state‑filtered views.
- **Tableau performance**:
  - Extracts created from ~17k rows load very quickly in Tableau Desktop and Tableau Public.
  - Aggregations at month/quarter/year grain are trivial in terms of computational cost.

---

### 4. Performance Considerations and Headroom

- The current dataset easily fits into memory for both Python (pandas) and Tableau.
- The schema and indexes are designed to scale to **hundreds of thousands** of rows without structural changes:
  - Additional years can be appended by simply re‑running or extending the ingestion process.
  - Region, latitude, and longitude attributes can be back‑filled later without altering the core analytics.
- For much larger datasets (millions of rows), recommended optimizations would include:
  - Partitioning by year or region at the database level.
  - Pre‑aggregating to daily or monthly state totals before exposing to Tableau.
  - Using Tableau extracts rather than live connections in production dashboards.

