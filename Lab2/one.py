import os
import pathlib
import csv

def x():
    '''ввод первой строки в Х файл'''
    with open("C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/X.csv", mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Дата"])

def y():
    '''ввод первой строки в Y файл'''
    with open("C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/Y.csv", mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Информация"])

def x_file():
    '''разделение первоначального файла на подфайл с датами'''
    with open("C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv")as csvfile:
        x()
        with open("C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/X.csv",mode="a") as csvX:
            reader = csv.DictReader(csvfile, delimiter=";")
            writer = csv.writer(csvX,lineterminator="\r")
            for rov in reader:
                writer.writerow([rov["Дата"]])

def y_file():
    '''разделение первоначального файла на подфайл с данными'''
    with open("C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv")as csvfile:
        y()
        with open("C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/Y.csv",mode="a") as csvX:
            reader = csv.DictReader(csvfile, delimiter=";")
            writer = csv.writer(csvX,lineterminator="\r")
            for rov in reader:
                writer.writerow([rov["Информация"]])

if __name__ == "__main__":
    if os.path.exists("C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/X.csv")==True:
        file = pathlib.Path("C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/X.csv")
        file.unlink()
    if os.path.exists("C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/Y.csv") == True:
        file = pathlib.Path("C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/Y.csv")
        file.unlink()
    x_file()
    y_file()