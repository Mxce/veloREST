import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle

with open('Ids.pickle', 'rb') as f:
	allIds = pickle.load(f)
	allIds.sort()

with open('OnlyZerosW.csv', 'w', newline='') as fout:
	writer = csv.writer(fout)

	for station in range(len(allIds)):
		print("Treatment of station number "+str(station))
		counthours=0
		countdays=6
		countweeks=21
		countyear=2013
		over = False

		while not over:
			newrow=[]
			newrow.append(int(allIds[station]))
			newrow.append(countyear)
			newrow.append(countweeks)
			newrow.append(countdays)
			newrow.append(counthours)
			newrow.append(0)
			date=datetime.datetime.strptime(str(countyear)+","+str(countweeks)+","+str(countdays),'%Y,%U,%w')
			if counthours <= 9:
				hour="0"+str(counthours)
			else:
				hour=str(counthours)
			fakedate=str(countyear)+"-"+date.strftime('%m')+"-"+date.strftime('%d')+" "+hour+":00:00"
			newrow.append(fakedate)
			newrow.append(0)
			writer.writerow(newrow)
			counthours=(counthours+1)%24
			if counthours==0:
				countdays=(countdays+1)%7
				if countdays==0:
					countweeks=countweeks+1
				if countweeks==52 and countyear==2013 and countdays==3:
					countyear=2014
					countweeks=0
				elif countweeks==52 and countyear==2014 and countdays==4:
					countyear=2015
					countweeks=0
				elif countweeks==52 and countyear==2015 and countdays==5:
					countyear=2016
					countweeks=0
				elif countweeks==53 and countyear==2016 and countdays==0:
					countyear=2017
					countweeks=1
				elif countweeks==43 and countyear==2017 and countdays==6:
					over = True
