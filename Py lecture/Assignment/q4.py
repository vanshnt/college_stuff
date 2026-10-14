#read a file.split its content into words and store them in a list.
# I. Print the total number of words.
# II.Print all unique words.


with open(r'd:\college\Py lecture\Assignment\file.txt', 'r') as file:
    content = file.read()

words = content.split()

# I. Print total number of words
print("Total number of words:", len(words))

# II. Print all unique words
unique_words = set(words)
print("Unique words:", unique_words)
