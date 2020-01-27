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
	with open('finalCSV/'+files, 'r', newline='') as f, open('CSVReg/'+number+'reg.csv', 'w', newline='') as fout:
		reader=csv.reader(f)
		writer=csv.writer(fout)
		writer.writerow(['data','label'])
		for row in reader:
			tempdata=[int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[7])]
			templabel=int(row[5])+int(row[6])
			tempout=[tempdata,templabel]
			writer.writerow(tempout)
