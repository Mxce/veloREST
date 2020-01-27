import csv
import pandas as pd
import pickle
from datetime import date
import os
import time
	
first=True
start=time.time()
for files in os.listdir('../CSVs'):
	local=time.time()
	readvelo = pd.read_csv('../CSVs/'+files, skiprows = 1,header=None, parse_dates = [1,2])
	readvelo.dropna(inplace=True)
	readvelo.iloc[:,3]=readvelo.iloc[:,3].astype('int64')
	readvelo.iloc[:,7]=readvelo.iloc[:,7].astype('int64')
	if first:
		first=False
		readvelo.to_csv("panda_out.csv")
	else:
		readvelo.to_csv("panda_out.csv", mode='a',header=False)
	end=time.time()
	print(files+" treated in "+str(end-local)+" s. Total time elapsed : "+str(end-start)+" s")
