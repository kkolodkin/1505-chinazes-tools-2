import random
n = 'qwertyuiopASDFGHJKLzxcvbnm,'
d = '(!@#$%^&*()_+{}:<>?,./;~'


def zxc1(spec, large):
    password = ''
    if spec == 'Да':
        if large%2!=0:
            for i in range(large//2):
                e = random.randint(1, len(n)-1)
                l = random.randint(1, len(d)-1)
                password += n[e]
                password += d[l]
        else:
            for i in range(large//2):
                e = random.randint(1, len(n)-1)
                l = random.randint(1, len(d)-1)
                password += n[e]
                password += d[l]
    else:
        for i in range(large):
            e = random.randint(1, len(n)-1)
            password += n[e]
    return password
asd = int(input('Введите длину пароля'))
zxc = input('Нужны ли специальные символы(Да/Нет)')

print(f'Ваш пароль {zxc1(zxc, asd)}')


        

#ilovegitoo
