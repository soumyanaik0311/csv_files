from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from project1.settings import CSV_DIR
from app.models import *
import csv
def data_insert_csv(request):
    with open('C:\\Users\\soumy\\OneDrive\\Desktop\\Django\\CSV_files\\Business-employment-data-september-2022-quarter-csv.csv','r') as file:
        GOcsvFile = csv.reader(file)
        next(GOcsvFile)
        for row in GOcsvFile:
            bo=BusinessEmployeMentData(Series_reference=row[0],Period=row[1],Data_value=row[2],Suppressed=row[3],STATUS=row[4],UNITS=row[5],Magnitude=row[6],Subject=row[7],Group=row[8],Series_title_1=row[9])
            bo.save()


    return HttpResponse('Data Inserted Successfully')


'''reader function usage
    reader() is used to read the file, which returns 
    an iterable reader object. The reader object is
     then iterated using a for loop to print the 
     contents of each row.

     it is a generator object

     next() is used to skip the first line of the csv file as we dont want to inset the column heading.
     
    '''