#This file gets the annotation information for the images in the 
#PASCAL VOC dataset. 
#We are only concerned the objects in the image.
#
import os
import xml.etree.ElementTree as ET
import pickle
next_number = 1
mappings = {}
for filename in os.listdir("./JPEGImages"):
	mappings[next_number] = [filename]
	next_number += 1

count = 0
different_items = []
#print len(mappings.keys())
for key in mappings:
	filename = mappings[key][0]
	xml_name = filename.strip(".jpg")+".xml"
	tree = ET.parse( "./Annotations/"+xml_name)
	objects = tree.findall("./object")
	for obj in objects:
		name = obj.find("name")
		if name.text not in different_items:
			different_items.append(name.text)
		#print name.text
		bndbx = obj.find("bndbox")
		xmin = bndbx.find("xmin").text
		xmax = bndbx.find("xmax").text
		ymin = bndbx.find("ymin").text
		ymax = bndbx.find("ymax").text
		#print xmin, ymin, xmax, ymax
		mappings[key].append((name.text, xmin, ymin, xmax, ymax))
	#print objects
	count+=1	
	#print mappings[key]


for key in mappings:
	print mappings[key]

f = open("mappings.pkl", "w")
pickle.dump(mappings, f, pickle.HIGHEST_PROTOCOL)
f.close()
f = open("different_items","w")
f.write(",".join(different_items))
f.close()


 
print different_items
