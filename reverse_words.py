# input: string
# output: string with the words reversed
# ex in: "Dogs are great"
# out: "great are Dogs"


def reverseWords(input):
    if not input:
        return ""
    if type(input) == str:
        input = input.split(" ")
    return reverseWords(input[1:]) + " " + input[0]
#     HELPER RECURSIVE METHOD
#     out = []

#     def reverse(input_list):
#         if not input_list:
#             return
#         reverse(input_list[1:])
#         out.append(input_list[0])

#     reverse(input.split(" "))
#     return " ".join(out)



#     ITERATIVE METHOD:
#     words = input.split(" ")

#     for idx in range(len(words)/2):
#         words[idx], words[-idx-1] = words[-idx-1], words[idx]

#     return " ".join(words)

print reverseWords("Dogs are great")
