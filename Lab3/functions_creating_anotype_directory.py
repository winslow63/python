import csv
import logging
import os


logging.basicConfig( level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def create_folders_with(base_dir:str)->None:
    """
    создание в директории поддиректорий
    :param base_dir: путь к папке для создания поддиректорий.
    :type base_dir: str
    """
    new_folder_names=['X Y','года','недели']
    for folder_name in new_folder_names:
        folder_path = os.path.join(base_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        logging.info(f"Создана папка: {folder_path}")


def check_file_existence(directory:str, filename:str)->bool:
    """
    существование файла в директории
    :param directory: путь к папке.
    :type directory: str
    :param filename: имя файла.
    :type filename: str
    :return: есть ли файл в директории
    :rtype:bool
    """
    file_path = os.path.join(directory, filename)
    exists = os.path.exists(file_path)
    logging.debug(f"Проверка существования файла: {file_path} - {'существует' if exists else 'не существует'}")
    return exists


def create_annotation_file(folderpath:str,filepath:str,csvs:str)->None:
    """
    создание файла анотации
    :param folderpath: путь к папке.
    :type folderpath: str
    :param filepath: путь к файлу анотации.
    :type filepath: str
    :param csvs: имя файла исходного.
    :type csvs: str
    """
    url="http://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To="
    try:
        if check_file_existence(folderpath, csvs):
            file= os.path.join(folderpath,csvs)
            with open(file) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=";")
                for rov in reader:
                    with open(filepath, 'a') as file:
                        file.write(f'{url}{rov['Дата'].replace("-",".")}\n')
    except Exception as e:
        logging.error(f"Ошибка при вводе оздании файла анотации {filepath}: {e}")
