import os
import requests
import re
import pathlib
import datetime
import csv
import argparse


def Urls(url:str,date:str)->dict:
    """
    получение данных из файла
    """
    date.replace('-', '/')
    url = url.format(date=date)
    html = requests.get(url)
    if html.status_code != 200:
        return {"error"}
    json = html.json()
    return json


def write_Csv(course:str,data:str,way_file:str)->None:
    """добавление в файл"""
    with open(way_file, mode="a", encoding="utf-8") as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
        file_writer.writerow([data,course])


def business_logic(url:str,way_file:str)->None:
    """
    бизнес логика
    """
    date = datetime.date.today()
    n = 0
    while n < 9000:  # счетчик количества длей для считывания долара
        date_str=str(date).replace('-', '/')
        URL = Urls(url,date_str)
        if "error" in URL:
            write_Csv("nane",date_str,way_file)
            date -= datetime.timedelta(days=1)
        else:
            course=URL["Valute"]["USD"]["Value"]
            date_str=date_str.replace('/', '-')
            write_Csv(course, date_str, way_file)
            date -= datetime.timedelta(days=1)

        n = n + 1


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="курс")
    parser.add_argument('--url',type=str, default="https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js")
    parser.add_argument('--way_file',type=str, default='C:/Users/dog/Desktop/долги/прикладное/валюта/course.csv')
    args = parser.parse_args()
    if os.path.exists(args.way_file)==True:
        file = pathlib.Path(args.way_file)
        file.unlink()
    with open(args.way_file, mode="a") as csvfile:
        writer = csv.writer(csvfile, delimiter=";", lineterminator="\r")
        writer.writerow(["Дата","Информация"])
    business_logic(args.url,args.way_file)