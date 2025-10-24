import csv
# open and read the csv file
def main():
    with open("grades.csv", "r", newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
# iterator into list
        rows = list(csv_reader)
# format to give enough space for names, but slightly less for numbers
        print(f"{"First Name":<15}{"last Name":<15}{"Exam 1":<10}{"Exam 2":<10}{"Exam 3":<10}")
        print("-"*60)
# loop through the data, skip the header
        for row in rows[1:]:
            first, last, exam1, exam2, exam3 = row
# format data exactly like header
            print(f"{first:<15}{last:<15}{exam1:<10}{exam2:<10}{exam3:<10}")
# run main
if __name__ == '__main__':
    main()