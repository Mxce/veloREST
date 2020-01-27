import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle

dico={}

with open('resumeOut.csv', 'r', newline='') as f:
	reader=csv.reader(f)
	for row in reader:
		key=row[0]
		dico[key]=[]
		dico[key].append(row[1])
		dico[key].append(row[2])
		dico[key].append(row[3])

with open('countTrips.csv', 'r', newline='') as f, open('TripsAggreg.csv', 'w', newline='') as fout:
	reader=csv.reader(f)
	writer=csv.writer(fout)

	for row in reader:
		keyIn,keyOut=row[0].split("->")
		newrow=row.copy()
		newrow.append(dico[keyIn][0])
		newrow.append(dico[keyIn][1])
		newrow.append(dico[keyIn][2])
		newrow.append(dico[keyOut][0])
		newrow.append(dico[keyOut][1])
		newrow.append(dico[keyOut][2])
		writer.writerow(newrow)
