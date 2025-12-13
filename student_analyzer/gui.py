import tkinter as tk
import analyzer

root = tk.Tk()
root.title("Student Performance Analyzer")
root.geometry("400x400")

tk.Label(
    root,
    text="Student Performance Analyzer",
    font=("Arial", 16, "bold")
).pack(pady=10)

tk.Button(
    root, text="View Results",
    width=30, command=analyzer.calculate_results
).pack(pady=5)

tk.Button(
    root, text="Find Topper",
    width=30, command=analyzer.topper
).pack(pady=5)

tk.Button(
    root, text="Subject-wise Average",
    width=30, command=analyzer.subject_average
).pack(pady=5)

tk.Button(
    root, text="Subject Average Graph",
    width=30, command=analyzer.subject_average_graph
).pack(pady=5)

tk.Button(
    root, text="Student Total Graph",
    width=30, command=analyzer.student_total_graph
).pack(pady=5)

tk.Button(
    root, text="Exit",
    width=30, command=root.destroy
).pack(pady=10)

root.mainloop()
