from random import randrange

pp = ['Глеб', 'Степан', 'Сергей', 'Дмитрий']
for p in pp:
    print(p, [randrange(2) for _ in range(8)])
