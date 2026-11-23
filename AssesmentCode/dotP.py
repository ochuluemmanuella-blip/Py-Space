def dot_product(a, b):
    result = 0
    if len(a) != len(b):
        raise ValueError("length of vectors not equal")
    for i in range(len(a)):
        result += a[i]*b[i]
    return result
a = [1, 2, 3]
b =[4, 5]
print(dot_product(a, b))