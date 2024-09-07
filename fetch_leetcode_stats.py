import requests
import json

# Replace with your LeetCode username
LEETCODE_USERNAME = "your_leetcode_username"

# Fetch stats from LeetCode API
url = f"https://leetcode-stats-api.herokuapp.com/{LEETCODE_USERNAME}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Create a markdown text for the README file
    with open("README.md", "w") as f:
        f.write(f"# LeetCode Stats\n")
        f.write(f"![LeetCode Stats](https://img.shields.io/badge/Solved-{data['totalSolved']}-green)\n")
        f.write(f"Total Problems Solved: {data['totalSolved']}\n")
        f.write(f"Easy: {data['easySolved']} | Medium: {data['mediumSolved']} | Hard: {data['hardSolved']}\n")

else:
    print(f"Failed to fetch stats for {LEETCODE_USERNAME}")
