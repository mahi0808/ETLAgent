from agent.schema import EXPECTED_SCHEMA
from etl.extractor import extract_metadata, detect_schema_changes
from agent.planner import plan_etl, handle_schema_changes
from etl.quality import calculate_quality_score
from agent.planner import adjust_plan_based_on_quality


df, metadata = extract_metadata("data/orders.csv")

schema_changes = detect_schema_changes(
    metadata["dtypes"],
    EXPECTED_SCHEMA
)

schema_decisions = handle_schema_changes(schema_changes)
print("Schema decisions:", schema_decisions)

if "fail_pipeline_due_to_missing_columns" in schema_decisions:
    raise Exception("Schema validation failed")


quality_score = calculate_quality_score(metadata)
print("Data Quality Score:", quality_score)
plan = plan_etl(metadata)
plan = adjust_plan_based_on_quality(plan, quality_score)

