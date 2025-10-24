import csv

data = [
    ["Name", "Job", "Age"],
    ["Eduardo", "Warehouse", 20],
    ["Yael", "Gay", 43]
]

filename = "my_date.csv"

with open(filename, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(data)

print(f"CSV file '{filename}' created successfully using csv module.")