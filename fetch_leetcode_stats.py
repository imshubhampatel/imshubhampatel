import requests
from bs4 import BeautifulSoup

url = "https://leetcard.jacoblin.cool/imshubhampatel?ext=activity"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')
    
    rect = soup.find('rect', id='background')
    if rect:
        rect['style'] = 'opacity: 0;'
    
    modified_svg = str(soup)

    print(modified_svg[:1000]) 

    with open('leetcode_activity.svg', 'w') as file:
        file.write(modified_svg)
    print("SVG modified and saved successfully!")
else:
    print(f"Failed to fetch SVG. Status code: {response.status_code}")
