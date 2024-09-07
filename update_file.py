import xml.etree.ElementTree as ET

def update_rect_opacity(file_path):
    # Parse the SVG file
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}
    
    # Find and update the <rect> element with id="background"
    for elem in root.iter('rect'):
        if elem.get('id') == 'background':
            # Add or update the style attribute with opacity
            if 'style' in elem.attrib:
                # Append opacity to existing style
                style = elem.attrib['style']
                if 'opacity' not in style:
                    elem.attrib['style'] += ' opacity: 0;'
            else:
                # Set style attribute with opacity
                elem.attrib['style'] = 'opacity: 0;'
    
    # Save the modified SVG file
    tree.write('updated_' + file_path, encoding='utf-8', xml_declaration=True)

# Example usage
update_rect_opacity('leetcode_activity.svg')
