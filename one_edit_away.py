"""
given 2 strings (s,t).
determine if they are one edit distance apart
one deleted
one added
one changed

return T/F
time: O(N*M)
m*n space
"""

def is_one_edit(s,t):
    if abs(len(s)-len(t)) > 1:
        return False

    diff_seen = False
    # same length, check each letter, if > 1 diff or no diff, return false
    if len(s) == len(t):
        for i in xrange(len(s)):
            if s[i] != t[i]:
                if diff_seen:
                    return False
                else:
                    diff_seen = True
        return diff_seen
    # if lengths differ by 1
    # longer str idx pointer
    l_i = 0
    # shorter str idx pointer
    s_i = 0
    # find which is longer/shorter.
    if len(s) < len(t):
        shorter = s
        longer = t
    else:
        shorter = t
        longer = s

    while s_i < len(shorter):
        if shorter[s_i] != longer[l_i]:
            if diff_seen:
                return False
            else:
                # move the longer idx but not shorter
                l_i += 1
                # record we've seen a diff
                diff_seen = True
        else:
            # if both chars are same, move both pointers by 1
            l_i += 1
            s_i += 1
    # if we got thru string without finding 2 diffs, win!
    return True

print is_one_edit("geek", "gesek")
print is_one_edit("geek", "gaak")
print is_one_edit("eek", "geek")
print is_one_edit("geek", "geek")
