import csv

#Action,Adventure,Animation,Biography,Comedy,Crime,Documentary,Drama,Family,Fantasy,History,Horror,Music,Musical,Mystery,Romance,Sci-Fi,Sport,Thriller,War,Western

with open('new_out_with_finance.csv','r') as tsvin, open('fixed.csv', 'w') as csvout:
	tsvin = csv.reader(tsvin, delimiter=',')
	csvout = csv.writer(csvout)
	for row in tsvin:
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

		csvout.writerows([row])