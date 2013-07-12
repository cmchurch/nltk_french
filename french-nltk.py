# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# IMPORTS AND FUNCTION DEFINITIONS (Natural Language Toolkit and Stanford POS Tagger)

# <codecell>

#Christopher M. Church
#PhD Candidate, UC Berkeley, History
#Social Science D-Lab, UC Berkeley

# <codecell>

#IMPORTS AND FUNCTION DEFINITIONS

#NLTK

#imports
import nltk #import the natural language toolkit library
from nltk.stem.snowball import FrenchStemmer #import the French stemming library
from nltk.corpus import stopwords #import stopwords from nltk corpus
import re #import the regular expressions library; will be used to strip punctuation
from collections import Counter #allows for counting the number of occurences in a list

import os #import os module
root_path = "D:\\PhD Research - UC Berkeley\\Research\\Pelee XML" #define a working directory path
os.chdir(root_path) #set the working directory path

#reading in the raw text from the file
def read_raw_file(path):
    '''reads in raw text from a text file using the argument (path), which represents the path/to/file'''
    f = open(path,"r") #open the file located at "path" as a file object (f) that is readonly
    raw = f.read().decode('utf8') # read raw text into a variable (raw) after decoding it from utf8
    f.close() #close the file now that it isn;t being used any longer
    return raw

def get_tokens(raw,encoding='utf8'):
    '''get the nltk tokens from a text'''
    tokens = nltk.word_tokenize(raw) #tokenize the raw UTF-8 text
    return tokens

def get_nltk_text(raw,encoding='utf8'):
    '''create an nltk text using the passed argument (raw) after filtering out the commas'''
    #turn the raw text into an nltk text object
    no_commas = re.sub(r'[.|,|\']',' ', raw) #filter out all the commas, periods, and appostrophes using regex
    tokens = nltk.word_tokenize(no_commas) #generate a list of tokens from the raw text
    text=nltk.Text(tokens,encoding) #create a nltk text from those tokens
    return text

def get_stopswords(type="veronis"):
    '''returns the veronis stopwords in unicode, or if any other value is passed, it returns the default nltk french stopwords'''
    if type=="veronis":
        #VERONIS STOPWORDS
        raw_stopword_list = ["Ap.", "Apr.", "GHz", "MHz", "USD", "a", "afin", "ah", "ai", "aie", "aient", "aies", "ait", "alors", "après", "as", "attendu", "au", "au-delà", "au-devant", "aucun", "aucune", "audit", "auprès", "auquel", "aura", "aurai", "auraient", "aurais", "aurait", "auras", "aurez", "auriez", "aurions", "aurons", "auront", "aussi", "autour", "autre", "autres", "autrui", "aux", "auxdites", "auxdits", "auxquelles", "auxquels", "avaient", "avais", "avait", "avant", "avec", "avez", "aviez", "avions", "avons", "ayant", "ayez", "ayons", "b", "bah", "banco", "ben", "bien", "bé", "c", "c'", "c'est", "c'était", "car", "ce", "ceci", "cela", "celle", "celle-ci", "celle-là", "celles", "celles-ci", "celles-là", "celui", "celui-ci", "celui-là", "celà", "cent", "cents", "cependant", "certain", "certaine", "certaines", "certains", "ces", "cet", "cette", "ceux", "ceux-ci", "ceux-là", "cf.", "cg", "cgr", "chacun", "chacune", "chaque", "chez", "ci", "cinq", "cinquante", "cinquante-cinq", "cinquante-deux", "cinquante-et-un", "cinquante-huit", "cinquante-neuf", "cinquante-quatre", "cinquante-sept", "cinquante-six", "cinquante-trois", "cl", "cm", "cm²", "comme", "contre", "d", "d'", "d'après", "d'un", "d'une", "dans", "de", "depuis", "derrière", "des", "desdites", "desdits", "desquelles", "desquels", "deux", "devant", "devers", "dg", "différentes", "différents", "divers", "diverses", "dix", "dix-huit", "dix-neuf", "dix-sept", "dl", "dm", "donc", "dont", "douze", "du", "dudit", "duquel", "durant", "dès", "déjà", "e", "eh", "elle", "elles", "en", "en-dehors", "encore", "enfin", "entre", "envers", "es", "est", "et", "eu", "eue", "eues", "euh", "eurent", "eus", "eusse", "eussent", "eusses", "eussiez", "eussions", "eut", "eux", "eûmes", "eût", "eûtes", "f", "fait", "fi", "flac", "fors", "furent", "fus", "fusse", "fussent", "fusses", "fussiez", "fussions", "fut", "fûmes", "fût", "fûtes", "g", "gr", "h", "ha", "han", "hein", "hem", "heu", "hg", "hl", "hm", "hm³", "holà", "hop", "hormis", "hors", "huit", "hum", "hé", "i", "ici", "il", "ils", "j", "j'", "j'ai", "j'avais", "j'étais", "jamais", "je", "jusqu'", "jusqu'au", "jusqu'aux", "jusqu'à", "jusque", "k", "kg", "km", "km²", "l", "l'", "l'autre", "l'on", "l'un", "l'une", "la", "laquelle", "le", "lequel", "les", "lesquelles", "lesquels", "leur", "leurs", "lez", "lors", "lorsqu'", "lorsque", "lui", "lès", "m", "m'", "ma", "maint", "mainte", "maintes", "maints", "mais", "malgré", "me", "mes", "mg", "mgr", "mil", "mille", "milliards", "millions", "ml", "mm", "mm²", "moi", "moins", "mon", "moyennant", "mt", "m²", "m³", "même", "mêmes", "n", "n'avait", "n'y", "ne", "neuf", "ni", "non", "nonante", "nonobstant", "nos", "notre", "nous", "nul", "nulle", "nº", "néanmoins", "o", "octante", "oh", "on", "ont", "onze", "or", "ou", "outre", "où", "p", "par", "par-delà", "parbleu", "parce", "parmi", "pas", "passé", "pendant", "personne", "peu", "plus", "plus_d'un", "plus_d'une", "plusieurs", "pour", "pourquoi", "pourtant", "pourvu", "près", "puisqu'", "puisque", "q", "qu", "qu'", "qu'elle", "qu'elles", "qu'il", "qu'ils", "qu'on", "quand", "quant", "quarante", "quarante-cinq", "quarante-deux", "quarante-et-un", "quarante-huit", "quarante-neuf", "quarante-quatre", "quarante-sept", "quarante-six", "quarante-trois", "quatorze", "quatre", "quatre-vingt", "quatre-vingt-cinq", "quatre-vingt-deux", "quatre-vingt-dix", "quatre-vingt-dix-huit", "quatre-vingt-dix-neuf", "quatre-vingt-dix-sept", "quatre-vingt-douze", "quatre-vingt-huit", "quatre-vingt-neuf", "quatre-vingt-onze", "quatre-vingt-quatorze", "quatre-vingt-quatre", "quatre-vingt-quinze", "quatre-vingt-seize", "quatre-vingt-sept", "quatre-vingt-six", "quatre-vingt-treize", "quatre-vingt-trois", "quatre-vingt-un", "quatre-vingt-une", "quatre-vingts", "que", "quel", "quelle", "quelles", "quelqu'", "quelqu'un", "quelqu'une", "quelque", "quelques", "quelques-unes", "quelques-uns", "quels", "qui", "quiconque", "quinze", "quoi", "quoiqu'", "quoique", "r", "revoici", "revoilà", "rien", "s", "s'", "sa", "sans", "sauf", "se", "seize", "selon", "sept", "septante", "sera", "serai", "seraient", "serais", "serait", "seras", "serez", "seriez", "serions", "serons", "seront", "ses", "si", "sinon", "six", "soi", "soient", "sois", "soit", "soixante", "soixante-cinq", "soixante-deux", "soixante-dix", "soixante-dix-huit", "soixante-dix-neuf", "soixante-dix-sept", "soixante-douze", "soixante-et-onze", "soixante-et-un", "soixante-et-une", "soixante-huit", "soixante-neuf", "soixante-quatorze", "soixante-quatre", "soixante-quinze", "soixante-seize", "soixante-sept", "soixante-six", "soixante-treize", "soixante-trois", "sommes", "son", "sont", "sous", "soyez", "soyons", "suis", "suite", "sur", "sus", "t", "t'", "ta", "tacatac", "tandis", "te", "tel", "telle", "telles", "tels", "tes", "toi", "ton", "toujours", "tous", "tout", "toute", "toutefois", "toutes", "treize", "trente", "trente-cinq", "trente-deux", "trente-et-un", "trente-huit", "trente-neuf", "trente-quatre", "trente-sept", "trente-six", "trente-trois", "trois", "très", "tu", "u", "un", "une", "unes", "uns", "v", "vers", "via", "vingt", "vingt-cinq", "vingt-deux", "vingt-huit", "vingt-neuf", "vingt-quatre", "vingt-sept", "vingt-six", "vingt-trois", "vis-à-vis", "voici", "voilà", "vos", "votre", "vous", "w", "x", "y", "z", "zéro", "à", "ç'", "ça", "ès", "étaient", "étais", "était", "étant", "étiez", "étions", "été", "étée", "étées", "étés", "êtes", "être", "ô"]
    else:
        #get French stopwords from the nltk kit
        raw_stopword_list = stopwords.words('french') #create a list of all French stopwords
    stopword_list = [word.decode('utf8') for word in raw_stopword_list] #make to decode the French stopwords as unicode objects rather than ascii
    return stopword_list
    

def filter_stopwords(text,stopword_list):
    '''normalizes the words by turning them all lowercase and then filters out the stopwords'''
    words=[w.lower() for w in text] #normalize the words in the text, making them all lowercase
    #filtering stopwords
    filtered_words = [] #declare an empty list to hold our filtered words
    for word in words: #iterate over all words from the text
        if word not in stopword_list and word.isalpha() and len(word) > 1: #only add words that are not in the French stopwords list, are alphabetic, and are more than 1 character
            filtered_words.append(word) #add word to filter_words list if it meets the above conditions
    filtered_words.sort() #sort filtered_words list
    return filtered_words
    
def stem_words(words):
    '''stems the word list using the French Stemmer'''
    #stemming words
    stemmed_words = [] #declare an empty list to hold our stemmed words
    stemmer = FrenchStemmer() #create a stemmer object in the FrenchStemmer class
    for word in words:
        stemmed_word=stemmer.stem(word) #stem the word
        stemmed_words.append(stemmed_word) #add it to our stemmed word list
    stemmed_words.sort() #sort the stemmed_words
    return stemmed_words
   
def sort_dictionary(dictionary):
    '''returns a sorted dictionary (as tuples) based on the value of each key'''
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

def normalize_counts(counts):
    total = sum(counts.values())
    return dict((word, float(count)/total) for word,count in counts.items())
        
def print_sorted_dictionary(tuple_dict):
    '''print the results of sort_dictionary'''
    for tup in tuple_dict:
        print unicode(tup[1])[0:10] + '\t\t' + unicode(tup[0])
        
def print_words(words):
    '''clean print the unicode words'''
    for word in words:
        print word
        
#USING STANFORD'S FRENCH POS TAGGER, v.3.2
#http://nlp.stanford.edu/software/tagger.shtml
#note: to get NLTK to find java with the tagger, I had to comment out lines 59 and 85 [config_java(options=self.java_options, verbose=False)] in stanford.py [C:\Anaconda\Lib\site-packages\nltk\tag\stanford.py]
#then I had to set the python path directly
        
import nltk #import the Natural Language Processing Kit
from nltk.tag.stanford import POSTagger #Get the Part of Speech tagger from NLP at Stanford, python module that interacts with Java
nltk.internals.config_java("C:/Program Files/Java/jdk1.7.0_21/bin/java.exe", options='-mx1000m',verbose=False) #set the path to java (note: i had to edit stanford.py and comment conflicting settings on lines 59 and 85

tag_abbreviations = {
                    'A': 'adjective',
                    'Adv': 'adverb',
                    'CC': 'coordinating conjunction',
                    'Cl': 'weak clitic pronoun',
                    'CS': 'subordinating conjunction',
                    'D': 'determiner',
                    'ET': 'foreign word',
                    'I': 'interjection',
                    'NC': 'common noun',
                    'NP': 'proper noun',
                    'P': 'preposition',
                    'PREF': 'prefix',
                    'PRO': 'strong pronoun',
                    'V': 'verb',
                    'PONCT': 'punctuation mark',
                    'N': 'noun'}

def pos_tag(to_tag,model_path = root_path + "\\stanford-postagger-full-2013-06-20\\models\\french.tagger",jar_path = root_path + "\\stanford-postagger-full-2013-06-20\\stanford-postagger.jar"):
    '''tag the tokens with part of speech; to_tag is the tags; model_path is the file path to the stanford POS tagger model; and jar_path to the Stanford POS tagger jar file'''
    pos_tagger = POSTagger(model_path,jar_path,encoding='utf8') #create an object of class POSTagger that is encoded in UTF-8
    tags = pos_tagger.tag(to_tag) #run the tagging algorithm on the tokenized raw text
    return tags

def print_pos_tags(tags):
    '''print all the tags with their part of speech; tag[0] is the word; tag[1] is the Part of Speech'''
    for tag in tags: print tag[1]+'\t',tag[0] 
            
def get_pos_tags(tags,pos='ANY'):
    '''get all the tags with their part of speech; tag[0] is the word; tag[1] is the Part of Speech'''
    pos=pos.upper()
    get_tags = []
    if pos=='ANY':
        print 'Please specify a tag to get' 
    else:
        tag_abbreviations_upper = {k.upper():v for k,v in tag_abbreviations.items()}
        if pos in tag_abbreviations_upper:
            for tag in tags: 
                if tag[1].upper()==pos: get_tags.append(tag[0])
        else:
            print "%s is not a valid search term." %(pos)
    return get_tags
            
def search_pos(tags,search_term,pos):
    '''look for a particular POS word prior to the search term, see what comes after the search term'''
    print "POS\tPREC\t\tS.TERM\t\tSUC\n"
    for i,tag in enumerate(tags):
        if tags[i-1][1].upper()==pos.upper() and tag[0].lower()==search_term.lower():
            print str(i)+'\t'+tags[i-1][0]+"\t" + tag[0] + "\t" + tags[i+1][0]

# <headingcell level=2>

# LOAD THE XML FILES

# <codecell>

#this python file goes through the xml doccuments and prints out the text data for a particular element name

#included libraries
import os #allows for path crawling
from xml.dom import minidom #understands XML DOMs

#variables
xml_path= root_path + "\\xmls" #set the path that we are going to read through
elem_name = "para" #name of the dom element to look for
xmls=[] #open up an empty array into which we will store our XML filenames

#get filenames
for root,dirs,files in os.walk(xml_path): #walk through the filepath and look for xml files, storing them in xmls array
    for file in files:
        if file.endswith('.xml'):
            xmls.append(file)
print "Files Loaded: ",xmls


documents=[] #initialize an empty documents array
all_documents={'tokens':[],'raw':''} #initialize an empty all_documents list

#this turns our list of documents read in from the xml files into a list of nltk documents
#each document has an index (ex. documents[0]), and within each document is a dictionary with the items: newspaper, date, raw,tokens, and 
for xml in xmls: # go through each xml document in our xmls array
    xmldoc = minidom.parse(xml_path + "\\" + xml) #parse the XML doc
    itemlist = xmldoc.getElementsByTagName(elem_name) #get all paragraph (para) elements
    newspaper = xmldoc.getElementsByTagName('newspaper') #get newspaper element
    newspaper_name= newspaper[0].attributes['name'].value #set the newspaper_name to the name attribute of the newspaper element
    date = newspaper[0].attributes['date'].value #set the newspaper date to the date attribute of the newspaper element
    raw = '' #initialize the raw variable
    for item in itemlist:
        raw += ' '.join(t.nodeValue for t in item.childNodes if t.nodeType == t.TEXT_NODE) # add text from the node's data to the variable raw if the node's data is text
    raw = re.sub(r'\s+', ' ',raw) #remove the excess whitespace from the raw text
    tokens = get_tokens(raw) #get the tokens from the text
    text = get_nltk_text(raw) #create a nltk text from the xml document's raw text
    documents.append({'newspaper':newspaper_name,'date':date,'raw':raw,'tokens':tokens,'text':text}) #add all our elements to the array (documents); each element in the array is a dictionary
    all_documents['tokens'].extend(tokens)
    all_documents['raw']+=raw
    
documents = sorted(documents, key=lambda doc: doc['date'])#sort the array according to a document's date
#to sort by paper name then date, use documents = sorted(documents, key=lambda doc: (doc['newspaper'],doc['date']))

# <codecell>

# Set variables common to all functions in analysis
french_stopwords = get_stopswords()

# <headingcell level=2>

# ANALYSIS CODE

# <codecell>

#print a sorted dictionary of all stemmed and filtered words for each text
for document in documents:
    filtered_words = filter_stopwords(document['text'],french_stopwords)
    print '\n',document['newspaper'],'\t',document['date'],'\n---------------'
    print_sorted_dictionary(sort_dictionary(Counter(stem_words(filtered_words))))

# <codecell>

#print a count of all adjectives filtered for stopwords and stemmed for each text as well as a count of adjectives for all texts
def stemmed_adjectives(tokens):
     tags = pos_tag(tokens)
     adjectives = get_pos_tags(tags,'a') #get all adjectives from the text
     adj_text = nltk.Text(adjectives,'utf8') #create an nltk text from those adjectives
     filtered_adjectives = filter_stopwords(adj_text,french_stopwords) #filter out stopwwords from the adjectives
     stemmed_adjectives = stem_words(filtered_adjectives) #stem the adjectives to normalize them
     adjective_count = sort_dictionary(Counter(stemmed_adjectives)) #count and sort the adjectives
     print_sorted_dictionary(adjective_count) #print the adjectives
        
for document in documents:
     print '\n',document['newspaper'],' - ',document['date'],'\n-----------------------------'
     print stemmed_adjectives(document['tokens'])
print 'ALL TEXT\n----------\n', stemmed_adjectives(all_documents['tokens'])

# <codecell>

tags=pos_tag(all_documents['tokens'])
nouns=get_pos_tags(tags,'n') #get all the nouns from the pos tagger
filtered_nouns = filter_stopwords(nouns,french_stopwords) #filter the veronis stopwords out of the noun tags
noun_count = Counter(filtered_nouns) #count the filtered nouns
noun_count = normalize_counts(noun_count) #normalize the counts by how many words are in the articles related to Martinique
noun_count = sort_dictionary(noun_count) #sort the dictionary into a sorted tuple list
print_sorted_dictionary(noun_count) #print the sorted tuples 

# <codecell>

search_pos(tags,'catastrophe','a')

# <codecell>

sorted_stemmed_words = sort_dictionary(stemmed_word_count)
print_sorted_dictionary(sorted_stemmed_words)

# <codecell>

print Counter([tag[1] for tag in tags]) #count the parts of speech

# <codecell>

for document in documents: print document['newspaper'],': ',document['date'],'\n\n',document['raw'],'\n\n*******\n\n' #print out all the paragraphs from each xml file

# <codecell>

# print the concordance of a term for all of our nltk documents that had been read in from the xml files
for document in documents:
    print "DATE: %s \t NEWSPAPER: %s" %(document['date'],document['newspaper'])
    print '------'
    print document['text'].concordance('Martinique')
    print '\n'

# <codecell>

for document in documents: print "NEWSPAPER: %s \t DATE: %s \t WORD COUNT: %s \t CHARACTER COUNT: %s" %(document['newspaper'],document['date'],len(document['tokens']),len(document['raw']))

# <codecell>


