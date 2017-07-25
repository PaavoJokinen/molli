#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import xml.etree.ElementTree as ET
tree = ET.parse('dictionary.xml')
root = tree.getroot()
print(root.tag)

for child in root:
  print(child.tag, child.attrib)
  for grandchild in child:
    print(grandchild.tag)

print(len(root.getchildren()))


#print(Word.tag)
