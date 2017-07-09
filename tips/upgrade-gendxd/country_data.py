import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')

root = tree.getroot()

print root

# root = ET.fromstring(country_data_as_string)

for child in root:
    print child.tag, child.attrib

print root[0][0].text

for neighbor in root.iter('neighbor'):
    print neighbor.attrib

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print name, rank