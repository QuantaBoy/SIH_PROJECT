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

def fetch_leetcode_user(username):
    response = requests.post(
        LEETCODE_URL,
        json={"query": QUERY, "variables": {"username": username}},
        headers={"Content-Type": "application/json"},
        timeout=10
    )

    data = response.json()
    user = data.get("data", {}).get("matchedUser")

    if not user:
        return None

    stats = {s["difficulty"]: s["count"] for s in user["submitStats"]["acSubmissionNum"]}

    easy = stats.get("Easy", 0)
    medium = stats.get("Medium", 0)
    hard = stats.get("Hard", 0)

    return {
        "username": username,
        "easy_solved": easy,
        "medium_solved": medium,
        "hard_solved": hard,
        "total_solved": easy + medium + hard,
        "ranking": user["profile"]["ranking"],
        "reputation": user["profile"]["reputation"],
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
