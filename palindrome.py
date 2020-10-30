"""palindrome ignoring punctuation and case"""


"""using re (slower)"""
import re
string = input("Enter a string\n")
s = "".join(re.findall(r'[a-z]+',string.lower()))
if s[::-1]==s:
    print("PALINDROME")
else:
    print("NOT PALINDROME")

"""Using isalpha (faster)"""
# string = input("Enter a string\n")
# s = ""

# #extracting only the letters
# for char in string:
#     if char.isalpha():
#         s +=char

# #coverting to same case
# s = s.lower()

# if s[::-1]==s:
#     print("PALINDROME")
# else:
#     print("NOT PALINDROME")

