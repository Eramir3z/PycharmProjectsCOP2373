import csv

def create_csvfile():
# create an empty list
    grades_list = []
# get the number of students and loop it based on the number of students
    quantity = int(input("How many students: "))
    for i in range(quantity):
# get the first/last name and exam grades of the students and split them
        first, last = input("First and Last name: ").split(" ")
        grades = input("Grades from the 3 tests: ").split(" ")
# make the exam grades integers
        ex1, ex2, ex3 = map(int, grades)
# add info into the list
        grades_list.append([first, last, ex1, ex2, ex3])
# create the CSV file with header and info
    with open("grades.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])
        csv_writer.writerows(grades_list)
# run function
create_csvfile()
