import random
r = random.randint(1,100) # random integer

while True: 
    a = input('請輸入數字(整數):')
    a = int(a)
    if a == r:
        print('猜對了!')
        break
    elif a > r:
        print('數字要小一點')
    elif a < r:
        print('數字要大一點')


