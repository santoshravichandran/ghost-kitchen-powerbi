# Doorstep Kitchen Analytics — Power BI Portfolio Project (Ghost Kitchen - Concept)

> End-to-end Power BI solution answering 10 business questions across 5,000 simulated delivery orders from 3 ghost kitchen locations across a 60-day window.



## Project Summary


Ghost kitchens — delivery-only restaurants with no physical dining space — operate entirely in the data layer. 

This project transforms three raw CSV files into a production-grade Power BI solution covering data ingestion, transformation, modelling, DAX analytics, and published dashboards.



Dataset: Procedurally generated using Python (pandas/NumPy) — 5,000 orders, 3 kitchen locations, 5 menu items, 60 days of operations.


## Business Questions Answered


| # | Theme | Question | Report Page |

|---|-------|----------|-------------|

| Q1 | Quality Decay | At what delivery distance do Crispy item ratings drop below 4 stars? | Quality & Menu |

| Q2 | Kitchen Bottleneck | Which items cause the longest driver wait during peak hours? | Operations |

| Q3 | Batching Efficiency | Is batching 3 orders per driver more profitable than individual delivery? | Profitability |

| Q4 | Labor Forecasting | How many chefs keep the Prep-to-Driver gap under 5 minutes? | Operations |

| Q5 | Revenue by Location | Which kitchen generates the most revenue per hour? | Executive Summary |

| Q6 | Menu Performance | Which items have the best Rating-per-Prep-Minute efficiency? | Quality & Menu |

| Q7 | Peak Demand | What are the hour-of-day and day-of-week demand patterns? | Operations |

| Q8 | SLA Breach | What % of orders exceed 45-minute end-to-end delivery time? | SLA Compliance |

| Q9 | Driver Idle Cost | How much cumulative driver idle time occurs per kitchen per week? | Operations |

| Q10 | Rating Trend | Is average customer rating improving or degrading over 60 days? | Executive Summary |



## Tech Stack



- Power BI Desktop — Report authoring, star schema modelling, DAX

- DAX — 30+ measures across 10 business questions, 5 calculated columns

- Power Query (M) — 6 custom transformations, date dimension table

- Tabular Editor 2 — Calculation Groups (Time Intelligence switcher)

- DAX Studio — DMV queries, model inspection, measure export

- Python 3.x — Synthetic dataset generation (pandas, numpy)

- Git & GitHub — Version control with plain-text `.dax` files for diff-friendly measure tracking



## Power BI Features Used



- Star schema data model (FactOrders + 3 dimension tables + Date table)

- Time Intelligence via Calculation Groups (MTD, QTD, YTD, MoM, Prior Period)

- Field Parameters for dynamic metric switching across charts

- Row-Level Security (kitchen manager role filter via USERPRINCIPALNAME)

- AI Visuals — Key Influencers, Q&A, Smart Narrative, Anomaly Detection

- Bookmarks and custom navigation buttons (app-like UX)

- Synced slicers across all 6 report pages

- Tooltip pages (Order Detail + Rating Anomaly)

- Conditional formatting using DAX-driven hex color columns

- Custom theme JSON (Gk_Theme.json)

- Published to Power BI Service with scheduled refresh, KPI alerts, and App



## How to Use


1. Clone the repository - git clone https://github.com/santoshravichandran/ghost-kitchen-powerbi.git

2. Run the data generation script to produce the CSV files

3. Open `pbit/Doorstep Kitchen_Analytics.pbit` in Power BI Desktop

4. Point the three data sources to your local `data/raw/` folder when prompted

5. Refresh the model — all 5,000 rows and 30+ measures load automatically

6. Explore all 6 report pages




## Data Model


Star schema with FactOrders at the centre:



- `FactOrders` — 5,000 rows, timestamps, distance, rating, revenue

- `DimMenu` — 5 menu items with category and prep tier

- `DimKitchens` — 3 kitchen locations with chef headcount and tier

- `DimDate` — Full date dimension generated in Power Query M



All relationships are single-direction Many-to-One from FactOrders to each dimension.



## Connect


Built by Santosh Ravichandran.

(https://linkedin.com/in/santoshravichandran) — open to data analytics and BI roles.


If you find this useful, feel free to star the repo.







