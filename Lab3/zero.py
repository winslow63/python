import os
import requests
import re
import pathlib
import datetime
import csv

def word_find(line):
    if line.find("USD") != -1:
        return 1
    else:
        return 0

def dollar_search(file):
    y=0
    with open(file) as f:
        for i,x in enumerate(f, start=1):
            common = word_find(x)
            y=y-1
            if common==1:
                y=7
            if y==1:
                z = re.split('<td>|</td>|\n', x.strip())
                return z[1]

def URLS(n):
    URL = 'http://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To='
    past_date = datetime.datetime.today() - datetime.timedelta(days=n)
    if past_date.day<10:
        nul="0"
        day=f"{nul}{str(past_date.day)}"
    else:
        day=str(past_date.day)
    if past_date.month<10:
        nul = "0"
        month=f"{nul}{str(past_date.month)}"
    else:
        month=str(past_date.month)
    points = "."
    data = f"{day}{points}{month}{points}{str(past_date.year)}"
    points = "-"
    #existing_date = datetime.date(past_date.year, past_date.month, past_date.day)
    data1 = f"{str(past_date.year)}{points}{month}{points}{day}"
    URL1 = f"{URL}{data}"
    return URL1,data1

def writeCSV(course,data,folderpath):
    with open(f'{folderpath}/course.csv', mode="a", newline='', encoding="utf-8") as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        #iso_date = existing_date.isoformat()
        file_writer.writerow([data,course])
def create_course(folderpath):
    if os.path.exists(f'{folderpath}/course.csv')==True:
        file = pathlib.Path(f'{folderpath}/course.csv')
        file.unlink()
    with open(f'{folderpath}/course.csv', mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Дата","Информация"])

    n=0
    while n<1000:#счетчик количества длей для считывания долара
        URL,data=URLS(n)
        html_page = requests.get(URL)
        file_1 = open('D:/HTML.txt', 'w')
        file_1.write(html_page.text)
        file_1.close()
        course=dollar_search("D:/HTML.txt")
        writeCSV(course,data,folderpath)
        n=n+1
    file=pathlib.Path("D:/HTML.txt")
    file.unlink()