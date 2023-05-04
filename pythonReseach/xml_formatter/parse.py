import xml.etree.ElementTree as ET

mytree = ET.parse("product.xml")
myroot = mytree.getroot()

# tag, attrib, text
print(myroot.tag)
print(myroot[0].tag)
print(myroot[0].attrib)

#for x in myroot[0]:
#    print(x.tag, x.attrib)


# find all <tag> name
for x in myroot.findall('product'):
    item = x.find('name').text
    ids = x.find('id').text
    print("item : {} ids : {}".format(item, ids))
