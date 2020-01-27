#!/usr/bin/python
import sys
import datetime

first=True
for line in sys.stdin:
	data= line.strip().replace("\"",'').split(",")
	if not first:
		if len(data)==16:
			linenb,dur,btime,etime,bid,bname,blat,blong,eid,ename,elat,elong,bike,usrtype,birth,gender=data
			datebegin=datetime.datetime.strptime(btime, '%Y-%m-%d %H:%M:%S')
			timeweather=str(datebegin.strftime('%Y'))+"-"+str(datebegin.strftime('%m'))+"-"+str(datebegin.strftime('%d'))+" "+str(datebegin.strftime('%H'))+":00:00"
			print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(bid,datebegin.strftime('%Y'),datebegin.strftime('%U'),datebegin.strftime('%w'),datebegin.strftime('%H'),timeweather)
	first=False
