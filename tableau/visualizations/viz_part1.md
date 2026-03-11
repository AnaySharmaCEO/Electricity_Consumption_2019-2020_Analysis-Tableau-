## Tableau Visualization Plan – Part 1

This section focuses on high‑level comparisons of electricity consumption across 2019 and 2020, including total usage, regional breakdowns, and top/bottom states.

---

### 1. 2019 vs 2020 Total Consumption Over Time

- **Visualization type**: Dual line chart (or overlapping line chart)
- **Grain**: Monthly
- **Fields used**:
  - `date` (from `electricity_consumption.date`)
  - `usage` (SUM)
  - Derived fields:
    - `Year` = YEAR(`date`)
    - `Month` = DATETRUNC('month', `date`)
- **Layout**:
  - Columns: `Month`
  - Rows: `SUM(usage)`
  - Color: `Year` (2019 vs 2020)
- **Interpretation**:
  - Compare overall load profiles year‑over‑year.
  - Identify months where 2020 demand diverged sharply from 2019 (e.g., during lockdown and recovery).
  - Highlight seasonal peaks (summer, winter) and how they changed between the two years.

---

### 2. Total National Consumption (Overall KPI)

- **Visualization type**: KPI card / big number with comparison
- **Fields used**:
  - `usage` (SUM)
  - `Year`
- **Layout**:
  - Single number for total consumption in 2019.
  - Single number for total consumption in 2020.
  - Optional percent change indicator: \((\text{2020} - \text{2019})/\text{2019}\).
- **Interpretation**:
  - Provides a quick at‑a‑glance sense of whether overall national consumption increased or decreased.
  - Serves as a headline metric to anchor discussions in the dashboard and story.

---

### 3. Usage by Region (Aggregated)

*(Assumes `region` is populated or derived for states; if not, this can be treated as a design placeholder to be implemented once regional mappings are added.)*

- **Visualization type**: Horizontal bar chart
- **Fields used**:
  - `region`
  - `usage` (SUM)
  - `Year`
- **Layout**:
  - Columns: `SUM(usage)`
  - Rows: `region`
  - Color or Columns shelf: `Year` (side‑by‑side bars for 2019 vs 2020)
- **Interpretation**:
  - Compares total electricity consumption across major regions (e.g., Northern, Western, Southern, Eastern, North‑Eastern).
  - Highlights which regions are structurally more energy‑intensive.
  - Enables quick identification of regions with the strongest COVID‑era demand reductions or rebounds.

---

### 4. Top N and Bottom N States by Consumption

- **Visualization type**: Two separate bar charts or a single bar chart with dynamic Top N / Bottom N parameter
- **Fields used**:
  - `state`
  - `usage` (SUM)
  - `Year`
  - Parameters:
    - `N` (integer; default 10)
    - `Top/Bottom` selector (string parameter)
- **Layout (simple static version)**:
  - **Top N**:
    - Filter to 2019 or 2020 (or show both in separate sheets).
    - Sort states by `SUM(usage)` descending.
    - Keep first N states.
  - **Bottom N**:
    - Sort states ascending by `SUM(usage)`.
    - Keep first N states.
- **Layout (dynamic parameterized version)**:
  - Use a table calculation with INDEX() and the `Top/Bottom` parameter:
    - For Top N: `INDEX() <= [N]` on a descending sort.
    - For Bottom N: `INDEX() <= [N]` on an ascending sort.
- **Interpretation**:
  - Shows which states contribute the largest share of national demand (e.g., Maharashtra, Gujarat, Tamil Nadu).
  - Highlights smaller‑load states/UTs on the bottom end, which may still be critical from a grid stability or regional equity perspective.
  - When viewed by year, indicates whether state‑level rankings shifted between 2019 and 2020.

