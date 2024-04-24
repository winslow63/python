import argparse
import os
import functions_creating_anotype_directory
import next_element
import search
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QFileDialog
from Lab2.creature_x_y_file import x_file, y_file
from Lab2.creature_year_files import n_files
from Lab2.creature_week_files import separation_files_n


class MainWindow(QtWidgets.QMainWindow):


    def __init__(self)->None:
        self.tuple_list=[]
        super(MainWindow, self).__init__()
        self.main_widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
        self.folder_button = QtWidgets.QPushButton("Выбрать папку датасета")
        self.folder_button.clicked.connect(self.choose_folder)
        self.layout.addWidget(self.folder_button)
        self.split_xy_button = QtWidgets.QPushButton("Разделить на файлы X.csv и Y.csv")
        self.split_xy_button.clicked.connect(self.split_xy)
        self.layout.addWidget(self.split_xy_button)
        self.split_by_year_button = QtWidgets.QPushButton("Разделить по годам")
        self.split_by_year_button.clicked.connect(self.split_by_year)
        self.layout.addWidget(self.split_by_year_button)
        self.split_by_week_button = QtWidgets.QPushButton("Разделить по неделям")
        self.split_by_week_button.clicked.connect(self.split_by_week)
        self.layout.addWidget(self.split_by_week_button)
        self.date_edit = QtWidgets.QDateEdit()
        self.date_edit.setDisplayFormat("yyyy-MM-dd")
        self.layout.addWidget(self.date_edit)
        self.directory_button = QtWidgets.QPushButton("Выберите директорию для поиска")
        self.directory_button.clicked.connect(self.directory)
        self.layout.addWidget(self.directory_button)
        self.get_data_button = QtWidgets.QPushButton("Получить данные")
        self.get_data_button.clicked.connect(self.get_data)
        self.layout.addWidget(self.get_data_button)
        self.file_button = QtWidgets.QPushButton("Выберите файл для поиска самой раней даты")
        self.file_button.clicked.connect(self.file)
        self.layout.addWidget(self.file_button)
        self.next_button = QtWidgets.QPushButton("Самая ранняя дата в файле")
        self.next_button.clicked.connect(self.next)
        self.layout.addWidget(self.next_button)
        self.create_annotation_button = QtWidgets.QPushButton("Создать файл аннотации")
        self.create_annotation_button.clicked.connect(self.create_annotation)
        self.layout.addWidget(self.create_annotation_button)


    def choose_folder(self)->None:
        """выбор папки для записи файлов"""
        folderpath = QFileDialog.getExistingDirectory(self, 'Выберите папку')
        if folderpath:
            self.folderpath= folderpath
            functions_creating_anotype_directory.create_folders_with(self.folderpath)
            QtWidgets.QMessageBox.information(self, "Success", "Папка выбрана")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Не выбрана папка")



    def split_xy(self)->None:
        """создание файлов x и y"""
        try:
            files_x=os.path.join(self.folderpath,args.x)
            files_y = os.path.join(self.folderpath, args.y)
            files_csv=os.path.join(self.folderpath, args.csv)
            x_file(files_x,files_csv)
            y_file(files_y, files_csv)
            QtWidgets.QMessageBox.information(self, "Success", "Файлы X.csv и Y.csv созданы")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Произошла ошибка при создании файлов X.csv Y.csv: {e}")


    def split_by_year(self)->None:
        """создание файлов по годам"""
        try:
            files_csv = os.path.join(self.folderpath, args.csv)
            files_n = os.path.join(self.folderpath, args.year)
            n_files(files_csv,files_n)
            QtWidgets.QMessageBox.information(self, "Success", "Файлы по годам созданы")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Произошла ошибка при создании файлов по годам: {e}")


    def split_by_week(self)->None:
        """создание файлов по неделям"""
        try:
            files_csv = os.path.join(self.folderpath, args.csv)
            files_n = os.path.join(self.folderpath, args.week)
            separation_files_n(files_csv,files_n)
            QtWidgets.QMessageBox.information(self, "Success", "Файлы по неделям созданы")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Произошла ошибка при создании файлов по неделям: {e}")


    def directory(self)->None:
        """выбор папки для поиска по дате"""
        self.folderpath_search = QFileDialog.getExistingDirectory(self, 'Выберите папку')
        if self.folderpath_search:
            QtWidgets.QMessageBox.information(self, "Success", "Папка выбрана")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Не выбрана папка")



    def get_data(self)->None:
        """поиск по дате"""
        try:
            date = self.date_edit.date().toString("yyyy-MM-dd")
            data = search.get_data_by_date(date,self.folderpath_search)
            if data:
                QtWidgets.QMessageBox.information(self, "Data", data)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Произошла ошибка при поиске данных")



    def file(self)->None:
        """выбор файла для поиска минимальной даты"""
        selected_file = QFileDialog.getOpenFileName(caption="Выберите файл")
        if selected_file:
            self.file = selected_file[0]
            self.tuple_list = []
            QtWidgets.QMessageBox.information(self, "Success", "файл выбрана")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Не выбран файл")



    def next(self)->None:
        """самая раняя дата"""
        try:
            if self.tuple_list==[]:
                self.tuple_list=next_element.tuple(self.file)
            self.tuple_list,next = next_element.next(self.tuple_list)
            if next:
                QtWidgets.QMessageBox.information(self, "Данные", str(next))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Произошла ошибка")


    def create_annotation(self)->None:
        """создание файла анотации"""
        save_dialog = QFileDialog()
        filepath, _ = save_dialog.getSaveFileName(
            self, "Сохранить файл аннотации", "", "Text Files (*.txt)")

        if functions_creating_anotype_directory.check_file_existence(self.folderpath,args.csv):
            functions_creating_anotype_directory.create_annotation_file(self.folderpath, filepath, args.csv)
            QtWidgets.QMessageBox.information(self, "Success", "Файл аннотации создан")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Не выбран файл назначения")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="пример работы")
    parser.add_argument('--csv', type=str, default='course.csv')
    parser.add_argument('--x', type=str, default='X Y/X.csv')
    parser.add_argument('--y', type=str, default='X Y/Y.csv')
    parser.add_argument('--year', type=str, default='года')
    parser.add_argument('--week', type=str, default='недели')
    args = parser.parse_args()
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()