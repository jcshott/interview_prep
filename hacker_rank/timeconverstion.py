#!/bin/python

import sys

def convert(time):
	if time[-2] == "P":
	    # check noon
	    if time[:2] == "12":
	        return time[:-2]
	    else:   
	        hour = int(time[:2]) + 12
	        return str(hour) + time[2:-2]
	else:
	    # midnight
	    if time[:2] == "12":
	        return "00" + time[2:-2]
	    else:
	        return time[:-2]

print "midnight: ", convert("12:00:00AM")
print "midnight:33:37: ", convert("12:33:37AM")
print "Noon: ", convert("12:00:00PM")
print "2:50pm: ", convert("02:50:00PM")
print "1:25:33am: ", convert("01:25:33AM")