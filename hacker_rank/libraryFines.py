#!/bin/python

import sys


d1,m1,y1 = raw_input().strip().split(' ') 
d1,m1,y1 = [int(d1),int(m1),int(y1)] #day, month, yr returned
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)] # day, month, yr expected

# check if we returned before the due date
if y1 < y2:
    print 0
    # sys.exit()

elif y1==y2: #did we return in correct year?

    if m1 < m2: #did we return before due month?
        print 0
        # sys.exit()
    elif m1 == m2: # returned in month due
        
        if d1 <= d2: # did we return on or before correct day?
            print 0
            # sys.exit()
        else: # correct month but not correct day
            print 15*(d1-d2)
            # sys.exit() 
    else: # correct year but month(s) late
        print 500 * (m1-m2)
        # sys.exit()
else:
    print 10000 #returned in year after due, fixed fine

