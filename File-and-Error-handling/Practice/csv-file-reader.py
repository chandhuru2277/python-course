import csv

try:
    with open("File-and-Error-handling/Practice/csv-files/data.csv","r") as f:
        reader= csv.reader(f)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found is please give correct path!")
finally:
    print("Code run successfully")


