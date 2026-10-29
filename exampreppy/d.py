# D. List and Dictionary Programs
# 19. Find the largest and smallest elements in a list.
import statistics

lis = [1, 2, 3, 4, 5, 5]
print(max(lis))
print(min(lis))
# 20. Calculate the sum and average of list elements.

print(sum(lis))
print(statistics.mean(lis))

# 21. Remove duplicate elements from a list.

liss = set(lis)
print(liss)
# 22. Count even and odd numbers in a list.

counteve = 0
countodd = 0
for i in lis:
    if lis[i] % 2==0:
        counteve+=1
    else:
        countodd += 1
        
print("Even: ", counteve)
print("odd: ", countodd)

# 23. Store student names and marks in a dictionary.

students ={
    "Vansh": 35,
    "Atharv": 45,
    "Shreyans": 40
    
}

print(students)
print(students["Vansh"])

# 24. Count the frequency of each character in a string using a dictionary.

s = "hello"
freq = {}

for i in s:
    freq[i] = freq.get(i,0)+1
    # if i in freq:
    #     freq[i]+=1
    # else:
    #     freq[i] = 1
        
print(freq)