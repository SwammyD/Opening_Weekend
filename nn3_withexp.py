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
import locale

locale.setlocale( locale.LC_ALL, '' )
pd.options.mode.chained_assignment = None

print('Reading in Data')
prejoined = pd.read_csv("joined_100.csv")
actors = pd.read_csv("/Users/matthewgriswold/Desktop/Year4/EECS338/IMDB_Files/title.principals.tsv", delimiter='\t')

print("Begin Merging and Formaing Data")
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

#print(len(joined.index))
floatdf = joined.drop_duplicates(subset=['tconst'])
#print(len(floatdf.index))
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
	return "tt" + str(unclean).zfill(7)
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

testint = random.randint(0, len(floatdf.index))

x2 = floatdf.as_matrix()

x_0 = floatdf.drop_duplicates(subset=['tconst'])

del x_0['openingweekend']

y_0 = floatdf['openingweekend']


X_test = x_0.loc[testint].reshape(1, -1)
y_test = y_0.loc[testint].reshape(1, -1)

# x_0.drop(x_0.index[testint])

# y_0.drop(y_0.index[testint])

x = x_0.drop(testint).as_matrix()
y = y_0.drop(testint).as_matrix()



# print(x)
X_train = x.copy()
y_train = y.copy()
# print(X_train)

#X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

# print(X_train[38])

print("End Merging and Formaing Data")

#Action,Adventure,Animation,Biography,Comedy,Crime,Documentary,Drama,Family,Fantasy,History(10),Horror,Music,Musical,Mystery,Romance,Sci-Fi,Sport,Thriller,War,Western(20),budget,runtimeMinutes,startYear,tconst


def movieDistance(x,y):
	year = 1*abs(x[23]-y[23])
	budget = abs(x[21]-y[21])/10000000
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

	return (year + budget + genre + humans)

def movieDistanceExp(x,y):
	print("")
	print("Distance analysis:")
	year = 1*abs(x[23]-y[23])
	print("This neighbor was producted " + str(year) + " years apart from the given movie")
	budget = abs(x[21]-y[21])/100000
	percentdif = ((x[21] - y[21])/y[21])*100
	print("The budgets were "+ str(abs(percentdif)) + "%" + " percent different")
	genre = 0
	for i in range(21):
		index = i
		genre += abs(x[index]-y[index])
	print("This neighbor had " + str(genre) + " genres in common with the given movie")

	xhumans = [x[25],x[26],x[27],x[28],x[29]]
	yhumans = [y[25],y[26],y[27],y[28],y[29]]

	humans = 0

	for hum in xhumans:
		if hum in yhumans:
			humans += 1

	print("This neighbor had " + str(humans) + " actors in common with the given movie")

# nbrs = NearestNeighbors(n_neighbors=4, algorithm='auto', metric=movieDistance)

# test2 = []

# for i in range(9):
# 	random = randint(0,len(x2))
# 	test2.append(x2[random])

# nbrs.fit(x2)

# print(nbrs.kneighbors([[1., 1., 1.]])) 

nbrsreg = KNeighborsRegressor(n_neighbors=5, weights='distance', metric=movieDistance)
expnbrsreg = NearestNeighbors(n_neighbors=5, metric=movieDistance)

print("Start Fit")

nbrsreg.fit(X_train,y_train)
expnbrsreg.fit(X_train)

print("Start Perdiction")

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
	#if (abs(percentdiff)) < 1:
	results.append(abs(percentdiff))
	it.iternext()
	
print("")
print("Begin Results:")
print("Movie being perdicted")
print(X_test[0])
print("http://www.imdb.com/title/" + uncleartconsts(X_test[0][24]) +'/')
print("")
print("Perdicted Opening Weekend revenue: " + str(locale.currency(ow_perdiction[0], grouping=True)) )
print("percent error:")
print(sum(results)/len(results))
print("")
print("The Nearest Neighbors used to make perdiction:")
nneih_indexs = expnbrsreg.kneighbors(X_test,5)[1]

for (x,y), nindex in np.ndenumerate(nneih_indexs):
	print("Neighbor #"+str(y+1)+":")
	#sprint(nindex)
	print(X_train[nindex])
	print("")
	print("http://www.imdb.com/title/" + uncleartconsts(X_train[nindex][24]) +'/')
	print("This Neighbor's Opening Weekend Revenue: " + str(locale.currency(y_train[nindex], grouping=True)))
	print("The Nearest Neighbor distance: " + str(movieDistance(X_test[0],X_train[nindex])))
	movieDistanceExp(X_test[0],X_train[nindex])
	print("")
	print("")







