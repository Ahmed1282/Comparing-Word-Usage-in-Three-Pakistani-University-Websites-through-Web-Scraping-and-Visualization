import requests
from bs4 import BeautifulSoup

#Fast University
fast1_html = requests.get("http://nu.edu.pk/")
fast1_txt = fast1_html.text
fast1_soup = BeautifulSoup(fast1_txt, 'html.parser')
fast1_alltext = fast1_soup.get_text()
print(fast1_alltext)
fast2_html = requests.get("http://nu.edu.pk/Degree-Programs")
fast2_txt = fast2_html.text
fast2_soup = BeautifulSoup(fast2_txt, 'html.parser')
fast2_alltext = fast2_soup.get_text()
print(fast2_alltext)
fast3_html = requests.get("http://nu.edu.pk/University/History")
fast3_txt = fast3_html.text
fast3_soup = BeautifulSoup(fast3_txt, 'html.parser')
fast3_alltext = fast3_soup.get_text()
print(fast3_alltext)
fast4_html = requests.get("http://nu.edu.pk/Oric")
fast4_txt = fast4_html.text
fast4_soup = BeautifulSoup(fast4_txt, 'html.parser')
fast4_alltext = fast4_soup.get_text()
print(fast4_alltext)
fast5_html = requests.get("http://nu.edu.pk/Admissions/EligibilityCriteria")
fast5_txt = fast5_html.text
fast5_soup = BeautifulSoup(fast5_txt, 'html.parser')
fast5_alltext = fast5_soup.get_text()
print(fast5_alltext)

#Lums University
lums1_html = requests.get("https://lums.edu.pk/")
lums1_txt = lums1_html.text
lums1_soup = BeautifulSoup(lums1_txt, 'html.parser')
lums1_alltext = lums1_soup.get_text()
print(lums1_alltext)
lums2_html = requests.get("https://admission.lums.edu.pk/")
lums2_txt = lums2_html.text
lums2_soup = BeautifulSoup(lums2_txt, 'html.parser')
lums2_alltext = lums2_soup.get_text()
print(lums2_alltext)
lums3_html = requests.get("https://admissions.lums.edu.pk/application/")
lums3_txt = lums3_html.text
lums3_soup = BeautifulSoup(lums3_txt, 'html.parser')
lums3_alltext = lums3_soup.get_text()
print(lums3_alltext)
lums4_html = requests.get("https://lums.edu.pk/news")
lums4_txt = lums4_html.text
lums4_soup = BeautifulSoup(lums4_txt, 'html.parser')
lums4_alltext = lums4_soup.get_text()
print(lums4_alltext)
lums5_html = requests.get("https://lums.edu.pk/student-noticeboard")
lums5_txt = lums5_html.text
lums5_soup = BeautifulSoup(lums5_txt, 'html.parser')
lums5_alltext = lums5_soup.get_text()
print(lums5_alltext)

#Giki University
giki1_html = requests.get("https://giki.edu.pk/")
giki1_txt = giki1_html.text
giki1_soup = BeautifulSoup(giki1_txt, 'html.parser')
giki1_alltext = giki1_soup.get_text()
print(giki1_alltext)
giki2_html = requests.get("https://giki.edu.pk/institute/")
giki2_txt = giki2_html.text
giki2_soup = BeautifulSoup(giki2_txt, 'html.parser')
giki2_alltext = giki2_soup.get_text()
print(giki2_alltext)
giki3_html = requests.get("https://giki.edu.pk/admissions/")
giki3_txt = giki3_html.text
giki3_soup = BeautifulSoup(giki3_txt, 'html.parser')
giki3_alltext = giki3_soup.get_text()
print(giki3_alltext)
giki4_html = requests.get("https://giki.edu.pk/admissions/admissions-graduate/")
giki4_txt = giki4_html.text
giki4_soup = BeautifulSoup(giki4_txt, 'html.parser')
giki4_alltext = giki4_soup.get_text()
print(giki4_alltext)
giki5_html = requests.get("https://giki.edu.pk/administration/")
giki5_txt = giki5_html.text
giki5_soup = BeautifulSoup(giki5_txt, 'html.parser')
giki5_alltext = giki5_soup.get_text()
print(giki5_alltext)




