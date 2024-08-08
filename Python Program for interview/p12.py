# Find int values from a file

total = 0

with open('Python\Python Program for interview\p12_sample.txt', "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            if word.isdigit():
                total = total + int(word)

print("The total of int in file:", total)


# if their is any negative value

# if word.lstrip('-').isdigit():  # Check if the word is a digit, ignoring the negative sign
