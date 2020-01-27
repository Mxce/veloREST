import csv
import os
import re
import datetime
import pandas as pd
import shutil
import pickle


weathertoint={}

with open('weathertoint.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
    	weathertoint[row[0]]=row[1]
print(weathertoint)
with open('weathertoint.pickle', 'wb') as f:
    pickle.dump(weathertoint, f)