## Visualization Design – Electricity Consumption Analytics

This document summarizes the key visualizations designed for the project and how they connect to the analytical questions.

---

### 1. Design Principles

- **Clarity first**: Every view answers a concrete question (e.g., “Which states consume the most electricity?” or “How did national demand change after lockdown?”).
- **Consistent encoding**:
  - Time is almost always on the x‑axis.
  - Usage (MU) is on the y‑axis or represented by color intensity.
  - Regions and states use consistent color palettes throughout.
- **Drill‑down friendly**:
  - High‑level national and regional views link to more granular state‑level and quarter‑level views.
- **Performance‑aware**:
  - Aggregations are primarily at daily, monthly, or quarterly grain.
  - Visuals are designed to work efficiently even as more data is added.

---

### 2. Core Questions and Corresponding Views

1. **How has national electricity consumption evolved over time?**
   - View: National time series line chart (monthly, 2019 vs 2020).
   - Highlight: A vertical reference line at the March 2020 lockdown, plus KPI cards comparing total 2019 vs 2020 usage.

2. **Which states and regions consume the most electricity?**
   - Views:
     - Top N / Bottom N states bar charts.
     - Region comparison bar chart.
     - Region‑wise state usage hierarchy.
   - Insight: Identifies major load centers and smaller but strategically important states/UTs.

3. **How does seasonality affect demand?**
   - Views:
     - Month‑wise consumption charts for the nation and for each region.
     - Quarter‑wise usage for both 2019 and 2020.
   - Insight: Reveals expected seasonal peaks (summer, monsoon, winter) and any deviations during 2020.

4. **What was the impact of COVID‑19 lockdown on demand?**
   - Views:
     - Before vs After Lockdown bar charts.
     - 2020‑only time series with the lockdown period highlighted.
   - Insight: Quantifies both the depth and the duration of the demand shock and subsequent recovery.

---

### 3. Mapping to Tableau Workbooks

The visualization plans are broken into three markdown files under `tableau/visualizations`:

- `viz_part1.md` – 2019 vs 2020 comparison, total consumption KPIs, regional usage, and Top/Bottom N states.
- `viz_part2.md` – month‑wise and region‑wise temporal patterns, plus before/after lockdown comparisons.
- `viz_part3.md` – region‑wise state drill‑down, quarter‑wise analysis, and year‑level summaries.

Each file provides:

- Recommended chart type.
- Fields to use (dimensions, measures, derived fields).
- Interpretation guidance for stakeholders.

---

### 4. Dashboard and Story Integration

- **Dashboard**:
  - consolidates KPI cards, the national time series, region comparison bars, and the geographic map into a single interactive surface.  
  - Filters (state, region, date, lockdown period) apply across all relevant charts.

- **Story**:
  - arranges views into three scenes:
    1. National trend overview.
    2. Regional differences.
    3. Recovery after lockdown.
  - Each scene uses annotations and narrative captions to walk the audience through the analytic findings.

---

### 5. Extensibility

The current set of visuals can be extended in several directions:

- Adding sectoral breakdowns (industrial, commercial, residential) if data becomes available.
- Introducing forecast views (e.g., ARIMA or Prophet models trained on the 2019–2020 series).
- Creating “what‑if” scenarios (e.g., alternative lockdown timings, renewable penetration impacts).

Because the underlying schema is long and time‑series friendly, most new visuals can be layered on without structural database changes.

