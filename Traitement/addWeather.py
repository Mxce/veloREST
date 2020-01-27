import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle

with open('IdInLeave.pickle', 'rb') as f:
	allIds = pickle.load(f)
	allIds.sort()
with open('InOutv2.csv', 'r', newline='') as bikes:
	readb = csv.reader(bikes)
	rowB=next(readb)
	count=0
	for station in range(len(allIds)):
		print(str(station))
		with open('weatherInt.csv', 'r', newline='') as weather, open("finalCSV/"+str(allIds[station])+".csv",'w',newline='') as fout:
			readw = csv.reader(weather)
			writer = csv.writer(fout)
			for rowW in readw:
				dateinWeather=rowW[0]
				dateinBikes=rowB[6]
				if dateinWeather==dateinBikes:    
					newrow=rowB.copy()
					newrow.remove(dateinBikes)
					newrow.append(rowW[2])
					writer.writerow(newrow)	
					count+=1
					rowB=next(readb)
				else:
					print("Error on line "+str(count)+" -- W : "+str(dateinWeather)+" -- B : "+str(dateinBikes))
					
