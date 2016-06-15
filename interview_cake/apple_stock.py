def find_max_profit(stocks):
	"""
	>>> stock_list = [7, 5, 7, 3, 10, 4, 25, 3]
	>>> find_max_profit(stock_list)
	22
	"""
	max_profit = stocks[1] - stocks[0]
	min_price = stocks[0]

	for x in range(1, len(stocks)):
		temp_profit = stocks[x] - min_price
		if temp_profit > max_profit:
			max_profit = temp_profit
		if stocks[x] < min_price:
			min_price = stocks[x]
	return max_profit


if __name__ == '__main__':
	
	import doctest

	if doctest.testmod().failed == 0:
		print "\n*** ALL TESTS PASSED.\n"
	



    
