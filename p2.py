# Given string
word = "Programming"
print(word[::-1])
print(word[:3], word[-3:])
print(word.count('m'))
def check_palindrome(s):
    return s == s[::-1]
print(check_palindrome("level"), check_palindrome("python"))