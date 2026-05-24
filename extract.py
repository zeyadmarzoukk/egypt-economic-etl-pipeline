import requests
import pandas as pd
import os

def extract():
    indicators = {
        "NY.GDP.MKTP.CD": "gdp",
        "FP.CPI.TOTL.ZG": "inflation",
        "SL.UEM.TOTL.ZS": "unemployment"
    }

    all_data = []

    for code, name in indicators.items():
        url = f"https://api.worldbank.org/v2/country/EG/indicator/{code}?format=json&per_page=30"
        response = requests.get(url)
        data = response.json()[1]

        for entry in data:
            all_data.append({
                "year": entry["date"],
                "indicator": name,
                "value": entry["value"]
            })

    df = pd.DataFrame(all_data)
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/egypt_raw.csv", index=False)
    print(f"Extracted {len(df)} rows")
    return df

if __name__ == "__main__":
    extract()