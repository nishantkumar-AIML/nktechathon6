# agents/validation_agent.py
import pandas as pd
from utils.web_helpers import mock_search_provider_on_web, fuzzy_compare

def validate_providers(df):
    rows = []
    for _, row in df.iterrows():
        res = mock_search_provider_on_web(row['name'], row.get('city', ''))
        phone_score = 0
        address_score = 0
        validated_phone = None
        validated_address = None
        web_found = False
        source = None
        if res.get('found'):
            web_found = True
            source = res.get('source')
            validated_phone = res.get('phone')
            validated_address = res.get('address')
            phone_score = fuzzy_compare(row.get('phone'), validated_phone)
            address_score = fuzzy_compare(row.get('address'), validated_address)
        rows.append({
            **row.to_dict(),
            "web_found": web_found,
            "web_source": source,
            "validated_phone": validated_phone,
            "validated_address": validated_address,
            "phone_score": phone_score,
            "address_score": address_score
        })
    return pd.DataFrame(rows)
