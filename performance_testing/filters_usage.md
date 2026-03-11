## Filters Usage and Performance Considerations in Tableau

Well‑designed filters are essential for a responsive and insightful dashboard. This document describes how filters are used in the Tableau artifacts for this project and how to keep them performant.

---

### 1. Core Filters

The primary filters exposed to users are:

1. **State filter**
   - Field: `state`
   - Type: multi‑select list or dropdown.
   - Scope: applies to time series, regional/state bar charts, and the map.
   - Purpose: zoom into specific states (e.g., Maharashtra, Gujarat) while retaining national context.

2. **Region filter**
   - Field: `region`
   - Type: multi‑select list.
   - Scope: affects region comparison charts, region‑wise state usage, and optionally the map.
   - Purpose: compare demand behavior across broad geographic groupings.

3. **Date / Year filter**
   - Fields:
     - `date`
     - Derived `Year` and `Quarter` calculated fields.
   - Type: range slider for `date` or quick filters for `Year` and `Quarter`.
   - Scope: used across nearly all views to constrain the analysis window (e.g., focusing only on 2020 or lockdown months).

4. **Lockdown Period filter**
   - Field: Calculated `Lockdown Period` (`Before Lockdown` vs `After Lockdown` based on 24 March 2020).
   - Type: single‑select or multi‑select list.
   - Scope: especially relevant for before/after charts and comparison KPIs.

---

### 2. Filter Strategy and Best Practices

- **Use dimension filters for slicing, not for heavy aggregation logic**:
  - Dimensions like `state`, `region`, and `Lockdown Period` are highly selective and ideal as filters.
  - Avoid overly complex table calculation filters for core interactivity when a simple dimension filter will do.

- **Limit high‑cardinality filters**:
  - The `state` filter has a manageable number of options (34).  
  - If more granular entities are added (e.g., districts), prefer cascading filters (Region → State → District) to maintain usability and performance.

- **Apply filters to relevant worksheets only**:
  - Use “Apply to selected worksheets” in Tableau so that heavy filters (e.g., date range) affect only the views that truly need them.
  - This reduces unnecessary query recomputation when a filter changes.

- **Use context filters judiciously**:
  - For example, make `Year` or `Lockdown Period` a context filter if many other filters depend on these subsets.
  - This can improve performance by restricting the dataset early in the query pipeline.

---

### 3. Interaction Between Filters and Actions

- **Highlight vs filter actions**:
  - Clicking on a region in the bar chart or a state in the map can drive **highlight actions** rather than hard filters.
  - Highlighting preserves the full data range while visually emphasizing the selected entity, which is often faster for Tableau to compute.

- **Story actions**:
  - Scenes in the Tableau story carry over filters where appropriate (e.g., selected region/state).
  - This enables viewers to follow a consistent thread (such as “Southern region”) across the national, regional, and recovery views without re‑filtering manually.

---

### 4. Performance Impact of Filters

Given the modest size of the dataset (~17k rows in the `electricity_consumption` table), filters have limited performance impact. Still, the design follows several safeguards:

- Filters are placed on indexed fields (`state`, `region`, `date`), which speeds up queries in SQLite.
- The dashboard avoids large cross‑tab tables; visuals aggregate data at monthly or quarterly granularity, which reduces the number of marks.
- When published to Tableau Public/Server, an **extract** is recommended:
  - Extracts are columnar and highly optimized for filtering and aggregation.

---

### 5. Recommendations for Scaling Up

If the dataset grows substantially (e.g., more years, more granular geographic levels), consider:

- Pre‑aggregating data at daily or monthly state level before loading to Tableau.
- Reducing the number of global filters and relying more on guided navigation (e.g., story points, parameter‑driven views).
- Using conditional filters (e.g., show top N states only) to keep mark counts manageable.

