import pandas as pd

def transform(df):
    # drop rows with no value
    df = df.dropna(subset=["value"])

    # make year a number
    df["year"] = df["year"].astype(int)

    # round values
    df["value"] = df["value"].round(2)

    # pivot so each indicator becomes a column
    df_pivot = df.pivot(index="year", columns="indicator", values="value").reset_index()
    df_pivot.columns.name = None

    # sort by year
    df_pivot = df_pivot.sort_values("year")

    # save
    df_pivot.to_csv("data/processed/egypt_clean.csv", index=False)
    print(f"Transformed data: {len(df_pivot)} years")
    print(df_pivot.tail())
    return df_pivot

if __name__ == "__main__":
    raw = pd.read_csv("data/raw/egypt_raw.csv")
    transform(raw)