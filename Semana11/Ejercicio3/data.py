from actions import students_list
from Students import Students # Importamos la lista 'students' desde actions.py
import csv

def export_to_csv():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "section", "Spanish", "English", "Social Studies", "Science"])
        for student in students_list:
            writer.writerow([student.name, student.section, student.spanish, student.english, student.social_studies, student.science])
    print("Data successfully exported.")

def import_from_csv():
    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)
            students_list.clear()
            for row in reader:
                student = Students(
                row["name"],
                row["section"],
                float(row["Spanish"]),
                float(row["English"]),
                float(row["Social Studies"]),
                float(row["Science"])
                )
            students_list.append(student)
        print("Data successfully imported.")
    except FileNotFoundError:
        print("Not previously exported CSV file found.")