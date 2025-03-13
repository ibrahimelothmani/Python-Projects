# 📢 School Grade Management System 🏫🐍
# This program allows users to input students, courses, and marks, 
# then calculates and displays the best student, worst student, and class average.

def get_student_list():
    """Ask the user for the number of students and fill the student list."""
    num_students = int(input("Enter the number of students: "))
    students = []
    for i in range(num_students):
        name = input(f"Enter the name of student {i + 1}: ")
        students.append(name)
    return students

def get_course_list():
    """Ask the user for the number of courses and fill the course list."""
    num_courses = int(input("\nEnter the number of courses: "))
    courses = []
    for i in range(num_courses):
        course = input(f"Enter the name of course {i + 1}: ")
        courses.append(course)
    return courses

def get_marks(students, courses):
    """Ask the user to enter midterm and final marks for each student and course."""
    marks = []
    for i in range(len(students)):
        print(f"\nEnter marks for {students[i]}:")
        student_marks = []
        for j in range(len(courses)):
            midterm = float(input(f"  Enter {students[i]}'s midterm mark for {courses[j]}: "))
            final_exam = float(input(f"  Enter {students[i]}'s final exam mark for {courses[j]}: "))
            student_marks.append([midterm, final_exam])  # Store as [midterm, final_exam]
        marks.append(student_marks)
    return marks

def calculate_final_grades(marks):
    """Calculate the final grades of each student based on weighted averages."""
    final_grades = []
    for student_marks in marks:
        total_score = 0
        for midterm, final_exam in student_marks:
            final_score = (midterm * 0.3) + (final_exam * 0.7)  # Apply weight
            total_score += final_score
        final_average = total_score / len(student_marks)  # Average across courses
        final_grades.append(final_average)
    return final_grades

def find_best_and_worst_students(students, final_grades):
    """Find the best and worst students based on their final grades."""
    best_index = final_grades.index(max(final_grades))  # Highest grade
    worst_index = final_grades.index(min(final_grades))  # Lowest grade
    return students[best_index], final_grades[best_index], students[worst_index], final_grades[worst_index]

def calculate_class_average(final_grades):
    """Calculate the overall class average grade."""
    return sum(final_grades) / len(final_grades)

def display_results(students, final_grades, best_student, best_grade, worst_student, worst_grade, class_average):
    """Display all student grades, the best and worst student, and the class average."""
    print("\n📊 Final Grades:")
    for i in range(len(students)):
        print(f"{students[i]}: {final_grades[i]:.2f}")

    print("\n🏆 Best Student:", best_student, "with an average of", f"{best_grade:.2f}")
    print("📉 Worst Student:", worst_student, "with an average of", f"{worst_grade:.2f}")
    print("🎯 Class Average:", f"{class_average:.2f}")

def display_student_grades(students, courses, marks):
    """Allow the user to check grades for a specific student."""
    search_name = input("\nEnter a student's name to see their grades: ")
    if search_name in students:
        index = students.index(search_name)
        print(f"\n📜 {search_name}'s Grades:")
        for j in range(len(courses)):
            midterm, final_exam = marks[index][j]
            final_score = (midterm * 0.3) + (final_exam * 0.7)
            print(f"{courses[j]}: {final_score:.2f}")
    else:
        print("Student not found!")

# 🔥 Main Program Execution
students = get_student_list()
courses = get_course_list()
marks = get_marks(students, courses)
final_grades = calculate_final_grades(marks)
best_student, best_grade, worst_student, worst_grade = find_best_and_worst_students(students, final_grades)
class_average = calculate_class_average(final_grades)

display_results(students, final_grades, best_student, best_grade, worst_student, worst_grade, class_average)
display_student_grades(students, courses, marks)