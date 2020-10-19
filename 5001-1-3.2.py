import xml.dom.minidom
import re

dom = xml.dom.minidom.parse('/Users/JwPrince/Desktop/HKUST DDM/5001 Introduction to Computational and Modeling Tools/assi/assi1/blocklist.xml')
root = dom.documentElement
itemlist = root.getElementsByTagName('emItem')
for i in range(len(itemlist)):
    item = itemlist[i]
    att_value1 = item.getAttribute('blockID')
    att_value2 = item.getAttribute('id')
    result = re.match(r'^[A-Za-z0-9_]+@[A-Za-z0-9]+\.com$', att_value2)
    if result:
        print(r'<emItem blockID="{}" id="{}">'.format(att_value1,att_value2))
