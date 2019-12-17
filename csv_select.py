import csv

with open ('student.csv') as file1:
    rows = csv.DictReader(file1) 
    with open('shashank.csv','w') as file:
        writer = csv.DictWriter(file, ['name','email'])
        for row in rows:
            if int(row['sn'])%2==0:
                    writer.writerow({'name': row['name'],'email': row['email']})


