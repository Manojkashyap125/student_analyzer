import csv
import matplotlib.pyplot as plt

CSV_FILE = "students.csv"

def load_students():
    students = []
    with open(CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["maths"] = int(row["maths"])
            row["science"] = int(row["science"])
            row["english"] = int(row["english"])
            students.append(row)
    return students


def calculate_results():
    students = load_students()
    print("\n--- Student Results ---")

    for s in students:
        total = s["maths"] + s["science"] + s["english"]
        avg = total / 3

        if avg >= 90:
            grade = "A+"
        elif avg >= 75:
            grade = "A"
        elif avg >= 60:
            grade = "B"
        else:
            grade = "C"

        print(f"{s['name']} | Total: {total} | Avg: {avg:.2f} | Grade: {grade}")


def topper():
    students = load_students()
    top = max(students, key=lambda s: s["maths"] + s["science"] + s["english"])
    total = top["maths"] + top["science"] + top["english"]

    print(f"\n🏆 Topper: {top['name']} ({total} marks)")


def subject_average():
    students = load_students()

    maths = sum(s["maths"] for s in students) / len(students)
    science = sum(s["science"] for s in students) / len(students)
    english = sum(s["english"] for s in students) / len(students)

    print("\n--- Subject-wise Average ---")
    print(f"Maths: {maths:.2f}")
    print(f"Science: {science:.2f}")
    print(f"English: {english:.2f}")


def subject_average_graph():
    students = load_students()
    subjects = ["Maths", "Science", "English"]

    averages = [
        sum(s["maths"] for s in students) / len(students),
        sum(s["science"] for s in students) / len(students),
        sum(s["english"] for s in students) / len(students)
    ]

    plt.bar(subjects, averages)
    plt.title("Subject-wise Average Marks")
    plt.ylabel("Average Marks")
    plt.show()


def student_total_graph():
    students = load_students()

    names = [s["name"] for s in students]
    totals = [s["maths"] + s["science"] + s["english"] for s in students]

    plt.plot(names, totals, marker='o')
    plt.title("Student Total Marks")
    plt.ylabel("Total Marks")
    plt.show()
