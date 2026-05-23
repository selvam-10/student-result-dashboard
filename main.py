import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read dataset and combine with generated students data
data_A = pd.read_csv("Student.csv")
data_B = pd.read_csv("generated_students.csv")
data = pd.concat([data_A, data_B], ignore_index=True)

#print the combined dataset
print("\nStudents Result Data")
print(data)

#calculate average total and sort the students based on it
data["Avg_Total"] = (((data["Maths"] + data["Physics"] + data["Chemistry"]) / 3).astype(int))

#function to assign grade based on average total
def grade(avg):
    if avg >= 90:
        return "A+"

    elif avg >= 80:
        return "A"

    elif avg >= 70:
        return "B"

    elif avg >= 60:
        return "C"

    elif avg >= 40:
        return "Pass"

    else:
        return "Fail"

#assign grade to each student based on average total
data["Grade"] = data["Avg_Total"].apply(grade)

#sort the students based on average total and separate top 3 and remaining students
top_students = data.sort_values(by = "Avg_Total", ascending=False)

#separate top 3 students and remaining students
top_3 = top_students.head(3)

#print the top 3 students with their details
for i in range(3):
    print("\nTop Student", i+1)
    print("Name:", top_3["Name"].values[i])
    print("Maths:", top_3["Maths"].values[i])
    print("Physics:", top_3["Physics"].values[i])
    print("Chemistry:", top_3["Chemistry"].values[i])
    print("\nAverage Total:", top_3["Avg_Total"].values[i])


#print the remaining students with their details
remaining_students = top_students.iloc[3:]

print("\nRemaining Students")
print(remaining_students[["Name", "Avg_Total", "Grade"]].to_string(index=False))

#visualize the top 3 students using a bar chart
plt.bar(
    top_3["Name"],
    top_3["Avg_Total"]
)

plt.xlabel("Top Students")
plt.ylabel("Average Marks")
plt.title("Top 3 Students")
plt.show()


# visualize the average marks distribution using a histogram
plt.hist(data["Avg_Total"])

plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.title("Average Marks Distribution")

plt.show()

#visualize the pass vs fail distribution using a pie chart
result_count = data["Grade"].apply(lambda x: "Fail" if x == "Fail" else "Pass").value_counts()
plt.pie(result_count.values,labels=result_count.index,autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()

#save the final report to a csv file
data.to_csv("final_student_report.csv",index=False)