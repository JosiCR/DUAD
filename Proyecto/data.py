from actions import students  # Importamos la lista 'students' desde actions.py
import csv

def export_to_csv():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "section", "Spanish", "English", "Social Studies", "Science"])
        for student in students:
            writer.writerow([student["name"], student["section"], student["Spanish"], student["English"], student["Social Studies"], student["Science"]])
    print("Data successfully exported.")

def import_from_csv():
    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)
            students.clear()
            new_students = []
            for row in reader:
                row["Spanish"] = float(row["Spanish"])
                row["English"] = float(row["English"])
                row["Social Studies"] = float(row["Social Studies"])
                row["Science"] = float(row["Science"])
                new_students.append(row)
        students.extend(new_students)
        print("Data successfully imported.")
    except FileNotFoundError:
        print("No previously exported CSV file found.")