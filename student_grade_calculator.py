def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

print("📘 Student Grade Calculator")
print("--------------------------")

subjects = int(input("Enter number of subjects: "))

marks = []
for i in range(subjects):
    while True:
        mark = float(input(f"Enter marks for subject {i+1} (0–100): "))
        if 0 <= mark <= 100:
            marks.append(mark)
            break
        else:
            print("Invalid! Marks must be between 0 and 100.")

total = sum(marks)
average = total / subjects
grade = calculate_grade(average)

print("\n------ RESULT ------")
print(f"Total Marks : {total}")
print(f"Average     : {average:.2f}")
print(f"Grade       : {grade}")
print("---------------------")
