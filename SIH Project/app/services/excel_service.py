import pandas as pd
from app.services.leetcode_service import fetch_leetcode_user

INPUT_FILE = r"C:\Users\quant\Main_Project\SIH_PROJECT\SIH Project\app\data\users.xlsx"
OUTPUT_FILE = r"C:\Users\quant\Main_Project\SIH_PROJECT\SIH Project\app\data"

def update_leetcode_excel():
    users_df = pd.read_excel(INPUT_FILE,engine="openpyxl")

    if "enabled" in users_df.columns:
        users_df = users_df[users_df["enabled"] == 1]

    results = []

    for username in users_df["username"]:
        data = fetch_leetcode_user(username)
        if data:
            results.append(data)

    if results:
        pd.DataFrame(results).to_excel(OUTPUT_FILE, index=False)
