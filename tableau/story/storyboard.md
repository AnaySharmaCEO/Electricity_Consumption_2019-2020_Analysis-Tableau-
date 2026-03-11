## Tableau Storyboard – Plugging into the Future

This storyboard guides the viewer through three scenes that explain how India’s electricity consumption evolved nationally, regionally, and during recovery from the COVID‑19 lockdown.

---

### Scene 1 – National Electricity Consumption Trend

- **Objective**: Introduce the overall demand pattern and contextualize the impact of COVID‑19 at the national level.

- **Key views**:
  - National **time series line chart** of `SUM(usage)` by month from January 2019 to December 2020.
  - KPI tiles for:
    - Total consumption in 2019 vs 2020.
    - Percentage change year‑over‑year.
    - Peak consumption month.
  - A vertical reference line marking the start of lockdown (24 March 2020).

- **Narrative points**:
  - Describe baseline consumption patterns in 2019 (seasonality, peaks, troughs).
  - Show how the 2020 line diverges around March–April when lockdown begins.
  - Quantify the total reduction in demand in 2020 relative to 2019.
  - Pose framing questions for the next scene: Which regions were most affected? Did all parts of the country behave similarly?

---

### Scene 2 – Regional Demand Differences

- **Objective**: Reveal how consumption patterns differ across regions and which states drive those differences.

- **Key views**:
  - **Region comparison bar chart**: `SUM(usage)` by `region` (with optional YoY change).
  - **Region-wise state usage** chart: hierarchical bar chart or treemap showing states nested within regions.
  - Optional small multiple line charts showing monthly usage by region.

- **Narrative points**:
  - Compare total regional loads (e.g., Western vs Southern vs Northern regions).
  - Highlight regions with steep drops during lockdown relative to their 2019 levels.
  - Drill down to state‑level views within a selected region to show which states are dominant drivers.
  - Discuss structural factors: industrial concentration, urbanization, and climate‑driven cooling/heating loads that differ by region.

- **Transition**:
  - Conclude by noting that while lockdown initially suppressed demand, the post‑lockdown trajectory is crucial: did regions bounce back or remain subdued?

---

### Scene 3 – Recovery After COVID Lockdown

- **Objective**: Focus on pre‑ and post‑lockdown behavior, measuring the depth of the dip and the speed of recovery.

- **Key views**:
  - **Before vs After Lockdown** bar chart:
    - `Lockdown Period` (Before vs After) on Columns.
    - `SUM(usage)` on Rows, broken down by state or region.
  - **Quarter-wise usage** chart:
    - Quarterly `SUM(usage)` for 2019 and 2020 (Q1–Q4).
  - Optional additional view:
    - Line chart zoomed in on 2020 only, from January to December, with a band highlighting lockdown months.

- **Narrative points**:
  - Quantify how much demand dropped immediately after lockdown compared with pre‑lockdown levels.
  - Show which states and regions rebounded fastest in the second half of 2020.
  - Highlight whether consumption in late 2020 overshot, matched, or remained below 2019 levels, suggesting possible structural change.
  - Conclude with policy/operational implications:
    - Grid planning under uncertainty.
    - The importance of monitoring sectoral demand composition.
    - How improved forecasting using such time‑series analytics can support future resilience.

---

### Storytelling Tips

- Use **annotations** on charts to mark key policy events (lockdown start, easing phases).
- Keep text captions concise and focused on insights rather than chart mechanics.
- Encourage **interactive exploration**:
  - Let viewers click regions or states in Scene 2 to see how their recovery paths look in Scene 3.
- Maintain consistent color encoding across scenes (e.g., same colors for regions and the same two colors for 2019 vs 2020) to reduce cognitive load.

