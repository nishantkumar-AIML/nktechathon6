# app.py
import streamlit as st
import pandas as pd
from agents.master_agent import run_pipeline

st.title("Provider Directory Validation - Demo")
st.write("Demo of Challenge VI pipeline (mock sources).")

uploaded = st.file_uploader("Upload providers CSV (or skip to use sample)", type=['csv'])
input_path = None
if uploaded:
    input_path = "data/uploaded_providers.csv"
    with open(input_path, "wb") as f:
        f.write(uploaded.getbuffer())
else:
    input_path = "data/providers_sample.csv"
    st.info("Using sample dataset: data/providers_sample.csv")

if st.button("Run Validation Pipeline"):
    with st.spinner("Running agents..."):
        df, paths = run_pipeline(input_path, out_prefix="outputs/providers_validated")
    st.success("Pipeline finished")
    st.write(df[['id','name','city','confidence','status']].sort_values('confidence', ascending=False))
    st.markdown("### Download report")
    st.markdown(f"- CSV: {paths['csv']}  -  Excel: {paths['excel']}  -  PDF: {paths['pdf']}")
