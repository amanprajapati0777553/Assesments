import numpy as np
import pandas as pd

# Project 4: Student Attendance Analysis
# Analyze attendance percentages of students across four technical subjects


# Dataset
attendance = np.array([
    [90, 85, 95, 88],
    [75, 80, 70, 78],
    [95, 92, 98, 96],
    [65, 70, 72, 68],
    [85, 88, 90, 87]
])

subjects = ['Python', 'Java', 'SQL', 'ML']
students = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5']

print("=" * 60)
print("STUDENT ATTENDANCE ANALYSIS")
print("=" * 60)


# 1. Average attendance of each student
student_avg = attendance.mean(axis=1)
print("\n1. Average attendance per student:")
for i in range(len(students)):
    print(f"   {students[i]}: {student_avg[i]:.2f}%")


# 2. Average attendance of each subject
subject_avg = attendance.mean(axis=0)
print("\n2. Average attendance per subject:")
for i in range(len(subjects)):
    print(f"   {subjects[i]}: {subject_avg[i]:.2f}%")


# 3. Highest attendance in each subject
subject_max = attendance.max(axis=0)
print("\n3. Highest attendance per subject:")
for i in range(len(subjects)):
    print(f"   {subjects[i]}: {subject_max[i]}%")


# 4. Lowest attendance in each subject
subject_min = attendance.min(axis=0)
print("\n4. Lowest attendance per subject:")
for i in range(len(subjects)):
    print(f"   {subjects[i]}: {subject_min[i]}%")


# 5. Students with average attendance above 80%
above_80_names = [students[i] for i in range(len(students)) if student_avg[i] > 80]
above_80_values = [student_avg[i] for i in range(len(students)) if student_avg[i] > 80]
print("\n5. Students with average attendance above 80%:")
for name, val in zip(above_80_names, above_80_values):
    print(f"   {name}: {val:.2f}%")


# 6. Student with the highest average attendance
best_index = np.argmax(student_avg)
print(f"\n6. Student with highest average attendance: {students[best_index]} ({student_avg[best_index]:.2f}%)")


# 7. Standard deviation of attendance
overall_std = attendance.std()
student_std = attendance.std(axis=1)
subject_std = attendance.std(axis=0)

print(f"\n7. Standard Deviation:")
print(f"   Overall: {overall_std:.2f}")
print("   Per student:")
for i in range(len(students)):
    print(f"      {students[i]}: {student_std[i]:.2f}")
print("   Per subject:")
for i in range(len(subjects)):
    print(f"      {subjects[i]}: {subject_std[i]:.2f}")


# 8. Eligibility using np.where() (75% cutoff)
eligibility = np.where(student_avg >= 75, "Eligible", "Not Eligible")
print("\n8. Eligibility Status (based on average attendance, cutoff = 75%):")
for i in range(len(students)):
    print(f"   {students[i]}: {eligibility[i]}")


# 9. Convert data into a Pandas DataFrame
df = pd.DataFrame(attendance, columns=subjects, index=students)
print("\n9. DataFrame:")
print(df)


# 10. Add Average and Status column to DataFrame
df['Average'] = df.mean(axis=1)
df['Status'] = np.where(df['Average'] >= 75, "Eligible", "Not Eligible")

print("\n10. Final DataFrame with Average and Status:")
print(df)


# Save to CSV (optional)
df.to_csv("student_attendance_report.csv")
print("\nReport saved as 'student_attendance_report.csv'")