import csv

#tconst	titleType	primaryTitle	originalTitle	isAdult	startYear	endYear	runtimeMinutes	genres
#with open("imdbout_title.tsv")

goodmovies = 0
badmovies = 0

with open('imdbout_title.tsv','r') as tsvin, open('new_out2.csv', 'w') as csvout:
	tsvin = csv.reader(tsvin, delimiter='\t')
	csvout = csv.writer(csvout)
	for row in tsvin:
		#print(row)
		try:
			
			if (row[1] == "movie"): 
				goodmovies += 1
				if (int(row[5]) >= 2000):
					if (int(row[7]) >= 60): #check that row is a movie, that it was made more recently than 2000 and it is at least 1hr
						#get finance info
						goodmovies += 1
						#print(row)
						csvout.writerows([row])
		except:
				badmovies += 1
			# print("bad row:")
			# print(row)

print("good moves:")
print(goodmovies)