#Creating Our Dataset


import pandas as pd

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Exam_Score": [42, 45, 51, 55, 61, 66, 72, 78, 85, 91]
}

df = pd.DataFrame(data)

print(df)
