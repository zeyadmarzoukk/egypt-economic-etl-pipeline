from extract import extract
from transform import transform
from load import load

print("--- Starting Egypt Economic ETL Pipeline ---")

print("\n[1/3] Extracting data from World Bank API...")
raw_df = extract()

print("\n[2/3] Transforming data...")
clean_df = transform(raw_df)

print("\n[3/3] Loading into database...")
load(clean_df)

print("\n Pipeline complete!")