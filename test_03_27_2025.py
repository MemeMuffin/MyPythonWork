"""My python test on 03/27/2025"""

from collections import Counter

# Problem Statement:
# Count Unique Characters of All Substrings of a Given String

# Given a string s and an integer k, find the number of unique substrings of size k in the string. A substring is a contiguous sequence of characters within a string.

# 1. Input:
# s = "abacab"
# k = 3
# Output: 4

# 2. Input:
# s = "aaaaa"
# k = 2
# Output: 1


def unique_substrings(mainstr, k):
    """Checks a string for unique substrings with length k"""
    lst = []
    for i in range(len(mainstr)):
        if i + k <= len(mainstr):
            lst.append(mainstr[i : i + k])
    lst = set(lst)
    lst = list(lst)
    return len(lst)


s = "abacab"
print(unique_substrings(s, 3))
s = "aaaaa"
print(unique_substrings(s, 2))


# Problem Statement:
# Write an Function that find the First Non-Repeating Character in a String
# Given a string s, find the first non-repeating character and return its index. If there is no such character, return -1.

# Input:
# s = "aabb"
# Output: -1
# Input:
# s = "leetcode"
# Output: 2


def non_repeating_index(nonstr):
    """Checks for first non-repeating characters in a string and shows its index"""
    counter_dict = Counter(nonstr)
    for key, value in counter_dict.items():
        if value == 1:
            for i in range(len(nonstr)):
                if key == nonstr[i]:
                    return i
    return -1


s = "aabb"
print(f"The first non-repeating character of the string {s} is {non_repeating_index(s)}")
s = "madam"
print(f"The first non-repeating character of the string {s} is at {non_repeating_index(s)} index")


# Problem: Find all unique pairs in a list that sum up to a target.
# Example:

# Input: [1, 2, 3, 4, 5], Target = 6
# Output: [(1, 5), (2, 4)]


def unique_pairs(numlst, target):
    """Returns unique pairs which sum to target"""
    numlst_set = set(numlst)
    numlst_set = list(numlst_set)
    pair_lst = []
    for i in numlst_set:
        n = 0
        for j in range(len(numlst_set) - n):
            if target == (i + numlst_set[j]):
                str = i, numlst_set[j]
                pair_lst.append(str)
    pair_lst = set(pair_lst)
    pair_lst = list(pair_lst)
    return pair_lst


lst = [1, 2, 3, 4, 5]
print(f"The unique pairs of given list {lst} are \n{unique_pairs(lst,6)}")


# Find Common Elements in Two Dictionaries
# Problem: Find keys that exist in both dictionaries.
# Example:
# Input: {"a": 1, "b": 2}, {"b": 3, "c": 4}
# Output: ["b"]


def common_elements(dict1, dict2):
    """Finds and returns common keys between two dictionaries"""
    dict1_set = set(dict1.keys())
    dict2_set = set(dict2.keys())
    dict3_set = dict1_set.intersection(dict2_set)
    return dict3_set


print(f"The keys which exisits in both dictionaries are: {common_elements({"a": 1, "b": 2}, {"b": 3, "c": 4})}")


# Find the Second Largest Number in a List
# Problem: Find the second largest number without sorting the list.
# Example:

# Input: [10, 20, 4, 45, 99]
# Output: 45


def second_largest(numlst):
    """Finds and returns second largest number in a number list"""
    largest = numlst[0]
    sec_largest = numlst[1]
    if largest < sec_largest:
        largest, sec_largest = sec_largest, largest
    for i in range(len(numlst)):
        if numlst[i] > largest:
            largest = numlst[i]
    for i in range(len(numlst)):
        if numlst[i] > sec_largest and numlst[i] != largest:
            sec_largest = numlst[i]
    return sec_largest


print(f"The second largest number in the list is: {second_largest([10, 20, 4, 45, 99])}")


# Problem: Given a list, reverse it without using the built-in reverse() function.
# Example:

# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

lst = [1, 2, 3, 4, 5]
rev_lst = lst[::-1]
print(f"The reverse of the list {lst} is {rev_lst}")


# Problem: Find the first character that does not repeat in a given string.
# Example:

# Input: "swiss"
# Output: "w"


def non_repeating(nonstr):
    """Returns first non-repeating character in a given string"""
    counter_dict = Counter(nonstr)
    for key, value in counter_dict.items():
        if value == 1:
            return key
    return "No non-repeating character in given string"


s = "swiss"
print(f"The first non-repeating character of the string {s} is {non_repeating(s)}")
