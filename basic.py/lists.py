nums = [5, 3, 8, 1]
nums.append(10)
nums.insert(0, 0)
nums.sort()
last = nums.pop()
doubled_nums= [num * 2 for num in nums]
print(doubled_nums)
