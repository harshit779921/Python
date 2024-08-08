# Encode & Decode a String

alphabets = "abcdefghijklmnopqrstuvwxyz"
encode = "defg"
decode = " "
for i in range(len(encode)):
    decode += alphabets[(alphabets.index(encode[i]) - 3) % 26]
print("Message is :",decode)

# if ypu want to make it the decode then its simple jus add +3