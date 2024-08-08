# Find string is palindrome or not

n = input()

rev = ""
for char in n:
    rev = char + rev

if n == rev:
    print("Yes, string is palindrome")

else:
    print("No, string is not palindrome")
