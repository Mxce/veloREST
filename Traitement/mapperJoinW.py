#!/usr/bin/python
import sys
import datetime

first=True
for line in sys.stdin:
	data= line.strip().replace("\"",'').split(",")
	if not first:
		if len(data)==16:
			linenb,dur,btime,etime,bid,bname,blat,blong,eid,ename,elat,elong,bike,usrtype,birth,gender=data
			dateend=datetime.datetime.strptime(etime, '%Y-%m-%d %H:%M:%S')
			timeweather=str(dateend.strftime('%Y'))+"-"+str(dateend.strftime('%m'))+"-"+str(dateend.strftime('%d'))+" "+str(dateend.strftime('%H'))+":00:00"
			print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(bid,dateend.strftime('%Y'),dateend.strftime('%U'),dateend.strftime('%w'),dateend.strftime('%H'),timeweather)
	first=False
