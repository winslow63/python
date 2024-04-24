import argparse
import csv
import logging
import os
import pathlib


logging.basicConfig(filename='currency_log_creature_x_y_file.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def first_line_x(file_x:str)->None:
    '''
    ввод первой строки в Х файл
    :param file_x: путь к папке с файлом.
    :type file_x: str
    '''
    try:
        with open(file_x, mode="a") as csvfile:
            writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
            writer.writerow(["Дата"])
    except Exception as e:
        logging.error(f"Ошибка при вводе первой строки в файл {file_x}: {e}")


def first_line_y(file_y:str)->None:
    '''
    ввод первой строки в Y файл
    :param file_y: путь к папке с файлом.
    :type file_y: str
    '''
    try:
        with open(file_y, mode="a") as csvfile:
            writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
            writer.writerow(["Информация"])
    except Exception as e:
        logging.error(f"Ошибка при вводе первой строки в файл {file_y}: {e}")


def x_file(file_x:str,file_csv:str)->None:
    '''
    разделение первоначального файла на подфайл с датами
    :param file_x: путь к папке с файлом х.
    :type file_x: str
    :param file_csv: путь к папке с исходным файлом.
    :type file_csv: str
    '''
    try:
        with open(file_csv)as csvfile:
            first_line_x(file_x)
            with open(file_x,mode="a") as csvX:
                reader = csv.DictReader(csvfile, delimiter=";")
                writer = csv.writer(csvX,lineterminator="\r")
                for rov in reader:
                    writer.writerow([rov["Дата"]])
    except Exception as e:
        logging.error(f"Ошибка при разделении файла {file_csv} на подфайл с датами: {e}")


def y_file(file_y:str,file_csv:str)->None:
    '''
    разделение первоначального файла на подфайл с данными
    :param file_y: путь к папке с файлом y.
    :type file_y: str
    :param file_csv: путь к папке с исходным файлом.
    :type file_csv: str
    '''
    try:
        with open(file_csv)as csvfile:
            first_line_y(file_y)
            with open(file_y,mode="a") as csvX:
                reader = csv.DictReader(csvfile, delimiter=";")
                writer = csv.writer(csvX,lineterminator="\r")
                for rov in reader:
                    writer.writerow([rov["Информация"]])
    except Exception as e:
        logging.error(f"Ошибка при разделении файла {file_csv} на подфайл с данными: {e}")


if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler('currency_log_creature_x_y_file.log')
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

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