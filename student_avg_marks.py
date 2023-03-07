# student result sheet
# using def function create function it has to find average amrks and grade of thestudents
# create function for students average marks
# using conditions display grade of the students
# grade 'A' students who got 80 marks
# grade 'B' students who got 60 marks
# grade 'C' students who got 50 marks


def find_average_marks(marks):
    sum_of_marks = sum(marks)
    number_of_subjects = len(marks)

    average_marks = sum_of_marks / number_of_subjects

    return average_marks


# compute grade and return it
def compute_grade(average_marks):
    if average_marks >= 80.0:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'

    return grade


marks = [90, 90, 77, 80, 65]
average_marks = find_average_marks(marks)
grade = compute_grade(average_marks)

print("Your average marks is", average_marks)
print("Your grade is", grade)
