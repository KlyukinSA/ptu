import random, math, sys
n = int(sys.argv[1] or 8)
used1 = set()
used2 = set()
print("s la lb da db")
for i in range(n):
    v1=n
    while v1 in used1 or v1 == n:
        v1=math.floor(random.random() * n)
    used1.add(v1)
    v2=n
    while v2 in used2 or v2 == n:
        v2=math.floor(random.random() * n)
    used2.add(v2)
    o1=2
    while o1 == 2:
        o1=math.floor(random.random() * 2)
    o2=2
    while o2 == 2:
        o2=math.floor(random.random() * 2)
    print(i+1, o1+1, o2+1, v1+1, v2+1)
    
