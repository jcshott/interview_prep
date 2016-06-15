"""
Write a function to reverse a string.
Write function to compute Nth fibonacci number
print out the grade-school multiplication table up to 12x12.
Write a function that sums up integers from a text file, one int per line.
Write function to print the odd numbers from 1 to 99.
Find the largest int value in an int array.
Format an RGB value (three 1-byte numbers) as a 6-digit hexadecimal string.
"""

def reverse_string_iterative(mystring):
    str_list = list(mystring)

    for i in range(len(str_list)/2):
        str_list[i], str_list[-i-1] = str_list[-i-1], str_list[i]

    "".join(str_list)

def reverse_string_recursive(mystring):

    def _reverse_string(idx):
        if idx == len(mystring):
            return ""
        return _reverse_string(idx+1) + mystring[idx]

    return _reverse_string(0)

def nth_fib_iterative(n):
    pass

def nth_fib_recursive(n):
    cache = {}

    def fib(curr_n):
        if curr_n in cache:
            return cache[curr_n]
        if curr_n == 1 or curr_n == 2:
            return 1
        cache[curr_n] = fib(curr_n-1) + fib(curr_n-2)
        return cache[curr_n]

    return fib(n)


def multiplication_table(n):
    for x in range(1, n+1):
        for y in range(1, n+1):
            print x*y,
        print

def sum_text_file(file_handle):
    pass

def print_odd(n):
    pass

def largest_int(array):
    pass

def rgb_to_hex(rgb):
    pass


if __name__ == '__main__':
    multiplication_table(12)
    # print reverse_string_recursive('rockstar')
    #
    # print nth_fib_recursive(1)
    # print nth_fib_recursive(2)
    # print nth_fib_recursive(999)
