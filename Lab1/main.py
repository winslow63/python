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
    URL1 = f"{URL}{data}"
    return URL1,data

def writeCSV(course,data):
    with open("C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv", mode="a", encoding="utf-8") as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow([data,course])

if __name__ == '__main__':
    if os.path.exists("C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv")==True:
        file = pathlib.Path("C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv")
        file.unlink()
    with open("C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv", mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Дата","Информация"])

    n=0
    while n<9000:#счетчик количества длей для считывания долара
        URL,data=URLS(n)
        html_page = requests.get(URL)
        file_1 = open('D:/HTML.txt', 'w')
        file_1.write(html_page.text)
        file_1.close()
        course=dollar_search("D:/HTML.txt")
        writeCSV(course,data)
        n=n+1
    file=pathlib.Path("D:/HTML.txt")
    file.unlink()