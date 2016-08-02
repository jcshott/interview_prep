def all_perm(astring):
    permutations = []

    if len(astring) <= 1:
        permutations.append(astring)
        return permutations
    first = astring[0]
    remainder = astring[1:]
    options = all_perm(remainder)

    for o in options:
        for x in xrange(len(astring)):
            permutations.append(o[:x] + first + o[x:])
    return permutations


print len(all_perm("abcd"))
print len(all_perm("abc"))
