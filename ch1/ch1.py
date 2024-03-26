# 1.1
def is_unique_simple(s):
    h = set()
    for letter in s: 
        if letter in h:
            return False
        h.add(letter)
    return True


checker = 0 # 0000 0000 0000 0000 0000 0000 0000 0001
            # 0000 0000 0000 0000 0000 0000 0000 0010
            # 0000 0000 0000 0000 0000 0000 0000 0000 > 0

            # 0000 0000 0000 0000 0000 0000 0000 0001
            # 0000 0000 0000 0000 0000 0000 0000 0010
            # 0000 0000 0000 0000 0000 0000 0000 0011


# REMEMBER: case sensitivity, THE BELOW PROBLEMS DO NOT TAKE THAT INTO ACCOUNT, s1=dog, s2=God
# time complexity: O(n)
# space complexity: O(n)
# depends on unicode or ascii code for size
# ascii
# asci
def check_permutation_hash(s1, s2):
    if len(s1) != len(s2):
        return False
    
    h1 = {}
    for element in s1:
        if element in h1: 
            h1[element] += 1
        else:
            h1[element] = 1
    
    h2 = {}
    for element in s2:
        if element in h2:
            h2[element] += 1
        else:
            h2[element] = 1
    
    return h1 == h2

# O(1 n+m)
# O(n)

def check_permutation_ascii(s1, s2):
    if len(s1) != len(s2):
        return False
    
    arr = [0]*128 # assuming 
    
    for element in s1:
        arr[ord(element)] += 1
        # arr = [0,0,0,0,0,1,0,0,0,0,0]
        # arr = [0,0,0,0,0,1,0,0,1,0,0]
        # arr = [0,0,0,0,0,1,0,1,0,1,0,0]
        # arr = [0,0,0,0,0,1,0,1,0,2,1,0,0]


    for element in s2:
        if arr[ord(element)] == 0: #
            return False
        arr[ord(element)] -= 1
        # arr = [0,0,0,0,0,-1, 0, 0, 0,1, 0,0,0]
    
    return sum(arr) == 0

# O(n log n)
def check_permutation_quick_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    
    rand_i = len(s1) // 2 # choose random index
    
    quick_sort()
    pivot = s1[rand_i]
    lesser_half = s1[:pivot]
    greater_half = s1[pivot:]


def quick_sort(s):
    pass

# URLify:
# Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end 
# to hold the additional characters,and that you are given the 
# "true" length of the string. (Note: If implementing in Java,
# please use a character array so that you can perform this 
# operation in place.)

def URLify(s):
    replace = "%20"
    s2 = ""
    i = 0
    while i < len(s):
        if s[i] == " ":
            s2 += "%20"
        else: 
            s2 += s[i]
    return s2

# Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith"

def URLify(s, n):
    replace = "%20"
    s2 = ""
    i = 0
    while i < len(s):
        if s[i] == " ":
            s2 += "%20"
        else: 
            s2 += s[i]
    return s2

# Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.) Hints:#106,#121,#134,#136
def palindromePermutation(word):
    h = {}
    count_odd_letters = 0
    for letter in word:
        if letter in h:
            h[letter] += 1
            if h[letter] % 2 == 0:
                count_odd_letters -= 1
            else:
                count_odd_letters += 1
        else:
            h[letter] = 1
            count_odd_letters += 1
    
    # for key in h.keys():
    #     if h[key] % 2 == 0:
    #         count_odd_letters += 1

    return count_odd_letters < 2

def palindrome_permutation_ascii(word):
    h = [0]*26
    count_odd_letters = 0
    for letter in word:
        h[ord(letter.lower()) - ord('a')] += 1
        if h[ord(letter.lower()) - ord('a')] % 2 == 0:
            count_odd_letters -= 1
        else:
            count_odd_letters += 1
    

    return count_odd_letters < 2
# print("QUESTION 1.4")
# print(palindromePermutation("hello") == False and palindromePermutation("hello") == palindrome_permutation_ascii("hello") )
# print(palindromePermutation("helleh") == True and palindromePermutation("helleh") == palindrome_permutation_ascii("helleh") )
# print(palindromePermutation("a") == True and palindromePermutation("a") == palindrome_permutation_ascii("a") )
# print(palindromePermutation("ab") == False and palindromePermutation("ab") == palindrome_permutation_ascii("ab") )
# print(palindromePermutation("aba") == True and palindromePermutation("aba") == palindrome_permutation_ascii("aba") )
# print(palindromePermutation("aaa") == True and palindromePermutation("aaa") == palindrome_permutation_ascii("aaa") )
# print(palindromePermutation("aabba") == True and palindromePermutation("aabba") == palindrome_permutation_ascii("aabba") )


# problem 1.5
# There are three types of edits that can be performed on strings: 
# insert a character, 
# remove a character, or 
# replace a character. 

# Given two strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true 
# pales, pale -> true 
# pale, bale -> true 
# pale, bake -> false
def one_away(str1, str2):
    # insert a character
    # remove a character, or 
    # replace a character.
    h1 = {}
    for letter in str1: 
        if letter in h1: 
            h1[letter] += 1
        else: 
            h1[letter] = 1
    for letter in str2: 
        if letter in h1:
            h1[letter] -= 1
    
    differences = 0
    total = 0
    for key in h1.keys():
        if h1[key] != 0: 
            differences += 1
            total += h1[key]
    
    if total == 0 and differences == 2:
        return True
    else: 
        return differences <= 1


def one_away_ascii(str1, str2):
    # insert a character
    # remove a character, or 
    # replace a character.
    ascii_list = [0]*377
    for letter in str1:
        ascii_list[ord(letter)] += 1
    for letter in str2:
        ascii_list[ord(letter)] -= 1
    
    differences = 0
    for element in ascii_list:
        # print(f"element {element}")
        if element != 0:
            differences += 1
    
    total = sum(ascii_list)
    if total == 0 and differences == 2:
        return True
    else: 
        return differences <= 1

# print("QUESTION 1.5:")
# print("one_away:")
# print(f"pale, ple -> true : {one_away("pale", "ple")}")
# print(f"pales, pale -> true : {one_away("pales", "pale")}")
# print(f"pale, bale -> true : {one_away("pale", "bale")}")
# print(f"pale, bake -> false: {one_away("pale", "bake")}")
# print("one_away_ascii: ")
# print(f"pale, ple -> true : {one_away_ascii("pale", "ple")}")
# print(f"pales, pale -> true : {one_away_ascii("pales", "pale")}")
# print(f"pale, bale -> true : {one_away_ascii("pale", "bale")}")
# print(f"pale, bake -> false: {one_away_ascii("pale", "bake")}")


# problem 1.6
# String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3. 
# If the "compressed" string would not become smaller than the original string, your method should return
# the original string. 
# You can assume the string has only uppercase and lowercase letters (a - z).
# Hints:#92, #110

def string_compression(str1):
    if len(str1) <= 1:
        return str1
    
    new_str = ""
    letter = str1[0]
    letter_count = 1
    i = 1
    while i < len(str1):

        if letter != str1[i]:
            new_str += letter
            new_str += str(letter_count)
            letter = str1[i]
            letter_count = 1
            if i == len(str1) - 1:
                new_str += letter
                new_str += str(letter_count)
        else: 
            letter_count += 1
            if i == len(str1) - 1:
                new_str += letter
                new_str += str(letter_count)
        i += 1
    
    if len(new_str) < len(str1):
        return new_str
    return str1

print("QUESTION 1.6")
print(f'{string_compression("aabcccccaaa")} == "a2b1c5a3": {string_compression("aabcccccaaa") == "a2b1c5a3"}')
print(f'{string_compression("aabcccccaaab")} == "a2b1c5a3b1"): {string_compression("aabcccccaaab") == "a2b1c5a3b1"}')

# problem 1.7
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
# write a method to rotate the image by 90 degrees. Can you do this in place?
# example: 
# input: 
# [
# [0,1]
# [2,3]
# ]
# temp1 = 0
# temp2 = 2
# 
# output: 
# [
# [0,1]
# [2,3]
# ]
# 

# input: 
# [
# [0,1,2]
# [3,4,5]
# [6,7,8]
# ]
# output:
# [
# [6,1,0]
# [3,4,5]
# [8,7,2]
# ]
# 

import math
def rotate_matrix(matrix):
    if len(matrix) == 0 or len(matrix) == 1:
        return matrix
    
    i = 0
    # temp_val = i, i
    # swap temp_val w/ 0 + i, 0 + i
    # swap temp_val w/ i,len(arr) - i
    # swap temp_val w/ len(arr) - i, len(arr) - i
    # swap temp_val w/ len(arr) - i, 0 + i
    # swap temp_val w/ 0 + i, 0 + i
    

    while i < (len(matrix) - 1):
        j = i
        while j < len(matrix) -1:
            temp_val = matrix[i][i]
            # set to initial val
            
            # swap temp_val w/ 0 + i, 0 + i
            matrix[i][i], temp_val = temp_val, matrix[i][i]

            # swap temp_val w/ i,len(arr) - i
            matrix[i][len(matrix) -i - 1], temp_val = temp_val, matrix[i][len(matrix) -i-1]
            
            # swap temp_val w/ len(arr) - i, len(arr) - i
            matrix[len(matrix) -i-1][len(matrix) -i-1], temp_val = temp_val, matrix[len(matrix) -i-1][len(matrix) -i-1]
            
            # swap temp_val w/ len(arr) - i, 0 + i
            matrix[len(matrix) -i-1][i], temp_val = temp_val, matrix[len(matrix) -i-1][i]
            
            # swap temp_val w/ 0 + i, 0 + i
            matrix[i][i], temp_val = temp_val, matrix[i][i]

        i += 1
    return matrix

test_matrix = [ [0,1,2], [3,4,5], [6,7,8]]
# print(rotate_matrix(test_matrix))
test_matrix2 = [ [0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15]]
# print(rotate_matrix(test_matrix2))


print("QUESTION 1.8")
# Zero Matrix: Write an algorithm such that if an 
# element in an MxN matrix is 0, its entire row 
# and column are set to 0.
# Hints:#17, #74, #702
def zero_matrix(matrix):
    zero_array = []
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[0]):
            if matrix[i][j] == 0:
                zero_array.append((i,j))
            j += 1
        i += 1
    for zero_element in zero_array:
        i = zero_element[0]
        j = zero_element[1]
        set_column(matrix, i)
        set_row(matrix,j)
    
        
def set_column(matrix, col):
    k = len(matrix) - 1
    while k >= 0:
        matrix[col][k] = 0
        k -= 1

def set_row(matrix, row):
    k = len(matrix[0]) - 1
    while k >= 0:
        matrix[k][row] = 0
        k -= 1

# matrix1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [0,14,15,16]]
# zero_matrix(matrix1)
# print(matrix1)

# matrix2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,0,15,16]]
# zero_matrix(matrix2)
# print(matrix2)

# matrix3 = [[1,2,3,4], [5,0,7,8], [9,10,11,12], [13,14,15,16]]
# zero_matrix(matrix3)
# print(matrix3)

# matrix4 = [[0,2,3,4], [5,0,7,8], [9,10,11,12], [13,14,15,16]]
# zero_matrix(matrix4)
# print(matrix4)

print("QUESTION 1.9")
# String Rotation: Assume you have a method is Substring which checks 
# if one word is a substring of another. 
# Given two strings, sl and s2, write code to check if s2 is a 
# rotation of sl using only one call to isSubstring
#  (e.g.,"waterbottle" is a rotation of"erbottlewat").
# Chapter 1 I Arrays and Strings
# Hints:#34,#88, #704
def is_substring(s1,s2):
    if len(s1) != len(s2):
        return False
    i = 0
    while i < len(s1):
        if s1[i:] + s1[:i] == s2:
            return True
        i += 1
    return False

print(f"{is_substring('waterbottle', 'erbottlewat')} == True")
print(f"{is_substring("waterbottle", "erbottlewa")} == False")


