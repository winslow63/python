import re
import datetime
import csv

def csv_name(data,n):
    '''путь к файлу'''
    z = re.split('-', data.strip())
    past_date = datetime.date(int(z[0]), int(z[1]), int(z[2])) - datetime.timedelta(days=n-1)
    past_date = past_date.isoformat()
    csvV = ".csv"
    d="C:/Users/dog/Desktop/долги/прикладное/валюта/года/"
    slech="_"
    name_file=f"{d}{str(datetime.date(int(z[0]), int(z[1]), int(z[2])))}{slech}{str(past_date)}{csvV}"
    #print(name_file)
    return name_file

def row_quantity():
    '''подсчет строк в ссв'''
    with open("C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv") as csvfile:
        return sum(1 for line in csvfile)

def N(name_file):
    '''заполнение первой строки в ссв'''
    with open(name_file, mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Дата","Информация"])
def N_files():
    '''разделение первоначального файла на н подфайлов по условию'''
    days = 0#дни
    lines = 0# строки в ссв файле
    name_file=" "
    with open("C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        r_q=row_quantity()
        for rov in reader:
            if days >= 365:
                days = 0

            if days == 0:
                lines_left=r_q-lines
                if lines_left<365:
                    name_file = csv_name(rov['Дата'], lines_left-1)
                    N(name_file)

                else:
                    name_file=csv_name(rov['Дата'],365)
                    N(name_file)
            with open(name_file, mode="a") as csvX:
                writer = csv.writer(csvX,delimiter=";", lineterminator="\r")
                writer.writerow([rov['Дата'] , rov["Информация"]])
            days = days+1
            lines = lines+1





if __name__ == "__main__":
    N_files()