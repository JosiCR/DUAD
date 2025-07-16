
from actions import add_students, view_students, view_top_3, calculate_overall_average
from data import export_to_csv, import_from_csv

def show_menu():
    options = {
        "1": add_students,
        "2": view_students,
        "3": view_top_3,
        "4": calculate_overall_average,
        "5": export_to_csv,
        "6": import_from_csv
    }
    while True:
        print("""
        1. Add students
        2. View students
        3. View top 3 students
        4. View overall average
        5. Export data to CSV
        6. Import data from CSV
        7. Exit
        """)
        choice = input("Select an option: ")
        if choice == "7":
            print("Exiting program...")
            break
        elif choice in options:
            options[choice]()
        else:
            print("Invalid option. Please try again.")
