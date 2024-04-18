import os
import requests
import re
import pathlib
import datetime
import csv
import argparse


def csv_name(data:str,n:int)->str:
    '''путь к файлу n'''
    datas = re.split('-', data.strip())
    past_date = datetime.date(int(datas[0]), int(datas[1]), int(datas[2])) - datetime.timedelta(days=n-1)
    past_date = past_date.isoformat()
    name_file=os.path.join(args.week,f"{str(data)}_{str(past_date)}.csv")
    return name_file


def row_quantity()->int:
    '''подсчет строк в ссв'''
    with open(args.csv) as csvfile:
        return sum(1 for line in csvfile)


def first_line_N(name_file)->None:
    '''заполнение первой строки в ссв'''
    with open(name_file, mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Дата","Информация"])


def separation_files_N()->None:
    '''разделение первоначального файла на н подфайлов по условию'''
    days = 0
    lines = 0
    name_file=" "
    with open(args.csv) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        r_q=row_quantity()
        for rov in reader:
            if days >= 7:
                days = 0

            if days == 0:
                lines_left=r_q-lines
                if lines_left<7:
                    name_file = csv_name(rov['Дата'], lines_left-1)
                    first_line_N(name_file)
                else:
                    name_file=csv_name(rov['Дата'],7)
                    first_line_N(name_file)
            with open(name_file, mode="a") as csvX:
                writer = csv.writer(csvX,delimiter=";", lineterminator="\r")
                writer.writerow([rov['Дата'] , rov["Информация"]])
            days = days+1
            lines = lines+1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="надо")
    parser.add_argument('--csv', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv')
    parser.add_argument('--x', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/X.csv')
    parser.add_argument('--y', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/Y.csv')
    parser.add_argument('--year', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/года')
    parser.add_argument('--week', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/недели/')
    args = parser.parse_args()
    separation_files_N()