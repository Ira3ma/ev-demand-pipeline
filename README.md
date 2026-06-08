# ev-demand-pipeline
Data pipeline analyzing EV search demand in relation to fuel price volatility and geopolitical events.

## Project overview

This project explores whether changes in fuel prices and external market events may influence consumer interest in electric vehicles.

Google Trends data was used as a proxy for EV interest and combined with fuel price data to analyze patterns over time.

## Research question

Do rising fuel prices drive increased interest in electric vehicles?

## Data sources

- Google Trends data collected using Python and Pytrends
- Fuel price data collected from external market sources
- Event data related to geopolitical events

## Data pipeline architecture

### 1. Data extraction (Python)

Python scripts were used to collect Google Trends data and prepare CSV files.

### 2. Cloud storage (Azure Blob Storage)

Raw CSV files were stored in Azure Blob Storage as the raw data layer.

### 3. Data warehouse (Snowflake)

Data was loaded from Azure into Snowflake where raw tables were created.

### 4. Transformation layer (dbt)

dbt was used to:
- create staging models
- clean and standardize data
- handle missing values
- combine datasets into an analytics mart model

### 5. Analytics & visualization (Power BI)

Power BI was used to visualize:
- EV search interest trends
- fuel price changes
- demand categories over time

## Tools & technologies

- Python
- Azure Blob Storage
- Snowflake
- dbt
- SQL
- Power BI
- GitHub Actions

## Future improvements

Possible improvements:
- Use automated fuel price API ingestion
- Include real EV sales data
- Expand analysis to Nordic markets
- Add predictive models for demand forecasting

## Author

Iracema Thott  
Data Analyst DA27  
Hyper Island