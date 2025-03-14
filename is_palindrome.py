import re

def is_palindrome(s: str) -> bool:
    # Convert string to lowercase and remove non-alphanumeric characters
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]

# Test cases
def test_is_palindrome():
    # Basic tests
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    
    # Test with spaces and mixed case
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("No lemon no melon") == True
    
    # Edge cases
    assert is_palindrome("Madam, I'm Adam") == True  # Handles punctuation
    assert is_palindrome("12321") == True  # Numeric palindrome
    assert is_palindrome("Hello, world!") == False  # With punctuation
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Single space

    print("All tests passed!")

# Run tests
test_is_palindrome()
