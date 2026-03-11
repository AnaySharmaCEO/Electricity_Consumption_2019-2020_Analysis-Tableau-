## Project Workflow – Plugging into the Future

This document describes the end‑to‑end workflow for the project **“Plugging into the Future: An Exploration of Electricity Consumption Patterns”**.

---

### 1. Overview

The project implements a full analytics pipeline:

1. **Data ingestion and collection** from POSOCO weekly reports into a consolidated CSV.
2. **Data validation and preparation** using Python and pandas.
3. **Database storage and SQL analysis** using SQLite.
4. **Visualization and dashboarding** in Tableau.
5. **Narrative storytelling** via a Tableau story.
6. **Web integration** using a minimal Flask app.

Each step is documented and automated where possible so the repository is production‑ready and easy to extend.

---

### 2. Data Ingestion

1. **Source**:
   - POSOCO weekly energy reports (India).
2. **Consolidation**:
   - Extract daily state‑level consumption from each weekly report.
   - Normalize to a consistent unit (MU) and consistent column naming.
   - Combine into a single file: `data/Consumption.csv`.
3. **Assumptions**:
   - The consolidated CSV already reflects high‑quality, validated data from the source.

See `documentation/data_collection.md` for more detail.

---

### 3. Data Preparation

1. **Script**: `scripts/data_preparation.py`
2. **Steps**:
   - Read `data/Consumption.csv`.
   - Rename the first, unnamed column to `datetime`.
   - Inspect for missing values and duplicates.
   - Drop exact duplicate rows.
   - Parse `datetime` with day‑first semantics and drop rows where parsing fails.
   - Output descriptive statistics for numeric columns.
   - Write cleaned data to `data/prepared_consumption.csv`.

See `documentation/data_preparation.md` for details.

---

### 4. Database Storage and SQL Analysis

1. **Schema**:
   - Defined in `database/schema.sql`.
   - Core table: `electricity_consumption` with columns:
     - `id`, `state`, `region`, `latitude`, `longitude`, `date`, `usage`.
   - Designed as a **long format** table (one row per state per date).

2. **Ingestion script**: `scripts/load_to_db.py`
   - Reads `data/Consumption.csv`.
   - Renames the first column to `datetime`.
   - Uses `pandas.melt` to reshape from wide (one row per date with many state columns) to long (one row per state/date).
   - Parses dates and sets optional attributes (`region`, `latitude`, `longitude`) to `NULL` for now.
   - Writes into `database/electricity.db` using SQLite.

3. **Analytical queries**:
   - Stored in `scripts/sql_queries.sql`.
   - Cover:
     - Totals by state and region.
     - Year‑wise and quarter‑wise consumption.
     - Top 10 / bottom 10 states by usage.
     - Before vs after lockdown comparisons.

See `performance_testing/db_data_volume.md` for volume and performance notes.

---

### 5. Tableau Visualization and Dashboards

1. **Visualization planning**:
   - `tableau/visualizations/viz_part1.md` – 2019 vs 2020, totals, region usage, Top/Bottom N states.
   - `viz_part2.md` – month‑wise and region‑wise temporal patterns, lockdown impact.
   - `viz_part3.md` – region‑wise state drill‑downs, quarter usage, yearly summaries.

2. **Dashboard design**:
   - Documented in `tableau/dashboard/dashboard_design.md`.
   - Combines KPIs, national time series, region bars, and a geographic map.

3. **Story design**:
   - Documented in `tableau/story/storyboard.md` and `documentation/story.md`.
   - Three scenes: national trend, regional differences, and recovery after lockdown.

4. **Links**:
   - `tableau/tableau_links.md` contains placeholders for Tableau Public URLs to be filled in after publishing.

---

### 6. Web Integration (Flask)

1. **Application**:
   - `webapp/app.py` exposes a simple Flask application:
     - `/` renders `templates/index.html`.
     - `/health` provides a JSON health check.

2. **Template**:
   - `webapp/templates/index.html`:
     - Presents the project title and description.
     - Embeds the Tableau dashboard via an `<iframe>` using `{{ tableau_url }}`.
     - Provides design that is responsive and visually aligned with a modern analytics UI.

3. **Dependencies**:
   - Declared in `webapp/requirements.txt`:
     - `flask`
     - `pandas`

---

### 7. Demo and Documentation

- **Demo link**:
  - `demo/demo_video_link.md` holds a placeholder URL for a walkthrough video.

- **Documentation**:
  - `documentation/data_collection.md` – source and collection process.
  - `documentation/data_preparation.md` – cleaning and validation.
  - `documentation/visualization.md` – visualization strategy.
  - `documentation/dashboard.md` – dashboard layout and behavior.
  - `documentation/story.md` – Tableau story design.
  - `documentation/project_workflow.md` – this file.

---

### 8. End-to-End Flow Summary

1. Start with `data/Consumption.csv`.
2. Run `python scripts/data_preparation.py` to create `prepared_consumption.csv`.
3. Run `python scripts/load_to_db.py` to load the long‑format data into `database/electricity.db`.
4. Use `scripts/sql_queries.sql` as a basis for Tableau data sources or ad‑hoc analysis.
5. Build and publish Tableau workbooks and dashboard using the long‑format table.
6. Host the published dashboard via the Flask app (`webapp/app.py`) for a simple web integration.

This workflow ensures the repository is reproducible, transparent, and ready for extension to new years, new regions, or more detailed sectoral data.

