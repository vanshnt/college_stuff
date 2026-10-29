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


# Nested dictionary

# Given a dictionary containing student names and their subject-wise marks, 
# write a program to calculate and display each student's average marks.

print("")
print("")
students = {
    "Vansh": {"Python": 80, "SQL": 90, "DSA": 70},
    "Atharv": {"Python": 85, "SQL": 75, "DSA": 95},
    "Ishh": {"Python": 90, "SQL": 88, "DSA": 82}
}

for names, subjects in students.items():
    total = 0
    for marks in subjects.values():
        total+= marks
        
    avg = total/3
    print(names, avg)

    


# Q1. Easy–Moderate: Total marks
students = {    "A": {"Python": 80, "SQL": 70},    "B": {"Python": 90, "SQL": 85},    "C": {"Python": 60, "SQL": 75}}
highest = 0
topper = None
for names, subjects in students.items():
    total = 0
    
    for marks in subjects.values():
        total += marks
        
    print(names, total)
    
    if total> highest:
        highest = total
        topper = names
        
print(topper, highest)
    

# Q2. Moderate: Highest scorer
# Using the same dictionary, print the name of the student with the highest total marks.
    