import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle

with open('IdInLeave.pickle', 'rb') as f:
	allIds = pickle.load(f)

leave={}

for key in allIds:
	leave[str(key)]=0

with open('leavingGoodDates.csv', 'r', newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		leave[str(row[0])]+=int(row[5])

leavesorted={k: v for k, v in sorted(leave.items(),reverse=True, key=lambda item: item[1])}

with open('countleave.csv','w',newline='') as out:
	writer= csv.writer(out)
	for key in leavesorted:
		writelist=[]
		writelist.append(str(key))
		writelist.append(str(leavesorted[key]))
		writer.writerow(writelist)

