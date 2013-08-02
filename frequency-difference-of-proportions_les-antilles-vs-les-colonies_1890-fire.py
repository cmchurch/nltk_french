#Christopher M. Church
#PhD Candidate, UC Berkeley, History
#Social Science D-Lab, UC Berkeley

#This python file is used to compare two sets of Martiniquais Newspapers -- Les Colonies, Marius Hurard's conservative Republican paper, and Les Antilles, the beke-dominated, Catholic paper
#It was created to compare the news coverage of the 1890 Fire of Fort-de-France; it covers the first weeks of local coverage of the fire
#The Veronis Stopwords are filtered out of the results.
#Veronis stopwords were created by Jean VÉRONIS, Professeur de linguistique et d'informatique, University of Aix-en-Provence 
#    more info can be found at: 
#       a) http://sites.univ-provence.fr/~veronis/  
#       b) http://sites.univ-provence.fr/veronis/data/antidico.txt)
#The script generates a Difference of Proportions Frequency Distribution from the two sets of newspapers, and then uses matplotlib to create a graph that shows
#    1) the frequency of the tokens along the x-axis, as well with regard to the size of each token
#    2) the difference of proportions along the y-axis, as well as with regard to the color of each token (red = Les Colonies; blue = Les Antilles; yellow = neutral)
#The XML documents were created by an undergraduate research assistant, Yvonne Lin, as part of the SMART (Student Mentoring and Research Teams) Program at the University of California, Berkeley


#imports
import nltk #import the natural language toolkit library
import re #import the regular expressions library; will be used to strip punctuation
import os #allows for path crawling
from xml.dom import minidom #understands XML DOMs
import matplotlib.pyplot as plt #import plotter from matplotlib in the namespace plt
import matplotlib.cm as cm #import colormpas from matplotlib in the namespace cm (for more colormaps, see http://matplotlib.org/examples/pylab_examples/show_colormaps.html)



#--------------------
#=LOAD THE XML FILES-
#--------------------

#variables
global root_path
root_path = "D:\\PhD Research - UC Berkeley\\Research\\DisasterXML" #define a working directory path
xml_path= root_path + "\\SMART1890FireXML" #set the path that we are going to read through
elem_name = "para" #name of the dom element to look for

#get xml files
documents=[] #initialize an empty documents array
all_documents={'tokens':[],'raw':''} #initialize an empty all_documents list

for root,dirs,files in os.walk(xml_path): #walk through the filepath and look for xml files, storing them in xmls array
    for file in files:
        if file.endswith('.xml'):
            xmldoc = minidom.parse(xml_path + "\\" + file) #parse the XML doc
            itemlist = xmldoc.getElementsByTagName(elem_name) #get all paragraph (para) elements
            newspaper = xmldoc.getElementsByTagName('newspaper') #get newspaper element
            newspaper_name= newspaper[0].attributes['name'].value #set the newspaper_name to the name attribute of the newspaper element
            date = newspaper[0].attributes['date'].value #set the newspaper date to the date attribute of the newspaper element
            raw = '' #initialize the raw variable
            for item in itemlist:
                raw += ' '.join(t.nodeValue for t in item.childNodes if t.nodeType == t.TEXT_NODE)+' ' # add text from the node's data to the variable raw if the node's data is text, also add whitepsace afte reach para element when appended to the raw text variable
            raw = re.sub(r'\s+', ' ',raw) #remove the excess whitespace from the raw text
            tokens = nltk.word_tokenize(raw) #get the tokens from the text
            text = nltk.text.Text(tokens,'UTF8') #create a nltk text from the xml document's raw text
            documents.append({'newspaper':newspaper_name,'date':date,'raw':raw,'tokens':tokens,'text':text}) #add all our elements to the array (documents); each element in the array is a dictionary
            all_documents['tokens'].extend(tokens)
            all_documents['raw']+=raw
            print "Loaded: ", file
  
documents = sorted(documents, key=lambda doc: doc['date'])#sort the array according to a document's date
#to sort by paper name then date, use documents = sorted(documents, key=lambda doc: (doc['newspaper'],doc['date']))

# Set variables common to all functions in analysis
#VERONIS STOPWORDS
global french_stopwords
veronis_stopwords = ["Ap.", "Apr.", "GHz", "MHz", "USD", "a", "afin", "ah", "ai", "aie", "aient", "aies", "ait", "alors", "après", "as", "attendu", "au", "au-delà", "au-devant", "aucun", "aucune", "audit", "auprès", "auquel", "aura", "aurai", "auraient", "aurais", "aurait", "auras", "aurez", "auriez", "aurions", "aurons", "auront", "aussi", "autour", "autre", "autres", "autrui", "aux", "auxdites", "auxdits", "auxquelles", "auxquels", "avaient", "avais", "avait", "avant", "avec", "avez", "aviez", "avions", "avons", "ayant", "ayez", "ayons", "b", "bah", "banco", "ben", "bien", "bé", "c", "c'", "c'est", "c'était", "car", "ce", "ceci", "cela", "celle", "celle-ci", "celle-là", "celles", "celles-ci", "celles-là", "celui", "celui-ci", "celui-là", "celà", "cent", "cents", "cependant", "certain", "certaine", "certaines", "certains", "ces", "cet", "cette", "ceux", "ceux-ci", "ceux-là", "cf.", "cg", "cgr", "chacun", "chacune", "chaque", "chez", "ci", "cinq", "cinquante", "cinquante-cinq", "cinquante-deux", "cinquante-et-un", "cinquante-huit", "cinquante-neuf", "cinquante-quatre", "cinquante-sept", "cinquante-six", "cinquante-trois", "cl", "cm", "cm²", "comme", "contre", "d", "d'", "d'après", "d'un", "d'une", "dans", "de", "depuis", "derrière", "des", "desdites", "desdits", "desquelles", "desquels", "deux", "devant", "devers", "dg", "différentes", "différents", "divers", "diverses", "dix", "dix-huit", "dix-neuf", "dix-sept", "dl", "dm", "donc", "dont", "douze", "du", "dudit", "duquel", "durant", "dès", "déjà", "e", "eh", "elle", "elles", "en", "en-dehors", "encore", "enfin", "entre", "envers", "es", "est", "et", "eu", "eue", "eues", "euh", "eurent", "eus", "eusse", "eussent", "eusses", "eussiez", "eussions", "eut", "eux", "eûmes", "eût", "eûtes", "f", "fait", "fi", "flac", "fors", "furent", "fus", "fusse", "fussent", "fusses", "fussiez", "fussions", "fut", "fûmes", "fût", "fûtes", "g", "gr", "h", "ha", "han", "hein", "hem", "heu", "hg", "hl", "hm", "hm³", "holà", "hop", "hormis", "hors", "huit", "hum", "hé", "i", "ici", "il", "ils", "j", "j'", "j'ai", "j'avais", "j'étais", "jamais", "je", "jusqu'", "jusqu'au", "jusqu'aux", "jusqu'à", "jusque", "k", "kg", "km", "km²", "l", "l'", "l'autre", "l'on", "l'un", "l'une", "la", "laquelle", "le", "lequel", "les", "lesquelles", "lesquels", "leur", "leurs", "lez", "lors", "lorsqu'", "lorsque", "lui", "lès", "m", "m'", "ma", "maint", "mainte", "maintes", "maints", "mais", "malgré", "me", "mes", "mg", "mgr", "mil", "mille", "milliards", "millions", "ml", "mm", "mm²", "moi", "moins", "mon", "moyennant", "mt", "m²", "m³", "même", "mêmes", "n", "n'avait", "n'y", "ne", "neuf", "ni", "non", "nonante", "nonobstant", "nos", "notre", "nous", "nul", "nulle", "nº", "néanmoins", "o", "octante", "oh", "on", "ont", "onze", "or", "ou", "outre", "où", "p", "par", "par-delà", "parbleu", "parce", "parmi", "pas", "passé", "pendant", "personne", "peu", "plus", "plus_d'un", "plus_d'une", "plusieurs", "pour", "pourquoi", "pourtant", "pourvu", "près", "puisqu'", "puisque", "q", "qu", "qu'", "qu'elle", "qu'elles", "qu'il", "qu'ils", "qu'on", "quand", "quant", "quarante", "quarante-cinq", "quarante-deux", "quarante-et-un", "quarante-huit", "quarante-neuf", "quarante-quatre", "quarante-sept", "quarante-six", "quarante-trois", "quatorze", "quatre", "quatre-vingt", "quatre-vingt-cinq", "quatre-vingt-deux", "quatre-vingt-dix", "quatre-vingt-dix-huit", "quatre-vingt-dix-neuf", "quatre-vingt-dix-sept", "quatre-vingt-douze", "quatre-vingt-huit", "quatre-vingt-neuf", "quatre-vingt-onze", "quatre-vingt-quatorze", "quatre-vingt-quatre", "quatre-vingt-quinze", "quatre-vingt-seize", "quatre-vingt-sept", "quatre-vingt-six", "quatre-vingt-treize", "quatre-vingt-trois", "quatre-vingt-un", "quatre-vingt-une", "quatre-vingts", "que", "quel", "quelle", "quelles", "quelqu'", "quelqu'un", "quelqu'une", "quelque", "quelques", "quelques-unes", "quelques-uns", "quels", "qui", "quiconque", "quinze", "quoi", "quoiqu'", "quoique", "r", "revoici", "revoilà", "rien", "s", "s'", "sa", "sans", "sauf", "se", "seize", "selon", "sept", "septante", "sera", "serai", "seraient", "serais", "serait", "seras", "serez", "seriez", "serions", "serons", "seront", "ses", "si", "sinon", "six", "soi", "soient", "sois", "soit", "soixante", "soixante-cinq", "soixante-deux", "soixante-dix", "soixante-dix-huit", "soixante-dix-neuf", "soixante-dix-sept", "soixante-douze", "soixante-et-onze", "soixante-et-un", "soixante-et-une", "soixante-huit", "soixante-neuf", "soixante-quatorze", "soixante-quatre", "soixante-quinze", "soixante-seize", "soixante-sept", "soixante-six", "soixante-treize", "soixante-trois", "sommes", "son", "sont", "sous", "soyez", "soyons", "suis", "suite", "sur", "sus", "t", "t'", "ta", "tacatac", "tandis", "te", "tel", "telle", "telles", "tels", "tes", "toi", "ton", "toujours", "tous", "tout", "toute", "toutefois", "toutes", "treize", "trente", "trente-cinq", "trente-deux", "trente-et-un", "trente-huit", "trente-neuf", "trente-quatre", "trente-sept", "trente-six", "trente-trois", "trois", "très", "tu", "u", "un", "une", "unes", "uns", "v", "vers", "via", "vingt", "vingt-cinq", "vingt-deux", "vingt-huit", "vingt-neuf", "vingt-quatre", "vingt-sept", "vingt-six", "vingt-trois", "vis-à-vis", "voici", "voilà", "vos", "votre", "vous", "w", "x", "y", "z", "zéro", "à", "ç'", "ça", "ès", "étaient", "étais", "était", "étant", "étiez", "étions", "été", "étée", "étées", "étés", "êtes", "être", "ô"]
french_stopwords = [w.decode('utf8') for w in veronis_stopwords]

#-------------------------------------
#-CALCULATE DIFFERENCE OF PROPORTIONS-
#-------------------------------------

all_words ={'les colonies':'','les antilles':'','journal officiel de la guadeloupe':''}
for document in documents:
    all_words[str(document['newspaper'].lower())]+=document['raw'].lower()

def diff_prop(text1, text2):
    """
    returns a FreqDist that includes the difference in proportions between text 1 and text 2
	Thanks to Aditi Muralidharan for a great workshop on NLTK and the code for this function
    """
    vocab1 = text1.vocab()
    vocab2 = text2.vocab()

    diff_prop = nltk.FreqDist()

    for word in vocab1.keys():
        if word not in french_stopwords and len(word) > 1 and word.isalpha():
            freq1 = vocab1.freq(word)
            freq2 = vocab2.freq(word)
            diff_prop.inc(word, freq1 - freq2)

    for word in vocab2.keys():
        if word not in diff_prop and word not in french_stopwords and len(word)and word.isalpha() > 1:
            freq1 = vocab1.freq(word)
            freq2 = vocab2.freq(word)
            diff_prop.inc(word, freq1 - freq2)
    return diff_prop


#create texts from the two sets of newspapers (Les Antilles and Les Colonies)
les_antilles = nltk.text.Text(nltk.word_tokenize(all_words['les antilles']))
les_colonies = nltk.text.Text(nltk.word_tokenize(all_words['les colonies']))

#create a differences of proportion frequency distribution
differences = diff_prop(les_antilles,les_colonies)


#-----------------------------------------------
#-PRINT THE DIFFERENCE OF PROPORTIONS FREQ DIST-
#-----------------------------------------------
x=[]
y=[]
label=[]
keys = differences.keys()
v1 = les_antilles.vocab()
v2 = les_colonies.vocab()
print 'WORD\t','DIFF\t','FREQ'
for key in keys:
    print key,'\t',differences[key],'\t',int(v1[key]+v2[key])
    label.append(key)
    y.append(differences[key])
    x.append(int(v1[key]+v2[key]))


#------------
#-MATPLOTLIB-
#------------
#create a scatterplot with a colorscape 

for a,b,c in zip(label,x,y):
    Val=0.5+(c*1000)
    color=cm.Spectral(Val)
    plt.scatter(b, c,s=b**1.4,c=color,alpha=0.5)
    s=b/5
    if s > 20: s=20
    point_label = plt.annotate(a,xy=(b,c),size=s,horizontalalignment='center',verticalalignment='center') 
    point_label.draggable()
plt.xscale('log')
plt.xlim([0,200])
plt.ylim([-0.0025,0.0025])
plt.xlabel('Frequency of word in both newspapers (Logarithmic Scale)')
plt.ylabel('Difference of Proportions (Freq Difference)')
plt.title('Difference of Proportions in Word Distribution between Les Antilles (top) and Les Colonies (bottom)')
plt.show()