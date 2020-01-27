import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle


with open('weather_description.csv', 'r', newline='') as weatherbrut, open('weather.csv', 'w', newline='') as weather:
	reader = csv.reader(weatherbrut)
	writer = csv.writer(weather)
	startwrite=False
	for row in reader:
		if startwrite:
			if row[28]!='' and row[0]!="2017-10-28 00:00:00":
				newrow=[]
				newrow.append(row[0])
				newrow.append(row[28])
				writer.writerow(newrow)
		else:
			if row[0]=="2013-05-31 23:00:00":
				startwrite=True
