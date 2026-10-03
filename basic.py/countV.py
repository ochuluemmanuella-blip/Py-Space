
def vowel_count(text) -> int:
    tex = text.lower()
    vowels = ["a", "e", "i", "o", "u"]
    total_count = sum(tex.count(char) for char in vowels)
    return total_count 

word = vowel_count("my mothers name is TIti.")
print(word)    