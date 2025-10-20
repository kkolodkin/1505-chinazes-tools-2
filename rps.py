import random

def errors(user_choice):
    a = user_choice.lower()
    if a == 'пока':
        return 'До свидания'
    if a not in ['камень', 'ножницы', 'бумага']:
        return 'В следующий раз введите либо камень, либо ножницы, либо бумагу'
    else:
        return None
    
rps = ['камень', 'ножницы', 'бумага']
comp_choice = random.choice(rps)
user_choice = input('Камень, ножницы или бумага? (Если хотите закончить игру введите "Пока")')


if errors(user_choice) is None:
    if comp_choice == user_choice.lower():
        print(comp_choice)
        print('Ничья')
    elif comp_choice == 'камень' and user_choice.lower() == 'ножницы' or comp_choice == 'ножницы' and user_choice.lower() == 'бумага' or comp_choice == 'бумага' and user_choice.lower() == 'камень':
        print(comp_choice)
        print('Вы проиграли')
    else:
        print(comp_choice)
        print('Вы победили')
else:
     print(errors(user_choice))

#Тестирование прошло успешно
