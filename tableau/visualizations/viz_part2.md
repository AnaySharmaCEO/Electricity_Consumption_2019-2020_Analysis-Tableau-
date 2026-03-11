## Tableau Visualization Plan – Part 2

This section focuses on temporal seasonality, regional trends, and demand changes around the COVID‑19 lockdown.

---

### 1. Month-wise National Consumption

- **Visualization type**: Line chart or area chart
- **Fields used**:
  - `date`
  - `usage` (SUM)
  - Derived:
    - `Month` = DATETRUNC('month', `date`)
    - `Year` = YEAR(`date`)
- **Layout**:
  - Columns: `Month`
  - Rows: `SUM(usage)`
  - Color: `Year` (two lines – 2019 vs 2020)
  - Optional filter: `Year` (to view each year in isolation).
- **Interpretation**:
  - Reveals seasonal patterns such as summer peaks or monsoon/winter troughs.
  - Highlights any structural shift in the 2020 seasonal pattern compared with 2019, particularly around March–May (lockdown period).

---

### 2. Region-wise Monthly Consumption

- **Visualization type**: Small multiples of line charts or stacked bar chart
- **Fields used**:
  - `region`
  - `date`
  - `usage` (SUM)
  - `Month` (DATETRUNC('month', `date`))
  - `Year`
- **Layout (option A – small multiples)**:
  - Rows: `region`
  - Columns: `Month`
  - Rows shelf: `SUM(usage)`
  - Color: `Year`
- **Layout (option B – stacked bars)**:
  - Columns: `Month`
  - Rows: `SUM(usage)`
  - Color: `region`
  - Filter: `Year`
- **Interpretation**:
  - Compares how each region’s demand evolves month‑by‑month.
  - Surfaces regions with particularly high seasonality or volatility.
  - Aids regional planners in assessing whether changes are structural or seasonal.

---

### 3. Usage Before and After Lockdown

- **Visualization type**: Side‑by‑side bar chart or clustered column chart
- **Lockdown definition**:
  - **Before lockdown**: dates \< 24 March 2020
  - **After lockdown**: dates ≥ 24 March 2020
- **Fields used**:
  - `state`
  - `date`
  - `usage` (SUM or AVG)
  - Calculated field:
    - `Lockdown Period` =
      - `'Before Lockdown'` if `DATE([date]) < #24/03/2020#`
      - `'After Lockdown'` otherwise
- **Layout (state‑level comparison)**:
  - Columns: `state`
  - Rows: `SUM(usage)` or `AVG(usage)` (depending on focus)
  - Color: `Lockdown Period`
  - Filter: `Year` = 2020 (optional to focus only on 2020).
- **Layout (national summary)**:
  - Columns: `Lockdown Period`
  - Rows: `SUM(usage)`
  - Color: `Lockdown Period`
- **Interpretation**:
  - Quantifies the magnitude of demand reduction during lockdown relative to pre‑lockdown levels, by state and nationally.
  - Shows which states had the sharpest proportional drop, potentially linked to industrial/commercial composition.
  - When used with average daily consumption, isolates structural load change from the effect of differing numbers of days.

