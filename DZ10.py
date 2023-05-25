from random import randint
num_coin = int(input("Введите количество монеток: "))
i = 0
arrival = ""
sum = 0
while i < num_coin:
    coin = randint(0, 1)
    sum = sum + coin
    arrival = arrival + str(coin)
    i += 1
print(arrival)
if sum > num_coin // 2:
    print("Необходимо перевернуть ", num_coin - sum)
else:
    print("Необходимо перевернуть ", sum)
