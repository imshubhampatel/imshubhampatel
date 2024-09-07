import requests
from bs4 import BeautifulSoup

url = "https://leetcard.jacoblin.cool/JacobLinCool?ext=heatmap"

response = requests.get(url)

if response.status_code == 200:
    old_name_bytes =   '<rect id="background"></rect>'.encode('utf-8')
    new_name_bytes =  '<rect id="background" style="opacity: 0;"></rect>'.encode('utf-8')
    print(new_name_bytes)
    print("kidfsd")
    print("kidfsd")
    print(old_name_bytes)
    with open('leetcode_activity.svg', 'rb') as file:
        binary_data = file.read()
        updated_binary_data = binary_data.replace(old_name_bytes, new_name_bytes)
    with open("leetcode_activity.svg", 'wb') as file:
        file.write(updated_binary_data)
    print("SVG modified and saved successfully!")
else:
    print(f"Failed to fetch SVG. Status code: {response.status_code}")
