import xml.etree.ElementTree as ET

tree = ET.parse('xml/humidex_8h.xml')

root = tree.getroot()

fun = []
# for elem in tree.iterfind('compounddef/sectiondef/memberdef[@kind="%s"]' % "function"):
#     # fun.append(elem.find('name').text)
import time
for elem in tree.iterfind('compounddef/sectiondef/memberdef[@kind="%s"]' % "function"):
    for elem2 in elem.iterfind('briefdescription/para'):
        if len(elem2.tag) > 0:
            fun.append(elem.find('name').text)
print fun

