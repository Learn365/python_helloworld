def reverse(text):
    return text[::-1]


def is_plindrome(text):
    return text == reverse(text)


something = input("Enter Text: ")
if is_plindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
