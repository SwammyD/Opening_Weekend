#http://www.imdb.com/title/tt0468569/business

from bs4 import BeautifulSoup
from urllib.request import urlopen

tcount = "tt2488496"

url = "http://www.imdb.com/title/" + tcount + "/business"

#ws_response = urllib2.urlopen(ws_url)
ws_html = urlopen(url)
ws_soup = BeautifulSoup(ws_html, 'html.parser')

div = ws_soup.find('div', id='tn15content')
h5 = ws_soup.find_all('h5')

# print(budget.contents[1]) #header: budget
# print(div.contents[2]) #acutal budge
# print("wnated opening here")
# print(budget.contents[7])
# print(budget.contents[8]) #usa opening
#try:
print("budget:")
#budgetint = [int(s) for s in div.contents[2].split() if s.isdigit()]
opening_weekend_bool = False
budget_bool = False
for item in h5:
	if "Opening" in item.text and "Weekend" in item.text:
		opening_weekend_bool = True
	if "Budget" in item.text:
		budget_bool = True
		
print("bools")
print(opening_weekend_bool and budget_bool)
budgetstring = div.contents[2].split()[0].strip('$')
print(float(budgetstring.replace(",","")))
print("opening weekend: ")
#openingint = [int(s) for s in div.contents[8].split() if s.isdigit()]
print(div.contents[7])
openingstring = div.contents[8].split()[0].strip('$')
print(float(openingstring.replace(",","")))
# except:
# 	print("no revenue info")
