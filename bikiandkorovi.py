
import random

def generate_secret_number():
   
    while True:
        number =str(random.randint(1000, 9999))
        if len(set(number))==4:
            return number

def bulls_and_cows(secret_number, guess):
   
    bulls=0
    cows=0
    for i in range(4):
        if guess[i] == secret_number[i]:
            bulls +=1
        elif guess[i] in secret_number:
            cows +=1
    return bulls, cows

def play_game():
    
    secret_number=generate_secret_number()
    attempts=0
    
    print("вы зашли  в игру \"Быки и Коровы\"")
    print("Я загадал 4-значное число без повторяющихся цифр. Попробуйте угадать эти числа.")
    
    while True:
        guess = input("Введите ваши цифры (4 цифры): ")
        attempts += 1

        if len(guess) !=4 or not guess.isdigit() or len(set(guess)) !=4:
            print("неправильный ввод. Пожалуйста, введите 4 разные цифры.")
            continue
            
        bulls, cows =bulls_and_cows(secret_number, guess)
        
        if bulls==4:
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
            break
        else:
            print(f"Результат: {bulls} быка(ов), {cows} корова(ы). Попробуйте ещё раз.")

play_game()

#Тестирование прошло успешно
