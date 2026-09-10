"""
Project 1: Student Performance Analysis
Analyze student marks using NumPy and present results using Pandas.
"""

import numpy as np
import pandas as pd

# Given Dataset
marks = np.array([
    [85, 80, 90],
    [70, 75, 65],
    [92, 88, 95],
    [60, 72, 68],
    [78, 82, 80]
])

subjects = ["Python", "SQL", "Machine Learning"]
students = [f"Student {i+1}" for i in range(marks.shape[0])]

print("=" * 60)
print("RAW MARKS")
print("=" * 60)
print(pd.DataFrame(marks, columns=subjects, index=students))


# 1. Total marks obtained by each student
total_marks = marks.sum(axis=1)
print("\n1. Total marks per student:")
print(total_marks)


# 2. Average marks of each student
avg_marks = marks.mean(axis=1)
print("\n2. Average marks per student:")
print(np.round(avg_marks, 2))


# 3. Average marks in each subject
subject_avg = marks.mean(axis=0)
print("\n3. Average marks per subject:")
for subj, avg in zip(subjects, subject_avg):
    print(f"   {subj}: {avg:.2f}")


# 4. Highest score in each subject
subject_max = marks.max(axis=0)
print("\n4. Highest score per subject:")
for subj, mx in zip(subjects, subject_max):
    print(f"   {subj}: {mx}")


# 5. Lowest score in each subject
subject_min = marks.min(axis=0)
print("\n5. Lowest score per subject:")
for subj, mn in zip(subjects, subject_min):
    print(f"   {subj}: {mn}")


# 6. Students whose average marks are above 80
mask_above_80 = avg_marks > 80
above_80_students = np.array(students)[mask_above_80]
print("\n6. Students with average marks above 80:")
print(above_80_students if len(above_80_students) > 0 else "None")


# 7. np.where() to assign Pass / Fail status
#    (Pass condition: average marks >= 60; adjust cutoff as needed)
PASS_CUTOFF = 60
status = np.where(avg_marks >= PASS_CUTOFF, "Pass", "Fail")
print(f"\n7. Pass/Fail status (cutoff = {PASS_CUTOFF} avg marks):")
for s, st in zip(students, status):
    print(f"   {s}: {st}")

# Optional: subject-wise pass/fail matrix
subject_wise_status = np.where(marks >= PASS_CUTOFF, "Pass", "Fail")
print("\n   Subject-wise Pass/Fail matrix:")
print(pd.DataFrame(subject_wise_status, columns=subjects, index=students))


# 8. Index of the highest-performing student
top_student_index = np.argmax(total_marks)
print(f"\n8. Highest-performing student index: {top_student_index}")
print(f"   Name: {students[top_student_index]}, Total Marks: {total_marks[top_student_index]}")


# 9. Standard deviation for each subject
subject_std = marks.std(axis=0)
print("\n9. Standard deviation per subject:")
for subj, std in zip(subjects, subject_std):
    print(f"   {subj}: {std:.2f}")


# 10. Convert final results into a Pandas DataFrame
df = pd.DataFrame(marks, columns=subjects, index=students)
df["Total"] = total_marks
df["Average"] = np.round(avg_marks, 2)
df["Status"] = status

print("\n" + "=" * 60)
print("10. FINAL STUDENT RESULTS DATAFRAME")
print("=" * 60)
print(df)

# Bonus: Subject-wise summary DataFrame
summary = pd.DataFrame({
    "Average": np.round(subject_avg, 2),
    "Max": subject_max,
    "Min": subject_min,
    "Std Dev": np.round(subject_std, 2)
}, index=subjects)

print("\n" + "=" * 60)
print("BONUS: SUBJECT-WISE SUMMARY")
print("=" * 60)
print(summary)


# Save results to CSV (optional)
df.to_csv("student_results.csv")
summary.to_csv("subject_summary.csv")
print("\nResults saved to 'student_results.csv' and 'subject_summary.csv'")
