#  Find Vowels in given string

vowel = input().lower()
vowels = ""
if "a" in vowel:
    vowels += "a "
if "e" in vowel:
    vowels += "e "
if "i" in vowel:
    vowels += "i "
if "o" in vowel:
    vowels += "o "
if "u" in vowel:
    vowels += "u "

print("These are the vowels:",vowels)
