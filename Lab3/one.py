import os
import pathlib
import csv
def x(folderpath):
    '''ввод первой строки в Х файл'''
    with open(f'{folderpath}/X Y/X.csv', mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Дата"])

def y(folderpath):
    '''ввод первой строки в Y файл'''
    with open(f'{folderpath}/X Y/Y.csv', mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Информация"])

def x_file(folderpath):
    '''разделение первоначального файла на подфайл с датами'''
    with open(f'{folderpath}/course.csv')as csvfile:
        x(folderpath)
        with open(f'{folderpath}/X Y/X.csv',mode="a") as csvX:
            reader = csv.DictReader(csvfile, delimiter=";")
            writer = csv.writer(csvX,lineterminator="\r")
            for rov in reader:
                writer.writerow([rov["Дата"]])

def y_file(folderpath):
    '''разделение первоначального файла на подфайл с данными'''
    with open(f'{folderpath}/course.csv')as csvfile:
        y(folderpath)
        with open(f'{folderpath}/X Y/Y.csv',mode="a") as csvX:
            reader = csv.DictReader(csvfile, delimiter=";")
            writer = csv.writer(csvX,lineterminator="\r")
            for rov in reader:
                writer.writerow([rov["Информация"]])
def split_csv_xy(folderpath):
    if os.path.exists(f'{folderpath}/X Y/X.csv')==True:
        file = pathlib.Path(f'{folderpath}/X Y/X.csv')
        file.unlink()
    if os.path.exists(f'{folderpath}/X Y/Y.csv') == True:
        file = pathlib.Path(f'{folderpath}/X Y/Y.csv')
        file.unlink()
    x_file(folderpath)
    y_file(folderpath)