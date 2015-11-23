__author__ = 'JamesWaller'
#---------- Python Warmup-1 -----------#

# CodingBat - Warmup-1 - Sleep_in
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
def sleep_in(weekday, vacation):
    if vacation:
        return True
    if not weekday:
        return True
    return False;



# CodingBat - Warmup-1 - Monkey_Trouble
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile



# CodingBat - Warmup-1 - Sum_Double
# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
def sum_double(a, b):
    if a == b:
        return 2*(a + b)
    return a + b



# CodingBat - Warmup-1 - Diff21
# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
def diff21(n):
    if n > 21:
        return 2*abs(n - 21)
    return abs(n - 21)



# CodingBat - Warmup-1 - Parrot_Trouble
# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
def parrot_trouble(talking, hour):
    if (hour < 7 or hour > 20) and talking:
        return True
    return False



# CodingBat - Warmup-1 - Makes10
# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(a, b):
    if a == 10 or b == 10:
        return True
    if a + b == 10:
        return True
    return False



# CodingBat - Warmup-1 - Near_Hundred
# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
    if abs(100 - abs(n)) <= 10:
        return True
    if abs(200 - abs(n)) <= 10:
        return True
    return False



# CodingBat - Warmup-1 - Pos_Neg
# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
    if negative:
        if a < 0 and b < 0:
            return True
        else:
            return False
    return (a < 0 and b > 0) or (a > 0 and b < 0)



# CodingBat - Warmup-1 - Not_String
# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.
def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        return str
    return "not " + str



# CodingBat - Warmup-1 - Missing_Char
# Given a non-empty string and an int n, return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(str, n):
    return str[:n] + str[(n + 1):]



# CodingBat - Warmup-1 - Front_Back
# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
    if len(str) == 1 or len(str) == 0:
        return str;
    firstLetter = str[0]
    lastLetter = str[len(str) - 1]
    base = str[1:len(str) - 1]
    return lastLetter + base + firstLetter



# CodingBat - Warmup-1 - Front3
# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
def front3(str):
    firstThree = str[0:3]
    return firstThree * 3



#---------- Python Warmup-2 -----------#

# CodingBat - Warmup-2 - String_Times
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
    return n * str



# CodingBat - Warmup-2 - Front_Times
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def front_times(str, n):
    if len(str) <= 3:
        return n * str;
    return n * str[:3]



# CodingBat - Warmup-2 - String_bits
# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
    result = ""
    for i in xrange(len(str)):
        if i % 2 == 0:
            result += str[i]
    return result



# CodingBat - Warmup-2 - String_Splosion
# Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
    result = ""
    for i in xrange(len(str) + 1):
        result += str[:i]
    return result

# CodingBat - Warmup-2 - Last2
# Given a string, return the count of the number of times that a substring length 2 appears in the string
# and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
    if len(str) <= 2:
        return 0
    lastTwo = str[(len(str) - 2):]
    count = 0;
    for i in xrange(len(str) - 2):
        if str[i:(i + 2)] == lastTwo:
            count += 1
    return count



# CodingBat - Warmup-2 - Array_Count9
# Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
    count = 0
    for i in xrange(len(nums)):
        if nums[i] == 9:
            count += 1
    return count



# CodingBat - Warmup-2 - Array_Front9
# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
def array_front9(nums):
    if (len(nums) < 4):
        for i in xrange(len(nums)):
            if nums[i] == 9:
                return True
    else:
        for i in xrange(3):
            if nums[i] == 9:
                return True
    return False



# CodingBat - Warmup-2 - Array123
# Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.
def array123(nums):
    for i in xrange(len(nums) - 2):
        if (nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3):
            return True
    return False



# CodingBat - Warmup-2 - String_Match
# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
def string_match(a, b):
    smaller = 0
    count = 0
    if len(a) <= len(b):
        smaller = len(a)
    else:
        smaller = len(b)
    for i in xrange(smaller - 1):
        if (a[i:(i + 2)] == b[i:(i + 2)]):
            count += 1
    return count