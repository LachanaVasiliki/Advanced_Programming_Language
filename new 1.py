
import requests
import re
import matplotlib.pyplot as plt
import numpy as np

r = requests.get('https://www.skroutz.gr/c/3363/sneakers.html')

c = r.content

from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(c)

main_content = soup.find_all('ol', attrs = {'id': "sku-list"})

internal_content = main_content[0].find_all('li', attrs = {'class': "cf card"})


titlespattern = '[A-Z][A-Za-z0-9]* '
colourspattern = '(Λευκά)|(Μαύρα)|(Ροζ)|(Μπεζ)|(Γκρι)|(Μπορντό)|(Πολύχρωμα)|(Μπλε)|(Κόκκινα)'
fylopattern = '(Unisex)|(Γυναικεία)|(Ανδρικά)'
pricespattern = '(\d+),(\d+) €+'
urlpattern = 'data-e2e-testid="sku-price-link" href=\"([^"]+)'
reviewpattern = '\"reviewCount\">([0-9]+)'
urls = re.findall(urlpattern,r.text)
Titles = []
Prices = []
Colours = []
Fylo = []
Reviews = []
for i,content_ in enumerate(internal_content):
    match = re.search(titlespattern, content_.text)
    if match:
        Titles.append(match.group())
    else:
        Titles.append(None)
    match = re.search(pricespattern, content_.text)
    if match:
        Prices.append(match.group())
    else:
        Prices.append(None)
    match = re.search(colourspattern, content_.text)
    if match:
        Colours.append(match.group())
    else:
        Colours.append(None)
    match = re.search(fylopattern, content_.text)
    if match:
        Fylo.append(match.group())
    else:
        Fylo.append(None)
    

    r = requests.get('https://www.skroutz.gr/'+urls[i])
    #print(r.text)
    review = re.findall(reviewpattern, r.text)
    if match:
        Reviews.append(review[0])
    else:
        Reviews.append(None)
    if (i==47):
        break  #me to if mas emfanizei oses eggrafes toy zitisoyme emeis, an to svisoyme maw emfanizei oli tin selida

Prices = [float(p[:-2].replace(',','.')) for p in Prices]

Reviews = [int(r) for r in Reviews]


alldict = {'Titles': Titles, 'Prices': Prices, 'Colours': Colours,'Fylo': Fylo,'Reviews': Reviews}
tofile = pd.DataFrame.from_dict(alldict)
print(tofile)
tofile.to_excel("sneakers.xlsx",
             sheet_name='sneakers') 
