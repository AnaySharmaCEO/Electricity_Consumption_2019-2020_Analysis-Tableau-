## Plugging into the Future: An Exploration of Electricity Consumption Patterns

This repository implements a complete analytics workflow for exploring electricity consumption across Indian states between **January 2019 and December 2020**, using data derived from POSOCO weekly energy reports.

---

### Project Overview

An interactive data analytics project analyzing electricity consumption patterns across Indian states from **2019–2020**, including the impact of the **COVID-19 lockdown**.

---

## 🔗 Live Demo

Flask Web App (Render Deployment)

https://electricity-consumption-analysis.onrender.com

---

## 📂 GitHub Repository

https://github.com/AnaySharmaCEO/Electricity_Consumption_2019-2020_Analysis-Tableau-

---

## 👥 Team

- **Anay Sharma** — Team Lead  
- Animesh Verma  
- Anirudh Vashisth  
- Anchal Yadav  

---

## ⚙️ Tech Stack

- Python
- Flask
- SQL
- Tableau
- HTML/CSS

---

## 📊 Features

- Electricity consumption analysis (2019–2020)
- State-wise usage comparison
- Region-wise electricity demand
- COVID-19 lockdown impact analysis
- Interactive Tableau dashboard
- Data storytelling visualization

The project follows a full data pipeline:

- **Data ingestion** from a consolidated POSOCO‑based CSV.
- **Data validation and preparation** with Python and pandas.
- **Relational storage** in a SQLite database, using a long analytical schema.
- **SQL analysis** for key metrics (totals, rankings, quarters, lockdown comparison).
- **Visualization planning** for Tableau dashboards and stories.
- **Performance testing documentation** for database and dashboard design.
- **Flask web integration** that embeds the Tableau dashboard in a minimal web app.

This structure is designed to be production‑ready and suitable for submission as a portfolio or academic project.

---

### Dataset Description

- **Source**: POSOCO weekly energy reports (India).  
- **File**: `data/Consumption.csv`  
- **Grain**: **Daily** consumption for each Indian state/UT.  
- **Fields**:
  - First column: datetime (`DD/MM/YYYY HH:MM:SS`), parsed as day‑first.
  - 34 columns: state/UT names (Punjab, Haryana, Rajasthan, Delhi, UP, Uttarakhand, HP, J&K, Chandigarh, Chhattisgarh, Gujarat, MP, Maharashtra, Goa, DNH, Andhra Pradesh, Telangana, Karnataka, Kerala, Tamil Nadu, Pondy, Bihar, Jharkhand, Odisha, West Bengal, Sikkim, Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Tripura).
  - Values: electricity consumption in **Mega Units (MU)**.

See `documentation/data_collection.md` for additional context.

---

### Technology Stack

- **Language**: Python (3.x)
- **Libraries**:
  - `pandas` for data preparation and reshaping.
  - `sqlite3` (standard library) for database operations.
  - `Flask` for the minimal web interface.
- **Database**:
  - SQLite database at `database/electricity.db`.
  - Main table: `electricity_consumption` (long format).
- **Visualization**:
  - Tableau Desktop / Tableau Public for dashboards and stories.

---

### Project Architecture

Repository root: `electricity-consumption-analysis/`

- `data/`
  - `Consumption.csv` – raw consolidated dataset.
  - `prepared_consumption.csv` – cleaned version produced by `data_preparation.py`.
- `database/`
  - `schema.sql` – DDL for `electricity_consumption` and indexes.
  - `electricity.db` – SQLite database (created by `load_to_db.py`).
- `scripts/`
  - `data_preparation.py` – cleanse and validate the CSV, write `prepared_consumption.csv`.
  - `load_to_db.py` – reshape wide CSV into long format and load into SQLite using `schema.sql`.
  - `sql_queries.sql` – library of analytical SQL queries.
- `tableau/`
  - `visualizations/viz_part1.md` – 2019 vs 2020, totals, region, Top/Bottom N.
  - `visualizations/viz_part2.md` – month‑wise, region‑wise, lockdown impact.
  - `visualizations/viz_part3.md` – region‑wise states, quarters, yearly.
  - `dashboard/dashboard_design.md` – dashboard layout and UX.
  - `story/storyboard.md` – Tableau story scenes.
  - `tableau_links.md` – placeholders for Tableau Public URLs.
- `performance_testing/`
  - `db_data_volume.md` – dataset size and database structure.
  - `filters_usage.md` – filter design and performance notes.
  - `visualizations_count.md` – inventory of visualizations and scenes.
- `webapp/`
  - `app.py` – Flask application factory and routes.
  - `requirements.txt` – Python dependencies (`flask`, `pandas`).
  - `templates/index.html` – landing page with embedded Tableau dashboard.
- `documentation/`
  - `data_collection.md` – data sourcing and consolidation.
  - `data_preparation.md` – cleaning and validation logic.
  - `visualization.md` – visualization strategy and design principles.
  - `dashboard.md` – dashboard behavior and user interactions.
  - `story.md` – story structure and messaging.
  - `project_workflow.md` – complete step‑by‑step workflow.
- `demo/`
  - `demo_video_link.md` – placeholder link for a recorded walkthrough.
- `README.md` – this file.

---

### Setup Instructions

1. **Clone or copy the repository**

   Place `electricity-consumption-analysis` in your workspace. Ensure `data/Consumption.csv` is present.

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install web app dependencies**

   ```bash
   pip install -r webapp/requirements.txt
   ```

4. **Run data preparation (optional but recommended)**

   ```bash
   python scripts/data_preparation.py
   ```

5. **Load data into SQLite**

   ```bash
   python scripts/load_to_db.py
   ```

   This will:
   - Create `database/electricity.db` (if missing).
   - Apply `database/schema.sql`.
   - Insert the reshaped long‑format data into `electricity_consumption`.
   - Print the total row count.

6. **Open the dataset in Tableau**

   - Connect Tableau to `database/electricity.db` or to `data/prepared_consumption.csv`.
   - Use the documentation under `tableau/` as a blueprint for building dashboards and stories.

7. **Run the Flask web app**

   ```bash
   cd webapp
   python app.py
   ```

   - Visit `http://localhost:5000` in your browser.
   - Update the placeholder `TABLEAU_PUBLIC_DASHBOARD_LINK` in `app.py` and `templates/index.html` once your dashboard is published to Tableau Public.


### Notes

- The project is intentionally modular:
  - You can extend the schema to include regions, lat/long, or sector tags without breaking existing scripts.
  - Tableau workbooks can be refreshed as new years of data are loaded into the same schema.
- All Python scripts are designed to be simple, readable, and easily adaptable to more complex production environments (e.g., scheduled ETL jobs, containerized deployments).

