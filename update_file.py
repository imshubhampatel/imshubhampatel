from lxml import etree

# Load the SVG file
tree = etree.parse('leetcode_activity.svg')
print({"tree": tree})
root = tree.getroot()

# Namespace dictionary (for SVG files)
ns = {'svg': 'http://www.w3.org/2000/svg'}

# Find the element with the matching pattern
for elem in root.findall('.//svg:rect', namespaces=ns):
    if (elem.get('id') == 'background' and
        elem.get('transform') == 'translate(0.5px, 0.5px)' and
        elem.get('stroke') == 'var(--bg-2)' and
        elem.get('fill') == 'var(--bg-0)' and
        elem.get('stroke-width') == '1' and
        elem.get('width') == '499px' and
        elem.get('height') == '399px' and
        elem.get('rx') == '4px'):
        
        # Update the opacity attribute
        elem.set('opacity', '')  # You can set a specific value or leave it empty

# Save the modified SVG file
tree.write('modified_example.svg')
