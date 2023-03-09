"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
"""
# def lesser_of_two(number_one: int, number_two: int):
#     if number_one % 2 == 0 and number_two % 2 == 0:
#        return min(number_one, number_two)
#     else:
#        return max(number_one, number_two)

# result = lesser_of_two(20, 5)
# print(result)

"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
"""
# def animal_crackers(words: str):
#     word = words.split(' ')
#     if word[0][0] == word[1][0]:
#         return True
#     else:
#         return False
# result = animal_crackers('Cavalo Louco')
# print(result)

"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
"""
# def makes_twenty(number_one: int, number_two: int):
#     if number_one == 20 or number_two == 20:
#         return True
#     elif number_one + number_two == 20:
#         return True
#     else:
#         return False

# result = makes_twenty(10, 10)
# print(result)

"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
"""
# def old_macdonald(string: str):
#     first_letter = string[0]
#     middle = string[1:3]
#     fourth_letter = string[3]
#     rest = string[4:]
#     return first_letter.capitalize() + middle + fourth_letter.capitalize() + rest
# result = old_macdonald('macdonald')
# print(result)
    
"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
"""
# def reverse_function(sentence: str):
#     wordslist = sentence.split()
#     reversed_list = wordslist[::-1]
#     return ' '.join(reversed_list)
# result = reverse_function('Testando a funcao')
# print(result)

"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
"""
# def almost_there(n: int):
#     return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)