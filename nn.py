import sklearn
from sklearn.neighbors import NearestNeighbors
import numpy as np
from sklearn.neighbors import DistanceMetric
from sklearn.neighbors.ball_tree import BallTree
from sklearn.preprocessing import LabelEncoder
import pandas as pd

prejoined = pd.read_csv("joined_25.csv")
actors = pd.read_csv("title.principals.tsv", delimiter='\t')

# def cleanHumans(commanstr):
# 	return commanstr.split(",")

def cleanHumans0(commanstr):
	try:
		return str(commanstr.split(",")[0])
	except:
		return ""

def cleanHumans1(commanstr):
	try:
		return str(commanstr.split(",")[1])
	except:
		return ""
def cleanHumans2(commanstr):
	try:
		return str(commanstr.split(",")[2])
	except:
		return ""
def cleanHumans3(commanstr):
	try:
		return str(commanstr.split(",")[3])
	except:
		return ""
def cleanHumans4(commanstr):
	try:
		return str(commanstr.split(",")[4])
	except:
		return ""

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
floatdf['tconst'] = floatdf['tconst'].apply(LabelEncoder().fit_transform)
floatdf['titleType'] = floatdf['titleType'].apply(LabelEncoder().fit_transform)
floatdf['primaryTitle'] = floatdf['primaryTitle'].apply(LabelEncoder().fit_transform)
floatdf['originalTitle'] = floatdf['originalTitle'].apply(LabelEncoder().fit_transform)
floatdf['humans0'] = floatdf['humans0'].apply(LabelEncoder().fit_transform)
floatdf['humans1'] = floatdf['humans1'].apply(LabelEncoder().fit_transform)
floatdf['humans2'] = floatdf['humans2'].apply(LabelEncoder().fit_transform)
floatdf['humans3'] = floatdf['humans3'].apply(LabelEncoder().fit_transform)
floatdf['humans4'] = floatdf['humans4'].apply(LabelEncoder().fit_transform)
floatdf['budget'] = floatdf['budget'].astype(int)
floatdf['openingweekend'] = floatdf['openingweekend'].astype(int)


# for i, item in joined.iterrows():
# 	joined.loc[i,'principalCast'] = joined.loc[i,'principalCast'].split(",")


#del joined['principalCast']

# data = np.loadtxt(open("test.csv", "rb"), delimiter=",", skiprows=1)
# actors = np.loadtxt(open("test.csv", "rb"), delimiter='\t', skiprows=0)

#nparray = joined.values

#joined['principalCast'].astype(str)
print("floatdf types:")
print(floatdf.dtypes)
print(joined.ix[0])
print(joined.ix[37])

#floatdf = joined.apply(LabelEncoder().fit_transform)

nparray0 = floatdf.as_matrix()

nparray = np.squeeze(np.asarray(nparray0))


# for x in nparray:
# 	newlist = x[-1].split(",")
# 	x[-1] = "none"
	# try:
	# 	x[-1] = newlist[0]
	# except:
	# 	x[-1] = "none"
	# try:
	# 	x = np.append(x, newlist[1])
	# except:
	# 	x = np.append(x, "none")
	# try:
	# 	x = np.append(x, newlist[2])
	# except:
	# 	x = np.append(x, "none")
	# try:
	# 	x = np.append(x, newlist[3])
	# except:
	# 	x = np.append(x, "none")
	# try:
	# 	x.append(newlist[3])
	# except:
	# 	x = np.append(x, "none")


print("data properly formatted")
print(nparray[0])
print(nparray[37])

#index,tconst,titleType,primaryTitle,originalTitle,isAdult,startYear,endYear,runtimeMinutes,Action,Adventure,Animation,Biography,Comedy,Crime,Documentary,Drama,Family,Fantasy,History,Horror,Music,Musical,Mystery,Romance,Sci-Fi,Sport,Thriller,War,Western,budget,openingweekend

def movieDistance(x,y):
	#print(x)
	return (abs(x[30]-y[30]))

nbrs = NearestNeighbors(n_neighbors=4, algorithm='auto', metric=movieDistance)

# le = LabelEncoder()
# z = le.fit(nparray)

# print(z[926])

nbrs.fit(nparray)

nbrs.kneighbors(nparray)



