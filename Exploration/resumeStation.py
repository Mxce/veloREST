import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle

stations={}

with open('panda_out.csv', 'r', newline='') as f, open('resumeOut.csv', 'w', newline='') as fout:
	reader=csv.reader(f)
	writer=csv.writer(fout)
	next(reader,None)
	for row in reader:
		statin=row[4]
		if statin not in stations:
			stations[statin]=[]
			stations[statin].append(statin)
			stations[statin].append(row[5])
			stations[statin].append(row[6])
			stations[statin].append(row[7])
			writer.writerow(stations[statin])
		statout=row[8]
		if statout not in stations:
			stations[statout]=[]
			stations[statout].append(statout)
			stations[statout].append(row[9])
			stations[statout].append(row[10])
			stations[statout].append(row[11])
			writer.writerow(stations[statout])
	
