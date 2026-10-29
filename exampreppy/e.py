# 26. Write a function to check whether a number is prime.

def check(n):
    if n<2:
        print("Number is too small")
    else:
        isprime = True
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                isprime = False
        if isprime:
            print("Number is prime")
        else:
            print("Number is not prime")
check(5)
check(55)
check(35)
check(37)


# #27. Write a function with a default parameter value for a student's name.

def greet(name = "student"):
    print("hello", name)
    
greet()
greet("ATharv")

# # 28. Demonstrate positional and keyword arguments using a function.

def summ(a,b, c):
    print("C", c)
    print(a+b)
    
# sum(1, 2)

summ(a = 10,c = 33, b = 20)


# 29. Accept any number of positional arguments using *args and return their sum


def total(*args):
    return sum(args)

print(total(1, 2, 3, 4, 5))

# # 30. Accept keyword arguments using **kwargs and display them

def names(**kwargs):
    print(kwargs)

names(Atharv = 21, Vansh =23);
    
    
    