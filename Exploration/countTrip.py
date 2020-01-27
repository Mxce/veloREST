import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle

dico={}

with open('panda_out.csv', 'r', newline='') as f, open('countTrips.csv', 'w', newline='') as fout:
	reader=csv.reader(f)
	writer=csv.writer(fout)
	next(reader,None)
	
	for row in reader:
		statin=row[4]
		statout=row[8]
		identifier=str(statin)+"->"+str(statout)
		if identifier in dico:	
			dico[identifier][0]+=1			

		else:
			dico[identifier]=[]	
			dico[identifier].append(1)			# Nombre de trajets


	dictsort={k: v for k, v in sorted(dico.items(),reverse=True, key=lambda item: item[1][0])}

	for key in dictsort:
		newrow=[]
		newrow.append(key)
		newrow.append(dictsort[key])
		writer.writerow(newrow)


