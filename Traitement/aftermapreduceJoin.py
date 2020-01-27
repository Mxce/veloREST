import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle

stopdate=datetime.datetime.strptime('2017-10-28','%Y-%m-%d')

with open('joiningW.csv', 'r', newline='') as joincsv, open('joiningGoodDates.csv', 'w', newline='') as fout:
	reader= csv.reader(joincsv)
	writer=csv.writer(fout)
	
	for row in reader:
		currentdate=datetime.datetime.strptime(str(row[1])+'-'+str(row[2])+'-'+str(row[3]),'%Y-%U-%w')
		if currentdate<stopdate:
			writer.writerow(row)
	
