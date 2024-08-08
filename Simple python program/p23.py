# create a new file "practice.txt" using python. Add the following data in it:

with open("sample.txt", "r") as f:
    # f.write("hi everyone\nwe are learning file i/o\n")
    # f.write("using java.\ni like programming in java")
    data=f.read()

new_data= data.replace("java","python")

print(new_data)

with open("sample.txt","w") as f:
    f.write(new_data)

    
