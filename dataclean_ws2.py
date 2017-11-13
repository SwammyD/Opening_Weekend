import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
import itertools

#tconst	titleType	primaryTitle	originalTitle	isAdult	startYear	endYear	runtimeMinutes	genres budget 
#with open("imdbout_title.tsv")

start = 4000000

stop = 4587532

goodmovies = 0
badmovies = 0
fails = ""

with open('imdbout_title.tsv','r') as tsvin, open('new_out_with_finance_range_'+str(start)+'_'+str(stop)+'_2.csv', 'w') as csvout:
	tsvin = csv.reader(tsvin, delimiter='\t')
	csvout = csv.writer(csvout)
	for row in itertools.islice(tsvin,start,stop):
		#print(row)
		try:
			
			if (row[1] == "movie"): 
				if (int(row[5]) >= 2000):
					if (int(row[7]) >= 60): #check that row is a movie, that it was made more recently than 2000 and it is at least 1hr
						
						#get finance info
						tcount = row[0]

						print(tcount)

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

							if "Action" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Adventure" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Animation" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Biography" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Comedy" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Crime" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Documentary" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Drama" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Family" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Fantasy" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "History" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Horror" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Music" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Musical" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Mystery" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Romance" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Sci-Fi" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Sport" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Thriller" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "War" in row[8]:
								row.append(1)
							else: 
								row.append(0)
							if "Western" in row[8]:
								row.append(1)
							else: 
								row.append(0)

							row.pop(8)

							budgetstring = div.contents[2].split()[0].strip('$')
							row.append(float(budgetstring.replace(",",""))) #add budget

							openingstring = div.contents[8].split()[0].strip('$')
							row.append(float(openingstring.replace(",",""))) #add opening weekend revenue

							#print(row)
							csvout.writerows([row])
						else:
							fails += div


		except:
			badmovies += 1
			# print("bad row:")
			# print(row)

print("good moves:")
print(goodmovies)
print(fails)