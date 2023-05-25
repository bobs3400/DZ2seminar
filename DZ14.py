number = int(input("Введите целое число: "))
for i in range(1, number):
    x = 2 ** i
    if x < number:
       print(x)