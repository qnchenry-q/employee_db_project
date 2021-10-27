
import csv

fields = ['address_id', 'department_id', 'manager_id', 'employee_id', 'name', 'age', 'salary']

num_additions = int(input('How many employees are there? : '))


rows = []

for i in range(num_additions):
  rows.append([])
  current = rows[-1]
  print('Adding new employee')
  current.append(input("What is this employee's address_id? : "))
  current.append(input("What is this employee's department_id? : "))
  current.append(input("What is this employee's manager_id? : "))
  current.append(input("What is this employee's employee_id? : "))
  current.append(input("What is this employee's name? : "))
  current.append(input("What is this employee's age?: "))
  current.append(input("What is this employee's salary?: "))


with open('employees.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)
