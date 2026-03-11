## Visualizations Count and Inventory

This document lists and categorizes all planned visualizations in the project to support performance testing and coverage analysis.

---

### 1. Core Dashboard Views

1. **KPI Summary Cards** (1 composite view)
   - Total national consumption (2019–2020)
   - Total 2019 consumption
   - Total 2020 consumption
   - Peak month consumption
   - Largest consuming state

2. **National Time Series Line Chart** (1 view)
   - Monthly `SUM(usage)` with 2019 vs 2020 comparison and lockdown reference line.

3. **Region Comparison Bar Chart** (1 view)
   - `SUM(usage)` by region, optionally split by year or lockdown period.

4. **Geographic Map of States** (1 view)
   - Filled map of Indian states colored by consumption with interactive tooltips and filters.

**Subtotal (dashboard)**: 4 main visual components (plus multiple KPI tiles).

---

### 2. Analytical Sheets – Part 1 (viz_part1.md)

5. **2019 vs 2020 Consumption Over Time** – dual line chart.
6. **Total National Consumption KPI** – big number with YoY change.
7. **Usage by Region** – horizontal bar chart.
8. **Top N States by Consumption** – bar chart.
9. **Bottom N States by Consumption** – bar chart.

**Subtotal (Part 1)**: 5 distinct sheets.

---

### 3. Analytical Sheets – Part 2 (viz_part2.md)

10. **Month-wise National Consumption** – line or area chart.
11. **Region-wise Monthly Consumption** – small multiples or stacked bar chart.
12. **Before vs After Lockdown (National)** – side‑by‑side bar chart.
13. **Before vs After Lockdown by State** – clustered bar chart per state.

**Subtotal (Part 2)**: 4 distinct sheets.

---

### 4. Analytical Sheets – Part 3 (viz_part3.md)

14. **Region-wise State Usage (Drill‑down)** – hierarchical bar chart.
15. **Quarter-wise National Usage** – clustered bar chart by quarter and year.
16. **Quarter-wise Regional Usage** – bar chart with region color encoding.
17. **Usage by Year Summary** – simple bar chart with annotations.

**Subtotal (Part 3)**: 4 distinct sheets.

---

### 5. Story Views (Storyboard Scenes)

These scenes reuse existing sheets but combine and annotate them for narrative:

18. **Scene 1 – National Trend**:
    - National time series + KPIs.
19. **Scene 2 – Regional Differences**:
    - Region comparison bar chart + region‑wise state usage.
20. **Scene 3 – Recovery After Lockdown**:
    - Before/after lockdown bars + quarter‑wise usage.

**Subtotal (Story)**: 3 storyboard scenes (no new heavy queries beyond the underlying sheets).

---

### 6. Overall Visualization Footprint

- **Total distinct analytical sheets**: ~13–15 (depending on separation of Top/Bottom N and quarter views).  
- **Dashboard pages**: 1 main dashboard (with multiple components).  
- **Story pages**: 3 scenes.

From a performance perspective:

- The number of worksheets is modest.
- Each worksheet aggregates a relatively small dataset (~17k rows in the long table).
- Performance tuning mainly involves:
  - Efficient filters and actions.
  - Using extracts on Tableau Server/Public.
  - Avoiding unnecessary table calculations on the dashboard‑level sheets.

