import pandas as pd
from app.services.leetcode_service import fetch_leetcode_user

INPUT_FILE = r"C:\Users\quant\Main_Project\SIH_PROJECT\SIH Project\app\data\user_details.xlsx"
OUTPUT_FILE = r"C:\Users\quant\Main_Project\SIH_PROJECT\SIH Project\app\data\leetcode_data.xlsx"

def update_leetcode_excel():
    users_df = pd.read_excel(INPUT_FILE, engine="openpyxl")

    print("RAW DF:")
    print(users_df)

    users_df.columns = [
        str(col).strip().lower()
        for col in users_df.columns
    ]

    print("COLUMNS:", users_df.columns.tolist())

    if "enabled" in users_df.columns:
        users_df = users_df[users_df["enabled"] == 1]

    print("AFTER FILTER:")
    print(users_df)

    results = []

    for username in users_df["username"]:
        print("FETCHING:", username)

        data = fetch_leetcode_user(str(username).strip())
        print("RESULT:", data)

        if data:
            results.append(data)

    print("FINAL RESULTS:", results)

    if results:
        pd.DataFrame(results).to_excel(
            OUTPUT_FILE,
            index=False,
            engine="openpyxl"
        )
        print("OUTPUT FILE WRITTEN")
    else:
        print("NO DATA → FILE NOT CREATED")