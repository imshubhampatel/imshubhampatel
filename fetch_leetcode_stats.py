import requests
import json

# Replace with your LeetCode username
LEETCODE_USERNAME = "imshubhampatel"

# Fetch stats from LeetCode API
url = f"https://leetcard.jacoblin.cool/imshubhampatel?ext=activity"
response = requests.get(url)
if response.status_code == 200:
    # Open a file in binary write mode and save the content
    with open('leetcode_activity.svg', 'wb') as file:
        file.write(response.content)
    print("SVG saved successfully!")
else:
    print(f"Failed to fetch SVG. Status code: {response.status_code}")