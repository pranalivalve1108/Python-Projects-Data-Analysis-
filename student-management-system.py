students = []


def add_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))

    student = {
        "id": sid,
        "name": name,
        "marks": marks
    }
    students.append(student)
    print("✅ Student added successfully!\n")


def view_students():
    if not students:
        print("❌ No student records found.\n")
        return
    for student in students:
        print(student)
    print()


def update_student():
    sid = int(input("Enter Student ID to update: "))
    for student in students:
        if student["id"] == sid:
            student["marks"] = int(input("Enter new marks: "))
            print("✅ Student updated successfully!\n")
            return
    print("❌ Student not found.\n")


def delete_student():
    sid = int(input("Enter Student ID to delete: "))
    for student in students:
        if student["id"] == sid:
            students.remove(student)
            print("✅ Student deleted successfully!\n")
            return
    print("❌ Student not found.\n")


def menu():
    while True:
        print("---- Student Management System ----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            update_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            print("👋 Exiting program")
            break
        else:
            print("❌ Invalid choice\n")


menu()
