import random

left = random.randrange(2, 21)
print(f'Шифр в левой части: {left}')
psswrd = []
for i in range(1, left):
    for j in range(i + 1, left):
        if left % (i + j) == 0 and i < j:
            psswrd.append(i)
            psswrd.append(j)
#            psswrd.append("|")
print(f'Ответ при заданном в левой части числе "{left}" будет: ')
#print(psswrd)
print(*psswrd, sep = "")
