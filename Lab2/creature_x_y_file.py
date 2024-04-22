import argparse
import csv
import os
import pathlib


def first_line_x(file_x:str)->None:
    '''
    ввод первой строки в Х файл
    :param file_x: путь к папке с файлом.
    :type file_x: str
    '''
    with open(file_x, mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Дата"])


def first_line_y(file_y:str)->None:
    '''
    ввод первой строки в Y файл
    :param file_y: путь к папке с файлом.
    :type file_y: str
    '''
    with open(file_y, mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Информация"])


def x_file(file_x:str,file_csv:str)->None:
    '''
    разделение первоначального файла на подфайл с датами
    :param file_x: путь к папке с файлом х.
    :type file_x: str
    :param file_csv: путь к папке с исходным файлом.
    :type file_csv: str
    '''
    with open(file_csv)as csvfile:
        first_line_x(file_x)
        with open(file_x,mode="a") as csvX:
            reader = csv.DictReader(csvfile, delimiter=";")
            writer = csv.writer(csvX,lineterminator="\r")
            for rov in reader:
                writer.writerow([rov["Дата"]])


def y_file(file_y:str,file_csv:str)->None:
    '''
    разделение первоначального файла на подфайл с данными
    :param file_y: путь к папке с файлом y.
    :type file_y: str
    :param file_csv: путь к папке с исходным файлом.
    :type file_csv: str
    '''
    with open(file_csv)as csvfile:
        first_line_y(file_y)
        with open(file_y,mode="a") as csvX:
            reader = csv.DictReader(csvfile, delimiter=";")
            writer = csv.writer(csvX,lineterminator="\r")
            for rov in reader:
                writer.writerow([rov["Информация"]])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="надо")
    parser.add_argument('--csv', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv')
    parser.add_argument('--x', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/X.csv')
    parser.add_argument('--y', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/Y.csv')
    parser.add_argument('--year', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/года')
    parser.add_argument('--week', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/недели')
    args = parser.parse_args()
    if os.path.exists(args.x)==True:
        file = pathlib.Path(args.x)
        file.unlink()
    if os.path.exists(args.y) == True:
        file = pathlib.Path(args.y)
        file.unlink()
    x_file(args.x,args.csv)
    y_file(args.y,args.csv)