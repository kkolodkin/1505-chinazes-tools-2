import random
n = int(input())
q = input().split()
for i in range(n):
    print(random.randint(int(q[0]), int(q[1])))
