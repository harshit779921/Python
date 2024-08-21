#  Data Frames in Pandas

import pandas as pd

student_details = [(1, "Harshit", "male", "Gurugram"),
      (2, "Arpit", "male", "UP"),
      (3, "Shivangi", "female", "Kamsar"),
      (4, "Chunnilal", "Other", "Gaya")]

df = pd.DataFrame(student_details,columns=["std_ID","Name","Gender","City"])
print(df)

df.set_index("std_ID", inplace = True)
print(df)

df.to_csv("Student.csv", index = True)