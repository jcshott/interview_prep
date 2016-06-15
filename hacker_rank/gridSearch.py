#!/bin/python

import sys

#TODO: handle test case where the first line is in multiple places in the grid:
# 4 6
# 123412
# 561212
# 123612
# 781234
# 2 2
# 12
# 34

# Display 'YES' or 'NO', depending on whether (or not) you find that the larger grid GG contains the rectangular pattern PP. The evaluation will be case sensitive.

t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = [] # a list of R-num of strings that are C in length
    G_i = 0
    for G_i in xrange(R):
       G_t = str(raw_input().strip())
       G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = [] # list of strings indicating the pattern
    P_i = 0
    for P_i in xrange(r):
       P_t = str(raw_input().strip())
       P.append(P_t)
    
    # find the index of a string containing the first string in P
    # find the index in that string of the start of pattern
    # check the next grid[idx][string_idx] for the next pattern
    # and again for each in P
    
    for idx, pattern in enumerate(G):
        substring_idx = pattern.find(P[0])
        # if we find the first substring, look at the following patterns for the following substrings
        if substring_idx != -1:
            rows_checked = 1
            matched = True
            while rows_checked < r and matched: #r = 3
                # we've found first one. so if we check 2nd and its ok, we up rows_ch by 1 (r_c==2); check another row, r == 3. we want to stop
                if G[idx + rows_checked][substring_idx:substring_idx + len(P[rows_checked])] == P[rows_checked]:
                    # if the line we are looking matched next substring. go on to next substring we need to match
                    rows_checked += 1
                else:
                    matched = False
            if matched:
                print "YES"
                break
            else:
                print "NO"
                break

