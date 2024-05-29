def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True

if __name__ == "__main__":
    test_string = input("Enter a string to check if it is a palindrome: ")

    if is_palindrome(test_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
