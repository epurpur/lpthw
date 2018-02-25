class student():
    credits = 0 #old credits
    gpa = 0  #old gpa
    def __init__(self, current_gpa, current_credits):
        student.gpa = ((student.gpa * student.credits) + (current_gpa * current_credits)) / (student.credits + current_credits)

        print ("Current GPA = ", student.gpa)

        student.credits += current_credits
        print ("Current Credits = ", student.credits)

semester1 = student(4.0, 3)
semester2 = student(3.3, 3)
semester3 = student(2.3, 4)
