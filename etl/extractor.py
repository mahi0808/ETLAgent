import pandas as pd

def extract_metadata(csv_path):
    df = pd.read_csv(csv_path)

    metadata = {
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "null_counts": df.isnull().sum().to_dict(),
        "sample_rows": df.head(3).to_dict(orient="records")
    }

    return df, metadata


def detect_schema_changes(actual_schema, expected_schema):
    changes = {
        "missing_columns": [],
        "new_columns": [],
        "type_changes": []
    }

    for col in expected_schema:
        if col not in actual_schema:
            changes["missing_columns"].append(col)

    for col in actual_schema:
        if col not in expected_schema:
            changes["new_columns"].append(col)
        elif actual_schema[col] != expected_schema[col]:
            changes["type_changes"].append({
                "column": col,
                "expected": expected_schema[col],
                "actual": actual_schema[col]
            })

    return changes
