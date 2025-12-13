import analyzer

def menu():
    while True:
        print("\n===== Student Performance Analyzer =====")
        print("1. View Student Results")
        print("2. Find Topper")
        print("3. Subject-wise Average")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            analyzer.calculate_results()
        elif choice == "2":
            analyzer.topper()
        elif choice == "3":
            analyzer.subject_average()
        elif choice == "4":
            print("GOOD BYEE...")
            break
        else:
            print("Invalid choice!")

menu()
