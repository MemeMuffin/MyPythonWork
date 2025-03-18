"""Comprehensive Python Assginment"""

# Section: 1 Start


# # 1.1 First Code
# a, b = 1, 2
# print(f"The first number {a}, and the second number {b}. Before swapping ")
# a , b = b , a
# print(f"The first number {a}, and the second number {b}. After swapping ")

# # 1.1 Second Code
# #  "Hello, my name is Alesize, I am 25 years old, and I live in New York."
# name_str = input("Enter your name: ")
# age_str = input("Enter your age: ")
# city_str = input("Enter your city: ")
# print(f"Hello my name is {name_str}, Iam {age_str} years old, and I live in {city_str}")

# # 1.2 First Code
# num = int(input("Enter your number: "))
# lst = ["Even" , "Odd"]
# print(f"Given Number is {lst[num % 2]}")

# # 1.2 Second Code
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# operator = input("Enter operator: ")
# if(operator == "+"):
#     print(f"Addition is : {number1 + number2}")
# elif(operator == "-"):
#     print(f"Subtraction is : {number1 - number2}")
# elif(operator == "*"):
#     print(f"Multiplication is : {number1 * number2}")
# elif(operator == "/"):
#     print(f"Division is : {number1 / number2}")
# else:
#     print("Invalid Operator entered.")

# # 1.3 Fisrt Code
# lst = []
# lst.append(int(input("Enter First Number: ")))
# lst.append(int(input("Enter Second Number: ")))
# lst.append(int(input("Enter Third Number: ")))
# large = masize(lst)
# print(f"The Largest Number is: {large}")

# # 1.3 Second Code
# operator = input("Enter which operation do you want to run(add,subtract,multiply,divide): ")
# if(operator == "add" or operator == "+"):
#     number1 = int(input("Enter first number: "))
#     number2 = int(input("Enter second number: "))
#     print(f"Addition is : {number1 + number2}")
# elif(operator == "subtract" or operator == "-"):
#     number1 = int(input("Enter first number: "))
#     number2 = int(input("Enter second number: "))
#     print(f"Subtraction is : {number1 - number2}")
# elif(operator == "multiply" or operator == "*"):
#     number1 = int(input("Enter first number: "))
#     number2 = int(input("Enter second number: "))
#     print(f"Multiplication is : {number1 * number2}")
# elif(operator == "divide" or operator == "/"):
#     number1 = int(input("Enter first number: "))
#     number2 = int(input("Enter second number: "))
#     print(f"Division is : {number1 / number2}")
# else:
#     print("Invalid operation.")

# # 1.4 First Code
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a+b
#     print()
# num = int(input("Enter nth term for Fibonacci series: "))
# fib(num)

# # 1.4 Second Code
# for i in range(1,5):
#     for j in range(i):
#         print("*", end=" ")
#     print("\n")

# # 1.5 First Code
# size = input("Enter String to check Palindrome: ")
# y = "".join(reversed(size))
# if(size == y):
#     print("String is palindrome.")
# else:
#     print("String is not palindrome.")

# # 1.5 Second Code
# test_str = input("Enter string for vowel count: ")
# lst = ['a','e','i','o','u','A','E','I','O','U']
# count = 0
# for i in test_str:
#     if(i in lst):
#         count += 1
# print(f'Number of Vowels: {count}')

# # 1.6 First Code
# lst = [1,2,3,4,5,6,7,8,9,10]
# lst.sort
# reverse_lst = lst[::-1]
# print(f"Second largest in given list is: {reverse_lst[1]}")

# # 1.6 Second Code
# tup_num = (1,2,3,4,5,6,)
# print(type(tup_num), tup_num)
# lst = list(tup_num)
# lst.sort(reverse=True)
# print(type(lst),lst)

# # 1.7 First Code
# people = {"Ali": 18, "Hamza": 20, "Fatima": 16, "Noor": 25, "Gohar": 28}
# old = max(people, key=people.get) # type: ignore
# old = max(people, key=lambda name:people[name])
# print(f"Oldest person is {old}")

# # 1.7 Second Code
# num_lst = [1,2,3,4,1,2]
# num_set = set(num_lst)
# num_lst = list(num_set)
# print(type(num_lst), num_lst)

# # 1.8 First Code
# def factorial(n):
#     if(n <= 1 ):
#         return 1
#     return n * factorial(n-1)
# num = int(input("Enter number to calculate its factorial: "))
# print(f"Factorail of the given number is: {factorial(num)}")

# # 1.8 Second Code
# def unique_list(num_lst):
#     num_set = set(num_lst)
#     num_lst = list(num_set)
#     return num_lst
# lst = [1,2,3,4,5,1,4,2]
# print(f"List with unique values is: {unique_list(lst)}")

# # 1.9 First Code
# with open('test.tsizet', 'r') as myfile:
#     print(myfile.read())

# # 1.9 Second Code
# with open('test.tsizet', 'w') as myfile:
#     myfile.write(input("Enter data to write into the file: "))
# with open('test.tsizet', 'r') as myfile:
#     print(myfile.read())

# # 1.10 First Code
# numerator, denominator = 1, 0
# try:
#     division = numerator/denominator
#     print(f'The division of given esizepression {numerator}/{denominator} is {division}.')
# esizecept ZeroDivisionError:
#     print('You entered zero in place of the denominator so division is not possible.')

# # 1.10 Second Code
# try:
#     with open('file.tsizet', 'r') as myfile:
#         print(myfile.read())
# esizecept FileNotFoundError:
#     print("Entered file to be opened does not esizeist.")

# Section: 1 End


# Section: 2 Start
# Task#1
# import math
# circle_raduis = 5
# print(f"Area of circle is: {math.pi * (circle_raduis ** 2)}")

# # Task#2
# import datetime
# print(datetime.datetime.now())

# # Task#3
# import random
# for i in range(0,5):
#     print(random.randint(1,100), end=" ")

# # Task#4
# import csv
# with open('test.csv', 'r') as mycsvfile:
#     reader = csv.reader(mycsvfile)
#     row_lst = []
#     for i in reader:
#         row_lst = row_lst + i
#     for i in range(5):
#         print(row_lst[i])

# # Task#5
# import os
# print('List of directories and files before creation:')
# dir_list = os.listdir()
# print(dir_list)
# if(not os.path.esizeists("osTest")):
#     os.mkdir('osTest')
# print('List of directories and files After creation:')
# for folder in dir_list:
#     if('osTest' == folder):
#         print(os.listdir(folder))

# # Task#6
# import sys
# counter = 0
# for i in sys.argv:
#     counter += 1
#     print(f"Command Line Arguement {counter}: {i}")

# # Task#7
# import time
# def countdown_timer(n):
#     while n > 0:
#         print(f"Time Remaining: {n} seconds.")
#         time.sleep(1)
#         n = n - 1
# countdown_timer(10)

# # Task#8
# import collections
# collect_lst = [1,2,3,4,5,6,7,8,1,2,4,8]
# counter = collections.Counter(collect_lst)
# print(counter)

# # Task#9
# import requests
# response = requests.get("https://www.edclub.com/sportal/program-3/126.play")
# print(response.content)

# # Task#10
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('num1', type=int)
# parser.add_argument('num2', type=int)
# args = parser.parse_args()
# print(f'{args.num1} + {args.num2} = {args.num1 + args.num2}')


# Section 2 End


# Section 3 Start

# # Task#1
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self,data):
#         self.stack.append(data)

#     def pop(self):
#         if(len(self.stack) != 0):
#             item = self.stack.pop()
#             print(f'Removed item: {item} from stack.')
#         else:
#             print('Stack is empty')

#     def peek(self):
#         if(len(self.stack) != 0):
#             print(f"Item at the top of the stack is: {self.stack[len(self.stack) - 1]}")

# st = Stack()
# st.push(1)
# st.push(2)
# st.push(3)
# st.peek()

# # Task#2
# class Queue:
#     def __init__(self, size):
#         self.size = size
#         self.queue = [None] * size
#         self.head = self.tail = -1

#     def enqueue(self, data):
#         if(self.tail == self.size - 1):
#             print('Queue is full.')
#         elif(self.head == -1):
#             self.head = 0
#             self.tail = 0
#             self.queue[self.tail] = data
#         else:
#             self.tail = self.tail + 1
#             self.queue[self.tail] = data

#     def dequeue(self):
#         if(self.head == -1):
#             print('Queue is empty')
#         elif(self.head == self.tail):
#             temp = self.queue[self.head]
#             self.head = -1
#             self.tail = -1
#             return temp
#         else:
#             temp = self.queue[self.head]
#             self.head = self.head + 1
#             return temp

#     def show(self):
#         if(self.head == -1):
#             print("Queue is empty.")
#         else:
#             for i in range(self.head, self.tail + 1):
#                 print(self.queue[i], end=" ")

# obj_queue = Queue(5)
# for i in range(5):
#     obj_queue.enqueue(i+1)
# print('Queue Before Dequeue:')
# obj_queue.show()
# obj_queue.dequeue()
# print('\nQueue After Dequeue:')
# obj_queue.show()

# # Task#3
# from random import randint
# from statistics import mode
# def most_common(lst):
#     return mode(lst)
# frequent_lst = [1,2,3,4,2,4,3,7,1]
# print(f'The list is {frequent_lst}')
# print(f'The most frequent element is: {most_common(frequent_lst)}')

# # Task#4
# nested_dict = {'a': 1,
#                'b':{'c': 2, 'd':3},
#                'e':{'f':4, 'g': 5}}
# flat_dict = {}
# def flatten_dict(data, parent_key='',seperator='/'):
#     for k, v in data.items():
#         key = parent_key + seperator + k if parent_key else k
#         if isinstance(v, dict):
#             flatten_dict(v, key)
#         else:
#             flat_dict[key] = v
#     return flat_dict

# print(f'Nested Dict: {nested_dict}')
# print(f'Nested Dict after flatten function call: {flatten_dict(nested_dict)}')

# # Task#5
# class LinkedList:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#     def print_linkedlist(node):
#         while node is not None:
#             print(f"{node.data}", end=" ")
#             node = node.next
#         print()

# def reverse_linkedlist(linkedlist_head):
#     curr = linkedlist_head
#     prev = None
#     while curr is not None:
#         nextNode = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nextNode
#     return prev

# head = LinkedList(1)
# head.next = LinkedList(2)
# head.next.next = LinkedList(3)
# head.next.next.next = LinkedList(4)
# head.next.next.next.next = LinkedList(5)
# print('Linkedlist before reverse: ')
# head.print_linkedlist()
# head = reverse_linkedlist(head)
# print('Linkedlist after reverse: ')
# head.print_linkedlist()

# # Task#6
# def isbalanced_parenthesis(exp):
#     count = 0
#     for i in range(len(exp)):
#         if(exp[i] == '('):
#             count += 1
#         else:
#             count -= 1
#     if(count < 0 ):
#         print(f"Not balanced parenthesis: {exp}")
#     elif(count > 0):
#         print(f"Not balanced parenthesis: {exp}")
#     else:
#         print(f"Balanced parenthesis: {exp}")

# exp1 = "((()))())"
# exp2 = "((()))((()))"
# isbalanced_parenthesis(exp1)
# isbalanced_parenthesis(exp2)

# # Task#7
# num_set1 = {1,2,3,4}
# num_set2 = {1,4,2,5,6,7}
# print(f'First set is: {num_set1}'"\n"f'Secont set is: {num_set2}')
# print(f'Intersection of sets is: {num_set1.intersection(num_set2)}')
# print(f'Union of sets is: {num_set1.union(num_set2)}')

# # Task#8
# age_dict = {"Ali": 18, "Hamza": 20, "Fatima": 16, "Noor": 25, "Gohar": 28}
# age_tup = tuple(age_dict.items())
# print(type(age_tup), age_tup)
# new_dict = dict(age_tup)
# print(type(new_dict), new_dict)

# # Task#9
# from random import randint
# num_lst1 = [randint(1,10) for i in range(5)]
# num_lst2 = [randint(1,10) for i in range(5)]
# num_lst1.sort()
# num_lst2.sort()
# print(f'Sorted list No#1: {num_lst1}',"\n",f'Sorted list No#2: {num_lst2}')
# new_lst3 = []
# new_lst3.extend(num_lst1)
# new_lst3.extend(num_lst2)
# print(f'Before sort new list is: {new_lst3}')
# new_lst3.sort()
# print(f'After sort new list is: {new_lst3}')

# # Task#10
# def is_circularly_sorted(sorted_lst):
#     count = 0
#     for i in range(len(sorted_lst)):
#         if(sorted_lst[i] > sorted_lst[(i+1) % len(sorted_lst)]):
#             count += 1
#     return count <= 1
# s_lst = [randint(1,10) for i in range(5)]
# s_lst.sort()
# if(is_circularly_sorted(s_lst) <= 1):
#     print(f"List is circularly sorted. {s_lst}")
# else:
#     print(f"List is not circularly sorted. {s_lst}")


# Section: 3 End


# Section: 4 Start

# # Task#1
# from math import sqrt
# is_prime = lambda x: all(map(lambda y: x % y, range(2,x)))
# num = int(input("Enter Number to check prime: "))
# if(is_prime(num)):
#     print(f"Given number is prime: {num}")
# else:
#     print(f"Given number is not prime: {num}")

# # Task#2
# temperature_lst = [32,12,44,29]
# print(f"Temprature in Celsius is: {temperature_lst}")
# change_CtoF = list(map(lambda x: (x*(9/5)) + 32,temperature_lst))
# print(f"Temprature in Farenhiet is: {change_CtoF}")

# # Task#3
# words_lst = ["ali","sanctuary","drama","stamp","fire"]
# print(words_lst)
# longwords_lst = list(filter(lambda x: len(x) >= 5, words_lst))
# print(longwords_lst)

# # Task#4
# from functools import reduce
# from random import randint
# num4_lst = [randint(1,10) for i in range(5)]
# print(num4_lst)
# new_num4_lst = reduce(lambda x, y: x if x>y else y, num4_lst)
# print(new_num4_lst)

# # Task#5
# rand_str = "Hello my name is Python"
# print(rand_str)
# rev_str = lambda x: x[::-1]
# print(rev_str(rand_str))

# # Task#6
# from random import randint
# rand_lst = [randint(1,10) for i in range(5)]
# print(rand_lst)
# new_rand_lst = list(map(lambda x: x**2,rand_lst))
# print(new_rand_lst)

# # Task#7
# def iseven(n):
#     return n % 2 == 0
# rand_lst = [randint(1,10) for i in range(5)]
# print(rand_lst)
# new_rand_lst = list(filter(iseven,rand_lst))
# print(new_rand_lst)

# # Task#8
# def testdecorator(fx):
#     print("Function Executed")
#     fx()

# @testdecorator
# def hello():
#     print("Hello there.")

# hello

# # Task#9
# class TestingNumber:
#     def __init__(self) -> None:
#         pass

#     @staticmethod
#     def testing_add(x,y):
#         return x + y

# print(f"StaticMethod in play here: {TestingNumber.testing_add(1,2)}")

# # Task#10
# from functools import partial
# testing_parital = partial(lambda x: x*5)
# print(testing_parital(2))


# Section: 4 End


# Section: 5 Start

# # Task#1
# class Car:
#     def __init__(self, brand = 'N/A', model = 'N/A', year = 0000) -> None:
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def get_info(self):
#         print(f"The car maker is {self.brand}, model is {self.model} and the year is {self.year}")

# test_car = Car()
# test_car1 = Car("Toyota","Fielder","2022")
# test_car.get_info()
# test_car1.get_info()

# # Task#2
# from random import randint
# from typing import Any
# class Employee:
#     def __init__(self,id = None,name = "N/A",monthly_salary = 0) -> None:
#         self.name = name
#         self.id = id
#         self.monthly_salary = monthly_salary

#     def annual_income_calculation(self):
#         print(f'The Employee {self.name} with id {self.id} has an annual income of Rs.{self.monthly_salary * 12}')

# test_employee = Employee()
# test_employee1 = Employee(randint(1,100),"Ali", randint(1,50000))
# test_employee.annual_income_calculation()
# test_employee1.annual_income_calculation()

# # Task#3
# class BankAccount:
#     def __init__(self, id = None, name = "N/A", deposited_amount = 0) -> None:
#         self.id = id
#         self.name = name
#         self.deposited_amount = deposited_amount

#     def deposit_amount(self, amount):
#         self.deposited_amount = self.deposited_amount + amount
#         print(f'Deposited {amount} into user: {self.name} account')
#         print(f'After deposit current balance is: {self.deposited_amount}')

#     def withdraw_amount(self, amount):
#         if(self.deposited_amount < amount):
#             print(f"Can not withdraw amount as entered {amount} is greater than balance of user: {self.name}")
#         else:
#             print(f'Withdrawing {amount} from user: {self.name} account')
#             self.deposited_amount = self.deposited_amount - amount
#             print(f'After withdrawal current balance is: {self.deposited_amount}')

# test_bankaccount = BankAccount()
# test_bankaccount1 = BankAccount(randint(1,100),"Ali",randint(1,50000))
# test_bankaccount.withdraw_amount(100)
# test_bankaccount.deposit_amount(5000)
# test_bankaccount1.withdraw_amount(2500)
# test_bankaccount1.deposit_amount(6000)

# # Task#4
# class Person:
#     def __init__(self, name = "N/A", age = None) -> None:
#         self.name = name
#         self.age = age

#     def get_info(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")

# class Student(Person):
#     def __init__(self,student_id = None, name="N/A", age=None, grade = 'N/A') -> None:
#         super().__init__(name, age)
#         self.student_id = student_id
#         self.grade = grade

#     def get_info(self):
#         print(f'The Student {self.name} and with age {self.age} passed with following grade {self.grade}')

# test_student = Student()
# test_student1 = Student(randint(1,100),"ALi",18,"B+")
# test_student.get_info()
# test_student1.get_info()

# # Task#5
# class Bird:
#     def __init__(self) -> None:
#         pass

#     def fly(self):
#         print("Birds fly and hunt all kinds of things.")

# class Eagle(Bird):
#     def __init__(self) -> None:
#         super().__init__()

#     def fly(self):
#         print("Eagle's take flight and hunt snakes etc.")

# test_bird = Bird()
# test_eagle = Eagle()
# test_bird.fly()
# test_eagle.fly()

# # Task#6
# class Vector:
#     def __init__(self, x = 0,y = 0,z = 0):
#         self.x = x
#         self.y = y
#         self.z = z

#     def display_vector(self):
#         print(f'{self.x}x + {self.y}y + {self.z}z')

#     def __add__(self, i):
#         return Vector((self.x + i.x), (self.y + i.y), (self.z + i.z))

# test_vector = Vector(randint(1,9),randint(1,9),randint(1,9))
# test_vector1 = Vector(randint(1,9),randint(1,9),randint(1,9))
# test_vector.display_vector()
# test_vector1.display_vector()
# test_result_vector = test_vector + test_vector1
# test_result_vector.display_vector()

# # Task#7
# class Weatther:
#     def __init__(self, temperature = 0):
#         self._temperature = temperature

#     @property
#     def temperature(self):
#         print("The Temperature is:", end=" ")
#         return self._temperature

#     @temperature.setter
#     def temperature(self, val):
#         self._temperature = val

# test_temp = Weatther()
# test_temp1 = Weatther()
# print(test_temp.temperature)
# print(test_temp1.temperature)
# test_temp._temperature = 35
# test_temp1._temperature = 45
# print(test_temp.temperature)
# print(test_temp1.temperature)

# # Task#8
# class Singleton(type):
#     _instances = {}
#     def __call__(cls,*args, **kwargs,):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args,**kwargs)
#         return cls._instances[cls]

# class Test_Singleton(metaclass = Singleton):
#     def __init__(self, name = "N/A", occupation = "N/A") -> None:
#         self.name = name
#         self.occupation = occupation

#     def show(self):
#         print(f"My name is {self.name} and my occupation is {self.occupation}.")

# test_person = Test_Singleton("ALi","Programmer")
# test_person1 = Test_Singleton()
# print('Showing first instance of class Test_Singleton:')
# test_person.show()
# print('Showing second instance of class Test_Singleton:')
# test_person1.show()
# print(test_person is test_person1)

# # Task#9
# class MetaClass_Restriction_5(type):
#     _instances = {}
#     _count = 0
#     def __call__(cls,*args, **kwargs,):
#         if cls._count in range(5):
#             cls._instances = super().__call__(*args,**kwargs)
#             cls._count += 1
#             return cls._instances
#         return cls._instances

# class Plane(metaclass = MetaClass_Restriction_5):
#     def __init__(self, name = "N/A", passenger_count = 0) -> None:
#         self.name = name
#         self.passegner_count = passenger_count

#     def show(self):
#         print(f"The Plane is {self.name} and passenger count is {self.passegner_count}.")

# test_plane1 = Plane("AirBus A220", 180)
# test_plane2 = Plane("AirBus A320 Family", 300)
# test_plane3 = Plane("AirBus A330", 320)
# test_plane4 = Plane("Boeing 737", 300)
# test_plane5 = Plane("Boeing 767", 200)
# test_plane6 = Plane("Boeing 777", 150)

# test_plane1.show()
# test_plane2.show()
# test_plane3.show()
# test_plane4.show()
# test_plane5.show()
# test_plane6.show()
# print(test_plane5 is test_plane6)

# # Task#10
# class Observable:
#     def __init__(self):
#         self.observers = []

#     def add_observer(self, observer):
#         if observer not in self.observers:
#             self.observers.append(observer)

#     def remove_observer(self, observer):
#         if observer in self.observers:
#             self.observers.remove(observer)

#     def notify_observers(self, *args, **kwargs):
#         for observer in self.observers:
#             observer.update(self, *args, **kwargs)

# class Observer:
#     def update(self, observable, *args, **kwargs):
#         pass

# class WeatherStation(Observable):
#     def __init__(self, temperature):
#         super().__init__()
#         self.temperature = temperature
#         self.notify_observers()

#     def set_temperature(self, val):
#         self.temperature = val
#         self.notify_observers()

# class PhoneDisplay(Observer):
#     def update(self, observable, *args, **kwargs):
#         if isinstance(observable, WeatherStation):
#             temperature = observable.temperature
#             print(f"temperature is: {temperature}")

# class ComputerDisplay(Observer):
#     def update(self, observable, *args, **kwargs):
#         if isinstance(observable, WeatherStation):
#             temperature = observable.temperature
#             print(f"temperature is: {temperature}")

# testing_weather_station = WeatherStation(35)
# test_phone = PhoneDisplay()
# test_computer = ComputerDisplay()

# testing_weather_station.add_observer(test_phone)
# testing_weather_station.add_observer(test_computer)

# testing_weather_station.set_temperature(35)

# Section: 5 End


# Section: 6 Start


# # Task#1
# from threading import Thread
# class ThreadPool:
#     def __init__(self):
#         pass

#     @staticmethod
#     def pooling_threads(fx_lst):
#         thread_lst = []
#         for v in fx_lst:
#             thread_lst.append(Thread(target=v))

#         for i in range(len(thread_lst)):
#             thread_lst[i].start()

# def test_task1():
#     print("Iam Task 1")
# def test_task2():
#     print("Iam Task 2")
# def test_task3():
#     print("Iam Task 3")
# def test_task4():
#     print("Iam Task 4")

# task_lst = {test_task1,test_task2,test_task3,test_task4}
# pool = ThreadPool()
# pool.pooling_threads(task_lst)

# # Task#2
# import requests
# import multiprocessing
# import os

# def download_file(url, name):
#     os.makedirs("files", exist_ok=True)
#     response =requests.get(url)
#     with open(f"files/file{name}.jpg", 'wb') as f:
#         f.write(response.content)


# if __name__ == "__main__":
#     url = "https://picsum.photos/2000"
#     test_processes = []
#     for i in range(5):
#         test_multi_processing = multiprocessing.Process(target=download_file, args=[url, i])
#         test_multi_processing.start()
#         test_processes.append(test_multi_processing)

#     for p in test_processes:
#         p.join()

#     print("Done")

# # Task#3
# import ipaddress

# def check_ip(ip):
#     try:
#         ipaddress.ip_address(ip)
#         print("Valid IP Address")
#     except ValueError:
#         print("Invalid IP Address")

# check_ip("192.168.10.1")
# check_ip("192.168.10.111")
# check_ip("192.168.10.1.255")

# # Task#4
# from retrying import retry

# @retry(stop_max_attempt_number=3)
# def test_function():
#     try:
#         n = int(input("Enter number to calcutalte its square: "))
#         print(f"Square of {n} is {n**2}")
#     except ValueError:
#         print("Invalid Value entered.")
#         raise

# test_function()

# # Task#5
# import os
# import json

# class JsonParser:
#     def __init__(self, filename) -> None:
#         self.filename = filename

#     def  json_file_write(self, data):
#         with open(self.filename, 'w') as myjsonfile:
#             json.dump(data, myjsonfile, indent=2)
#             print(f"Writing successful in json file {self.filename}")

#     def json_file_read(self):
#         with open(self.filename, 'r') as myjsonfile:
#             return json.load(myjsonfile)

# parser = JsonParser("jsonfile.json")

# test_data = {"Employee#1" : {"name": "ALI", "age": 18, "role": "Lead Project Manager"}}

# parser.json_file_write(test_data)
# jsondata = parser.json_file_read()
# print(jsondata)

# # Task#6
# from typing import Any
# import time

# class MemoizeFunction:
#     def __init__(self, fx) -> None:
#         self.fx = fx
#         self.memo = {}

#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         if not args in self.memo:
#             self.memo[args] = self.fx(*args)
#         return self.memo[args]

# @MemoizeFunction
# def fibonacci(n):
#     time.sleep(5)
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
#     print()

# fibonacci(5)
# fibonacci(5)

# # Task#7
# import heapq
# from itertools import count

# class PriorityQueue():
#     def __init__(self):
#         self._value = []
#         self._counter = count()

#     def enqueue_with_priority(self, priority, value):
#         element = (priority, next(self._counter), value)
#         heapq.heappush(self._value, element)

#     def dequeue(self):
#         return heapq.heappop(self._value)[-1]

#     def show(self):
#         for i in range(len(self._value)):
#             print(self._value[i], end=" ")
#         print()

# test_priorityqueue = PriorityQueue()
# test_priorityqueue.enqueue_with_priority(1,2)
# test_priorityqueue.enqueue_with_priority(2,4)
# test_priorityqueue.enqueue_with_priority(3,6)
# test_priorityqueue.enqueue_with_priority(4,8)
# test_priorityqueue.enqueue_with_priority(5,10)
# test_priorityqueue.show()
# test_priorityqueue.dequeue()
# test_priorityqueue.show()

# # Task#8
# from functools import lru_cache
# import time

# @lru_cache(maxsize=None)
# def test_fx(n):
#     time.sleep(3)
#     print(f"Done for {n}: {n**2}")

# test_fx(2)
# test_fx(4)
# test_fx(6)
# test_fx(4)
# test_fx(6)

# # Task#10
# import yfinance as yf

# def get_stock_price(ticker):
#     stock = yf.Ticker(ticker)
#     price = stock.history(period="1d")['Close'].iloc[-1]
#     print(f"The latest price of {ticker.upper()} is ${price:.2f}")

# ticker_symbol = input("Enter stock ticker e.g.(AAPL,TSLA,GOOG): ")
# get_stock_price(ticker_symbol)
