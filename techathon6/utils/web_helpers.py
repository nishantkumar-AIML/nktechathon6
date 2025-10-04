# utils/web_helpers.py
import random, time
from fuzzywuzzy import fuzz

def mock_search_provider_on_web(name, city):
    """Mock web search that simulates finding provider details.
    In a real build, replace this with Google Places / NPI / hospital website scraping.
    Returns dict with phone, address, found boolean, source.
    """
    time.sleep(0.15)
    score = (sum(ord(c) for c in (name + (city or ""))) % 100)
    if score < 10:
        return {"found": False}
    phone_candidates = [
        "9876543210", "9834567890", "9812345678", "08012340000", "09099887766"
    ]
    address_candidates = [
        f"{random.randint(1,200)} Main St, {city}",
        f"{random.randint(1,100)} Medical Plaza, {city}",
        f"{random.randint(1,50)} Health Complex, {city}"
    ]
    return {
        "found": True,
        "phone": random.choice(phone_candidates),
        "address": random.choice(address_candidates),
        "source": "mock_web_site"
    }

def fuzzy_compare(a, b):
    if not a or not b:
        return 0
    try:
        return fuzz.token_sort_ratio(str(a), str(b))
    except Exception:
        return 0
