def is_palindrome(string):
    # '//' means rounds down to nearest whole number
    for index in range(len(string) // 2):
        if string[index] != string[len(string) - index - 1]:
            return False
    return True


print(is_palindrome('abcdeedcba'))
print(is_palindrome('pythonpython'))
print(is_palindrome('java'))
