"""Clean the raw bike sales export (mirrors the Power Query steps in the dashboard)."""
import pandas as pd

RAW = "data/raw/bike_sales_raw.csv"
OUT = "data/processed/bike_sales_clean.csv"

df = pd.read_csv(RAW, sep=";")                       # raw file is semicolon-delimited

for col in df.columns:
    if not pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].str.strip()                          # remove stray spaces

df["Product Category"] = df["Product Category"].str.title().replace({"Bmx Bikes": "BMX Bikes"})  # 13 casing variants -> 7 categories
df["Product Size"] = df["Product Size"].str.upper()            # m/l/s -> M/L/S
df["Product Subcategory"] = df["Product Subcategory"].fillna("Not Specified")          # missing subcategory
df["Product Description"] = df["Product Description"].fillna("Description Not Available")  # missing description
df["Order Date"] = pd.to_datetime(df["Order Date"]).dt.strftime("%Y-%m-%d")

df.to_csv(OUT, index=False)
print(f"Saved {len(df)} rows -> {OUT}")
