import requests
from bs4 import BeautifulSoup

# Define the URL to fetch the SVG
url = "https://leetcard.jacoblin.cool/imshubhampatel?ext=activity"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the SVG content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Find the <rect> element with id="background"
    rect = soup.find('rect', id='background')
    if rect:
        # Modify the style attribute
        rect['style'] = 'opacity: 0;'
    
    # Convert the modified content back to a string
    modified_svg = str(soup)

    # Open a file in write mode and save the modified content
    with open('leetcode_activity.svg', 'w') as file:
        file.write(modified_svg)
    print("SVG modified and saved successfully!")
else:
    print(f"Failed to fetch SVG. Status code: {response.status_code}")
