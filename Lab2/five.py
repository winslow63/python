import os
import datetime
import csv
import re
import argparse

class search_zero:
    def __init__(self, data:list,search_date:datetime,count:int)->None:
        self.data = data
        self.search_date = search_date
        self.i=0
        self.count=count

    def __iter__(self)->"search_zero":
        return self

    def __next__(self):
        if self.i<self.count:
            if self.data[self.i][0] == str(self.search_date):

                return self.data[self.i][1]
            else:
                self.i+=1
                return -1
        else:
            raise StopIteration


class search_one:
    def __init__(self, data_x:list,data_y:list,search_date:datetime,count:int)->None:
        self.data_x = data_x
        self.data_y = data_y
        self.search_date = search_date
        self.i=0
        self.count=count


    def __iter__(self)->"search_zero":
        return self


    def __next__(self):
        if self.i<self.count:
            if self.data_x[self.i][0] == str(self.search_date):

                return self.data_y[self.i][0]
            else:
                self.i+=1
                return -1
        else:
            raise StopIteration


def read_csv_data0(file_path:str)->[list,int]:
    """
    получение информации из cvs файла
    """
    data = []
    count=0
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=";")
        for row in csv_reader:
            data.append(row)
            count+=1
    return data,count


def read_csv_data1(X:str,Y:str)->[list,list,int]:
    """
        получение информации из cvs файла x и y
        """
    data_x = []
    data_y = []
    count=0
    with open(X, 'r') as file:
        csv_reader = csv.reader(file, delimiter=";")
        for row in csv_reader:
            data_x.append(row)
            count+=1
    with open(Y, 'r') as file:
        csv_reader = csv.reader(file, delimiter=";")
        for row in csv_reader:
            data_y.append(row)

    return data_x,data_y,count


def read_csv_data2_3(f_name:str)->[list,int]:
    """
        получение информации из cvs файлов
        """
    data= []
    count=0
    for filename in os.listdir(f_name):
        with open(f_name+"/"+filename) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")
            for row in csv_reader:
                data.append(row)
                count += 1
    return data,count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="пример работы")
    parser.add_argument('--date', type=datetime, default="2023-10-9")
    parser.add_argument('--csv', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv')
    parser.add_argument('--x', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/X.csv')
    parser.add_argument('--y', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/Y.csv')
    parser.add_argument('--year', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/года')
    parser.add_argument('--week', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/недели')
    args = parser.parse_args()
    search_date=args.date
    #search_date=datetime.date(2023, 10, 9)
    while True:
        print("из каких файлов искать:0.исходного файла, 1.X и Y, 2.по годам, 3. по неделям, 4. хватит искать")
        param = input("введите:")
        match int(param):
            case 0:
                data,count =read_csv_data0(args.csv)
                s_iter0 =search_zero(data,search_date,count)
                i=0
                for val in s_iter0:
                    if val!=-1:
                        i=1
                        print(val)
                        break
                if i==0:
                    print("None")
            case 1:
                data_x,data_y,count=read_csv_data1(args.x,args.y)
                s_iter1 =search_one(data_x,data_y,search_date,count)
                i = 0
                for val in s_iter1:
                    if val != -1:
                        i = 1
                        print(val)
                        break
                if i == 0:
                    print("None")
            case 2:
                data, count = read_csv_data2_3(args.year)
                s_iter0 = search_zero(data, search_date, count)
                i = 0
                for val in s_iter0:
                    if val != -1:
                        i = 1
                        print(val)
                        break
                if i == 0:
                    print("None")

            case 3:
                data, count = read_csv_data2_3(args.week)
                s_iter0 = search_zero(data, search_date, count)
                i = 0
                for val in s_iter0:
                    if val != -1:
                        i = 1
                        print(val)
                        break
                if i == 0:
                    print("None")
            case 4:
                break
