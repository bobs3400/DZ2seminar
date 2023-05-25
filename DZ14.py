number = int(input("Введите целое число: "))
for i in range(0, number):
    x = 2 ** i
    if x <= number:
       print(x)