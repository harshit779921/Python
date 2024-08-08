def find_line_word():
    # word = "learning"
    data = True
    line_no = 1
    with open("sample.txt", "r") as f:
        while data:
            data = f.readline()
            if "python" in data:
                print(line_no)
                return
            line_no += 1

    return -1


find_line_word()
