
students = []

def add_students():
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        name = input("Full name: ")
        section = input("Section: ")
        grades = {}
        for subject in ["Spanish", "English", "Social Studies", "Science"]:
            while True:
                try:
                    grade = float(input(f"Grade for {subject}: "))
                    if 0 <= grade <= 100:
                        grades[subject] = grade
                        break
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")
        students.append({"name": name, "section": section, **grades})

def view_students():
    if not students:
        print("No students registered.")
        return
    for student in students:
        print(student)

def view_top_3():
    if len(students) < 3:
        print("Not enough students registered.")
        return
    top_students = sorted(students, key=lambda x: sum(x[subj] for subj in ["Spanish", "English", "Social Studies", "Science"]) / 4, reverse=True)[:3]
    for student in top_students:
        print(student)

def calculate_overall_average():
    if not students:
        print("No students registered.")
        return
    overall_average = sum(sum(student[subj] for subj in ["Spanish", "English", "Social Studies", "Science"]) / 4 for student in students) / len(students)
    print(f"Overall average: {overall_average:.2f}")