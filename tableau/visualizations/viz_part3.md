## Tableau Visualization Plan – Part 3

This section focuses on regional–state drill‑downs, quarterly behavior, and year‑level summaries.

---

### 1. Region-wise State Usage (Drill-down View)

- **Visualization type**: Hierarchical bar chart (Region → State)
- **Fields used**:
  - `region`
  - `state`
  - `usage` (SUM)
  - `Year`
- **Layout**:
  - Rows: `region`, then `state` (placed beneath `region` for hierarchy)
  - Columns: `SUM(usage)`
  - Color: `region` or `Year`
  - Filters:
    - `Year` (2019, 2020, or both)
    - Optional `Lockdown Period` (pre/post lockdown calculated field)
- **Interaction**:
  - Allow users to expand/collapse each region to see contribution of individual states.
  - Optional highlight action from a map or KPI section to focus on a specific region.
- **Interpretation**:
  - Across each region, identifies the major consuming states and smaller contributors.
  - Useful for explaining why some regions show high totals—driven by a few very large states or a broad base of medium‑load states.

---

### 2. Quarter-wise Usage (National and Regional)

- **Visualization type**: Clustered bar chart
- **Fields used**:
  - `date`
  - `usage` (SUM)
  - Calculated:
    - `Year` = YEAR(`date`)
    - `Quarter` =
      - Q1: Jan–Mar
      - Q2: Apr–Jun
      - Q3: Jul–Sep
      - Q4: Oct–Dec
  - Optional: `region`
- **Layout (national view)**:
  - Columns: `Quarter`
  - Rows: `SUM(usage)`
  - Color: `Year`
  - Filters: `Year`, optional `Lockdown Period`
- **Layout (regional view)**:
  - Columns: `Quarter`
  - Rows: `SUM(usage)`
  - Color: `region`
  - Filters: `Year`
- **Interpretation**:
  - Shows quarter‑to‑quarter demand changes within each year and across years.
  - Helps compare COVID‑affected quarters (e.g., Q2 2020) vs reference quarters (e.g., Q2 2019).
  - Exposes whether some regions recovered more quickly in late 2020.

---

### 3. Usage by Year (High-Level Summary)

- **Visualization type**: Simple bar chart with annotations
- **Fields used**:
  - `Year`
  - `usage` (SUM)
- **Layout**:
  - Columns: `Year`
  - Rows: `SUM(usage)`
  - Label: `SUM(usage)` formatted in GWh/MU with thousand separators.
  - Optional reference line: average yearly consumption across the period.
- **Interpretation**:
  - Provides an easily digestible summary of how total annual electricity consumption evolved across 2019 and 2020.
  - When combined with lockdown insights, frames the big picture: whether demand shifted structurally or largely reverted by late 2020.

