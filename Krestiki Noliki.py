import random
c1 = ['*', '|', '*', '|', '*']
c2 = ['*', '|', '*', '|', '*']
c3 = ['*', '|', '*', '|', '*']
start = True
def hod(x1, y1):
    if y1 == 1:
        if x1==1:
            c1[0]='0'
        elif x1 == 2:
            c1[2]='0'
        elif x1 == 3:
            c1[4]='0'
    elif y1 == 2:
        if x1==1:
            c2[0]='0'
        elif x1 == 2:
            c2[2]='0'
        elif x1 == 3:
            c2[4]='0'
    elif y1 == 3:
        if x1==1:
            c3[0]='0'
        elif x1 == 2:
            c3[2]='0'
        elif x1 == 3:
            c3[4]='0'

def hod2(x1, y1):
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    a = 0
    if x1 == x and y1 == y:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
    while a ==0:
        if y == 1:
            if x == 1 and c1[0]!='0':
                c1[0]='X'
                a=1
            elif x == 2  and c1[2]!='0':
                c1[2]='X'   
                a=1
            elif x ==3 and c1[4]!='0':
                c1[4] = 'X'
                a=1
        elif y ==2:
            if x == 1 and c2[0]!='0':
                c2[0]='X'
                a=1
            elif x == 2 and c2[2]!='0':
                c2[2]='X'
                
                a=1
            elif x ==3 and c2[4]!='0':
                c2[4] = 'X'
                a=1
        elif y == 3:
            if x == 1  and c3[0]!='0':
                c3[0]='X'
                a=1
            elif x == 2 and c3[2]!='0':
                c3[2]='X'
                a=1
            elif x ==3  and c3[4]!='0':
                c3[4] = 'X'
                a=1    
        else:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            if y == 1:
                if x == 1 and c1[0]!='0':
                    c1[0]='X'
                    a=1
                elif x == 2  and c1[2]!='0':
                    c1[2]='X'
                    a=1
                elif x ==3 and c1[4]!='0':
                    c1[4] = 'X'
                    a=1
            elif y ==2:
                if x == 1 and c2[0]!='0':
                    c2[0]='X'
                    a=1
                elif x == 2 and c2[2]!='0':
                    c2[2]='X'
                    a=1
                elif x ==3 and c2[4]!='0':
                    c2[4] = 'X'
                    a=1
            elif y == 3:
                if x == 1  and c3[0]!='0':
                    c3[0]='X'
                    a=1
                elif x == 2 and c3[2]!='0':
                    c3[2]='X'
                    a=1
                elif x ==3  and c3[4]!='0':
                    c3[4] = 'X'
                    a=1
    print(c1)
    print(c2)
    print(c3)


            
while start:
    if c1[0]==c1[2]==c1[4]=='X' or c2[0]==c2[2]==c2[4]=='X' or c3[0]==c3[2]==c3[4]=='X' or c1[0]==c2[0]==c3[0]=='X' or c1[2]==c2[2]==c3[2]=='X' or c1[4]==c2[4]==c3[4]=='X' or c1[0]==c2[2]==c3[4]=='X' or c1[4]==c2[2]==c3[0]=='X':
        print('Поражание')
        start = False
    elif c1[0]==c1[2]==c1[4]=='0' or c2[0]==c2[2]==c2[4]=='0' or c3[0]==c3[2]==c3[4]=='0' or c1[0]==c2[0]==c3[0]=='0' or c1[2]==c2[2]==c3[2]=='0' or c1[4]==c2[4]==c3[4]=='0' or c1[0]==c2[2]==c3[4]=='0' or c1[4]==c2[2]==c3[0]=='0':
        print('Победа')
        start = False
    else:
        y1 = int(input('Выберите строчку'))
        x1 = int(input('Выберите столбик'))
        hod(x1, y1)
        hod2(x1, y1)

        
    
