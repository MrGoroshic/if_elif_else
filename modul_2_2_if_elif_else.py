print("Введи 3 числа")
first = input()
second = input()
third = input()

if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
elif first != second != third:
    print(0)