"""Print items in the list, using recursion.

For example::

   >>> print_recursively([1, 2, 3])
   1
   2
   3
   
   >>> print_recursively([5, 7, 9, 10, 3])
   5
   7
   9
   10
   3

   >>> print_recursively([])

"""


def print_recursively(lst):
    """Print items in the list, using recursion."""

    if lst:
      print lst[0]
      print_recursively(lst[1:])


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. GREAT JOB!\n"
