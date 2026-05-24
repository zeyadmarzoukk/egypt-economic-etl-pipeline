import pandas as pd
import sqlite3
import os

def load(df):
    os.makedirs("data/processed", exist_ok=True)
    
    # save to database
    conn = sqlite3.connect("data/processed/egypt_economics.db")
    df.to_sql("egypt_indicators", conn, if_exists="replace", index=False)
    conn.close()

    print(f"Loaded {len(df)} rows into database")
    print("Database saved to data/processed/egypt_economics.db")

if __name__ == "__main__":
    df = pd.read_csv("data/processed/egypt_clean.csv")
    load(df)