## Tableau Dashboard Design – Plugging into the Future

This dashboard brings together KPIs, time series, regional comparisons, and geography to tell a cohesive story of electricity consumption across Indian states between January 2019 and December 2020.

---

### 1. Layout Overview

- **Dashboard title**:  
  **Plugging into the Future: Electricity Consumption Patterns in India (2019–2020)**

- **Zones (top to bottom)**:
  1. **Header and filters bar**
  2. **KPI summary cards**
  3. **Time series line chart**
  4. **Region comparison bar chart**
  5. **Geographic map of states**

The layout is designed for a 16:9 aspect ratio (e.g., 1366×768 or 1920×1080), with responsive containers to adapt to different screens.

---

### 2. KPI Summary Cards

- **Visualization type**: Four to five KPI tiles aligned horizontally.
- **Metrics**:
  1. **Total Consumption (2019–2020)** – `SUM(usage)` across full period.
  2. **Total 2019 vs 2020** – two numbers with percentage change.
  3. **Peak Month Consumption** – max monthly `SUM(usage)` and month label.
  4. **Largest Consuming State** – state name with its total usage.
  5. **Average Daily National Demand** – `AVG(daily usage)` aggregated nationally.
- **Design**:
  - Use consistent color palette (e.g., deep blue background with white text).
  - Include small trend icons or up/down arrows to indicate change vs previous year.
- **Purpose**:
  - Provide a compact overview for decision‑makers before they interact with detailed charts.

---

### 3. Time Series Line Chart (Central Focus)

- **Visualization type**: Line chart with optional banding or reference lines.
- **Fields**:
  - Columns: `date` (or `Month` = DATETRUNC('month', `date`))
  - Rows: `SUM(usage)`
  - Color: `Year` or `Lockdown Period` for emphasis.
- **Features**:
  - Vertical reference line on 24 March 2020 (start of lockdown).
  - Tooltip showing:
    - Exact date/month
    - Total national consumption
    - Optional breakdown by top 3 states.
- **Purpose**:
  - Anchor the narrative around how demand evolved over time and where disruptions occurred.

---

### 4. Region Comparison Bar Chart

- **Visualization type**: Horizontal bar chart
- **Fields**:
  - Rows: `region`
  - Columns: `SUM(usage)`
  - Color: `Year` or `Lockdown Period`
  - Tooltip: total consumption, share of national total, and YoY change.
- **Interactions**:
  - Acts as a **highlighter** for the map and line chart:
    - Selecting a region filters or highlights corresponding states and time series.
- **Purpose**:
  - Quickly compare energy usage across regions and identify leaders/laggards.

---

### 5. Geographic Map of States

- **Visualization type**: Filled map of Indian states
- **Fields**:
  - Geometry: state geocoding (either Tableau’s built‑in `State/Province` role or custom latitude/longitude).
  - Color: `SUM(usage)` or `AVG(usage)` over selected period.
  - Tooltip: state name, total consumption, rank among states, and regional membership.
- **Interactions**:
  - Clicking a state:
    - Filters the line chart to that state.
    - Filters/updates KPIs to show state‑level stats.
  - Hover tooltips highlight contextual information without navigating away.
- **Purpose**:
  - Make spatial patterns (e.g., coastal vs inland, industrial belts) visually obvious.

---

### 6. Global Filters and Controls

Place filters in a dedicated horizontal bar at the top or a vertical sidebar on the right:

- **Filters**:
  - `State` (multi‑select, with “All” default)
  - `Region` (multi‑select)
  - `Date Range` (from–to or quick year selector: 2019, 2020, both)
  - `Lockdown Period` (Before, After, Both)
- **Design considerations**:
  - Use single‑value dropdowns or multi‑select dropdowns for compactness.
  - Where helpful, use highlighters rather than hard filters to preserve context.

---

### 7. Usability and Performance Considerations

- Use **extracts** for the underlying dataset when publishing to Tableau Server/Public for faster loads.
- Limit the number of highly detailed charts on the initial dashboard; use drill‑down actions to open more granular views on demand.
- Avoid overly complex table calculations on the dashboard itself; pre‑aggregate when possible (e.g., monthly or quarterly views from the SQL layer).
- Make tooltips concise and focused on decision‑relevant metrics to keep the dashboard easy to read and performant.

