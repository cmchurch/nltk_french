# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Christopher M. Church
#PHD Candidate, Department of History
#Social Science Data Lab (D-Lab)
#University of California, Berkeley

#USE REGEX INSTEAD OF XML PARSE; lower overhead; also, the files themselves had some problems in the XML and were not properly formed, which resulted in a parse error exception; regex is agnostic to this problem
import re #regex library
import os #operating system library for os-walk

#global variables

#set the root path for the working directory
#root_path="E:\\Webscraping\\20130827_bnfscrape-data\\working-files\\period2" #set the path that we are going to read through
root_path = "C:\\Users\\Christopher\\Desktop\\nltk - le temps data\\edit"

# <codecell>

#STRIP TEXT FROM BNF OCR HTML


elem_name = "span" #name of the dom element to look for
xmls=[] #open up an empty array into which we will store our XML filenames

#get filenames through OS.walk
for root,dirs,files in os.walk(path): #walk through the filepath and look for xml files, storing them in xmls array
    for file in files:
        if file.endswith('.html'):
            xmls.append(file)

for xml in xmls: #for each file found that ended with html, read it and grab the text in SPAN elements and export it to a 'txt' file
    output=open(path+"\\text\\"+xml.replace(".html",".txt"),"w")
    print xml,
    f = open(path + "\\" + xml, "r")
    text = f.read()
    regex = re.compile('(<span class="PAG.*?>)(.*?)(</span>)')
    matches = regex.findall(text)
    for match in matches: output.write(match[1]+" ")
    f.close()
    output.close()

# <codecell>

#ADD TEXT TO DATA STRUCTURE (dictionary)
# data structure model
# docs[] = { 
#              "newspaper_name": name ,                   #THE NAME OF THE NEWSPAPER
#              "newspaper_date":date ,                    #THE DATE OF THE NEWSPAPER
#              "newspaper_rawtext": open_doc_text,        #THE RAW TEXT OF THE NEWSPAPER
#              "tokens": tokens,                          #TOKENS (words) FROM NLTK, word_tokenize
#              "sentences": sentences,                    #SENTENCES (sent) FROM NLTK, sent_tokenize
#              "text", text                               #THE CONVERTED NLTK TEXT OF THE DOCUMENT BASED ON TOKENS
#              "dist", freqDist                           #WORD FREQUENCY DISTRIBUTION OF THE NEWSPAPER
#          }


import string #include the string library to use "endswith()"
import nltk #import the natural language toolkit library

#get filenames
relative_path = "\\text" #set the relative working path
docs=[] #init an empty docs array to store our newspaper documents

for root,dirs,files in os.walk(path): #walk through the filepath and look for xml files, storing them in docs array
    for file in files:
        if file.endswith('.txt'):
             open_doc = open(root_path+relative_path+"\\"+file, "r") #open the file
             open_doc_text = open_doc.read() #read the text
             filename_array = string.split(str(file),"_") #explode the file name on the "_" character, grabbing the newspaper name and the date
             tokens = nltk.word_tokenize(open_doc_text) #create tokens based on whitespace (word_tokenize)
             sentences = nltk.sent_tokenize(open_doc_text) #grab sentences from nltk (sent_tokenize)
             text = nltk.text.Text(tokens,'UTF8') #create an NTLK text from the word tokens
             freqDist = nltk.FreqDist(word.lower() for word in tokens) #create a frequency distribution (normalized with lowercase words) for this newspaper issue
             docs.append({"newspaper_name":filename_array[1],"newspaper_date":filename_array[0],"newspaper_rawtext":open_doc_text,"tokens":tokens,"sentences":sentences,"text":text,"dist":freqDist }) #add all the information to a dictionary object in an array (see above)
             print "read: " + filename_array[0] #let the user know what document we are on
             open_doc.close() #close the open document that was being read

                
print "Done!" #print complete message

# <codecell>

#CREATE A SCATTERPLOT OF KEYTERM USE BY MONTH FOR THE PERIOD
#USING MATPLOTLIB
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import date #needed to parse the dates

#ENTER SEARCH TERM HERE
search_term="fort-de-france"

points={} #create an empty dictionary known as "points" -- this will store the informtion for each data point (x,y) on our scatterplot


#this aggregates the information by month
for doc in docs: #go through all the documents
    date_month = doc['newspaper_date'][:6] #grab the date from the first 6 characters, which gives you the year and month
    current_y = doc['dist'][search_term] #look up the raw count of the word from "search_term" in a given document
    if date_month in points: #if the month is already in our points array, then look up its key and add the current value to it
        total_y = current_y + points[date_month]
        points[date_month]=total_y
    else: #if we haven't already created a key for a given month, do it now
        points[date_month]=current_y

x=[] #initialize an empty array for our X values
y=[] #initialize an empty array for our Y values
 
for a,b in points.iteritems(): #iterate through the points dictionary, and concatenate the month and year as a date for the x value; the frequency will be the y value
     year = a[:4]
     month = a[4:6]
     x.append(date(int(year),int(month),1))
     y.append(int(b))
        
        
dateformat = dates.DateFormatter('%Y-%m', tz=None) #format the date, YYYY-MM
plt.scatter(x,y) #create the scatter plot
ax=plt.gca() #call up the axis and store it as "ax"
ax.xaxis.set_major_formatter(dateformat) #convert the xaxis of the plot to match our date formatter
plt.show() #print the graph

# <codecell>

#export All Frequency distributions for each individual newspaper issue to its own CSV file
relative_path = "\\freqdist" #set the relative path
print "Exporting frequency distributions" #let the user know what we are doing
for doc in docs: #go through all our documents
    f = open(root_path + relative_path + "\\" + str(doc["newspaper_date"])+"_"+doc["newspaper_name"]+"_freqdist.txt","w") #open a file to store our frequency distribution
    for k,v in doc["dist"].items(): #go through each frequency distribution and write it to a file that matches the "newspaper_name"-"newspaper_date"
        string = "'"+k +"'," + str(v) + "\n" #write it in the following CSV format ( 'KEY',value )
        f.write(string) #write it to the file
    f.close() #close the working file
    print ".", #print a dot to let the user know we're working
print "Done!" #let the user know the task is done

# <codecell>

for doc in docs:
    print doc["newspaper_date"]

# <codecell>

#AGGREGATE FREQUENCY DISTRIBUTIONS BY MONTH -- note: not working!
relative_path = "\\freqdist\\bymonth"
month = {}
#this aggregates the information by month
for doc in docs: #go through all the documents
    date_month = str(doc['newspaper_date'][:6]) #grab the date from the first 6 characters, which gives you the year and month
    current_distribution = doc['dist']
    if date_month in month: #if the month is already in our months array, then look up its key and add the current value to it
        for k,v in current_distribution.items(): #go through each frequency distribution and write it to a file that matches the "newspaper_name"-"newspaper_date"
            if k in month[date_month]:
                month[date_month][k]+=v
            else:
                month[date_month][k]=v
    else: #if we haven't already created a key for a given month, do it now
        month[date_month]=current_distribution

# <codecell>

print month

# <codecell>

print month['189104']

# <codecell>


