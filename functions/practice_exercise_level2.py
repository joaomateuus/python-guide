"""
FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""
# def find_thirty_three(given_list: list):
#     for i in range(0, len(given_list) - 1):
#         if given_list[i : i + 2] == [3, 3]:
#             return True
#     return False

"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
"""
# def paper_doll(word: str):
#     word_list = list(word)
#     counter = 0
#     for i in word_list:
#         word_list[counter] = i + i + i
#         counter += 1
#     return ''.join(word_list)
# result = (paper_doll('caju'))
# print(result)

"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
"""
# def blackjack(n1: int, n2: int, n3: int):
#     sum = n1 + n2 + n3
#     if sum <= 21:
#         return sum
#     elif 11 in [n1, n2, n3] and sum - 10 <= 21:
#         return sum
#     else: 
#         return 'BUST'

"""
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
"""
# def summer_of_sixty_nine(int_list: list):
#     sum = 0
#     for i in int_list:
#         if i not in [6, 7, 8, 9]:
#             sum += i
#     return sum
# result = summer_of_sixty_nine([4, 5, 6, 7, 8, 9])
# print(result)
