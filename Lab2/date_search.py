import argparse
import csv
import datetime
import logging
import os
import re
from datetime import datetime


logging.basicConfig(filename='currency_log_date_search.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def search_elementary_file(search_date:datetime,file_vsv:str)->None:
    """
    поиск по дате в исходном файле
    :param search_date: дата для поиска.
    :type search_date: datetime
    :param file_vsv: путь к файлу.
    :type file_vsv: str
    """
    i=0
    try:
        with open(file_vsv) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for rov in reader:
                if rov['Дата']==str(search_date):
                    logging.info(f"Найдена информация: {rov['Информация']}")
                    print(rov['Информация'])
                    i=1
            if i==0:
                logging.info("Информация не найдена.")
                print("None")
    except FileNotFoundError:
        logging.error(f"Файл {file_vsv} не найден.")
        print("Файл не найден.")

def search_files_x_y(search_date:datetime,file_x:str,file_y:str)->None:
    """
    поиск по дате в  x и y файлах
    :param search_date: дата для поиска.
    :type search_date: datetime
    :param file_x: путь к файлу х.
    :type file_x: str
    :param file_y: путь к файлу у.
    :type file_y: str
    """
    i=0
    p=0
    try:
        with open(file_x) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for rov in reader:
                i = i+1
                if rov["Дата"] == str(search_date):
                    p=1
                    Y_file(i,file_y)
            if p==0:
                logging.info("Информация не найдена.")
                print("None")
    except FileNotFoundError:
        logging.error(f"Файл {file_x} не найден.")
        print("Файл не найден.")


def Y_file(i:int,file_y:str)->None:
    """
    поиск по дате в y файле
    :param i: строка из которой надо взять информацию
    :type i: int
    :param file_y: путь файлу.
    :type file_y: str
    """
    try:
        with open(file_y) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            y = 0
            for rov in reader:
                y = y + 1
                if y == i:
                    logging.info(f"Найдена информация из файла {file_y}: {rov['Информация']}")
                    print(rov['Информация'])
    except FileNotFoundError:
        logging.error(f"Файл {file_y} не найден.")
        print("Файл не найден.")


def search_files_year(search_date:datetime,file_year:str)->None:
    """
    поиск по дате в файлах разбитых на года
    :param search_date: дата для поиска.
    :type search_date: datetime
    :param file_year: путь к папке.
    :type file_year: str
    """
    i=0
    try:
        for filename in os.listdir(file_year):
            file_n=os.path.join(file_year,filename)
            with open(file_n) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=";")
                for rov in reader:
                    if rov['Дата'] == str(search_date):
                        logging.info(f"Найдена информация: {rov['Информация']}")
                        print(rov['Информация'])
                        i = 1
        if i == 0:
            logging.info("Информация не найдена.")
            print("None")
    except FileNotFoundError:
        logging.error(f"Папка {file_year} не найдена.")
        print("Папка не найдена.")

def search_files_week(search_date:datetime,file_week:str)->None:
    """
    поиск по дате в файлах разбитых на недели
    :param search_date: дата для поиска.
    :type search_date: datetime
    :param file_week: путь к папке.
    :type file_week: str
    """
    i=0
    try:
        for filename in os.listdir(file_week):
            file_n = os.path.join(file_week, filename)
            with open(file_n) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=";")
                for rov in reader:
                    if rov['Дата'] == str(search_date):
                        logging.info(f"Найдена информация: {rov['Информация']}")
                        print(rov['Информация'])
                        i = 1

        if i == 0:
            logging.info("Информация не найдена.")
            print("None")
    except FileNotFoundError:
        logging.error(f"Папка {file_week} не найдена.")
        print("Папка не найдена.")


def information_in_file(way:str)->list:
    """
    вывод списка информации из файла
    :param way: путь к файлу.
    :type way: str
    :return: список данных из файла
    :rtype: list
    """
    tuple_list = []
    try:
        with open(way) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for rov in reader:
                tuple_list.append((rov['Дата'],rov['Информация']),)
            return tuple_list
    except FileNotFoundError:
        logging.error(f"Файл {way} не найден.")
        print("Файл не найден.")
        return tuple_list

def next(tuple:list)->list:
    """
    поиск минимальной даты в файле
    :param tuple: список данных из файла.
    :type tuple: list
    :return: список данных из файла без последнего элемента
    :rtype: list
    """
    try:
        u=re.split('-', tuple[0][0].strip())
        min_data=datetime.date(int(u[0]), int(u[1]), int(u[2]))
        tuple_element=tuple[0]
        for item in tuple:
            z = re.split('-', item[0].strip())
            data_next=datetime.date(int(z[0]), int(z[1]), int(z[2]))
            if min_data>data_next and item[1]!='' :
                min_data=data_next
                tuple_element=item
        logging.info(f"Минимальная дата: {tuple_element}")
        print (tuple_element)
        tuple_list = []
        for item in tuple:
            if tuple_element==item:
                continue
            tuple_list.append(item,)
        return tuple_list
    except Exception as e:
        logging.error(f"Произошла ошибка при поиске минимальной даты: {e}")
        return []


if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler('currency_log_date_search.log')
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    parser = argparse.ArgumentParser(description="пример работы c разными файлами")
    parser.add_argument('--date', type=lambda d: datetime.strptime(d, '%Y-%m-%d'), default="2023-10-9")
    parser.add_argument('--csv', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv')
    parser.add_argument('--x', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/X.csv')
    parser.add_argument('--y', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/Y.csv')
    parser.add_argument('--year', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/года')
    parser.add_argument('--week', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/недели')
    parser.add_argument('--next', type=str, default='минимальный элемент')
    args = parser.parse_args()
    search_date = args.date
    if args.csv:
        search_elementary_file(search_date,args.csv)
    elif args.x|args.y:
        search_files_x_y(search_date,args.x,args.y)
    elif args.year:
        search_files_year(search_date,args.year)
    elif args.week:
        search_files_week(search_date,args.week)
    elif args.next:
        tuple = information_in_file(args.csv)
        tuple = next(tuple)

