import argparse
import csv
import datetime
import os
import re


def csv_name(data:str,n:int,year:str)->str:
    '''
    путь к файлу n
    :param data: дата.
    :type data: str
    :param n: число дней.
    :type n: int
    :param year: путь к папке с годами.
    :type year: str
    :return: путь к файлу для заполнгения
    :rtype:str
    '''
    datas = re.split('-', data.strip())
    past_date = datetime.date(int(datas[0]), int(datas[1]), int(datas[2])) - datetime.timedelta(days=n-1)
    past_date = past_date.isoformat()
    name_file=os.path.join(year,f"{str(data)}_{str(past_date)}.csv")
    return name_file


def row_quantity(file_csv:str)->int:
    '''
    подсчет строк в ссв
    :param file_csv: путь к исходному файлу.
    :type file_csv: str
    :return: количество строк в файле
    :rtype:int
    '''
    with open(file_csv) as csvfile:
        return sum(1 for line in csvfile)


def first_line_n(name_file:str)->None:
    '''
    заполнение первой строки в ссв
    :param name_file: путь файлу для заполнения.
    :type name_file: str
    '''
    with open(name_file, mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Дата","Информация"])


def n_files(file_csv:str, year:str)->None:
    '''
    разделение первоначального файла на н подфайлов по условию
    :param file_csv: путь к исходному файлу.
    :type file_csv: str
    :param year: путь к папке с годами.
    :type year: str
    '''
    days = 0
    lines = 0
    name_file=" "
    with open(file_csv) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        r_q=row_quantity(file_csv)
        for rov in reader:
            if days >= 365:
                days = 0

            if days == 0:
                lines_left=r_q-lines
                if lines_left<365:
                    name_file = csv_name(rov['Дата'], lines_left-1,year)
                    first_line_n(name_file)

                else:
                    name_file=csv_name(rov['Дата'],365,year)
                    first_line_n(name_file)
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
    parser.add_argument('--year', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/года/')
    parser.add_argument('--week', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/недели/')
    args = parser.parse_args()
    n_files(args.csv,args.year)