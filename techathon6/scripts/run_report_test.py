import pandas as pd
from agents.directory_agent import create_directory_and_report

def main():
    data = [
        {
            "id": 1, "name": "Provider A", "city": "Delhi", "phone": "1111111111",
            "validated_phone": "1111111111", "address": "Addr A", "validated_address": "Addr A",
            "confidence": 0.98, "status": "VERIFIED"
        },
        {
            "id": 2, "name": "Provider B", "city": "Mumbai", "phone": "2222222222",
            "validated_phone": "", "address": "Addr B", "validated_address": "",
            "confidence": 0.45, "status": "REVIEW"
        },
    ]
    df = pd.DataFrame(data)
    paths = create_directory_and_report(df, out_prefix="outputs/providers_validated")
    print("Created files:", paths)

if __name__ == "__main__":
    main()