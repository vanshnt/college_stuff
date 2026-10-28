# C. String Programs
# 13. Reverse a string without using a built-in reverse function.

str = "abcd"

for i in range(len(str)-1, -1, -1):
    print(str[i], end ="")

# 14. Check whether a string is a palindrome.
print("")
test = "eve"

if test == test[::-1]:
    print("is palindrome")
else:
    print("not")
    
    
# 15. Count vowels and consonants in a string.

test = "udhauidnaa"
count = 0
for i in test.lower():
    if i in "aeiou":
        count +=1
print(count)
        
# 16. Count how many times a character occurs in a string.

test = "yeiwuieuwiwuieuwiu"
count = 0
for i in test.lower():
    if i in "i":
        count+=1
        
print(count)

# 17. Count words in a sentence.



def count(a):
    words = a.split()
    print(len(words))
count("hello this is bullshit")   

# 18. Replace spaces with hyphens and display the string in uppercase.

def modidy(s):
    s = s.replace(" ", "-")
    print(s.upper())
    
modidy("Jaajaja that shit is funny")