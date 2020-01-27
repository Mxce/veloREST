import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle

with open('IdInLeave.pickle', 'rb') as f:
	allIds = pickle.load(f)

join={}

for key in allIds:
	join[str(key)]=0

with open('joiningGoodDates.csv', 'r', newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		join[str(row[0])]+=int(row[5])

joinsorted={k: v for k, v in sorted(join.items(),reverse=True, key=lambda item: item[1])}

with open('countjoin.csv','w',newline='') as out:
	writer= csv.writer(out)
	for key in joinsorted:
		writelist=[]
		writelist.append(str(key))
		writelist.append(str(joinsorted[key]))
		writer.writerow(writelist)

