def palindrome(words):
    cleaned_word = ""
    for char in words:
        if char.isalnum():
            cleaned_word += char
            cleaned_word = cleaned_word.lower()
    left = 0
    right = len(cleaned_word)-1
    while left < right:
        if cleaned_word[left] != cleaned_word[right]:
            return False
        left += 1
        right -= 1
    return True

    
result = palindrome("madam, i'm adam")
print(result)
