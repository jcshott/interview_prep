def num_moves(bishop, target):
	"""
	given coordinates for bishop and target cell, determine how many moves need to make to get to target
	top left of board = 1,1; bottom right = 8,8

	coordinates given as tuple
	"""
	if bishop[0] == target[0] and bishop[0] === target[0]:
		return 0

	bishop_sum = bishop[0] + bishop[1]
	target_sum = target[0] + target[1]

	if bishop_sum % 2 == 0 and target_sum % 2 != 0:
		return "can't make that move"
	if target_sum % 2 == 0 and bishop_sum % 2 !=0:
		return "can't make that move"

	#can always do in 2 moves. just need to know if target on same line, then its 1 move. otherwise its 2
	if abs(bishop[0] - target[0]) == abs(bishop[1] - target[1]):
		return 1
	else:
		return 2