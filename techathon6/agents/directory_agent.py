# agents/directory_agent.py
import os
from pathlib import Path
import pandas as pd
from utils.report_generator import create_pdf_report

def create_directory_and_report(final_df, out_prefix="outputs/providers_validated"):
    """
    Save final_df to CSV, Excel and generate a PDF report.
    Ensures output directory exists and accepts a DataFrame or data convertible to one.
    Returns dict with created file paths (None if a format could not be created).
    """
    # ensure we have a DataFrame
    if not isinstance(final_df, pd.DataFrame):
        try:
            final_df = pd.DataFrame(final_df)
        except Exception as e:
            raise ValueError(f"final_df must be a pandas.DataFrame or convertible to one: {e}")

    out_prefix = str(out_prefix)
    out_dir = Path(out_prefix).parent
    # create output directory if needed
    out_dir.mkdir(parents=True, exist_ok=True)

    csv_path = f"{out_prefix}.csv"
    excel_path = f"{out_prefix}.xlsx"
    pdf_path = f"{out_prefix}.pdf"

    # write CSV (should always work if directory exists)
    final_df.to_csv(csv_path, index=False)

    # try write Excel, if engine not available return None for excel path
    try:
        final_df.to_excel(excel_path, index=False)
    except Exception:
        excel_path = None

    # try create PDF report, if it fails return None for pdf path
    try:
        create_pdf_report(final_df, pdf_path)
    except Exception:
        pdf_path = None

    return {"csv": csv_path, "excel": excel_path, "pdf": pdf_path}
