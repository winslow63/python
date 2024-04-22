import argparse
import csv
import datetime
import os


class search_undivided_files:

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


class ssearch_in_split_files:

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


def read_csv_data_file(file_path:str)->[list,int]:
    """
    получение информации из cvs файла
    :param file_path: сылка.
    :type file_path: str
    :return: список данных из файла и количество сток в файле
    :rtype: list,int
    """
    data = []
    count=0
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=";")
        for row in csv_reader:
            data.append(row)
            count+=1
    return data,count


def read_csv_data_files_x_y(X_file:str,Y_file:str)->[list,list,int]:
    """
    получение информации из cvs файла x и y
    :param X_file: путь к файлу.
    :type X_file: str
    :param Y_file: путь к файлу.
    :type Y_file: str
    :return: список данных из файлов  (x y)  и количество сток в файле
    :rtype: list,int
    """
    data_x = []
    data_y = []
    count=0
    with open(X_file, 'r') as file:
        csv_reader = csv.reader(file, delimiter=";")
        for row in csv_reader:
            data_x.append(row)
            count+=1
    with open(Y_file, 'r') as file:
        csv_reader = csv.reader(file, delimiter=";")
        for row in csv_reader:
            data_y.append(row)

    return data_x,data_y,count


def read_csv_data_files(f_name:str)->[list,int]:
    """
    получение информации из cvs файлов
    :param f_name: путь к папке с файлами.
    :type f_name: str
    :return: список данных из файлов и количество сток в файле
    :rtype: list,int
    """
    data= []
    count=0
    f_name=f_name+"/"
    for filename in os.listdir(f_name):
        file_name=os.path.join(f_name,filename)
        with open(file_name) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")
            for row in csv_reader:
                data.append(row)
                count += 1
    return data,count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="пример работы c разными файлами")
    parser.add_argument('--date', type=datetime, default="2023-10-9")
    parser.add_argument('--csv', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv')
    parser.add_argument('--x', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/X.csv')
    parser.add_argument('--y', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/Y.csv')
    parser.add_argument('--year', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/года')
    parser.add_argument('--week', type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/недели')
    args = parser.parse_args()
    search_date=args.date
    if args.csv:
        data,count =read_csv_data_file(args.csv)
        s_iter0 =search_undivided_files(data,search_date,count)
        i=0
        for val in s_iter0:
            if val!=-1:
                  i=1
                  print(val)
                  break
        if i==0:
            print("None")
    elif args.x|args.y:
        data_x,data_y,count=read_csv_data_files_x_y(args.x,args.y)
        s_iter1 =ssearch_in_split_files(data_x,data_y,search_date,count)
        i = 0
        for val in s_iter1:
            if val != -1:
                i = 1
                print(val)
                break
        if i == 0:
            print("None")
    elif args.year:
        data, count = read_csv_data_files(args.year)
        s_iter0 = search_undivided_files(data, search_date, count)
        i = 0
        for val in s_iter0:
            if val != -1:
                i = 1
                print(val)
                break
        if i == 0:
            print("None")

    elif args.week:
        data, count = read_csv_data_files(args.week)
        s_iter0 = search_undivided_files(data, search_date, count)
        i = 0
        for val in s_iter0:
            if val != -1:
                i = 1
                print(val)
                break
        if i == 0:
            print("None")
