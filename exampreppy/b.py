
# B. Conditions and Loops
# 5. Check whether a number is even or odd.

def Chk(a):
    if a%2 == 0:
        print(a, " is even")
    else:
        print(a, " is odd")
    
Chk(3)
Chk(4)

# 6. Find the largest of three numbers.

def larg(a,b,c):
    largest = a
    if a<b:
        largest = b
        if b<c:
            largest = c
    return largest
print(larg(4, 6, 9))
print(larg(499, 67, 9))


# 7. Check whether a year is a leap year.

def year(year):
    if (year%400 == 0) or year%4 == 0 and year % 100 != 0:
        print(year, " is a leap year")
    else:
        print(year, " is not a leap year")
        
year(1993)
year(2016)


# 8. Find the factorial of a number using a loop.

def fact(num):
    a = 1
    for i in range(1, num+1):
        a *= i
    return a

print(fact(3))
print(fact(4))


# 9. Print the multiplication table of a number.

def multi(a):
    for i in range(1, 11):
        print(a, " x ", i, " = ", i*a)
        
multi(5)

# 10. Find the sum of digits of a number.

def summ(a):
    b = str(a)
    total = 0
    for digit in b:
        total += int(digit)
    return total

print(summ(583))

print("")
print("")
print("")

# 11. Check whether a number is prime.

def isprime(a):
    if a<2:
        return False
    else:
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                return False
        return True
print(isprime(5))
print(isprime(65))
# 12. Print a number pattern using nested loops

n = 5

for i in range(n, 0, -1):
    print(" " * (n-i) + "*" * (2* i -1))
    
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
    
    
    
