## Dashboard Documentation

This document describes the Tableau dashboard built for the project **“Plugging into the Future: An Exploration of Electricity Consumption Patterns”**.

---

### 1. Dashboard Objectives

The dashboard is designed to:

- Provide a **national overview** of electricity usage trends across 2019–2020.
- Allow users to **compare states and regions** quickly.
- Highlight the **impact of COVID‑19 lockdown** on electricity demand.
- Serve as a navigational hub for deeper analysis and for the Tableau story.

---

### 2. Layout Summary

The dashboard comprises four primary components:

1. **Header and Filter Bar**
   - Title: “Plugging into the Future – Electricity Consumption Patterns”
   - Filters:
     - State
     - Region
     - Date range / Year
     - Lockdown period (Before/After)

2. **KPI Summary Row**
   - Tiles showing:
     - Total national consumption (2019–2020).
     - 2019 vs 2020 totals and percent change.
     - Peak month consumption.
     - Largest consuming state.

3. **Central Time Series Panel**
   - Monthly national consumption with 2019 and 2020 lines.
   - Lockdown start date (24 March 2020) annotated as a reference line.

4. **Regional and Spatial Views**
   - Region comparison bar chart (usage by region, optionally split by year).
   - Filled map of India highlighting state‑level consumption and linking to state‑specific drill‑downs.

---

### 3. User Interactions

- **Filtering**:
  - Selecting a state or region updates all relevant views in the dashboard.
  - Date and lockdown period filters allow focused analysis of the COVID era.

- **Drill‑down**:
  - Clicking on a region bar can filter the map and time series to that region.
  - Selecting a state on the map highlights that state in the bar charts and updates KPIs to a state‑specific view.

- **Tooltips**:
  - Provide additional detail (exact consumption values, year‑over‑year change, national share) without cluttering the canvas.

---

### 4. Data Source

- Primary source table: `electricity_consumption` in `database/electricity.db`.
- Connection mode:
  - **Recommended**: Tableau extract for production deployment.
  - Development: live connection to SQLite or extracted CSV as needed.

The table contains one row per (`state`, `date`), which supports efficient filtering and aggregation at daily, monthly, and quarterly levels.

---

### 5. Performance Considerations

- The source dataset is relatively small (~17k rows), which makes queries and visual updates fast.
- Indexes on `state`, `region`, and `date` in SQLite reduce response times for state/region/date filters.
- To keep the dashboard responsive:
  - Use only essential filters in the global filter bar.
  - Avoid high‑mark views; aggregate to daily or monthly grain rather than plotting all raw points where not necessary.
  - Prefer highlight actions over heavy cross‑filters when appropriate.

---

### 6. Future Enhancements

- Add a second dashboard for **forecasting and scenario analysis** once predictive models are built.
- Include **sectoral split** (industrial, commercial, residential) if additional source data is available.
- Integrate **performance monitoring** metrics (e.g., dashboard load time, extract refresh duration) for production deployments.

