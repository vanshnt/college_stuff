#count odd digits


n = 252321

count = 0

for i in str(n):
    if int(i) % 2 == 0:
        count += 1
print(count)