import pandas as pd
from pathlib import Path

RAW = Path("data/raw/prio3_prices.csv")
OUT = Path("data/intermediate/prio3_prices_clean.parquet")

def main() -> None:
    df = pd.read_csv(RAW)

    # Drop unused columns
    df = df.drop(columns=["Dividends", "Stock Splits"], errors="ignore")

    # Rename to snake_case
    df = df.rename(columns={
        "Date":   "date",
        "Open":   "price_open",
        "High":   "price_high",
        "Low":    "price_low",
        "Close":  "price_close",
        "Volume": "volume"
    })

    # Type conversions
    df["date"] = pd.to_datetime(df["date"], utc=True, errors="coerce")
    price_cols = ["price_open", "price_high", "price_low", "price_close"]
    df[price_cols] = df[price_cols].astype(float)
    df["volume"]   = pd.to_numeric(df["volume"], errors="coerce").astype("Int64")

    # Tidy index & save
    df = (df
          .dropna(subset=["date"])
          .set_index("date")
          .sort_index())

    df.to_parquet(OUT)
    print(f"✅  Clean PRIO3 price file written to {OUT}  ({len(df):,} rows).")

if __name__ == "__main__":
    main()