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

prejoined = pd.read_csv("joined_100.csv")
actors = pd.read_csv("/Users/matthewgriswold/Desktop/Year4/EECS338/IMDB_Files/title.principals.tsv", delimiter='\t')

# def cleanHumans(commanstr):
# 	return commanstr.split(",")

def cleanHumans0(commanstr):
	try:
		return str(commanstr.split(",")[0])
	except:
		return "nm0000000"

def cleanHumans1(commanstr):
	try:
		return str(commanstr.split(",")[1])
	except:
		return "nm0000000"
def cleanHumans2(commanstr):
	try:
		return str(commanstr.split(",")[2])
	except:
		return "nm0000000"
def cleanHumans3(commanstr):
	try:
		return str(commanstr.split(",")[3])
	except:
		return "nm0000000"
def cleanHumans4(commanstr):
	try:
		return str(commanstr.split(",")[4])
	except:
		return "nm0000000"

actors['humans0'] = actors['principalCast'].apply(cleanHumans0)
actors['humans1'] = actors['principalCast'].apply(cleanHumans1)
actors['humans2'] = actors['principalCast'].apply(cleanHumans2)
actors['humans3'] = actors['principalCast'].apply(cleanHumans3)
actors['humans4'] = actors['principalCast'].apply(cleanHumans4)

del actors['principalCast']

#print(data)
joined = pd.merge(prejoined, actors,  how='left', on='tconst')
#joined['humans'] = joined['principalCast'].split(",")

floatdf = joined.copy()
del floatdf['endYear']
del floatdf['originalTitle']
del floatdf['primaryTitle']
del floatdf['titleType']
del floatdf['isAdult']
del floatdf['index']
del floatdf['Unnamed: 0']

def cleantconst(tconst):
	return int(tconst[2:])
def uncleartconsts(unclean):
	return "tt" + str(unclean)
def cleanhuman(human):
	return int(human[2:])
def uncleanhuman(unclean):
	return "nm" + str(unclean)

floatdf['tconst'] = floatdf['tconst'].apply(cleantconst)
floatdf['humans0'] = floatdf['humans0'].apply(cleanhuman)
floatdf['humans1'] = floatdf['humans1'].apply(cleanhuman)
floatdf['humans2'] = floatdf['humans2'].apply(cleanhuman)
floatdf['humans3'] = floatdf['humans3'].apply(cleanhuman)
floatdf['humans4'] = floatdf['humans4'].apply(cleanhuman)
floatdf['budget'] = floatdf['budget'].astype("int")
floatdf['openingweekend'] = floatdf['openingweekend'].astype("int")



#floatdf = joined.apply(LabelEncoder().fit_transform)

# nparray0 = floatdf.as_matrix()

# nparray = np.squeeze(np.asarray(nparray0))

x2 = floatdf.as_matrix()

x_0 = floatdf.copy()

del x_0['openingweekend']

x = x_0.as_matrix()

# print(x[38])

y = floatdf['openingweekend'].as_matrix()

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# print(X_train[38])

print("data properly formatted")

#Action,Adventure,Animation,Biography,Comedy,Crime,Documentary,Drama,Family,Fantasy,History(10),Horror,Music,Musical,Mystery,Romance,Sci-Fi,Sport,Thriller,War,Western(20),budget,runtimeMinutes,startYear,tconst

yearcof = 1
budgetcof = 1
genrecof = 1
humanscof = 1

def movieDistance(x,y):
	year = 1*abs(x[23]-y[23])
	budget = abs(x[21]-y[21])/100000
	genre = 20
	for i in range(21):
		index = i
		# genre += abs(x[index]-y[index])
		if abs(x[index]+y[index]) is 2:
			genre -= 1
	genre = genre*10

	xhumans = [x[25],x[26],x[27],x[28],x[29]]
	yhumans = [y[25],y[26],y[27],y[28],y[29]]

	humans = 0

	for hum in xhumans:
		if hum in yhumans:
			humans += -40

	return (year*yearcof + budget*budgetcof + genre*genrecof + humans*humanscof)

def runnn(x):

	print(x)
	global yearcof
	yearcof = x[0]
	global budgetcof
	budgetcof = x[1]
	global genrecof
	genrecof = x[2]
	global humanscof
	humanscof = x[3]

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


x0 = np.array([1.1, 0.5, 1, 2])
# 'eps': 1
res = minimize(runnn, x0, method='SLSQP', options={'eps': 1,'disp': True})

print(res.x)


