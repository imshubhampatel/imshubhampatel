import requests
from bs4 import BeautifulSoup

# Define the URL to fetch the SVG
url = "https://leetcard.jacoblin.cool/imshubhampatel?ext=activity"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
     svg_content = response.content
    
    # Parse the SVG content
    root = ET.fromstring(svg_content)
    
    # Modify the <rect> element with id="background"
    for rect in root.findall(".//{http://www.w3.org/2000/svg}rect"):
        if rect.get('id') == 'background':
            rect.set('style', 'opacity: 0;')
    
    # Convert the modified content back to a string
    modified_svg = ET.tostring(root, encoding='unicode')
    
    # Save the modified SVG to a file
    with open('leetcode_activity.svg', 'w') as file:
        file.write(modified_svg)
    print("SVG modified and saved successfully!")
else:
    print(f"Failed to fetch SVG. Status code: {response.status_code}")
