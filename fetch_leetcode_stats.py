import requests
from bs4 import BeautifulSoup

# Define the URL to fetch the SVG
url = "https://leetcard.jacoblin.cool/imshubhampatel?ext=activity"

# Send a GET request to the URL
response = requests.get(url)


if response.status_code == 200:
    svg_content = response.content.decode('utf-8')
    original_style = '#background {\n    transform: translate(0.5px, 0.5px);\n    stroke: var(--bg-2);\n    fill: var(--bg-0);\n    stroke-width: 1;\n    width: 499px;\n    height: 399px;\n    rx: 4px\n}\n'
    new_style = '#background {\n    transform: translate(0.5px, 0.5px);\n    stroke: var(--bg-2);\n    fill: var(--bg-0);\n    stroke-width: 1;\n    width: 499px;\n    height: 399px;\n    opacity: 0;\n    rx: 4px\n}\n'
    

    svg_content = svg_content.replace(original_style,'#backgroud{}')
   
    with open('leetcode_activity.svg', 'w') as file:
        file.write(svg_content)
    print("SVG modified and saved successfully!")
else:
    print(f"Failed to fetch SVG. Status code: {response.status_code}")
