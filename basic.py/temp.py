def celsius_to_Fahrenheit(value):
    result = value * 9/5 + (32)
    return result

val = celsius_to_Fahrenheit(37.8)
print(f"{val}F")


def Fahrenheit_to_celsuis(number):
    res = (number - 32) * 5/9
    return res

answer = Fahrenheit_to_celsuis(100)
resul = round(answer, 1)
print(f"{resul}C")
