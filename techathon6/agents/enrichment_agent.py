# agents/enrichment_agent.py
import pandas as pd
import random, time

SPECIALTY_EXTRAS = {
    "Cardiologist": ["MD Cardiology", "Fellow - Cardio Dept"],
    "Dermatologist": ["MBBS, MD - Dermatology"],
    "Orthopedics": ["MS Orthopedics"],
    "General Physician": ["MBBS"],
    "ENT": ["MS ENT"]
}

def enrich_provider(row):
    time.sleep(0.05)
    spec = row.get('specialization') or ""
    educ = SPECIALTY_EXTRAS.get(spec, ["MBBS"])
    website = None
    if row.get('web_found'):
        website = f"https://{row['name'].lower().replace(' ', '')}.clinic.example"
    practice_hours = f"{random.randint(8,10)}:00 AM - {random.randint(5,8)}:00 PM"
    return {
        "education": "; ".join(educ),
        "board_certified": random.choice([True, False]),
        "practice_hours": practice_hours,
        "website": website
    }

def batch_enrich(df):
    enrichments = []
    for _, r in df.iterrows():
        enrichments.append(enrich_provider(r))
    enrich_df = df.reset_index(drop=True)
    enrich_info = pd.DataFrame(enrichments)
    return pd.concat([enrich_df, enrich_info], axis=1)
