#this python file goes through the xml doccuments and generates a filetree xml document
#Christopher M. Church
#PhD Candidate, UC Berkeley, History
#Social Science D-Lab, UC Berkeley

import os

xmls=[]
for root,dirs,files in os.walk(r'C:\Users\Christopher\Dropbox\xml'):
    for file in files:
        if file.endswith('.xml'):
            xmls.append(file)

filetree = open("C:\\Users\\Christopher\\Dropbox\\xml\\filetree.txt", "w")

filetree.write('<?xml version="1.0" encoding="UTF-8"?>\n')
filetree.write("<filetree>\n")
for xml in xmls:
    filetree.write("<fpath>"+xml+"</fpath>\n")
filetree.write("</filetree>")
    
filetree.close()