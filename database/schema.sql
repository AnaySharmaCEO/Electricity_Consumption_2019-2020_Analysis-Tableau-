-- SQLite schema for electricity consumption analysis
-- Table is designed in a long, analytical format:
-- one row per (state, date) with optional geographic attributes.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS electricity_consumption (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    state TEXT NOT NULL,
    region TEXT,
    latitude REAL,
    longitude REAL,
    date DATE NOT NULL,
    usage REAL NOT NULL
);

-- Helpful indexes for common analytical patterns
CREATE INDEX IF NOT EXISTS idx_electricity_consumption_state_date
    ON electricity_consumption (state, date);

CREATE INDEX IF NOT EXISTS idx_electricity_consumption_region_date
    ON electricity_consumption (region, date);

