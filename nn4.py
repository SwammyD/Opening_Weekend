import sklearn
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
from sklearn.neighbors import DistanceMetric
from sklearn.neighbors.ball_tree import BallTree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import random
import pandas as pd
import pickle
import hashlib

prejoined = pd.read_csv("joined_100.csv")
actors = pd.read_csv("/Users/matthewgriswold/Desktop/Year4/EECS338/IMDB_Files/title.principals.tsv", delimiter='\t')
newdata = pickle.load(open("data.p", "rb"))


# 	return commanstr.split(",")

# def cleanHumans0(commanstr):
# 	try:
# 		return str(commanstr.split(",")[0])
# 	except:
# 		return "nm0000000"

# def cleanHumans1(commanstr):
# 	try:
# 		return str(commanstr.split(",")[1])
# 	except:
# 		return "nm0000000"
# def cleanHumans2(commanstr):
# 	try:
# 		return str(commanstr.split(",")[2])
# 	except:
# 		return "nm0000000"
# def cleanHumans3(commanstr):
# 	try:
# 		return str(commanstr.split(",")[3])
# 	except:
# 		return "nm0000000"
# def cleanHumans4(commanstr):
# 	try:
# 		return str(commanstr.split(",")[4])
# 	except:
# 		return "nm0000000"

# actors['humans0'] = actors['principalCast'].apply(cleanHumans0)
# actors['humans1'] = actors['principalCast'].apply(cleanHumans1)
# actors['humans2'] = actors['principalCast'].apply(cleanHumans2)
# actors['humans3'] = actors['principalCast'].apply(cleanHumans3)
# actors['humans4'] = actors['principalCast'].apply(cleanHumans4)

# del actors['principalCast']

# #print(data)
# joined = pd.merge(prejoined, actors,  how='left', on='tconst')
# #joined['humans'] = joined['principalCast'].split(",")

# floatdf = joined.copy()
# del floatdf['endYear']
# del floatdf['originalTitle']
# del floatdf['primaryTitle']
# del floatdf['titleType']
# del floatdf['isAdult']
# del floatdf['index']
# del floatdf['Unnamed: 0']

def cleantconst(tconst):
	return int(tconst[2:])
def uncleartconsts(unclean):
	return "tt" + str(unclean)
def cleanhuman(human):
	return int(human[2:])
def uncleanhuman(unclean):
	return "nm" + str(unclean)

# floatdf['tconst'] = floatdf['tconst'].apply(cleantconst)
# floatdf['humans0'] = floatdf['humans0'].apply(cleanhuman)
# floatdf['humans1'] = floatdf['humans1'].apply(cleanhuman)
# floatdf['humans2'] = floatdf['humans2'].apply(cleanhuman)
# floatdf['humans3'] = floatdf['humans3'].apply(cleanhuman)
# floatdf['humans4'] = floatdf['humans4'].apply(cleanhuman)
# floatdf['budget'] = floatdf['budget'].astype("int")
# floatdf['openingweekend'] = floatdf['openingweekend'].astype("int")
#[movieID, title, runtime(min), [Genres], production_company, total_gross, total_theaters, openeing_weekend, opening_theaters, opening_date, [actorID, actor_name, birthyear, deathyear, top4_titles, total_gross, total_movies, avg_gross, top_grossing_movie, movie_total_gross]]
x = []
y = []
#tconst,runtime,genres,production company, total_gross, total theaters, month, actor1,actor2,actor,3,actor4,actor5,actor6,actor,7,bestavg,besthighest,21 geners
for movie in newdata:
	y.append(movie[7])
	actors = movie[10]
	newactors = []
	production_company = movie[4]
	new = [cleantconst(movie[0]),movie[2],int(hashlib.sha256(production_company.encode('utf-8')).hexdigest(), 16) % 10**8,movie[5],movie[6],movie[8],int(movie[9][5:7])]
	bestavg = 0
	besthighest = 0
	for actor in actors:
		#,actor[7],actor[9]
		new.append(cleanhuman(actor[0]))
		if actor[7] > bestavg:
			bestavg = actor[7]
			besthighest = actor[9]

	for i in range(7-len(actors)):
		new.append(0)

	new.append(bestavg)
	new.append(besthighest)

	if "Action" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Adventure" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Animation" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Biography" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Comedy" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Crime" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Documentary" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Drama" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Family" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Fantasy" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "History" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Horror" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Music" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Musical" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Mystery" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Romance" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Sci-Fi" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Sport" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Thriller" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "War" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	if "Western" in movie[3]:
		new.append(1)
	else: 
		new.append(0)
	x.append(new)
	#for range()
print(newdata[27])
print(x[27])
print(newdata[107])
print(x[107])
print(newdata[1107])
print(x[1107])

#floatdf = joined.apply(LabelEncoder().fit_transform)

# nparray0 = floatdf.as_matrix()

# nparray = np.squeeze(np.asarray(nparray0))

x2 = floatdf.as_matrix()

x_0 = floatdf.copy()

del x_0['openingweekend']

x = x_0.as_matrix()

# print(x[38])

y = floatdf['openingweekend'].as_matrix()

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

# print(X_train[38])

print("data properly formatted")

#Action,Adventure,Animation,Biography,Comedy,Crime,Documentary,Drama,Family,Fantasy,History(10),Horror,Music,Musical,Mystery,Romance,Sci-Fi,Sport,Thriller,War,Western(20),budget,runtimeMinutes,startYear,tconst


def movieDistance(x,y):
	year = 1*abs(x[23]-y[23])
	budget = abs(x[21]-y[21])/100000
	genre = 0
	for i in range(21):
		index = i
		genre += abs(x[index]-y[index])
	genre = genre*10

	xhumans = [x[25],x[26],x[27],x[28],x[29]]
	yhumans = [y[25],y[26],y[27],y[28],y[29]]

	humans = 0

	for hum in xhumans:
		if hum in yhumans:
			humans += -40
	
	# year = 1*abs(x[4]-y[4])
	# budget = abs(x[26]-y[26])/100000
	# genre = 0
	# for i in range(20):
	# 	index = i + 5
	# 	genre += abs(x[index]-y[index])
	# genre = genre*10

	# xhumans = [x[27],x[28],x[29],x[30],x[31]]
	# yhumans = [y[27],y[28],y[29],y[30],y[31]]

	# humans = 0

	# for hum in xhumans:
	# 	if hum in yhumans:
	# 		humans += -20

	#print("********")
	# print(x)
	# print(y)
	# print(x[26])
	# print(y[26])
	# print(len(x))
	# print("**")
	# print(year)
	# print(budget)
	# print(genre)
	# print(humans)
	# print(year + budget + genre + humans)

	return (year + budget + genre + humans)

# nbrs = NearestNeighbors(n_neighbors=4, algorithm='auto', metric=movieDistance)

# test2 = []

# for i in range(9):
# 	random = randint(0,len(x2))
# 	test2.append(x2[random])

# nbrs.fit(x2)

# print(nbrs.kneighbors([[1., 1., 1.]])) 

nbrsreg = KNeighborsRegressor(n_neighbors=5, metric=movieDistance)

print("START FIT")

nbrsreg.fit(X_train,y_train)

print("START PREDICTION")

ow_perdiction = nbrsreg.predict(X_test)

# print("regression perdiction:")
# print(ow_perdiction)
# print("actual restults:")
# print(y_test)

results = []

it = np.nditer(ow_perdiction, flags=["c_index"])

# for x,y in np.ndenumerate(ow_perdiction):
# 	percentdiff = (ow_perdiction[x,y] - ytest[x,y])/ytest[x,y]
# 	results.append(percentdiff)

while not it.finished:
	percentdiff = (ow_perdiction[it.index] - y_test[it.index])/y_test[it.index]
	if (abs(percentdiff)) < 1:
		results.append(abs(percentdiff))
	it.iternext()
	
#print(results)
print("average percent error:")
print(sum(results)/len(results))







