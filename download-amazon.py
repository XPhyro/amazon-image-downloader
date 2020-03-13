#!/usr/bin/env python
# Downloads all images of a product on Amazon

import json
# import requests
import os

source=input("Enter the name of the file that the page source is in.\n> ")

token="jQuery.parseJSON"

with open(source,"r") as f:
	strippedlines=[line for line in f if token in line]

imageline=strippedlines[0][28:][:-4].replace("\\\'","\'")
obj=json.loads(imageline)

links=[]

for i in obj["colorImages"].values():
	for j in i:
		if "hiRes" in j.keys():
			links.append(j["hiRes"])
		else:
			links.append(list(j["main"])[0])

#this might be a false alert #len(links)==0 => check for obj["staticImages"] or other variants

#for i in range(0,len(links)):
#	with open("amazon/{}.jpg".format(i),"wb") as f:
#		response=requests.get(links[i],stream=True)
#		for block in response.iter_content(1024):
#			if not block:
#				break
#		f.write(block)

path=input("Where would you like to download the images to (default: ~/Downloads/amazon-images)?\n> ")
if path=="":
	path="~/Downloads/amazon-images"

os.system("mkdir -p \"{}\"".format(path))

for i in links:
	os.system("wget -P \"{}\" \"{}\"".format(path,i))
