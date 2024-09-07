import requests
from bs4 import BeautifulSoup

# Define the URL to fetch the SVG
url = "https://leetcard.jacoblin.cool/imshubhampatel?ext=activity"

# Send a GET request to the URL
response = requests.get(url)


if response.status_code == 200:
    svg_content = response.content.decode('utf-8')
    updated_style = '''
#background {
    transform: translate(0.5px, 0.5px);
    stroke: var(--bg-2);
    fill: var(--bg-0);
    stroke-width: 1;
    width: 499px;
    height: 399px;
    opacity: 0;
    rx: 4px
}
'''

    svg_content = svg_content.replace(
            '#background {\n    transform: translate(0.5px, 0.5px);\n    stroke: var(--bg-2);\n    fill: var(--bg-0);\n    stroke-width: 1;\n    width: 499px;\n    height: 399px;\n    rx: 4px\n}\n',
            updated_style
        )
   
    with open('leetcode_activity.svg', 'w') as file:
        file.write(svg_content)
    print("SVG modified and saved successfully!")
else:
    print(f"Failed to fetch SVG. Status code: {response.status_code}")
