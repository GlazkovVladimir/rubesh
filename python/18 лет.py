import random
random_value = random.randint(18,18)
attempt = 0
print(":)")
for i in range(1,):
    test2word = input("Ваше имя? ")
    choice = int(input("Ваш возраст: "))
    if choice > random_value:
        print(test2word,"вам уже больше 18 лет! ")
    elif choice < random_value:
        print(test2word,"Вам ещё меньше 18 лет!")
    else:
        print(test2word,f"это хорошо что вам 18 лет;)")
        break
    
    

    
