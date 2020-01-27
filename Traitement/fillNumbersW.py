import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle

with open('OnlyZerosW.csv', 'r', newline='') as f, open('InOutv2.csv', 'w', newline='') as fout, open('joiningGoodDates.csv', 'r', newline='') as joincsv, open('leavingGoodDates.csv', 'r', newline='') as leavecsv:
	zeros = csv.reader(f)
	joining= csv.reader(joincsv)
	leaving= csv.reader(leavecsv)
	numbers = csv.writer(fout)
	rowjoin=next(joining)
	rowleave=next(leaving)
	
	linejoinleft=True
	lineleaveleft=True

	for row in zeros:
		newrow=row.copy()
		if row[6]==rowjoin[6] and row[0]==rowjoin[0] and linejoinleft:
			newrow[5]=rowjoin[5]
			try:
				rowjoin=next(joining)
			except:
				linejoinleft=False
				print("Join over")
		if row[6]==rowleave[6] and row[0]==rowleave[0] and lineleaveleft:
			newrow[7]=rowleave[5]
			try:
				rowleave=next(leaving)
			except:
				lineleaveleft=False
				print("Leave over")
		numbers.writerow(newrow)
	print(rowleave)
	print(rowjoin)
