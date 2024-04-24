import argparse
import csv
import datetime
import logging
import os
import re


logging.basicConfig(filename='currency_log_creature_week_files.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def csv_name(data:str,n:int,week:str)->str:
    '''
    путь к файлу n
    :param data: дата.
    :type data: str
    :param n: число дней.
    :type n: int
    :param week: путь к папке с неделями.
    :type week: str
    :return: путь к файлу для заполнгения
    :rtype:str
    '''
    datas = re.split('-', data.strip())
    past_date = datetime.date(int(datas[0]), int(datas[1]), int(datas[2])) - datetime.timedelta(days=n-1)
    past_date = past_date.isoformat()
    name_file=os.path.join(week,f"{str(data)}_{str(past_date)}.csv")
    logging.info(f"Путь к файлу: {name_file} создан.")
    return name_file


def row_quantity(file_csv:str)->int:
    '''
    подсчет строк в ссв
    :param file_csv: путь к исходному файлу.
    :type file_csv: str
    :return: количество строк в файле
    :rtype:int
    '''
    try:
        with open(file_csv) as csvfile:
            return sum(1 for line in csvfile)
    except Exception as e:
        logging.error(f"Ошибка при подсчете строк в файле {file_csv}: {e}")


def first_line_n(name_file:str)->None:
    '''
    заполнение первой строки в ссв
    :param name_file: путь файлу для заполнения.
    :type name_file: str
    '''
    try:
        with open(name_file, mode="a") as csvfile:
            writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
            writer.writerow(["Дата","Информация"])
    except Exception as e:
        logging.error(f"Ошибка при вводе первой строки в файл {name_file}: {e}")


def separation_files_n(file_csv:str,week:str)->None:
    '''
    разделение первоначального файла на н подфайлов по условию
    :param file_csv: путь к исходному файлу.
    :type file_csv: str
    :param week: путь к папке с неделями.
    :type week: str
    '''
    days = 0
    lines = 0
    name_file=" "
    with open(file_csv) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        r_q=row_quantity(file_csv)
        for rov in reader:
            if days >= 7:
                days = 0

            if days == 0:
                lines_left=r_q-lines
                if lines_left<7:
                    name_file = csv_name(rov['Дата'], lines_left-1,week)
                    first_line_n(name_file)
                    logging.info(f"Создан новый файл: {name_file}")
                else:
                    name_file=csv_name(rov['Дата'],7,week)
                    first_line_n(name_file)
                    logging.info(f"Создан новый файл: {name_file}")
            with open(name_file, mode="a") as csvX:
                writer = csv.writer(csvX,delimiter=";", lineterminator="\r")
                writer.writerow([rov['Дата'] , rov["Информация"]])
            days = days+1
            lines = lines+1
            logging.debug(f"Обработана строка {lines}: {rov['Дата']}")

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler('currency_log_creature_week_files.log')
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    parser = argparse.ArgumentParser(description="надо")
    parser.add_argument('--csv', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv')
    parser.add_argument('--x', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/X.csv')
    parser.add_argument('--y', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/Y.csv')
    parser.add_argument('--year', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/года')
    parser.add_argument('--week', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/недели/')
    args = parser.parse_args()
    separation_files_n(args.csv,args.week)