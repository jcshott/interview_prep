#!/bin/python

import sys

def main(mystring, rotation):
    # length of phrase to encrypt (don't need here, was part of HR input)
    # n = int(raw_input().strip())
    # string to encrypt
    
    uppercase = [chr(char) for char in range(65, 91)]
    lowercase = [chr(char) for char in range(97, 123)]

    out = ""
    
    for x in mystring:
        # ascii_x = ord(x)
        # #rotate capital letter
        # if 65 <= ascii_x <= 90:
        #     # find how far the ltr is from 'A'
        #     new_char = ascii_x - 65
        #     # find how far the new ltr is from 'A', if its over 26, need to rotate around.
        #     new_char = ((new_char + k) % 26) + 65
        #     out += chr(new_char)
        
        # # rotate lowercase letter
        # elif 97 <= ascii_x <= 122:
            
        #     new_char = ascii_x - 97
        #     new_char = ((new_char + k) % 26) + 97
        #     out += chr(new_char)
        
        # # only rotate letters   
        # else:
        #     out += x

        if x.isupper():
            # find where our current char is in our list
            start_idx = uppercase.index(x)
            # find what the new idx would be
            # if it goes past the last one (z aka 26th letter in alphabet), wrap around
            new_idx = (start_idx + rotation) % 26
            out += uppercase[new_idx]
        elif x in lowercase:
            start_idx = lowercase.index(x)
            new_idx = (start_idx + rotation) % 26
            out += lowercase[new_idx]
        else:
            out += x
    return out

def test(inputStr, rotate, outputStr):
    assert main(inputStr, rotate) == outputStr

if __name__ == "__main__":

    try:
        test("www.abc.xy", 87, "fff.jkl.gh")
    except Exception, e:
        print "oops, my function is broken, come again later"
        sys.exit()

    # string to encrypt
    s = raw_input("what do you want to encrypt? ").strip()
    # number of "rotations" to use to encrypt
    k = int(raw_input("how much should I rotate? ").strip())
    
    print main(s, k)