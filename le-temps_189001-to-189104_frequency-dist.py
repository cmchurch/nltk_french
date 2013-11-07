# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Christopher M. Church
#PHD Candidate, Department of History
#Social Science Data Lab (D-Lab)
#University of California, Berkeley

import os #operating system library for os-walk

#global variables

#set the root path for the working directory
#root_path="E:\\Webscraping\\20130827_bnfscrape-data\\working-files\\period2" #set the path that we are going to read through
root_path = "C:\\Users\\Church\\Desktop\\working-folder"

#VERONIS STOPWORDS (http://sites.univ-provence.fr/veronis/) (http://www.up.univ-mrs.fr/veronis/data/antidico.txt)
stopwords = ["Ap.", "Apr.", "GHz", "MHz", "USD", "a", "afin", "ah", "ai", "aie", "aient", "aies", "ait", "alors", "après", "as", "attendu", "au", "au-delà", "au-devant", "aucun", "aucune", "audit", "auprès", "auquel", "aura", "aurai", "auraient", "aurais", "aurait", "auras", "aurez", "auriez", "aurions", "aurons", "auront", "aussi", "autour", "autre", "autres", "autrui", "aux", "auxdites", "auxdits", "auxquelles", "auxquels", "avaient", "avais", "avait", "avant", "avec", "avez", "aviez", "avions", "avons", "ayant", "ayez", "ayons", "b", "bah", "banco", "ben", "bien", "bé", "c", "c'", "c'est", "c'était", "car", "ce", "ceci", "cela", "celle", "celle-ci", "celle-là", "celles", "celles-ci", "celles-là", "celui", "celui-ci", "celui-là", "celà", "cent", "cents", "cependant", "certain", "certaine", "certaines", "certains", "ces", "cet", "cette", "ceux", "ceux-ci", "ceux-là", "cf.", "cg", "cgr", "chacun", "chacune", "chaque", "chez", "ci", "cinq", "cinquante", "cinquante-cinq", "cinquante-deux", "cinquante-et-un", "cinquante-huit", "cinquante-neuf", "cinquante-quatre", "cinquante-sept", "cinquante-six", "cinquante-trois", "cl", "cm", "cm²", "comme", "contre", "d", "d'", "d'après", "d'un", "d'une", "dans", "de", "depuis", "derrière", "des", "desdites", "desdits", "desquelles", "desquels", "deux", "devant", "devers", "dg", "différentes", "différents", "divers", "diverses", "dix", "dix-huit", "dix-neuf", "dix-sept", "dl", "dm", "donc", "dont", "douze", "du", "dudit", "duquel", "durant", "dès", "déjà", "e", "eh", "elle", "elles", "en", "en-dehors", "encore", "enfin", "entre", "envers", "es", "est", "et", "eu", "eue", "eues", "euh", "eurent", "eus", "eusse", "eussent", "eusses", "eussiez", "eussions", "eut", "eux", "eûmes", "eût", "eûtes", "f", "fait", "fi", "flac", "fors", "furent", "fus", "fusse", "fussent", "fusses", "fussiez", "fussions", "fut", "fûmes", "fût", "fûtes", "g", "gr", "h", "ha", "han", "hein", "hem", "heu", "hg", "hl", "hm", "hm³", "holà", "hop", "hormis", "hors", "huit", "hum", "hé", "i", "ici", "il", "ils", "j", "j'", "j'ai", "j'avais", "j'étais", "jamais", "je", "jusqu'", "jusqu'au", "jusqu'aux", "jusqu'à", "jusque", "k", "kg", "km", "km²", "l", "l'", "l'autre", "l'on", "l'un", "l'une", "la", "laquelle", "le", "lequel", "les", "lesquelles", "lesquels", "leur", "leurs", "lez", "lors", "lorsqu'", "lorsque", "lui", "lès", "m", "m'", "ma", "maint", "mainte", "maintes", "maints", "mais", "malgré", "me", "mes", "mg", "mgr", "mil", "mille", "milliards", "millions", "ml", "mm", "mm²", "moi", "moins", "mon", "moyennant", "mt", "m²", "m³", "même", "mêmes", "n", "n'avait", "n'y", "ne", "neuf", "ni", "non", "nonante", "nonobstant", "nos", "notre", "nous", "nul", "nulle", "nº", "néanmoins", "o", "octante", "oh", "on", "ont", "onze", "or", "ou", "outre", "où", "p", "par", "par-delà", "parbleu", "parce", "parmi", "pas", "passé", "pendant", "personne", "peu", "plus", "plus_d'un", "plus_d'une", "plusieurs", "pour", "pourquoi", "pourtant", "pourvu", "près", "puisqu'", "puisque", "q", "qu", "qu'", "qu'elle", "qu'elles", "qu'il", "qu'ils", "qu'on", "quand", "quant", "quarante", "quarante-cinq", "quarante-deux", "quarante-et-un", "quarante-huit", "quarante-neuf", "quarante-quatre", "quarante-sept", "quarante-six", "quarante-trois", "quatorze", "quatre", "quatre-vingt", "quatre-vingt-cinq", "quatre-vingt-deux", "quatre-vingt-dix", "quatre-vingt-dix-huit", "quatre-vingt-dix-neuf", "quatre-vingt-dix-sept", "quatre-vingt-douze", "quatre-vingt-huit", "quatre-vingt-neuf", "quatre-vingt-onze", "quatre-vingt-quatorze", "quatre-vingt-quatre", "quatre-vingt-quinze", "quatre-vingt-seize", "quatre-vingt-sept", "quatre-vingt-six", "quatre-vingt-treize", "quatre-vingt-trois", "quatre-vingt-un", "quatre-vingt-une", "quatre-vingts", "que", "quel", "quelle", "quelles", "quelqu'", "quelqu'un", "quelqu'une", "quelque", "quelques", "quelques-unes", "quelques-uns", "quels", "qui", "quiconque", "quinze", "quoi", "quoiqu'", "quoique", "r", "revoici", "revoilà", "rien", "s", "s'", "sa", "sans", "sauf", "se", "seize", "selon", "sept", "septante", "sera", "serai", "seraient", "serais", "serait", "seras", "serez", "seriez", "serions", "serons", "seront", "ses", "si", "sinon", "six", "soi", "soient", "sois", "soit", "soixante", "soixante-cinq", "soixante-deux", "soixante-dix", "soixante-dix-huit", "soixante-dix-neuf", "soixante-dix-sept", "soixante-douze", "soixante-et-onze", "soixante-et-un", "soixante-et-une", "soixante-huit", "soixante-neuf", "soixante-quatorze", "soixante-quatre", "soixante-quinze", "soixante-seize", "soixante-sept", "soixante-six", "soixante-treize", "soixante-trois", "sommes", "son", "sont", "sous", "soyez", "soyons", "suis", "suite", "sur", "sus", "t", "t'", "ta", "tacatac", "tandis", "te", "tel", "telle", "telles", "tels", "tes", "toi", "ton", "toujours", "tous", "tout", "toute", "toutefois", "toutes", "treize", "trente", "trente-cinq", "trente-deux", "trente-et-un", "trente-huit", "trente-neuf", "trente-quatre", "trente-sept", "trente-six", "trente-trois", "trois", "très", "tu", "u", "un", "une", "unes", "uns", "v", "vers", "via", "vingt", "vingt-cinq", "vingt-deux", "vingt-huit", "vingt-neuf", "vingt-quatre", "vingt-sept", "vingt-six", "vingt-trois", "vis-à-vis", "voici", "voilà", "vos", "votre", "vous", "w", "x", "y", "z", "zéro", "à", "ç'", "ça", "ès", "étaient", "étais", "était", "étant", "étiez", "étions", "été", "étée", "étées", "étés", "êtes", "être", "ô"]
lower_stopwords = [] #make all the stopwords lowercase in order to normalize them
for stopword in stopwords:
    lower_stopwords.append(stopword.lower())

# <headingcell level=1>

# STRIP TEXT FROM BNF OCR

# <codecell>

#STRIP TEXT FROM BNF OCR HTML

#USE REGEX INSTEAD OF XML PARSE; lower overhead; also, the files themselves had some problems in the XML and were not properly formed, which resulted in a parse error exception; regex is agnostic to this problem
import re #regex library

path=root_path
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

# <headingcell level=1>

# READ IN TEXT ONCE IT'S BEEN STRIPPED AND ADD IT TO A DATA STRUCTURE

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
path=root_path+relative_path
docs=[] #init an empty docs array to store our newspaper documents

for root,dirs,files in os.walk(path): #walk through the filepath and look for xml files, storing them in docs array
    for file in files:
        if file.endswith('.txt'):
             open_doc = open(path+"\\"+file, "r") #open the file
             open_doc_text = open_doc.read() #read the text
             filename_array = string.split(str(file),"_") #explode the file name on the "_" character, grabbing the newspaper name and the date
             tokens = nltk.word_tokenize(open_doc_text) #create tokens based on whitespace (word_tokenize)
             sentences = nltk.sent_tokenize(open_doc_text) #grab sentences from nltk (sent_tokenize)
             text = nltk.text.Text(tokens,'UTF8') #create an NTLK text from the word tokens
             freqDist = nltk.FreqDist(word.lower() for word in tokens if re.match("^[a-zäáàëéèíìöóòúùñç.-]+$", word.lower()) and word.lower() not in stopwords) #create a frequency distribution (normalized with lowercase words) for this newspaper issue, and discard any non-alphanumeric words
             docs.append({"newspaper_name":filename_array[1],"newspaper_date":filename_array[0],"newspaper_rawtext":open_doc_text,"tokens":tokens,"sentences":sentences,"text":text,"dist":freqDist }) #add all the information to a dictionary object in an array (see above)
             print "read: " + filename_array[0], #let the user know what document we are on
             open_doc.close() #close the open document that was being read

                
print "Done!" #print complete message

# <codecell>

#AGGREGATE FREQUENCY DISTRIBUTIONS BY MONTH
#stores this in a dictionary called "MONTH"
relative_path = "\\freqdist\\bymonth"
month = {}

print "Aggregating"
#this aggregates the information by month
for doc in docs: #go through all the documents
    print ".",
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
print "Done!"

# <headingcell level=1>

# OUTPUT TO / READ FROM JSON

# <codecell>

#output all the frequencies aggregated by month into a json

#whitespace=1 for pretty print; whitespace=0 to decrease size
whitespace=0 

#path information
relative_path = "\\text\\freqdist\\bymonth" #relative path
path=root_path+relative_path #absolute path

#begin creating json file
print "Outputting frequencies by month to a json file" #let user know the process started
f = open(path + "\\" + "freqdist_monthly.json","w") #open a month file to output to
f.write("{")
total_months = len(month.items()) #total number of months in the list
j=0 #track the number of months, so that commas are not added at the end of the list
for m,dist in month.items(): #go through our monthly distributions
    j+=1 #j++
    if whitespace==1: f.write('\n') #add in whitespace for pretty print
    f.write('"'+m+'":{')
    length=len(dist.items()) #total number of items in the frequency distribution
    i=0 #use i to track the position in the list, so that commas are not added to the end of the list
    for k,v in dist.items(): #get the keys (k) and values (v) for each frequency distribution based on a given month
        if whitespace==1: f.write('\n\t') #add white space for pretty print
        f.write('"'+str(k)+'":'+str(v)) #write it out following the format ("KEY", value)
        i+=1 #i++
        if i<length: #only add a comma if not at the end of the list
            f.write(',')
    f.write("}")
    if j<total_months: #only add a comma if not at the end of the list
        f.write(',')
    print ".", #print a dot to let the user know it's working
if whitespace==1: f.write("\n")
f.write("}")
f.close() #close the file
print "Done!" #let the user know we are all done

# <codecell>

#REIMPORT THE JSON FILE CREATED
import json #import the json library
json_path = root_path + "\\text\\freqdist\\bymonth\\freqdist_monthly.json" #relative path

json_data=open(json_path,"r") #open the json file
data = json.load(json_data) #load the json file as an object (converts it into a dictionary) and store it as "data"
json_data.close() #close the open file

# <headingcell level=1>

# OUTPUT TO CSV FILES

# <codecell>

#export All Frequency distributions for each individual newspaper issue to its own CSV file
relative_path = "\\freqdist" #set the relative path
path = root_path+relative_path
print "Exporting frequency distributions" #let the user know what we are doing
for doc in docs: #go through all our documents
    f = open(path + "\\" + str(doc["newspaper_date"])+"_"+doc["newspaper_name"]+"_freqdist.txt","w") #open a file to store our frequency distribution
    for k,v in doc["dist"].items(): #go through each frequency distribution and write it to a file that matches the "newspaper_name"-"newspaper_date"
        string = "'"+k +"'," + str(v) + "\n" #write it in the following CSV format ( 'KEY',value )
        f.write(string) #write it to the file
    f.close() #close the working file
    print ".", #print a dot to let the user know we're working
print "Done!" #let the user know the task is done

# <codecell>

#output all the frequencies aggregated by month into a text csv for each month

relative_path = "\\text\\freqdist\\bymonth" #relative path
path=root_path+relative_path #absolute path

print "Outputting frequencies by month" #let user know the process started
for m,dist in month.items(): #go through our monthly distributions
    f = open(path + "\\" + str(m) + "_freqdist_monthly.txt","w") #open a month file to output to
    for k,v in dist.items(): #get the keys (k) and values (v) for each frequency distribution based on a given month
        f.write("'"+str(k)+"', "+str(v)+'\n') #write it out following the format ("KEY", value)
    print ".", #print a dot to let the user know it's working
    f.close() #close the file
print "Done!" #let the user know we are all done

# <headingcell level=1>

# MATPLOTLIB APPLICATION

# <codecell>

#CREATE A SCATTERPLOT OF KEYTERM USE BY MONTH FOR THE PERIOD
#USING MATPLOTLIB
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import date #needed to parse the dates

#ENTER SEARCH TERM HERE
search_term="paris"

coords = [] #initialize an array to store x,y tuples

for a,b in data.iteritems(): #iterate through the points dictionary, and concatenate the month and year as a date for the x value; the frequency will be the y value
     year = a[:4]
     month = a[4:6]
     if search_term in b.keys():
          freq  = b[search_term]
     else:
          freq = 0
     xy=(date(int(year),int(month),1),freq)
     coords.append(xy)

x=[] #initialize an empty array of x coordinates
y=[] #initialize an empty array of y coordinates

for a,b in sorted(coords):
    x.append(a)
    y.append(b)
        
dateformat = dates.DateFormatter('%Y-%m', tz=None) #format the date, YYYY-MM
plt.plot(x,y) #create the scatter plot
ax=plt.gca() #call up the axis and store it as "ax"
ax.xaxis.set_major_formatter(dateformat) #convert the xaxis of the plot to match our date formatter
plt.show() #print the graph

# <headingcell level=1>

# WORKSPACE - testing code that isn't yet operational

# <codecell>

#NOT WORKING - DO NOT RUN
#output all the frequencies aggregated by month into a text csv for overall, with the following format:
#   TOKEN    1890-01    1890-02    1890-03    .....
#   france     1            2         0       .....
#   incendie   0            10        2       .....



relative_path = "\\text\\freqdist\\total" #relative path
path=root_path+relative_path #absolute path

print "Outputting frequencies by month to a single csv" #let user know the process started

f = open(path + "\\" + "total_freqdist_monthly.csv","w") #open a file to output to

for m,dist in month.items(): #go through our monthly distributions 
    for k,v in dist.items(): #get the keys (k) and values (v) for each frequency distribution based on a given month
        f.write("'"+str(k)+"', "+str(v)+'\n') #write it out following the format ("KEY", value)
    print ".", #print a dot to let the user know it's working
    f.close() #close the file
print "Done!" #let the user know we are all done

# <codecell>

print data

# <codecell>

print xmls

# <codecell>

for stopword in lower_stopwords:
    print '"'+stopword + '", ',

# <codecell>


