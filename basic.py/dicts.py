book = {"title": "Renaissance", "author": "Stephan Reyes", "year": 2005}
book["pages"] = 412
book["year"] = 2007

print(book.get("rating", 0))
print(book)

words = ["a", "b", "a", "c", "a", "b"]
word_dict = {word: words.count(word) for word in words}
print(word_dict)