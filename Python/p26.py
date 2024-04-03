count=0
with open("practice.txt", "r") as f:
    # f.write("1, 2, 76, 84, 90, 101")
    data = f.read()
    print(data)

    # num = ""
    # for i in range(len(data)):
    #     if data[i] == ",":
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

    nums=data.split(",")
    for val in nums:
        if (int(val)%2==0):
            count += 1
    print("number of even value:",count)