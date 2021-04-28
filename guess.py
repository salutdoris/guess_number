import random
r = random.randint(1,100) # random integer
count = 0

while True: 
    count += 1
    a = input('請輸入數字(整數):')
    a = int(a)
    if a == r:
        print('猜對了!')
        break
    elif a > r:
        print('數字要小一點')
    elif a < r:
        print('數字要大一點')
    print('你已嘗試', count, '次')

