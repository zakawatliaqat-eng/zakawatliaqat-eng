import json

# File to store data
FILENAME = "students.json"

# Load existing data
def load_data():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save data
def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

# Add student
def add_student(data):
    name = input("Enter student name: ")
    marks = {}
    subjects = ["Python", "AI", "Math"]
    for subject in subjects:
        marks[subject] = int(input(f"Enter marks in {subject}: "))
    
    avg = sum(marks.values()) / len(subjects)
    if avg >= 85:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "F"
    
    data[name] = {"marks": marks, "average": avg, "grade": grade}
    print(f"Student {name} added with Grade {grade}")
    save_data(data)

# View all students
def view_students(data):
    for name, details in data.items():
        print(f"\nName: {name}")
        print(f"Marks: {details['marks']}")
        print(f"Average: {details['average']:.2f}")
        print(f"Grade: {details['grade']}")

# Main program
def main():
    data = load_data()
    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        
        choice = input("Choose option: ")
        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

main()
