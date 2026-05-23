import pandas as pd
import random

students = []
names = ["Vijay","Meena","Ravi","Divya","Suresh","Lakshmi","Manoj","Keerthi","Bala","Nisha",
        "Hari","Pooja","Gokul","Sneha","Raj","Deepa","Karthik","Swathi","Ajith","Gayathri"]
selected_names = random.sample(names, 20)

for names in selected_names:
    student = {
        "Name": names,
        "Maths": random.randint(30, 100),
        "Physics": random.randint(30, 100),
        "Chemistry": random.randint(30, 100)   
    }
    students.append(student)
data = pd.DataFrame(students)

print(data.to_string(index=False))

data.to_csv("generated_students.csv", index=False)