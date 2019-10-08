# pip install nltk
import nltk
import psycopg2
import pandas as pd
from collections import Counter

test = "Bonjour, je suis un texte d'exemple pour le cours d'Openclassrooms. Soyez attentifs à ce cours !"

nltk.download('punkt')
nltk.word_tokenize(test)

# use expression reguliere pour recuperer les mots
tokenizer = nltk.RegexpTokenizer(r'\w+')
test_token = tokenizer.tokenize(test) # que les mots sont garde

# get stopwords
# pip install stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words("french"))
for w in test_token:
	if w not in stop_words:
		print(w)
		

# --------------------------------------------------------------
# une autre data source

# connect to DB
conn = psycopg2.connect(database = "EDU", user = "postgres", password = "gdrp1&L@tifi", host = "dbp.gdrpi.fr", port = "5432")
cur = conn.cursor()
# get phrase a analyser
cur.execute('''select "Suggestions" from "AP_DIABETE_QUESTIONNAIRE" where "Suggestions" is not null;''')
rows = cur.fetchall()

# transformer list to DataFrame
rows_df = pd.DataFrame(list(rows), columns=[1])

# les mots qui n'ont pas de sense
stopword = ["de","le","la","les","contre","qui","quoi","pourquoi","que","quel","quelle","souvent","car","lors","!",",","?",".","-",
"il","elle","je","tu","moi","toi","etre","tous","tout","toute","ne","peux","peut","ce","cet","cette","avec","sans","faire","ca","soit","sois",
"fait","fais","au","aux","a","ou","et","dans","en","pas","du","pour","des","sur","dessous","dessus","/",":","serait","d","avoir",
"est","on","pouvoir","pourrait","lorsque","par","dont","d'autres","d'autre","autre","lieu","peu","beaucoup","plus","moins","tres",
"du","une","un","autres","autre","cas","j'ai","nous","ils","elles","oui","non","apres","se","me","te","don","vih","vis","mst","meme","orl","rien"]
# lemmatisation, get origin of word
from nltk.stem.snowball import FrenchStemmer
stemmer = FrenchStemmer()
# define function pour conter les mots
def most_common_words(labels):
		words = []
		for lab in labels:
				#words += tokenizer.tokenize(lab)
				words += [w for w in tokenizer.tokenize(lab.lower()) if not w in stopword]
				words += [re.sub(r'(d\'.*|l\'.*|.*\xc3\xa9.*|.*\xc3\xa8.*|.*\xc3\xaa.*|.*\xc3\xb4.*|.*\xc3\xa0.*|.*\xc3|\xc3|\xe2)','',''.join(w)) for w in tokenizer.tokenize(lab.lower()) if not w in stopword]
				words += [stemmer.stem(re.sub(r'(d\'.*|l\'.*|.*\xc3\xa9.*|.*\xc3\xa8.*|.*\xc3\xaa.*|.*\xc3\xb4.*|.*\xc3\xa0.*|.*\xc3|\xc3|\xe2)','',''.join(w))) for w in tokenizer.tokenize(lab.lower()) if not w in stopword]
		counter = Counter(words)
		for word in counter.most_common(100):
				if not word:
						pass
				elif word not in stop_words:
						print(word)
				else:
						pass
						
# utiliser "iloc" pour choisir la colonne
most_common_words(rows_df.iloc[:,0])