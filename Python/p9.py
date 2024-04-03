# wap to enter marks of 3 subject from the user and store them in a dict.

marks = {}

m1 = int(input(" Enter the marks of phys:\n"))
marks.update({"phys": m1})

m2 = int(input(" Enter the marks of maths:\n"))
marks.update({"maths": m2})

m3 = int(input(" Enter the marks of chem:\n"))
marks.update({"chem": m3})

print(list(marks.items()))
