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
from scipy.optimize import minimize
import pickle
import hashlib

# prejoined = pd.read_csv("joined_100.csv")
# actors = pd.read_csv("/Users/matthewgriswold/Desktop/Year4/EECS338/IMDB_Files/title.principals.tsv", delimiter='\t')

newdata = pickle.load(open("data.p", "rb"))

def cleantconst(tconst):
	return int(tconst[2:])
def uncleartconsts(unclean):
	return "tt" + str(unclean)
def cleanhuman(human):
	return int(human[2:])
def uncleanhuman(unclean):
	return "nm" + str(unclean)

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
	for actor in actors[:7]:
		#,actor[7],actor[9]
		new.append(cleanhuman(actor[0]))
		if actor[7] > bestavg:
			bestavg = actor[7]
			besthighest = actor[9]

	if len(actors) < 7:

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


xx = np.array(x, dtype=object)
yy = np.array(y, dtype=float)

X_train, X_test, y_train, y_test = train_test_split(xx, yy.reshape(-1, 1), test_size=0.2)

# print(X_train[38])

print("data properly formatted")

#tconst,runtime,genres,production company, total_gross, total theaters, month, actor1,actor2,actor,3,actor4,actor5,actor6,actor,7,bestavg,besthighest,21 geners

runtimecof = 1
productioncof = 1
total_grosscof = 1
total_theaterscof = 1
monthcof = 1
genrecof = 1
humanscof = 1
avgcof = 1
highestcof = 1

def movieDistance(x,y):
	#runtime
	runtime = x[1]-y[1]

	#production company
	production = 1
	if x[3] is y[3]:
		production = 0

	#total gross
	total_gross = abs(x[4] - y[4])

	#total theaters
	total_theaters = abs(x[5] - y[5])

	#month
	month = abs(x[6] - y[6])

	genre = 21
	for i in range(21):
		index = i + 16
		# genre += abs(x[index]-y[index])
		if abs(x[index]+y[index]) is 2:
			genre -= 1

	xhumans = [x[7],x[8],x[9],x[10],x[11],x[12],x[13]]
	yhumans = [y[7],y[8],y[9],y[10],y[11],y[12],y[13]]

	humans = 7

	for hum in xhumans:
		if hum in yhumans and hum is not 0:
			humans += -1

	avg = abs(x[14] - y[14])
	highest = abs(x[15] - y[15])

	return (runtime*runtimecof + production*productioncof + total_gross*total_grosscof + total_theaters*total_theaterscof + month*monthcof + genre*genrecof + humans*humanscof + avg*avgcof + highestcof*highest)

def runnn(x):

	print(x)
	global runtimecof
	runtimecof = x[0]
	global productioncof
	productioncof = x[1]
	global total_grosscof
	total_grosscof = x[2]
	global total_theaterscof
	total_theaterscof = x[3]
	global monthcof
	monthcof = x[4]
	global genrecof
	genrecof = x[5]
	global humanscof
	humanscof = x[6]
	global avgcof
	avgcof = x[7]
	global highestcof
	highestcof = x[8]

	nbrsreg = KNeighborsRegressor(n_neighbors=4, weights='distance', metric=movieDistance)

	#print("START FIT")

	nbrsreg.fit(X_train,y_train)

	#print("START PREDICTION")

	ow_perdiction = nbrsreg.predict(X_test)


	results = []

	it = np.nditer(ow_perdiction, flags=["c_index"])


	while not it.finished:
		percentdiff = (ow_perdiction[it.index] - y_test[it.index])/y_test[it.index]
		results.append(abs(percentdiff))
		it.iternext()
		
	#print(results)
	#print("average percent error:")
	print(sum(results)/len(results))
	return (sum(results)/len(results))


x0 = np.array([.7, 1.8, .1, .9, 1, 1.5, 2, .2, .2])
# 'eps': 1
res = minimize(runnn, x0, method='Nelder-Mead', options={'disp': True})

print(res.x)


