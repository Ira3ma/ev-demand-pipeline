from pytrends.request import TrendReq
import pandas as pd

# Connect to Google Trends
pytrends = TrendReq(hl='sv-SE', tz=360)

# Search terms
keywords = ["elbil", "Tesla", "begagnad elbil"]

# Build request
pytrends.build_payload(
    keywords,
    timeframe='today 3-m',
    geo='SE'
)

# Fetch trend data
df = pytrends.interest_over_time()

print(df.head())

# Save CSV
df.to_csv("data/google_trends.csv")
