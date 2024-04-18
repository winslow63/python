import argparse
import os
import datetime
from datetime import datetime
import csv
import re


def search_zero(search_date:datetime)->None:
    """поиск по дате в исходном файле"""
    i=0
    with open(args.csv) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for rov in reader:
            if rov['Дата']==str(search_date):
                print(rov['Информация'])
                i=1
        if i==0:
            print("None")


def search_one(search_date:datetime)->None:
    """поиск по дате в  x и y файлах"""
    i=0
    p=0
    with open(args.x) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for rov in reader:
            i = i+1
            if rov["Дата"] == str(search_date):
                p=1
                Y_file(i)
        if p==0:
            print("None")


def Y_file(i:int)->None:
    """поиск по дате в y файле"""
    with open(args.y) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        y = 0
        for rov in reader:
            y = y + 1
            if y == i:
                print(rov['Информация'])


def search_two(search_date:datetime)->None:
    """поиск по дате в файлах разбитых на года"""
    i=0
    for filename in os.listdir(args.year):
        with open(args.year+filename) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for rov in reader:
                if rov['Дата'] == str(search_date):
                    print(rov['Информация'])
                    i = 1

    if i == 0:
        print("None")


def search_three(search_date:datetime)->None:
    """поиск по дате в файлах разбитых на недели"""
    i=0
    for filename in os.listdir(args.week):
        with open(args.week + filename) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for rov in reader:
                if rov['Дата'] == str(search_date):
                    print(rov['Информация'])
                    i = 1

    if i == 0:
        print("None")


def tuple(way:str)->list:
    """вывод списка информации из файла"""
    tuple_list = []
    with open(way) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for rov in reader:
            tuple_list.append((rov['Дата'],rov['Информация']),)
        return tuple_list


def next(tuple:list)->list:
    """поиск минимальной даты в файле"""
    u=re.split('-', tuple[0][0].strip())
    min_data=datetime.date(int(u[0]), int(u[1]), int(u[2]))
    tuple_element=tuple[0]
    for item in tuple:
        z = re.split('-', item[0].strip())
        data_next=datetime.date(int(z[0]), int(z[1]), int(z[2]))
        if min_data>data_next and item[1]!='' :
            min_data=data_next
            tuple_element=item
    print (tuple_element)
    tuple_list = []
    for item in tuple:
        if tuple_element==item:
            continue
        tuple_list.append(item,)
    return tuple_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="пример работы")
    parser.add_argument('--date', type=lambda d: datetime.strptime(d, '%Y-%m-%d'), default="2023-10-9")
    parser.add_argument('--csv', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv')
    parser.add_argument('--x', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/X.csv')
    parser.add_argument('--y', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/Y.csv')
    parser.add_argument('--year', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/года')
    parser.add_argument('--week', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/недели')
    args = parser.parse_args()
    search_date = args.date
    while True:
        print("из каких файлов искать:0.исходного файла, 1.X и Y, 2.по годам, 3. по неделям, 4. хватит искать")
        param = input("введите:")
        match int(param):
            case 0:
                search_zero(search_date)
            case 1:
                search_one(search_date)
            case 2:
                search_two(search_date)
            case 3:
                search_three(search_date)
            case 4:
                break
    print("введите полный путь к файлу для поиска самой ранней даты")
    way = input("введите пусть:")
    tuple = tuple(way)
    while True:
        tuple = next(tuple)
        print("1. продолжить 2. завершить")
        i = input("введите пусть:")
        if i==2:
            break
