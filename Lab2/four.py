import os
import datetime
import csv
import re

def vvod():
    g = input("введите год:")
    while int(g) > 2024:
        print("некорректный ввод")
        g = input("введите год:")
    m = input("введите месяц:")
    while int(m)>12:
        print("некорректный ввод")
        m = input("введите месяц:")

    d=input("введите день:")
    if int(m)==1 or int(m)==3 or int(m)==5 or int(m)==7 or int(m)==8 or int(m)==10 or int(m)==12:
        while int(d) > 31:
            print("некорректный ввод")
            d = input("введите день:")
    if int(m) == 4 or int(m) == 6 or int(m) == 9 or int(m) == 11:
        while int(d) > 30:
            print("некорректный ввод")
            d = input("введите день:")
    if int(m)==2:
        if int(g) % 4 != 0:
            while int(d) > 28:
                print("некорректный ввод")
                d = input("введите день:")
        else:
            while int(d) > 29:
                print("некорректный ввод")
                d = input("введите день:")



    day = datetime.date(int(g), int(m), int(d))
    return (day)
def search0(v):
    i=0
    with open("C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for rov in reader:
            if rov['Дата']==str(v):
                print(rov['Информация'])
                i=1
        if i==0:
            print("None")

def search1(v):
    i=0
    p=0
    with open("C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/X.csv") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for rov in reader:
            i = i+1
            if rov["Дата"] == str(v):
                p=1
                Y(i)
        if p==0:
            print("None")
def Y(i):
    with open("C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/Y.csv") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        y = 0
        for rov in reader:
            y = y + 1
            if y == i:
                print(rov['Информация'])


def search2(v):
    i=0
    for filename in os.listdir("C:/Users/dog/Desktop/долги/прикладное/валюта/года"):
        #print(filename)
        with open("C:/Users/dog/Desktop/долги/прикладное/валюта/года/"+filename) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for rov in reader:
                if rov['Дата'] == str(v):
                    print(rov['Информация'])
                    i = 1

    if i == 0:
        print("None")
def search3(v):
    i=0
    for filename in os.listdir("C:/Users/dog/Desktop/долги/прикладное/валюта/недели"):
        #print(filename)
        with open("C:/Users/dog/Desktop/долги/прикладное/валюта/недели/" + filename) as csvfile:
        #with open("D:\\3\\"+filename) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for rov in reader:
                if rov['Дата'] == str(v):
                    print(rov['Информация'])
                    i = 1

    if i == 0:
        print("None")
def tuple(way):
    tuple_list = []
    with open(way) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for rov in reader:
            tuple_list.append((rov['Дата'],rov['Информация']),)
        return tuple_list

def next(tuple):
    u=re.split('-', tuple[0][0].strip())
    min_data=datetime.date(int(u[0]), int(u[1]), int(u[2]))
    tuple_element=tuple[0]
    #print(min_data)
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
    #v=vvod()
    v=datetime.date(2023, 10, 9)
    while True:
        print("из каких файлов искать:0.исходного файла, 1.X и Y, 2.по годам, 3. по неделям, 4. хватит искать")
        param = input("введите:")
        match int(param):
            case 0:
                search0(v)
            case 1:
                search1(v)
            case 2:
                search2(v)
            case 3:
                search3(v)
            case 4:
                break
    #print(v)
    #search0(v)
    #search0(v)
    #search1(v)
    #search2(v)
    #search3(v)
    print("введите полный путь к файлу для поиска самой ранней даты")
    way = input("введите пусть:")
    tuple = tuple(way)
    while True:

    #print(tuple)
        tuple = next(tuple)
        print("1. продолжить 2. завершить")
        i = input("введите пусть:")
        if i==2:
            break
