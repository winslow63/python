import argparse

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication, QFileDialog
import functions
import zero
import one
import two
import three
import search
import nextt


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
        self.create_course_button = QtWidgets.QPushButton("создать файл course.csv")
        self.create_course_button.clicked.connect(self.create_course)
        self.layout.addWidget(self.create_course_button)
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
            functions.create_folders_with(self.folderpath)
            QtWidgets.QMessageBox.information(self, "Success", "Папка выбрана")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Не выбрана папка")


    def create_course(self)->None:
        """создание исходного файла"""
        try:
            zero.create_course(self.folderpath)
            QtWidgets.QMessageBox.information(self, "Success", "Файл course.csv был создан")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Произошла ошибка при создании файла course.csv: {e}")


    def split_xy(self)->None:
        """создание файлов x и y"""
        try:
            one.split_csv_xy(self.folderpath)
            QtWidgets.QMessageBox.information(self, "Success", "Файлы X.csv и Y.csv созданы")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Произошла ошибка при создании файлов X.csv Y.csv: {e}")


    def split_by_year(self)->None:
        """создание файлов по годам"""
        try:
            two.split_csv_by_year(self.folderpath)
            QtWidgets.QMessageBox.information(self, "Success", "Файлы по годам созданы")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Произошла ошибка при создании файлов по годам: {e}")


    def split_by_week(self)->None:
        """создание файлов по неделям"""
        try:
            three.split_csv_by_week(self.folderpath)
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
            #selected_file = QFileDialog.getOpenFileName(caption="Выберите файл")
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
                self.tuple_list=nextt.tuple(self.file)
            self.tuple_list,next = nextt.next(self.tuple_list)
            if next:
                QtWidgets.QMessageBox.information(self, "Данные", str(next))
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"Произошла ошибка")


    def create_annotation(self)->None:
        """создание файла анотации"""
        save_dialog = QFileDialog()
        filepath, _ = save_dialog.getSaveFileName(
            self, "Сохранить файл аннотации", "", "Text Files (*.txt)")

        if functions.check_file_existence(self.folderpath,args.csv):
            functions.create_annotation_file(self.folderpath, filepath, args.csv)
            QtWidgets.QMessageBox.information(self, "Success", "Файл аннотации создан")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Не выбран файл назначения")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="пример работы")
    parser.add_argument('--csv', type=str, default='course.csv')
    args = parser.parse_args()
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()