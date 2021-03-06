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

prejoined = pd.read_csv("joined_25.csv")
actors = pd.read_csv("title.principals.tsv", delimiter='\t')

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

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

# print(X_train[38])

print("data properly formatted")


#index,tconst,isAdult,startYear,runtimeMinutes,Action,Animation,Biography,Comedy,Crime,Documentary,Drama,Family,Fantasy,History,Horror,Music,Musical,Mystery,Romance,Sci-Fi,Sport,Thriller,War,Western,budget,human0-4

def movieDistance(x,y):
	
	year = 1*abs(x[4]-y[4])
	budget = abs(x[26]-y[26])/100000
	genre = 0
	for i in range(20):
		index = i + 5
		genre += abs(x[index]-y[index])
	genre = genre*10

	xhumans = [x[27],x[28],x[29],x[30],x[31]]
	yhumans = [y[27],y[28],y[29],y[30],y[31]]

	humans = 0

	for hum in xhumans:
		if hum in yhumans:
			humans += -20

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

print("START PERDICTION")

ow_perdiction = nbrsreg.predict(X_test)

print("regression perdiction:")
print(ow_perdiction)
print("actual restults:")
print(y_test)

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

print(results)

print(sum(results)/len(results))







