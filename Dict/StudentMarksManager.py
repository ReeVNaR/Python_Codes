def display_menu():
    print("\n🎓 Student Marks Manager")
    print("1. Add Student")
    print("2. View Student Marks")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Display All Records")
    print("6. Exit")

def main():
    students = {}

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter student name: ").strip()
            if name in students:
                print("⚠️ Student already exists.")
            else:
                marks = int(input("Enter marks: "))
                students[name] = marks
                print("✅ Student added.")
        
        elif choice == '2':
            name = input("Enter student name: ").strip()
            print(f"📘 Marks for {name}: {students.get(name, 'Not found')}")

        elif choice == '3':
            name = input("Enter student name: ").strip()
            if name in students:
                marks = int(input("Enter new marks: "))
                students[name] = marks
                print("✏️ Marks updated.")
            else:
                print("⚠️ Student not found.")
        
        elif choice == '4':
            name = input("Enter student name to delete: ").strip()
            if name in students:
                del students[name]
                print("🗑️ Student deleted.")
            else:
                print("⚠️ Student not found.")
        
        elif choice == '5':
            if students:
                print("\n📋 Student Records:")
                for name, marks in students.items():
                    print(f"  {name}: {marks}")
            else:
                print("No records found.")
        
        elif choice == '6':
            print("👋 Exiting Student Marks Manager.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
