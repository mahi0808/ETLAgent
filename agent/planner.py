import json
import os
from openai import OpenAI

def plan_etl(metadata):
    """
    GenAI-powered ETL planning function with safe fallback.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    # 🔁 Fallback mode (no API key)
    if not api_key:
        return {
            "validations": [
                "order_date should not be null",
                "amount should be numeric"
            ],
            "transformations": [
                "drop rows with null order_date",
                "convert order_date to date",
                "standardize status to uppercase"
            ],
            "load_strategy": "overwrite"
        }

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are an intelligent ETL planning agent.

Given the following dataset metadata, generate an ETL plan.

Metadata:
{metadata}

Return STRICT JSON with:
- validations
- transformations
- load_strategy
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an ETL planning agent."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return json.loads(response.choices[0].message.content)



def handle_schema_changes(schema_changes):
    """
    Rule-based guardrails for schema drift.
    These act as safety checks around the GenAI agent.
    """

    decisions = []

    if schema_changes["missing_columns"]:
        decisions.append("fail_pipeline_due_to_missing_columns")

    if schema_changes["new_columns"]:
        decisions.append("accept_new_columns")

    if schema_changes["type_changes"]:
        decisions.append("cast_columns_to_expected_types")

    return decisions


def adjust_plan_based_on_quality(plan, quality_score):
    """
    Deterministic adjustment of the GenAI plan
    based on data quality signals.
    """

    if quality_score < 80:
        plan["transformations"].insert(
            0, "drop rows with critical nulls"
        )

    return plan
