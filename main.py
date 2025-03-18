"""First Python assignment involving basics"""

# **********Lists, Tuples and Sets**********
# movies_list = ['Anaconda', 'A Bronx Tale', 'BlindSide', 'Iron-Man', 'Man Of Steel']
# print(movies_list)
# movies_list.sort(reverse=True)
# print(movies_list)


# movies_list = ['Anaconda', 'A Bronx Tale', 'BlindSide', 'Iron-Man', 'Man Of Steel']
# movies_tuple = tuple(movies_list)
# print(movies_tuple)
# for i in movies_tuple:
#     print(f'{i} is repeated {movies_tuple.count(i)} times.')


# set_a = {1,2,3,4}
# print(f'First Set: {set_a}')
# set_b = {4,5,2,6}
# print(f'Second Set: {set_b}')
# set_x = set_a.union(set_b)
# print(f'Union of both Sets: {set_x}')


# numbers_list = [x for x in range(1,11)]
# print(f'List of numbers before operation: {numbers_list}')
# for i in numbers_list:
#     if((i+1)%2 == 0):
#         numbers_list[i] *= numbers_list[i]
# print(f'List of numbers after operation: {numbers_list}')


# # Difference:
# # Lists are mutable collection of elements which allow duplicate values. They are defined using []. i.e:
# list_test = [1,2,3,4,5,1,4]
# print(list_test, type(list_test))
# # Tuples are immutable collection of elements which allow duplicate values. They are defined using (). i.e:
# tuple_test = (1,2,3,4,5,2,3)
# print(tuple_test, type(tuple_test))
# # Sets are unordered mutable collection of elements which dont allow and duplicates. They are defined using {} or set(). i.e:
# set_test = {1,2,3,4,5,'ali'}
# print(set_test, type(set_test))

# **********Dictionaries**********
# country_dict = {'Canda': 'Ottawa', 'Japan': 'Tokyo', 'Brazil': 'Brasila', 'Australia': 'Canberra', 'South Africa': 'Pretoria'}
# print(f'Dictionary Before Appending: {country_dict}')
# country_dict.update({'Pakistan':'Islamabad'})
# print(f'Dictionary After Appending: {country_dict}')


# students_dict = {'Alice': 85, 'Bob': 78, 'Charlie': 92, 'David': 67, 'Emma': 74}
# highest = max(students_dict, key=students_dict.get)
# print(f'The Top Student is {highest} with {students_dict[highest]} marks.')


# students_dict = {'Alice': 85, 'Bob': 78, 'Charlie': 92, 'David': 67, 'Emma': 74}
# # We can iterate over only keys of a dictionary using for loop
# for key in students_dict:
#     print(key)
# # We can also use python in-bulit method for dictionary .keys()
# for key in students_dict.keys():
#     print(key)
# # We can Iterate over only values using .values()
# for value in students_dict.values():
#     print(value)
# # We can iterate over key-value pairs using items()
# for key, value in students_dict.items():
#     print(f'Key: {key} => Value: {value}', end="\n")


# test_dict = {'Ali': 1020, 'Hamza': 3021, 'Salman': 4020}
# check = input('Enter key for searching in dict: ')
# if(test_dict.get(check)):
#     print(f'{check} found. Value is: {test_dict[check]}')
# else:
#     print(f'{check} not found in dict.')

# num_dict = {x: x**2 for x in range(1,6)}
# print(f'Numbers Dict before inversion: {num_dict}')
# num_dict_inverted = {value: key for key, value in num_dict.items()}
# print(f'Numbers Dict after inversion: {num_dict_inverted}')

# **********Conditions, Loops and Exception Handling**********
# def leapyear(year):
#     if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# while True:
#     try:
#         year = int(input('Enter year to calculate Leap Year: '))
#         break
#     except ValueError:
#         print('Invalid entry.Enter year again to calculate Leap Year: ')

# check = leapyear(year)
# if(check):
#     print(f'{year} is Leap Year.')
# else:
#     print(f'{year} is not Leap Year.')


# i = 1
# while True:
#     if(i % 4 == 0):
#         print(f'Breaking loop as {i} is divisible by 4.')
#         break
#     else:
#         print(f'{i}')
#         i += 1


# def numcheck(num):
#     if(num == 0):
#         print(f'You entered Zero. {num}')
#     elif(num < 0):
#         print(f'You entered Negative Integer. {num}')
#     else:
#         print(f'You entered Positive Integer. {num}')

# while True:
#     try:
#         num = int(input('Enter Your Number: '))
#         break
#     except ValueError:
#         print('Invalid Input!! \nKindly Enter your number again.')
# numcheck(num)


# # We use exception handling as to guide the user to perform some custom defined task instead of crashing the program. We can also stop the user from continue running the program using assert to satisfy some condition or even raise custom exceptions
# while True:
#     try:
#         numerator = int(input('Enter Numerator: '))
#         break
#     except ValueError:
#         print('Invalid Input!! \nKindly Enter your number again.')
# while True:
#     try:
#         denominator = int(input('Enter Denominator: '))
#         break
#     except ValueError:
#         print('Invalid Input!! \nKindly Enter your number again.')

# try:
#     division = numerator/denominator
#     print(f'The division of given expression {numerator}/{denominator} is {division}.')
# except ZeroDivisionError:
#     print('You entered zero in place of the denominator so division is not possible.')


# number_list = [x for x in range(1,11)]
# for i in number_list:
#     if(i % 2 != 0):
#         print(i)
