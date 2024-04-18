import os
import pathlib
import csv
import argparse


def first_line_x()->None:
    '''ввод первой строки в Х файл'''
    with open(args.x, mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Дата"])


def first_line_y()->None:
    '''ввод первой строки в Y файл'''
    with open(args.y, mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Информация"])


def x_file()->None:
    '''разделение первоначального файла на подфайл с датами'''
    with open(args.csv)as csvfile:
        first_line_x()
        with open(args.x,mode="a") as csvX:
            reader = csv.DictReader(csvfile, delimiter=";")
            writer = csv.writer(csvX,lineterminator="\r")
            for rov in reader:
                writer.writerow([rov["Дата"]])


def y_file()->None:
    '''разделение первоначального файла на подфайл с данными'''
    with open(args.csv)as csvfile:
        first_line_y()
        with open(args.y,mode="a") as csvX:
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
    x_file()
    y_file()