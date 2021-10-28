
import csv

fields = ['department_id', 'department_name', 'manager_id', 'address_id']

num_additions = int(input('How many departments are there? : '))


rows = []

for i in range(num_additions):
  rows.append([])
  current = rows[-1]
  print('Adding new department')
  current.append(input("What is the department id for this department? : "))
  current.append(input("What is the name of this department? : "))
  current.append(input("What is the manager id for this department? : "))
  current.append(input("What is the address id for this department's headquarters? : "))




with open('departments.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)
