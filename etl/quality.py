def calculate_quality_score(metadata):
    total_fields = len(metadata["columns"])
    total_nulls = sum(metadata["null_counts"].values())

    if total_fields == 0:
        return 0

    score = max(0, 100 - (total_nulls * 5))
    return score
