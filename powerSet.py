
# powerSet
#
# input: string
# output: array of strings
#
# input: 'abc'
# output: ['', 'a', 'b', 'ab', 'c', 'ac', 'bc', 'abc']
#
#

def powerSet(input):

    # char_lst = list(input)

    # out_list = [[]]
    
    # for char in char_lst:
    #     print "out: ", out_list
    #     out_list.extend([sublist +[char] for sublist in out_list])

    # print out_list
    out_list = [""]

    for char in input:
    	sublist = []
    	for item in out_list:
    		sublist.append(item + char)
    	out_list.extend(sublist)
    	# out_list.extend([item + char for item in out_list])

    print out_list

powerSet('abc')




        

    
    
    
    
    
    
    
    
    

    

    
    
    
    