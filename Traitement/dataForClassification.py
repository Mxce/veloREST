import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle

count=0
for files in os.listdir('finalCSV'):
	count+=1
	number=files.split(".")[0]
	print(number+" -> file number "+str(count))
	with open('finalCSV/'+files, 'r', newline='') as f, open('CSVClassif/'+number+'class.csv', 'w', newline='') as fout:
		reader=csv.reader(f)
		writer=csv.writer(fout)
		writer.writerow(['data','label'])
		for row in reader:
			tempdata=[int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[7])]
			templabel=int(row[5])+int(row[6])
			if templabel<=10:
				labelwithclass=0
			elif templabel>10 and templabel <=30:
				labelwithclass=1
			elif templabel>30 and templabel <=60:
				labelwithclass=2
			elif templabel>60 and templabel <=120:
				labelwithclass=3
			elif templabel>120:
				labelwithclass=4
			tempout=[tempdata,labelwithclass]
			writer.writerow(tempout)
