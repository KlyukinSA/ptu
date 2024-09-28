t2 = [46, 29, 8]
t3 = [98, 149, 123]      
t4 = [1859, 1754, 1769]
t5 = [46716, 46701, 46937]

t = [t2, t3, t4, t5]
avs = []
print('average')
for ti in t:
    av = int(sum(ti) / len(t2))
    avs.append(av)
    print(av)

N = 26
print('~ speed')
sps = []
for i, K in enumerate([2, 3, 4, 5]):
    S = N**K / avs[i]
    sps.append(S)
    print(K, avs[i], S)

futsp = sps[-1]

for i in [6, 7, 8]:
    T = N**i/futsp
    print(i, T, T / 3600_000)

print('report')
for av in avs:
    print(av)
print(futsp)
print(N**8 / futsp / 3600_000)
