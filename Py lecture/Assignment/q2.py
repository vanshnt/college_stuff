#read all lines from file into list. Print the total number of lines and display the 2nd and 4th line
with open(r'd:\college\Py lecture\Assignment\file.txt') as f:
    lines = f.readlines()

print("Total number of lines:", len(lines))
print("2nd line:", lines[1].strip())
print("4th line:", lines[3].strip())
