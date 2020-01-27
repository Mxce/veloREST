import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle

with open('leavingW.csv', 'r', newline='') as f, open('IdsLeave.csv', 'w', newline='') as fout:
	reader=csv.reader(f)
	writer=csv.writer(fout)

	allIds=[]
	for row in reader:
		if row[0] not in allIds:
			allIds.append(row[0])
			writer.writerow([row[0]])
	print(str(len(allIds)))

with open('IdInLeave.pickle', 'wb') as f:
	pickle.dump(allIds, f)
