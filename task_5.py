import pandas as pd


df = pd.read_json('students.json')
df["passed"] = df["score"] >= 60
max_stud = df.loc[df["score"].idxmax()]
print('Лучший студент')
print(max_stud)
df.to_json('new_students.json', orient='records')
