import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle

with open('weathertoint.pickle', 'rb') as f:
    weathertoint = pickle.load(f)

with open('weather.csv', 'r', newline='') as weather, open('weatherInt.csv', 'w', newline='') as weatherint:
	reader = csv.reader(weather)
	writer = csv.writer(weatherint)
	count=0
	for row in reader:
		count+=1
		print(str(count))
		newrow=row.copy()
		newrow.append(weathertoint[row[1]])
		writer.writerow(newrow)
