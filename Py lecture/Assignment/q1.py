#write a program to read a file and findhow many vowels are present in the content.
file = open(r'd:\college\Py lecture\Assignment\file.txt', 'r')
content = file.read()

count = 0
for ch in content:
    if ch.lower() in 'aeiou':
        count += 1
file.close()
print("Total vowels:", count)