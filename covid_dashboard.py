import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fetch data from API
url = "https://data.covid19india.org/data.json"
response = requests.get(url).json()

# Daily data
daily_data = response["cases_time_series"]
df = pd.DataFrame(daily_data)

# Convert to numeric
df["dailyconfirmed"] = pd.to_numeric(df["dailyconfirmed"])
df["dailydeceased"] = pd.to_numeric(df["dailydeceased"])
df["date"] = pd.to_datetime(df["date"] + "2020", format="%d %B %Y")

# Plot daily cases
plt.figure(figsize=(10, 4))
plt.plot(df["date"], df["dailyconfirmed"], label="Daily Confirmed")
plt.plot(df["date"], df["dailydeceased"], label="Daily Deaths")
plt.title("COVID-19 Daily Cases in India")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.legend()
plt.tight_layout()
plt.savefig("covid_daily_cases.png")
