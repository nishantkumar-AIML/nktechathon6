# agents/master_agent.py
import pandas as pd
from agents.validation_agent import validate_providers
from agents.enrichment_agent import batch_enrich
from agents.qa_agent import qa_pass
from agents.directory_agent import create_directory_and_report

def run_pipeline(input_csv, out_prefix="outputs/providers_validated"):
    df = pd.read_csv(input_csv)
    validated_df = validate_providers(df)
    enriched_df = batch_enrich(validated_df)
    qa_df = qa_pass(enriched_df)
    paths = create_directory_and_report(qa_df, out_prefix=out_prefix)
    return qa_df, paths

if __name__ == "__main__":
    import os
    os.makedirs("outputs", exist_ok=True)
    df, paths = run_pipeline("data/providers_sample.csv")
    print("Outputs saved:", paths)
