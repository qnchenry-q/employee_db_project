
import csv

fields = ['address_id', 'street', 'city', 'state']

num_additions = int(input('How many addresses are there? : '))


rows = []

for i in range(num_additions):
  rows.append([])
  current = rows[-1]
  print('Adding new address')
  current.append(input("What is the address_id for this address? : "))
  current.append(input("What is the street adress for this address? : "))
  current.append(input("What is the city for this address? : "))
  current.append(input("What is the state for this address? : "))



with open('adresses.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)
