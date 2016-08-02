def  stringSimilarity(inputs):
    output = []
    for input_str in inputs:
        total = 0
        curr_i = 0
        while curr_i < len(input_str):
            # grab each suffix
            suffix = input_str[curr_i:]
            curr_i += 1
            local_count = 0
            idx = 0
            while idx < len(suffix) and input_str[idx] == suffix[idx]:
                local_count += 1
                idx += 1
            total += local_count
        output.append(total)
    return output


"""
For two strings A and B, we define the similarity of the strings to be the length of the longest prefix common to both strings.

For example, the similarity of strings abc and abd is 2, while the similarity of strings aaa and aaab is 3.

Calculate the sum of similarities of a string S with each of its suffixes, including the string itself as the first suffix.

Explanation

Sample Case 1:

T = 1

S = ababaa
The suffixes of the string are ababaa, babaa, abaa, baa, aa and a. The similarities of each of these strings with the string ababaa are 6,0,3,0,1,1 respectively.

Hence the output is 6 + 0 + 3 + 0 + 1 + 1 = 11.

Sample Case 2:

T = 1

S = aa

The Suffixes of the string are aa, a.The similarities of each of these strings with the string aa is 2, 1 .

Hence the output is 2 + 1 = 3.
"""
