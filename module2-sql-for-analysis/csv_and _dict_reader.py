""" TO PREVENT 

#### CSVReader Example... focus on the format of the output
import csv
with open('titanic.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        # print(', '.join(row))  # Keep an eye on the ouput versus belows.
        print(row)


#### DictReader Example... focus on the format of the output
# import csv
# with open('titanic.csv', newline='') as csvfile:
#      reader = csv.DictReader(csvfile)
#      for row in reader:
#         #  print(row['Survived'], 
#         #        row['Pclass'], 
#         #        row['Name'], 
#         #        row['Sex'], 
#         #        row['Siblings/Spouses Aboard'], 
#         #        row['Parents/Children Aboard'], 
#         #        row['Fare'])
#         print(row)