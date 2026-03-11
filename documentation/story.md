## Tableau Story Documentation

This document describes the Tableau story that presents the findings from the electricity consumption analysis in a narrative, step‑by‑step format.

---

### 1. Story Title and Theme

- **Title**: Plugging into the Future – How India’s Electricity Demand Evolved Through COVID‑19  
- **Theme**: The story shows how electricity consumption changed nationally, varied by region, and recovered after the COVID‑19 lockdown using three concise scenes.

---

### 2. Scene 1 – National Electricity Consumption Trend

- **Purpose**:
  - Establish baseline demand patterns for 2019 and 2020.
  - Highlight the timing and initial impact of the COVID‑19 lockdown.

- **Key visuals**:
  - Monthly national time series for 2019 and 2020.
  - KPI tiles summarizing total consumption and year‑over‑year change.
  - Lockdown reference line on 24 March 2020.

- **Key messages**:
  - 2019 provides the “normal” reference profile.
  - 2020 follows a similar trajectory initially, then deviates around the onset of lockdown.
  - Overall national demand in 2020 is compared to 2019 to quantify the high‑level impact.

---

### 3. Scene 2 – Regional Demand Differences

- **Purpose**:
  - Show that the impact of COVID‑19 on electricity demand was not uniform across India.
  - Reveal which regions and states drive national trends.

- **Key visuals**:
  - Region comparison bar chart showing total consumption by region.
  - Region‑wise state usage hierarchy (e.g., bar chart or treemap with states nested under regions).
  - Optional small multiple line charts: monthly consumption by region.

- **Key messages**:
  - Some regions are structurally higher‑load due to industrial concentration and urbanization.
  - Lockdown effects vary by region; some show sharper drops and slower recoveries.
  - Within each region, a few states often account for the majority of the consumption.

---

### 4. Scene 3 – Recovery After COVID Lockdown

- **Purpose**:
  - Examine how quickly (and fully) electricity demand rebounded after lockdown.

- **Key visuals**:
  - Before vs After Lockdown comparison for states and/or regions.
  - Quarter‑wise usage chart contrasting 2019 and 2020 (Q1–Q4).
  - 2020 time series zoomed in on the lockdown and post‑lockdown period.

- **Key messages**:
  - Quantifies the drop in demand during lockdown months relative to pre‑lockdown levels.
  - Shows which states/regions returned to near‑normal consumption, and which remained subdued.
  - Provides evidence for whether demand changes were temporary shocks or indicate longer‑term shifts.

---

### 5. Navigation and User Guidance

- Scene captions provide:
  - A one‑sentence summary of the main takeaway.
  - Brief instructions on how to interact with filters (e.g., “Select a region to see its states’ recovery path.”).
- Consistent color schemes:
  - Same colors for regions across all scenes.
  - Same two colors for 2019 vs 2020 lines and bars.
- Tooltips:
  - Are concise, focusing on values, year, region/state, and percent changes where relevant.

---

### 6. Extensibility

The current 3‑scene story can be extended or refined:

- Add a **Scene 4** focused on forecasting or future scenarios once models are developed.
+- Introduce **sectoral stories** (e.g., industrial vs residential demand) when sector‑level data becomes available.
  - Include **data quality and methodology** scene for stakeholders who want to understand the pipeline behind the visuals.

