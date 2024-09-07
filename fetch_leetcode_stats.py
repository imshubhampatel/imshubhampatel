import requests
from bs4 import BeautifulSoup

url = "https://leetcard.jacoblin.cool/imshubhampatel?ext=activity"

response = requests.get(url)

if response.status_code == 200:
    with open('leetcode_activity.svg', 'w') as file:
        file.write(response.content)
    print("SVG modified and saved successfully!")
else:
    print(f"Failed to fetch SVG. Status code: {response.status_code}")
