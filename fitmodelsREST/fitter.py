from sklearn.ensemble import RandomForestRegressor as RandForReg
from sklearn.model_selection import train_test_split

import csv




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
    
def modelfitter(file):
	X,Y = read_df_csv(file)
	trainsize=0.7
	xtrain, xtest, ytrain, ytest = train_test_split(X, Y, train_size=trainsize)
	rfr = RandForReg(n_estimators = 100)
	rfr.fit(xtrain, ytrain)
	return rfr
	
