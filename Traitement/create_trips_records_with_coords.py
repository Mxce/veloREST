import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle

topstations=[519,435,402,293,285,426,490,477,284]

for stat in topstations:
	print("Treating station "+str(stat))
	with open('TripsAggreg.csv', 'r', newline='') as f: 
		with open(str(stat)+'.csv', 'w', newline='') as fout:
			reader=csv.reader(f)
			writer=csv.writer(fout)
		
			for line in reader:
				startstat=line[0].split("->")[0]
				if startstat==str(stat):
					nbtrips=line[1].replace("[","").replace("]","")
					coord1=line[6]
					coord2=line[7]
					name=line[2]
					writer.writerow([name,coord1,coord2,nbtrips])
			
