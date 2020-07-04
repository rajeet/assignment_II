# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.



def is_palindrome(str):
    reversed_str = "".join(reversed(str))
    print(reversed_str)
    if str.lower() == reversed_str.lower():
        return "The passed string is palindrome"
    else:
        return "The passed string is not palindrome"

print(is_palindrome("cat"))
