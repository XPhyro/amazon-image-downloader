#!/usr/bin/env python
# Downloads all images of a product on Amazon

import json
import os

source = input("Enter the name of the file that the page source is in.\n> ")

token = "jQuery.parseJSON"

with open(source,"r") as f:
    strippedlines=[line for line in f if token in line]

imageLine = strippedlines[0][28:][:-4].replace("\\\'","\'")
obj = json.loads(imageLine)

links=[]

for i in obj["colorImages"].values():
    for j in i:
        if "hiRes" in j.keys():
	    links.append(j["hiRes"])
	else:
	    links.append(list(j["main"])[0])

defaultPath = "~/downloads/amazon-images/{}".format(source)

path = input("Where would you like to download the images to (default: {})?\n> ".format(defaultPath))

if path == "":
    path = defaultPath

os.system("mkdir -p \"{}\"".format(path))

for i in links:
    os.system("wget -P \"{}\" \"{}\"".format(path,i))

