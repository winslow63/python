import os
import csv

def check_file_existence(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.exists(file_path)

def check_file_extension(filename, desired_extension):
    return filename.endswith(desired_extension)
def Y(i,folderpath_search):
    #Y=folderpath_search.replace("X.csv", "")
    with open(f'{folderpath_search}/Y.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        y = 0
        for rov in reader:
            y = y + 1
            if y == i:
                return (rov['Информация'])

def get_data_by_date(data, folderpath_search):
    if check_file_existence(folderpath_search,'course.csv'):
        i = 0
        with open(f'{folderpath_search}/course.csv') as csvfile:
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
        with open(f'{folderpath_search}/X.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for rov in reader:
                i = i + 1
                if rov["Дата"] == str(data):
                    p = 1
                    return Y(i, folderpath_search)
            if p == 0:
                return ("None")
    i = 0
    for filename in os.listdir(folderpath_search):
        if check_file_extension(filename, ".csv"):
            with open(f'{folderpath_search}/{filename}') as csvfile:
                # with open("D:\\3\\"+filename) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=";")
                for rov in reader:
                    if rov['Дата'] == str(data):
                        return (rov['Информация'])
                        i = 1

    if i == 0:
        return ("None")
