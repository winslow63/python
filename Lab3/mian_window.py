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
    def __init__(self):
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




    def choose_folder(self):
        folderpath = QFileDialog.getExistingDirectory(self, 'Выберите папку')
        self.folderpath= folderpath
        functions.create_folders_with(self.folderpath)

    def create_course(self):
        zero.create_course(self.folderpath)
        QtWidgets.QMessageBox.information(self, "Success", "Файл course.csv был создан")

    def split_xy(self):
        one.split_csv_xy(self.folderpath)
        QtWidgets.QMessageBox.information(self, "Success", "Файлы X.csv и Y.csv созданы")

    def split_by_year(self):
        two.split_csv_by_year(self.folderpath)
        QtWidgets.QMessageBox.information(self, "Success", "Файлы по годам созданы")

    def split_by_week(self):
        three.split_csv_by_week(self.folderpath)
        QtWidgets.QMessageBox.information(self, "Success", "Файлы по неделям созданы")

    def directory(self):
        self.folderpath_search = QFileDialog.getExistingDirectory(self, 'Выберите папку')
        #selected_file = QFileDialog.getOpenFileName(caption="Выберите файл")

        #self.tuple_list=[]

    def get_data(self):
        date = self.date_edit.date().toString("yyyy-MM-dd")
        #selected_file = QFileDialog.getOpenFileName(caption="Выберите файл")
        data = search.get_data_by_date(date,self.folderpath_search)
        if data:
            QtWidgets.QMessageBox.information(self, "Data", data)

    def file(self):
        selected_file = QFileDialog.getOpenFileName(caption="Выберите файл")
        self.file = selected_file[0]
        self.tuple_list=[]

    def next(self):
        #selected_file = QFileDialog.getOpenFileName(caption="Выберите файл")
        if self.tuple_list==[]:
            self.tuple_list=nextt.tuple(self.file)
        self.tuple_list,next = nextt.next(self.tuple_list)
        if next:
            QtWidgets.QMessageBox.information(self, "Данные", str(next))

    def create_annotation(self):
        save_dialog = QFileDialog()
        filepath, _ = save_dialog.getSaveFileName(
            self, "Сохранить файл аннотации", "", "Text Files (*.txt)")

        if filepath:
            functions.create_annotation_file(self.folderpath, filepath)
            QtWidgets.QMessageBox.information(self, "Success", "Файл аннотации создан")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Не выбран файл назначения")








if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()