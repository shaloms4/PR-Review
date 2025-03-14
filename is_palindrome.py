def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.
    
    :param s: Input string
    :return: True if s is a palindrome, False otherwise
    """
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

# Test Cases
def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("No lemon no melon") == True
    assert is_palindrome("Was it a car or a cat I saw") == True

test_is_palindrome()
print("All tests passed!")
