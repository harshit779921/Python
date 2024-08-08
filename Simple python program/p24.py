def check_for_word():
    with open("sample.txt", "r") as f:
       data = f.read()
    if (data.find("learning")!=-1):
        print("found")
    else:
        print("not found")

check_for_word()