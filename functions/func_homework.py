"""
Write a function that computes the volume of a sphere given its radius.
"""
# def vol(rad):
#     return (4 / 3) * (3.14) * (rad ** 3)
"""
Write a function that checks whether a number is in a given range (inclusive of high and low)
"""
# def is_in_range(number, high, low) -> bool:
#     range_list = range(low, high + 1)
#     return number in range_list
# result = is_in_range(5, 10, 20)
# print(result)

"""
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33
"""
# def counting_upper_lower(sentence):
#     list_sentence = list(sentence)
#     print(list_sentence)
#     upper_case_counter = 0
#     lower_case_counter = 0
#     for i in list_sentence:
#         if i != ' ':
#             if i == i.upper():
#                 upper_case_counter += 1
#             else:
#                 lower_case_counter += 1
#     print(f'Numero de letras maiusculas {upper_case_counter}')
#     print(f'Numero de letras minusculas {lower_case_counter}')
# print(counting_upper_lower("Ola jamelao seu louco"))

"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
"""
# def return_unique_list(given_list):
#     unique_numbers = []
#     for i in given_list:
#         if i not in unique_numbers:
#             unique_numbers.append(i)
#     return unique_numbers
# result = return_unique_list([4, 5, 6, 6, 2, 2, 6, 9, 3, 12, 5])
# print(result)


"""
Write a Python function to multiply all the numbers in a list.
"""
# def multiply_all_nums(given_list):
#     loop_count = 0
#     mult = given_list[0]
#     for i in given_list:
#         if loop_count >= 1:
#             mult *= i
#         loop_count += 1
#     return mult
# result = multiply_all_nums([5, 5, 10])
# print(result)
        
    

"""
Write a Python function that checks whether a word or phrase is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
"""
# def is_palindrome(word):
#   word = word.replace(' ', '')   
#   return word == word[::-1]
# result = is_palindrome('arara')
# print(result)

"""
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
"""
# import string
# def ispangram(str1, alphabet = string.ascii_lowercase):
#     alphaset = set(alphabet)
#     str1 = str1.replace(' ', '')
#     str1 = str1.lower()
#     str1 = set(str1)
#     return str1 == alphaset