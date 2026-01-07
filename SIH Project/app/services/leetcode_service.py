import requests
from datetime import datetime

LEETCODE_URL = "https://leetcode.com/graphql"

QUERY = """
query userProfile($username: String!) {
  matchedUser(username: $username) {
    submitStats {
      acSubmissionNum {
        difficulty
        count
      }
    }
    profile {
      ranking
      reputation
    }
  }
}
"""

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

def fetch_leetcode_user(username: str):
    try:
        response = requests.post(
            LEETCODE_URL,
            json={"query": QUERY, "variables": {"username": username}},
            headers=HEADERS,
            timeout=10
        )

        if response.status_code != 200:
            return None

        data = response.json()
        user = data.get("data", {}).get("matchedUser")
        if not user:
            return None

        submit_stats = user.get("submitStats", {}).get("acSubmissionNum", [])
        profile = user.get("profile", {})

        stats = {s["difficulty"]: s["count"] for s in submit_stats}

        easy = stats.get("Easy", 0)
        medium = stats.get("Medium", 0)
        hard = stats.get("Hard", 0)

        return {
            "username": username,
            "easy_solved": easy,
            "medium_solved": medium,
            "hard_solved": hard,
            "total_solved": easy + medium + hard,
            "ranking": profile.get("ranking"),
            "reputation": profile.get("reputation"),
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception:
        return None
