import os
import datetime
import csv
import re
class search0:
    def __init__(self, data,v,count):
        self.data = data
        self.v = v
        self.i=0
        self.count=count

    def __iter__(self):
        return self

    def __next__(self):
        if self.i<self.count:
            if self.data[self.i][0] == str(self.v):

                return self.data[self.i][1]
            else:
                self.i+=1
                return -1
                #raise StopIteration
        else:
            raise StopIteration
class search1:
    def __init__(self, X,Y,v,count):
        self.X = X
        self.Y = Y
        self.v = v
        self.i=0
        self.count=count

    def __iter__(self):
        return self

    def __next__(self):
        if self.i<self.count:
            if self.X[self.i][0] == str(self.v):

                return self.Y[self.i][0]
            else:
                self.i+=1
                return -1
                #raise StopIteration
        else:
            raise StopIteration

def read_csv_data0(file_path):
    data = []
    count=0
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=";")
        for row in csv_reader:
            data.append(row)
            count+=1
    return data,count

def read_csv_data1(X,Y):
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

def read_csv_data2_3(f_name):
    data= []
    count=0
    for filename in os.listdir(f_name):
        #print(filename)
        with open(f_name+"/"+filename) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=";")
            for row in csv_reader:
                data.append(row)
                count += 1
    return data,count

if __name__ == "__main__":
#s_iter1 = SimpleIterator(3)
    v=datetime.date(2023, 10, 9)
    while True:
        print("из каких файлов искать:0.исходного файла, 1.X и Y, 2.по годам, 3. по неделям, 4. хватит искать")
        param = input("введите:")
        match int(param):
            case 0:
                data,count =read_csv_data0("C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv")
                s_iter0 =search0(data,v,count)
                i=0
                for val in s_iter0:
                    if val!=-1:
                        i=1
                        print(val)
                        break
                if i==0:
                    print("None")
            case 1:
                data_x,data_y,count=read_csv_data1("C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/X.csv","C:/Users/dog/Desktop/долги/прикладное/валюта/X Y/Y.csv")
                s_iter1 =search1(data_x,data_y,v,count)
                i = 0
                for val in s_iter1:
                    if val != -1:
                        i = 1
                        print(val)
                        break
                if i == 0:
                    print("None")
            case 2:
                data, count = read_csv_data2_3("C:/Users/dog/Desktop/долги/прикладное/валюта/года")
                s_iter0 = search0(data, v, count)
                i = 0
                for val in s_iter0:
                    if val != -1:
                        i = 1
                        print(val)
                        break
                if i == 0:
                    print("None")

            case 3:
                data, count = read_csv_data2_3("C:/Users/dog/Desktop/долги/прикладное/валюта/недели")
                s_iter0 = search0(data, v, count)
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
