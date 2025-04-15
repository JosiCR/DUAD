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
            global students
            students = [
                {"name": row["name"], "section": row["section"], "Spanish": float(row["Spanish"]), "English": float(row["English"]), "Social Studies": float(row["Social Studies"]), "Science": float(row["Science"])}
                for row in reader
            ]
        print("Data successfully imported.")
    except FileNotFoundError:
        print("No previously exported CSV file found.")