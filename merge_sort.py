def merge_sort(a,b):
	out = []
	i = 0
	j = 0

	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			out.append(a[i])
			i += 1
		elif b[j] < a[i]:
			out.append(b[j])
			j += 1
		elif a[i] == b[j]:
			out.append(a[i])
			out.append(b[j])
			i += 1
			j += 1

	if i < len(a):
		out.extend(a[i:])
	if j < len(b):
		out.extend(b[j:])

	return out

lst1 = [0, 2, 5, 7]
lst2 = [3, 4, 9, 10, 11]

print merge_sort(lst1, lst2)