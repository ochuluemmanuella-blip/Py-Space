num = set([1, 2, 2, 3, 4, 4, 5])
print(num)

python_fans = {"Ann", "Bo", "Cy"}
go_fans = {"Bo", "Dee", "Cy"}



both_lang =  python_fans & go_fans
everyone =python_fans | go_fans
only_python = python_fans - go_fans

print(both_lang)
print(only_python)
print(everyone)

