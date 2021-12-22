import random
random_value = random.randint(0,20)
attempt = 0
print("Загадано число от 0 до 20. Попробуйте отгадать за 10 попыток")
for i in range(1,11):
    choice = int(input("Введите число: "))
    if choice > random_value:
        print("Многовато будет")
    elif choice < random_value:
        print("Маловато будет")
    else:
        print(f"ВЫ угодали! Осталось количество попыток - {i}")
        break
    attempt += 1
    print(f"Осталось попыток {10-attempt}")
if attempt >= 10:
    print(f"Попытки закончились! Было загадано {random_value}")
