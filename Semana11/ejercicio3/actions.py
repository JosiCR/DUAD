from Students import Students

students_list = []

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
        student = Students(name, section, grades["Spanish"], grades["English"], grades["Social Studies"], grades["Science"])
        students_list.append(student)

def view_students():
    if not students_list:
        print("No students registered.")
        return
    for s in students_list:
        print(f"Name: {s.name}, Section: {s.section}, Spanish: {s.spanish}, English: {s.english}, Social Studies: {s.social_studies}, Science: {s.science}")

def view_top_3():
    if len(students_list) < 3:
        print("Not enough students registered.")
        return
    
    top_students = sorted(students_list, key=lambda s: s.average(), reverse=True)[:3]
    for s in top_students:
        print(f"Name: {s.name}, Average: {s.average():.2f}")

def calculate_overall_average():
    if not students_list:
        print("No students registered.")
        return
    overall_average = sum(s.average() for s in students_list) / len(students_list)
    print(f"Overall average: {overall_average:.2f}")