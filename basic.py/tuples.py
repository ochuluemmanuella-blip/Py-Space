person = ("Ada", 36, "London")
a, b, c = person
#person[1] = 40
print(person)
def stats(nums):
    total = sum(nums)
    count = len(nums)
    average = total / count
    return total, average

total, average =stats([10, 20, 30])
print(total)
print(average)