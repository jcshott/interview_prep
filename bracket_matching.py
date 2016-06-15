def bracket_matching(astring):
    """
    determines whether string has valid bracket matching.

    input: string
    output: boolean
    example:
    >>> bracket_matching("({[]}())")
    True

    >>> bracket_matching("(()])")
    False

    >>> bracket_matching("test{variable()}")
    True

    >>> bracket_matching("]()")
    False
    """
    stack = []
    open_brackets = '({[<'
    closing_brackets = ')}]>'
    for char in astring:
        if char in open_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            if open_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False
        else:
            continue
    if stack:
        return False
    return True

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "tests pass"
