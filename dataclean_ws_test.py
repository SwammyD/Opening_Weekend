import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

#tconst	titleType	primaryTitle	originalTitle	isAdult	startYear	endYear	runtimeMinutes	genres budget 
#with open("imdbout_title.tsv")

goodmovies = 0
badmovies = 0

with open('imdbout_title.tsv','r') as tsvin, open('new_out_test.csv', 'w') as csvout:
	tsvin = csv.reader(tsvin, delimiter='\t')
	csvout = csv.writer(csvout)
	for row in tsvin:
		#print(row)
		try:
			if (row[0] == "tt2488496"): 
				if (row[1] == "movie"):
					if (int(row[5]) >= 2000):
						if (int(row[7]) >= 60): #check that row is a movie, that it was made more recently than 2000 and it is at least 1hr
							
							#get finance info
							tcount = row[0]

							#print(tcount)

							url = "http://www.imdb.com/title/" + tcount + "/business"



							ws_html = urlopen(url)
							ws_soup = BeautifulSoup(ws_html, 'html.parser')

							div = ws_soup.find('div', id='tn15content')
							h5 = ws_soup.find_all('h5')

							opening_weekend_bool = False
							budget_bool = False
							for item in h5:
								if "Opening" in item.text and "Weekend" in item.text:
									opening_weekend_bool = True
								if "Budget" in item.text:
									budget_bool = True
									
							if (opening_weekend_bool and budget_bool):

								budgetstring = div.contents[2].split()[0].strip('$')
								row.append(float(budgetstring.replace(",",""))) #add budget

								openingstring = div.contents[8].split()[0].strip('$')
								row.append(float(openingstring.replace(",",""))) #add opening weekend revenue

								#print(row)
								csvout.writerows([row])


		except:
			badmovies += 1
			# print("bad row:")
			# print(row)

print("good moves:")
print(goodmovies)