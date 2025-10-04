# agents/qa_agent.py
import pandas as pd

def compute_confidence(row):
    base = 30 if row.get('web_found') else 10
    phone_s = float(row.get('phone_score') or 0)
    addr_s = float(row.get('address_score') or 0)
    board = 10 if row.get('board_certified') else 0
    score = base + 0.45 * phone_s + 0.45 * addr_s + board
    if score > 100:
        score = 100
    return round(score, 1)

def qa_pass(df):
    df = df.copy()
    df['confidence'] = df.apply(compute_confidence, axis=1)
    def status_from_conf(c):
        if c >= 80:
            return "VERIFIED"
        if c >= 50:
            return "REVIEW"
        return "MANUAL_CHECK"
    df['status'] = df['confidence'].apply(status_from_conf)
    return df
