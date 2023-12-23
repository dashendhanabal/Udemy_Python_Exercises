#Average Height Calculator type 1
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = total_height/number_of_students
print(round(average_height))
