import csv
import datetime
import re


def next(tuple:list)->list:
    """
    поиск минимальной даты в файле
    :param tuple: список данных из файла.
    :type tuple: list
    :return: список данных из файла без последнего элемента
    :rtype: list
    """
    datas = re.split('-', tuple[0][0].strip())
    min_data = datetime.date(int(datas[0]), int(datas[1]), int(datas[2]))
    tuple_element = tuple[0]
    for item in tuple:
        datass = re.split('-', item[0].strip())
        data_next = datetime.date(int(datass[0]), int(datass[1]), int(datass[2]))
        if min_data > data_next and item[1] != '':
            min_data = data_next
            tuple_element = item
    tuple_list = []
    for item in tuple:
        if tuple_element == item:
            continue
        tuple_list.append(item, )
    return tuple_list,tuple_element


def tuple(selected_file:str)->list:
    """
    вывод списка информации из файла
    :param selected_file: путь к файлу.
    :type selected_file: str
    :return: список данных из файла
    :rtype: list
    """
    tuple_list = []
    with open(selected_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for rov in reader:
            tuple_list.append((rov['Дата'],rov['Информация']),)
        return tuple_list