# run_pipeline.py
from agents.master_agent import run_pipeline
import os

def main():
    os.makedirs("outputs", exist_ok=True)
    df, paths = run_pipeline("data/providers_sample.csv")
    print("Done! Files created:")
    for k,v in paths.items():
        print(k, "->", v)

if __name__ == "__main__":
    main()
