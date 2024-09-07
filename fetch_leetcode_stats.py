import requests
from bs4 import BeautifulSoup

# Define the URL to fetch the SVG
url = "https://leetcard.jacoblin.cool/imshubhampatel?ext=activity"

# Send a GET request to the URL
response = requests.get(url)


if response.status_code == 200:
    svg_content = response.content.decode('utf-8')

    old_style_pattern = r'#background {\s+transform: translate\(0\.5px, 0\.5px\);\s+stroke: var\(--bg-2\);\s+fill: var\(--bg-0\);\s+stroke-width: 1;\s+width: 499px;\s+height: 399px;\s+rx: 4px\s+}'
    new_style = '#background {\n    transform: translate(0.5px, 0.5px);\n    stroke: var(--bg-2);\n    fill: var(--bg-0);\n    stroke-width: 1;\n    width: 499px;\n    height: 399px;\n    opacity: 0;\n    rx: 4px\n}\n'

    svg_content = re.sub(old_style_pattern, new_style, svg_content, flags=re.DOTALL)
    print(svg_content[:1000])
    with open('leetcode_activity.svg', 'w') as file:
        file.write(svg_content)
    print("SVG modified and saved successfully!")
    print(svg_content)
else:
    print(f"Failed to fetch SVG. Status code: {response.status_code}")
