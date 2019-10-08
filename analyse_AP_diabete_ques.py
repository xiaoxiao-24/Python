import psycopg2
import re
import pandas as pd
from collections import Counter
from PIL import Image,ImageFont
from os import path
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt


# connect to DB
conn = psycopg2.connect(database = "EDU", user = "postgres", password = "gdrp1&L@tifi", host = "dbp.gdrpi.fr", port = "5432")
cur = conn.cursor()
# get phrase a analyser
cur.execute('''select "Suggestions" from "AP_DIABETE_QUESTIONNAIRE" where "Suggestions" is not null;''')
rows = cur.fetchall()
'''
for row in rows:
	print(row)
'''	
conn.close()

# les mots qui n'ont pas de sense
stopword = ["de","le","la","les","contre","qui","quoi","pourquoi","que","quel","quelle","souvent","car","lors","!",",","?",".","-",
"il","elle","je","tu","moi","toi","etre","tous","tout","toute","ne","peux","peut","ce","cet","cette","avec","sans","faire","ca","soit","sois",
"fait","fais","au","aux","a","ou","et","dans","en","pas","du","pour","des","sur","dessous","dessus","/","serait","d","avoir",
"est","on","pouvoir","pourrait","lorsque","par","dont","d'autres","d'autre","autre","lieu","peu","beaucoup","plus","moins","tres",
"du","une","un","autres","autre","cas","j'ai","nous","ils","elles","oui","non","apres","se","me","te","don","vih","vis","mst","meme","orl","rien"]

# define function pour conter les mots
def most_common_words(labels):
		words = []
		for lab in labels:
				words += [re.sub(r'(d\'.*|l\'.*|.*\xc3\xa9.*|.*\xc3\xa8.*|.*\xc3\xaa.*|.*\xc3\xb4.*|.*\xc3\xa0.*)','',''.join(w)) for w in lab.lower().split(" ") if not w in stopword]
		counter = Counter(words)
		for word in counter.most_common(100):
				if word is '':
						pass
				else:
						print(word)
				

# transformer list to DataFrame
rows_df = pd.DataFrame(list(rows), columns=[1])

# utiliser "iloc" pour choisir la colonne
most_common_words(rows_df.iloc[:,0])

def get_words(labels):
    words = []
    for lab in labels:
		words += [w for w in lab.lower().split(" ") if not w in stopword]
    return words

nuage = get_words(rows_df.iloc[:,0])
#nuage2 = nuage.decode("utf-8")
#nuage2 = [x.encode('utf-8') for x in nuage]  # list to string
nuage_str = ",".join(nuage)
	
#d = path.dirname('__file__')
#fonts_path = path.join(d, 'NotoSansCJK-DemiLight.ttc')
fonts_path = "C:\Windows\Fonts\Arial.ttf"
wc = WordCloud(font_path = fonts_path, width=800, height=400, background_color='white').generate(nuage_str)

# show image directly
#image = wc.to_image()
#image.show()

# save image to path
plt.figure(1,figsize=(13, 13))
plt.imshow(wc)
plt.axis('off')
plt.savefig('D:\\xiaoxiao\\script\\python\\connect_postgres\\QuesDiabete.png')
plt.close()