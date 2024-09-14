i = 1
while i <= 10:
    print(i)
    i += 1

n = int(input("Son kiriting: "))
while n >= 1:
    print(n)
    n -= 1
    
m = int(input("Son kiriting: "))
total = 0
i = 1
while i <= m:
    total += i
    i += 1
print("Yig'indisi:", total)

hzor = 0
while True:
    l = int(input("Son kiriting: "))
    if l == 0:
        break
    hzor += l
print("Yig'indi:", hzor)


