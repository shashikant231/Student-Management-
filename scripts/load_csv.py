from app1.models import Student,School,Book
import csv


#scripts to insert CSV data into django database
def run():
    with open('app1/Students_data.csv') as file:
        reader = csv.reader(file)
        # print(reader)
        next(reader) #advance past the header



        for row in reader:
            School(name=row[-2],
            contact_no=str(+918544003521)).save()
            Book(name=row[-1]).save()
            Student(first_name=row[1],
            last_name=row[2],
            email=row[3],
            gender=row[4]).save()