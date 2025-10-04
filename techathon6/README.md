# Provider Directory Validation - Techathon 6.0 (Challenge VI)

## Setup
1. Create a Python venv and activate:
   ```
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Run pipeline (CLI)
```
python run_pipeline.py
```
Outputs will be in `outputs/providers_validated.csv`, `.xlsx`, `.pdf`.

## Run Streamlit UI (optional)
```
streamlit run app.py
```

## Notes
- Uses mock web lookups so no API key required.
- Replace `utils/web_helpers.mock_search_provider_on_web` with real APIs for production.
