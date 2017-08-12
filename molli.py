#!/Users/pjjokine/anaconda/bin/python3
#import xml.etree.ElementTree

from xml.etree import ElementTree



FromLang = "ru"
ToLang = "fi"

WordClasses = []

def appendWordClasses (MyClass, WCs):
  ShouldWeAppend = 'yes'
  for WordClass in (WCs):
    if WordClass == MyClass:
      ShouldWeAppend = 'no'
  if ShouldWeAppend == 'yes':
    WCs += MyClass
  print(WCs)

tree = ElementTree.parse('dictionary.xml')
root = tree.getroot()
#print(root.tag)
#print(tree)

for node in tree.iter('Word'):
  appendWordClasses(node.get('wordclass'),WordClasses)
  print (node.tag)
  print (node.attrib)
  print (node.get('wordclass'))
  for child in node:
    print (child.tag, "=", child.text)



#for word in root.findall('Word'):

#for child in root:
#  print(child.tag, child.attrib)
#  for grandchild in child:
#    print(grandchild.tag)
#
#print(len(root.getchildren()))


#print(Word.tag)


#Tarvittavia funktioita
#Hae sanaluokat
#Hae sanojen määrä
#Hae luokkakohtaiste määrät
#Hae tarjolla olevat kielet
#Hae kielivaihtoehtojen "mahtavuus"
