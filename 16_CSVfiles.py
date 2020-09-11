import csv
# reader() and writer() functions
# For Writing:
with open('myfile.csv', 'w', newline='') as fp:
    w_obj = csv.writer(fp)
    mylist = [['Ram', 'Manager', 75000], ['Lakshmi', 'Asst. Manager', 60000],
              ['Kumar', 'Clerk', 30000], ['Raja', 'Peon', 10000]]
    w_obj.writerows(mylist)

# For Reading:
with open('myfile.csv', 'r', newline='') as fp:
    r_obj = csv.reader(fp)
    for row in r_obj:
        print(row)


with open('employee_file.csv', mode='w', newline='') as ef:
    ew = csv.writer(ef, delimiter=':', quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)
    ew.writerow(['Kumar', 'Marketing', 'January'])
    ew.writerow(['Raja', 'Finance', 'May'])
with open('employee_file.csv') as ef:
    er = csv.reader(ef, delimiter=':', quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)
    for row in er:
        print(row)


# Read / Write as Dictionary DictReader(),DictWriter()
with open('employee_file2.csv', mode='w', newline='') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'emp_name': 'Ram', 'dept': 'Accounting',
                     'birth_month': 'November'})
    writer.writerow(
        {'emp_name': 'Lakshmi', 'dept': 'IT', 'birth_month': 'March'})


with open('employee_file2.csv') as employee_file:
    employee_reader = csv.DictReader(employee_file)
    for row in employee_reader:
        print(row)
with open('employee_file2.csv') as employee_file:
    employee_reader = csv.DictReader(employee_file)
    for row in employee_reader:
        print('Name:', row['emp_name'], '\nDepartment:', row['dept'], '\nBirth Month:',
              row['birth_month'])
