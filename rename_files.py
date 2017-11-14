#This file renames all the images in the PASCAL VOC dataset.
#The files are renamed in numerical order with neccessary padding
#of '0's to make the name 6 character long.
#
import pickle
import os

f = open("mappings.pkl", "r")

mappings = pickle.load(f)

f.close()


f = open("mappings.pkl","w")
pickle.dump( mappings, f, pickle.HIGHEST_PROTOCOL) 
f.close()

PADDING_LENGTH = 6
for file_number in mappings:
	old_name = mappings[file_number][0]
	#print old_name
	new_name = str(file_number)
	new_name = (PADDING_LENGTH - len(new_name))*"0" + new_name
	#print new_name
	os.rename("./JPEGImages/"+old_name, "./JPEGImages/"+new_name+".jpg")

