import csv # use writer

rows=[ 
    [3,'malar',20,'female'],
    [4,'prabha',22,'female'],
    [5,'mani',19,'male']
]

with open("File-and-Error-handling/data.csv","w") as f:
    writer= csv.writer(f)
    writer.writerow(['sno','name','age','gender'])
    writer.writerow([1,'william',22,'male'])
    writer.writerow([2,'sekar',20,'male'])

    writer.writerows(rows)

with open("File-and-Error-handling/data.csv","r") as f:
    reader= csv.reader(f)

    for row in reader:
        print(row)