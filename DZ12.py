sum = int(input("Введите сумма двух чисел: "))
compos = int(input("Введите произведение двух чисел: "))
mean = False
for x in range(1, 1000):
    for y in range(1, 1000):
        if sum == x + y and compos == x * y:
            mean = True
            print(x, y)
if mean == False:
    print("Нет таких чисел")   