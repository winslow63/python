import argparse
import csv
import os


def check_file_existence(directory:str, filename:str)->bool:
    """
    проверка на существование файла в директории
    :param directory: путь к папке.
    :type directory: str
    :param filename: имя файла.
    :type filename: str
    :return: есть ли файл в директории
    :rtype:bool
    """
    file_path = os.path.join(directory, filename)
    return os.path.exists(file_path)


def check_file_extension(filename:str, desired_extension:str)->bool:
    """
    проверака существует ли файл с расширением .csv в директории
    :param filename: расширение файла
    :type filename: str
    :param desired_extension: путь к папке.
    :type desired_extension: str
    :return: есть ли файл с данным расширением в директории
    :rtype:bool
    """
    return filename.endswith(desired_extension)


def Y(i:int,folderpath_search:str,y_file:str)->float:
    """
    поиск информации в игрик файле
    :param i: строка в которой находится курс долара
    :type i: int
    :param folderpath_search: путь к папке.
    :type folderpath_search: str
    :param y_file: имя файла.
    :type y_file: str
    :return: курс долара
    :rtype:float
    """
    file = os.path.join(folderpath_search, y_file)
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        y = 0
        for rov in reader:
            y = y + 1
            if y == i:
                return (rov['Информация'])


def get_data_by_date(data:str, folderpath_search:str)->float:
    """
    поиск по дате
    :param data: дата по которой ищем
    :type data: str
    :param folderpath_search: путь к папке.
    :type folderpath_search: str
    :return: курс долара
    :rtype:float
    """
    csvs="course.csv"
    x="X.csv"
    y="Y.csv"
    csv1=".csv"
    if check_file_existence(folderpath_search,csvs):
        i = 0
        file = os.path.join(folderpath_search,csvs)
        with open (file) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for rov in reader:
                if rov['Дата'] == str(data):
                    return (rov['Информация'])
                    i = 1
            if i == 0:
                return ("None")
    if check_file_existence(folderpath_search, x):
        i = 0
        p = 0
        file = os.path.join(folderpath_search, x)
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for rov in reader:
                i = i + 1
                if rov["Дата"] == str(data):
                    p = 1
                    return Y(i, folderpath_search,y)
            if p == 0:
                return ("None")
    i = 0
    for filename in os.listdir(folderpath_search):

        if check_file_extension(filename,csv1):
            file = os.path.join(folderpath_search, filename)
            with open(file) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=";")
                for rov in reader:
                    if rov['Дата'] == str(data):
                        return (rov['Информация'])
                        i = 1

    if i == 0:
        return ("None")
