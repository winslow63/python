import argparse
import os
import csv


def check_file_existence(directory:str, filename:str)->bool:
    """проверка на существование файла в директории"""
    file_path = os.path.join(directory, filename)
    return os.path.exists(file_path)


def check_file_extension(filename:str, desired_extension:str)->bool:
    """проверака существует ли файл с расширением .csv в директории"""
    return filename.endswith(desired_extension)


def Y(i:int,folderpath_search:str,y_file:str)->float:
    """поиск информации в игрик файле"""
    folderpath = f"{folderpath_search}/'"
    file = os.path.join(folderpath, y_file)
    with open(f'{folderpath_search}/Y.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        y = 0
        for rov in reader:
            y = y + 1
            if y == i:
                return (rov['Информация'])


def get_data_by_date(data:str, folderpath_search:str)->float:
    """поиск по дате"""
    parser = argparse.ArgumentParser(description="пример работы")
    parser.add_argument('--csv', type=str, default='course.csv')
    parser.add_argument('--x', type=str, default='X.csv')
    parser.add_argument('--y', type=str, default='Y.csv')
    parser.add_argument('--csv1', type=str, default='.csv')
    parser.add_argument('--week', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/недели')
    args = parser.parse_args()
    if check_file_existence(folderpath_search,args.csv):
        i = 0
        folderpath = f"{folderpath_search}/'"
        file = os.path.join(folderpath, args.csv)
        with open (file) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for rov in reader:
                if rov['Дата'] == str(data):
                    return (rov['Информация'])
                    i = 1
            if i == 0:
                return ("None")
    if check_file_existence(folderpath_search, 'X.csv'):
        i = 0
        p = 0
        folderpath = f"{folderpath_search}/'"
        file = os.path.join(folderpath, args.x)
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for rov in reader:
                i = i + 1
                if rov["Дата"] == str(data):
                    p = 1
                    return Y(i, folderpath_search,args.y)
            if p == 0:
                return ("None")
    i = 0
    for filename in os.listdir(folderpath_search):

        if check_file_extension(filename, args.csv1):
            folderpath = f"{folderpath_search}/'"
            file = os.path.join(folderpath, filename)
            with open(file) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=";")
                for rov in reader:
                    if rov['Дата'] == str(data):
                        return (rov['Информация'])
                        i = 1

    if i == 0:
        return ("None")
