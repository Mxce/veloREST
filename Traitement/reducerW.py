#!/usr/bin/python
import sys
outcount=0
oldId=None
oldYear=None
oldMonth=None
oldDay=None
oldHour=None

for line in sys.stdin:
	data=line.strip().split("\t")
	thisId, thisYear, thisMonth, thisDay, thisHour,timeweather = data
	if oldId and oldYear and oldMonth and oldDay and oldHour and (oldId != thisId or oldYear != thisYear or oldMonth != thisMonth or oldDay != thisDay or oldHour != thisHour):
		print "{0},{1},{2},{3},{4},{5},{6}".format(oldId,oldYear,oldMonth,oldDay,oldHour,outcount,oldweather)
		outcount=0

	oldId=thisId
	oldYear=thisYear
	oldMonth=thisMonth
	oldDay=thisDay
	oldHour=thisHour
	outcount += int(1)
	oldweather=timeweather

if oldId!=None and oldYear!=None and oldMonth!=None and oldDay!=None and oldHour!=None:
	print "{0},{1},{2},{3},{4},{5},{6}".format(oldId,oldYear,oldMonth,oldDay,oldHour,outcount,oldweather)
	
