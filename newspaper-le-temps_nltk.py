#this python file goes through the xml doccuments and prints out the text data for a particular element name
#Christopher M. Church
#PhD Candidate, UC Berkeley, History
#Social Science D-Lab, UC Berkeley

#USE REGEX INSTEAD OF XML PARSE; lower overhead; also, the files themselves had some problems in the XML and were not properly formed, which resulted in a parse error exception; regex is agnostic to this problem
import re

#variables
path="C:\\Users\\Christopher\\Desktop\\1890\\edit" #set the path that we are going to read through
elem_name = "span" #name of the dom element to look for
xmls=[] #open up an empty array into which we will store our XML filenames
output_file="\\all-text.txt"

#get filenames
for root,dirs,files in os.walk(path): #walk through the filepath and look for xml files, storing them in xmls array
    for file in files:
        if file.endswith('.html'):
            xmls.append(file)

output=open(path+output_file,"w") #OPEN AN OUTPUT FILE FOR ALL THE REGEX MATCHES
for xml in xmls: #iterate over the files found in the os path walk
    print xml, #for debugging, print what xml we are on
    f = open(path + "\\" + xml, "r") #open the xml (xhtml)
    text = f.read() #read it as raw text
    regex = re.compile('(<span class="PAG.*?>)(.*?)(</span>)') #create a regular expression with three groups (<span>) (VALUE) (</span>)
    matches = regex.findall(text) #create a list of tuples that contain our three matched regular expressions
    for match in matches: output.write(match[1]+" ") #save only the second group (the value) and delimit it with a space so we can tokenize later 
    f.close() #close the xml (xhtml)
output.close() #close the output file)