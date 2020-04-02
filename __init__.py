import csv
import os

class Ppp:

    def __init__(self, name, department, birthday):  
        self.name = name
        self.department = department
        self.birthday = birthday

    

    

# r = read
        
with open('employee.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    
    print(f'Processed {line_count} lines.')
    #To print type of a variable:
    print(type(line_count))
    
    
with open('employee_write.txt', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['John Smithhh', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyersss', 'IT', 'March'])
        
print ("") 
print ("employee_write.txt file") 
#print new created file  employee_write.txt from   C:\Users\polin\eclipse-workspace\Python\src\File directory  
employee_writer = open("employee_write.txt", "r")
print(employee_writer.read())

#First create an empty file. Only empty file can be deleted
if os.path.exists('koko.txt'):
    os.remove("koko.txt")
    print ("File koko.txt was deleted")
else:
    print("The file does not exist")
    
    
    
