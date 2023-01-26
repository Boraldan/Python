import csv   
with open('python1.csv') as csv_file:   
    csv_reader = csv.reader(csv_file, delimiter=',')   
    line_count = 0   
    for row in csv_reader:   
        if line_count == 1:   
            print(f'Column names are {", ".join(row)}')   
        line_count += 1 


with open('python2.txt', mode='r') as csv_file:   
    csv_reader = csv.DictReader(csv_file)   
    line_count = 0   
    for row in csv_reader:   
        if line_count == 0:   
            print(f'The Column names are as follows {", ".join(row)}')   
            line_count += 1   
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')   
        line_count += 1   
    print(f'Processed {line_count} lines.') 

    

with open('Python.csv', 'w') as csvfile:   
    fieldnames = ['first_name', 'last_name', 'Rank']   
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)   
    
    writer.writeheader()   
    writer.writerow({'Rank': 'B', 'first_name': 'Parker', 'last_name': 'Brian'})   
    writer.writerow({'Rank': 'A', 'first_name': 'Smith',   
                     'last_name': 'Rodriguez'})   
    writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})   
    writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})   
    
print("Writing complete")  



with open('python.csv', mode='w') as csv_file:   
    fieldnames = ['emp_name', 'dept', 'birth_month']   
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)   
    writer.writeheader()   
    writer.writerow({'emp_name': 'Parker', 'dept': 'Accounting', 'birth_month': 'November'})   
    writer.writerow({'emp_name': 'Smith', 'dept': 'IT', 'birth_month': 'October'})   


import csv
with open('Python1.csv', mode="a", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["Имя", "Класс", "Возраст"])
    file_writer.writerow(["Женя", "3", "10"])
    file_writer.writerow(["Саша", "5", "12"])
    file_writer.writerow(["Маша", 11, "18"])



def process(lines):
    for line in lines:
        yield line.upper()

    with open('for_import.csv', 'r', 'utf-8') as infile:
        with codecs.open(file2, 'w', 'utf-8') as outfile:
            for line in process(infile):
                outfile.write(line)