from bs4 import BeautifulSoup
'''import matplotlib
import networkx'''
import requests
import matplotlib.pyplot as plt
import spacy
import numpy as num
import matplotlib.pyplot as plotting

fast_nouns = []
fast_adjectives = []
fast_verbs = []
lums_nouns = []
lums_adjectives = []
lums_verbs = []
giki_nouns = []
giki_adjectives = []
giki_verbs = []


fast1_html = requests.get("http://nu.edu.pk/")
fast1_txt = fast1_html.text
fast1_soup = BeautifulSoup(fast1_txt, 'html.parser')
fast1_alltext = fast1_soup.get_text()
print(fast1_alltext)

word1 = fast1_alltext
nlp = spacy.load('en_core_web_sm')
wordw1 = nlp(word1)
for token in wordw1:
    if token.pos_ == 'NOUN':
        fast_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       fast_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        fast_verbs.append(token.text)

fast2_html = requests.get("http://nu.edu.pk/Degree-Programs")
fast2_txt = fast2_html.text
fast2_soup = BeautifulSoup(fast2_txt, 'html.parser')
fast2_alltext = fast2_soup.get_text()
print(fast2_alltext)

word2 = fast2_alltext
nlp = spacy.load('en_core_web_sm')
wordw2 = nlp(word2)
for token in wordw2:
    if token.pos_ == 'NOUN':
        fast_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       fast_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        fast_verbs.append(token.text)

fast3_html = requests.get("http://nu.edu.pk/University/History")
fast3_txt = fast3_html.text
fast3_soup = BeautifulSoup(fast3_txt, 'html.parser')
fast3_alltext = fast3_soup.get_text()
print(fast3_alltext)

word3 = fast3_alltext
nlp = spacy.load('en_core_web_sm')
wordw3 = nlp(word3)
for token in wordw3:
    if token.pos_ == 'NOUN':
        fast_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       fast_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        fast_verbs.append(token.text)

fast4_html = requests.get("http://nu.edu.pk/Oric")
fast4_txt = fast4_html.text
fast4_soup = BeautifulSoup(fast4_txt, 'html.parser')
fast4_alltext = fast4_soup.get_text()
print(fast4_alltext)
word4 = fast4_alltext
nlp = spacy.load('en_core_web_sm')
wordw4 = nlp(word4)
for token in wordw4:
    if token.pos_ == 'NOUN':
        fast_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       fast_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        fast_verbs.append(token.text)

fast5_html = requests.get("http://nu.edu.pk/Admissions/EligibilityCriteria")
fast5_txt = fast5_html.text
fast5_soup = BeautifulSoup(fast5_txt, 'html.parser')
fast5_alltext = fast5_soup.get_text()
print(fast5_alltext)

word5 = fast5_alltext
nlp = spacy.load('en_core_web_sm')
wordw5 = nlp(word5)
for token in wordw5:
    if token.pos_ == 'NOUN':
        fast_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       fast_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        fast_verbs.append(token.text)

lums1_html = requests.get("https://lums.edu.pk/")
lums1_txt = lums1_html.text
lums1_soup = BeautifulSoup(lums1_txt, 'html.parser')
lums1_alltext = lums1_soup.get_text()
print(lums1_alltext)

word6 = lums1_alltext
nlp = spacy.load('en_core_web_sm')
wordw6 = nlp(word6)
for token in wordw6:
    if token.pos_ == 'NOUN':
        lums_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       lums_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        lums_verbs.append(token.text)

lums2_html = requests.get("https://admission.lums.edu.pk/")
lums2_txt = lums2_html.text
lums2_soup = BeautifulSoup(lums2_txt, 'html.parser')
lums2_alltext = lums2_soup.get_text()
print(lums2_alltext)

word7 = lums2_alltext
nlp = spacy.load('en_core_web_sm')
wordw7 = nlp(word7)
for token in wordw7:
    if token.pos_ == 'NOUN':
        lums_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       lums_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        lums_verbs.append(token.text)

lums3_html = requests.get("https://admissions.lums.edu.pk/application/")
lums3_txt = lums3_html.text
lums3_soup = BeautifulSoup(lums3_txt, 'html.parser')
lums3_alltext = lums3_soup.get_text()
print(lums3_alltext)

word8 = lums3_alltext
nlp = spacy.load('en_core_web_sm')
wordw8 = nlp(word8)
for token in wordw8:
    if token.pos_ == 'NOUN':
        lums_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       lums_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        lums_verbs.append(token.text)

lums4_html = requests.get("https://lums.edu.pk/news")
lums4_txt = lums4_html.text
lums4_soup = BeautifulSoup(lums4_txt, 'html.parser')
lums4_alltext = lums4_soup.get_text()
print(lums4_alltext)

word9 = lums4_alltext
nlp = spacy.load('en_core_web_sm')
wordw9 = nlp(word9)
for token in wordw9:
    if token.pos_ == 'NOUN':
        lums_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       lums_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        lums_verbs.append(token.text)

lums5_html = requests.get("https://lums.edu.pk/student-noticeboard")
lums5_txt = lums5_html.text
lums5_soup = BeautifulSoup(lums5_txt, 'html.parser')
lums5_alltext = lums5_soup.get_text()
print(lums5_alltext)

word10 = lums5_alltext
nlp = spacy.load('en_core_web_sm')
wordw10 = nlp(word10)
for token in wordw10:
    if token.pos_ == 'NOUN':
        lums_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       lums_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        lums_verbs.append(token.text)

giki1_html = requests.get("https://giki.edu.pk/")
giki1_txt = giki1_html.text
giki1_soup = BeautifulSoup(giki1_txt, 'html.parser')
giki1_alltext = giki1_soup.get_text()
print(giki1_alltext)

word11 = giki1_alltext
nlp = spacy.load('en_core_web_sm')
wordw11 = nlp(word11)
for token in wordw11:
    if token.pos_ == 'NOUN':
        giki_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       giki_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        giki_verbs.append(token.text)

giki2_html = requests.get("https://giki.edu.pk/institute/")
giki2_txt = giki2_html.text
giki2_soup = BeautifulSoup(giki2_txt, 'html.parser')
giki2_alltext = giki2_soup.get_text()
print(giki2_alltext)

word12 = giki2_alltext
nlp = spacy.load('en_core_web_sm')
wordw12 = nlp(word12)
for token in wordw12:
    if token.pos_ == 'NOUN':
        giki_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       giki_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        giki_verbs.append(token.text)

giki3_html = requests.get("https://giki.edu.pk/admissions/")
giki3_txt = giki3_html.text
giki3_soup = BeautifulSoup(giki3_txt, 'html.parser')
giki3_alltext = giki3_soup.get_text()
print(giki3_alltext)

word13 = giki3_alltext
nlp = spacy.load('en_core_web_sm')
wordw13 = nlp(word13)
for token in wordw13:
    if token.pos_ == 'NOUN':
        giki_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       giki_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        giki_verbs.append(token.text)

giki4_html = requests.get("https://giki.edu.pk/admissions/admissions-graduate/")
giki4_txt = giki4_html.text
giki4_soup = BeautifulSoup(giki4_txt, 'html.parser')
giki4_alltext = giki4_soup.get_text()
print(giki4_alltext)

word14 = giki4_alltext
nlp = spacy.load('en_core_web_sm')
wordw14 = nlp(word14)
for token in wordw14:
    if token.pos_ == 'NOUN':
        giki_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       giki_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        giki_verbs.append(token.text)

giki5_html = requests.get("https://giki.edu.pk/administration/")
giki5_txt = giki5_html.text
giki5_soup = BeautifulSoup(giki5_txt, 'html.parser')
giki5_alltext = giki5_soup.get_text()
print(giki5_alltext)

word15 = giki5_alltext
nlp = spacy.load('en_core_web_sm')
wordw15 = nlp(word15)
for token in wordw15:
    if token.pos_ == 'NOUN':
        giki_nouns.append(token.text)
    if token.pos_ == 'ADJ':
       giki_adjectives.append(token.text)
    if token.pos_ == 'VERB':
        giki_verbs.append(token.text)


FLGnouns = []
FLGnouns.append(len(fast_nouns))
FLGnouns.append(len(lums_nouns))
FLGnouns.append(len(giki_nouns))

FLGadjectives = []
FLGadjectives.append(len(fast_adjectives))
FLGadjectives.append(len(lums_adjectives))
FLGadjectives.append(len(giki_adjectives))

FLGverbs = []
FLGverbs.append(len(fast_verbs))
FLGverbs.append(len(lums_verbs))
FLGverbs.append(len(giki_verbs))

FLGaxis = [1, 2, 3]
nounsTotal = num.array(FLGnouns)
adjectivesTotal = num.array(FLGadjectives)
verbsTotal = num.array(FLGverbs)

plt.style.use("seaborn")
plt.title("PHASE-2 , i201833-i201884-PART-2 - VISUALLIZATION")
plt.scatter(FLGaxis, FLGnouns, s=nounsTotal, c=["Black"])
plt.xticks(([1, 2, 3]), ["FAST", "LUMS", "GIKI"])
plt.yticks([0, 250, 500, 750, 1000, 1500, 2000])
plt.ylabel("Nouns, Adjectives and Verbs Freq")
plt.grid(True)
plt.show()
plt.scatter(FLGaxis, FLGadjectives, s=adjectivesTotal/2, c=["Blue"])
plt.xticks(([1, 2, 3]), ["FAST", "LUMS", "GIKI"])
plt.yticks([0, 250, 500, 750, 1000, 1500, 2000])
plt.ylabel("Nouns, Adjectives and Verbs Freq")
plt.grid(True)
plt.show()
plt.scatter(FLGaxis, FLGverbs, s=verbsTotal, c=["Yellow"])
plt.xticks(([1, 2, 3]), ["FAST", "LUMS", "GIKI"])
plt.yticks([0, 250, 500, 750, 1000, 1500, 2000])
plt.ylabel("Nouns, Adjectives and Verbs Freq")
plt.grid(True)
plt.show()