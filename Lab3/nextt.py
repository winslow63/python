import re
import datetime
import csv
def next(tuple):
    u = re.split('-', tuple[0][0].strip())
    min_data = datetime.date(int(u[0]), int(u[1]), int(u[2]))
    tuple_element = tuple[0]
    # print(min_data)
    for item in tuple:
        z = re.split('-', item[0].strip())
        data_next = datetime.date(int(z[0]), int(z[1]), int(z[2]))
        if min_data > data_next and item[1] != '':
            min_data = data_next
            tuple_element = item
    #print(tuple_element)
    tuple_list = []
    for item in tuple:
        if tuple_element == item:
            continue
        tuple_list.append(item, )
    return tuple_list,tuple_element
def tuple(selected_file):
    tuple_list = []
    with open(selected_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for rov in reader:
            tuple_list.append((rov['Дата'],rov['Информация']),)
        return tuple_list