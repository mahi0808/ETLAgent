import pandas as pd

def apply_transformations(df, plan):
    for step in plan["transformations"]:
        if "drop rows with null order_date" in step:
            df = df.dropna(subset=["order_date"])

        if "convert order_date to date" in step:
            df["order_date"] = pd.to_datetime(df["order_date"])

        if "standardize status" in step:
            df["status"] = df["status"].str.upper()

    return df
