import os
import csv
def create_folders_with(base_dir):
    new_folder_names=['X Y','года','недели']
    for folder_name in new_folder_names:
        folder_path = os.path.join(base_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

def check_file_existence(directory, filename):
    file_path = os.path.join(directory, filename)
    return os.path.exists(file_path)
def create_annotation_file(folderpath,filepath):
    if check_file_existence(folderpath, 'course.csv'):
        with open(f'{folderpath}/course.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for rov in reader:
                with open(filepath, 'a') as file:
                    file.write(f'http://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={rov['Дата'].replace("-",".")}\n')

