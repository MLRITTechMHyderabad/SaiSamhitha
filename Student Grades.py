x=int(input("enter no of students"))
students={}
for i in range(x):
    name = input("Enter name")
    grades = list(map(int, input("Enter grades ").split()))
    students[name] = grades
    avg_grades = {name: sum(grades) / len(grades) for name, grades in students.items()}
    top_student = max(avg_grades, key=avg_grades.get)
    passed_students = sum(1 for avg in avg_grades.values() if avg >= 50)

print("Student Grades:", students)
print("Average Grades:", avg_grades)
print("Top Student:", top_student)
print("Number of Students Passed:", passed_students)
