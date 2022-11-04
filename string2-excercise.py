#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    if len(s) >= 3:
        if s.find("ing") and s.find("ing") != -1:
            # print("ing found", s)
            return s + "ly"
        else:
            return s + "ing"
    else:
        return s


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
# def not_bad(s):
#   li = list(s.split(" "))
#  for n in range(len(li)):
#     if li[n:] == "not":
#        print(li[n:])


# not_bad("movie was not so bad!")
def not_bad(s):
    not_index = s.find("not")
    bad_index = s.find("bad")
    if bad_index > not_index:
        string2 = s[0:not_index] + "good" + s[bad_index + 3 :]
        return string2
    else:
        return s


# print(not_bad("i am not a girl bad bitch for you"))


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    x = int((len(a) / 2))
    if len(a) % 2 == 0:
        front_1 = a[0:x]
        back_1 = a[x:]
    else:
        front_1 = a[0 : x + 1]
        back_1 = a[x + 1 :]
    y = int((len(b) / 2))
    if len(b) % 2 == 0:
        front_2 = b[0:y]
        back_2 = b[y:]
    else:
        front_2 = b[0 : y + 1]
        back_2 = b[y + 1 :]
    # print(
    #   "front_1=", front_1, "front_2=", front_2, "back_1=", back_1, "back_2=", back_2
    # )
    return front_1 + front_2 + back_1 + back_2


# print(front_back("abcd","xy"))


# print(front_back("axbx","abcde"))


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print("%s got: %s expected: %s" % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print("verbing")
    test(verbing("hail"), "hailing")
    test(verbing("swiming"), "swimingly")
    test(verbing("do"), "do")

    print
    print("not_bad")
    test(not_bad("This movie is not so bad"), "This movie is good")
    test(not_bad("This dinner is not that bad!"), "This dinner is good!")
    test(not_bad("This tea is not hot"), "This tea is not hot")
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print("front_back")
    test(front_back("abcd", "xy"), "abxcdy")
    test(front_back("abcde", "xyz"), "abcxydez")
    test(front_back("Kitten", "Donut"), "KitDontenut")


if __name__ == "__main__":
    main()
