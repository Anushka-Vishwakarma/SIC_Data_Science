print("Student Grade Calculator")
print("-------------------------" )
name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")
marks = {}
print("Enter marks for 5 subjects:")
for i in range(1, 6):
    try:
        subject_name=input(f"Enter {1} Subject Name: ")
        mark = float(input(f"Subject mark {subject_name}: "))
        if mark < 0 or mark > 100:
            raise ValueError("Marks should be between 0 and 100.")
        marks[subject_name] = mark
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid number.")
        exit()
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")
        exit()
total_marks = sum(marks.values())
percentage = (total_marks / 500) * 100
print(f"Total Marks: {total_marks}")    
average_marks = total_marks / 5
print(f"Average Marks: {average_marks}")
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'
print("-------------------------")
print(f"Student Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")    
print("-------------------------")
