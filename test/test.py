from flask import Flask
import yaml
import requests
import csv
import pickle
from io import StringIO,BytesIO

from sklearn.ensemble import RandomForestRegressor as RandForReg
from sklearn.model_selection import train_test_split
import csv

station_id = 519
dirname='MODELS'
addresses = yaml.safe_load(open("conf.yaml"))['addresses']

#DOES NOT WORK
def read_reg_csv(file):
    print('do not use read_reg_csv, really')
    X = [] # Contient tous les vecteurs [annee,semaine,jour,heure,weather]
    Y = [] # Contient toutes les affluences (representees par un entier, somme des departs et arrivees)
    reader = csv.reader(file)
    next(reader,None)
    for line in reader: 
        temp=[]
        for elem in line:
            temp.append(int(elem))
        X.append(temp)
        Y.append(int(line[1]))
    return X,Y
        
def read_df_csv(file):
    X = [] # Contient tous les vecteurs [annee,semaine,jour,heure,weather]
    Y = [] # Contient toutes les affluences (representees par un entier, somme des departs et arrivees)
    reader = csv.reader(file)
    next(reader,None)
    for line in reader: 
        temp=[]
        a=line[0].replace("[","").replace("]","").replace(".0","").split(",")
        for elem in a:
            temp.append(int(elem))
        X.append(temp)
        Y.append(int(line[1]))
    return X,Y
	

print(addresses['csvREST'] + '/stations/' + str(station_id))

'''gets the trained model using modelfitter from imported module'''
csv_as_text = requests.get(addresses['csvREST'] + '/stations/' + str(station_id)).text
#print(csv_as_text)
io = StringIO(csv_as_text)

X,Y = read_df_csv(io)
#print(X)
#print(Y)
trainsize=0.7
xtrain, xtest, ytrain, ytest = train_test_split(X, Y, train_size=trainsize)
print(xtest[0])


rfr = RandForReg(n_estimators = 100)
rfr.fit(xtrain, ytrain)

'''fits a model then POSTs it to predictREST'''
srlzd = pickle.dumps(rfr)
model = pickle.loads(srlzd)
file = open(dirname + '/' + str(station_id), 'wb')
pickle.dump(model,file)
file.close()
###############################################################

file2= open(dirname + '/' + str(station_id), 'rb')
mod = pickle.load(file2)
print(mod.predict([[519,2020,14,6,12]]))
