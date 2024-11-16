import os

import sys

from PyQt5 import QtCore

from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

import first_script
import script_three
import script_two
import iterator_and_function


class Window(QMainWindow):
    def button_first_click(self):
        dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        first_script.first_script(dirlist)

    def button_second_click(self):
        dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        script_two.script_two(dirlist)

    def button_three_click(self):
        dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
        script_three.script_three(dirlist)

    def one_star_click(self):
        # self.one_star.hide()
        self.two_star.hide()
        self.three_star.hide()
        self.four_star.hide()
        self.five_star.hide()
        self.start_iterator.hide()
        self.main_text.show()
        self.back.show()
        self.main_text.setText("asds")
        elem = str(next(self.iterat_1))
        if elem == "['absolut path,relativ path,quote']":
            elem = str(next(self.iterat_1))
        self.one_star.setText("Следующий отзыв")
        self.one_star.adjustSize()
        self.one_star.move(750, 50)
        self.read_directory(elem)

    def two_star_click(self):
        self.one_star.hide()
        # self.two_star.hide()
        self.three_star.hide()
        self.four_star.hide()
        self.five_star.hide()
        self.start_iterator.hide()
        self.main_text.show()
        self.back.show()
        self.main_text.setText("asds")
        elem = str(next(self.iterat_2))
        if elem == "['absolut path, relativ path, quote']":
            elem = str(next(self.iterat_2))
        self.two_star.setText("Следующий отзыв")
        self.two_star.adjustSize()
        self.two_star.move(750, 50)
        self.read_directory(elem)

    def three_star_click(self):
        self.one_star.hide()
        self.two_star.hide()
        # self.three_star.hide()
        self.four_star.hide()
        self.five_star.hide()
        self.start_iterator.hide()
        self.main_text.show()
        self.back.show()
        self.main_text.setText("asds")
        elem = str(next(self.iterat_3))
        if elem == "['absolut path, relativ path, quote']":
            elem = str(next(self.iterat_3))
        self.three_star.setText("Следующий отзыв")
        self.three_star.adjustSize()
        self.three_star.move(750, 50)
        self.read_directory(elem)

    def four_star_click(self):
        self.one_star.hide()
        self.two_star.hide()
        self.three_star.hide()
        # self.four_star.hide()
        self.five_star.hide()
        self.main_text.show()
        self.back.show()
        self.start_iterator.hide()
        self.main_text.setText("asds")
        elem = str(next(self.iterat_4))
        if elem == "['absolut path, relativ path, quote']":
            elem = str(next(self.iterat_4))
        self.four_star.setText("Следующий отзыв")
        self.four_star.adjustSize()
        self.four_star.move(750, 50)
        self.read_directory(elem)

    def five_star_click(self):
        # self.next_response.show()
        self.back.show()
        self.one_star.hide()
        self.two_star.hide()
        self.three_star.hide()
        self.four_star.hide()
        # self.five_star.hide()
        self.start_iterator.hide()
        self.main_text.show()
        self.main_text.setText("asds")
        elem = str(next(self.iterat_5))
        if elem == "['absolut path, relativ path, quote']":
            elem = str(next(self.iterat_5))
        self.five_star.setText("Следующий отзыв")
        self.five_star.adjustSize()
        self.five_star.move(750, 50)
        self.read_directory(elem)

    # def next_response_click(self):
    #  print("f")

    def back_click(self):
        print("fg")
        self.button_first.show()
        self.button_second.show()
        self.button_three.show()
        self.start_iterator.show()
        self.one_star.hide()
        self.two_star.hide()
        self.three_star.hide()
        self.four_star.hide()
        self.five_star.hide()
        self.main_text.hide()
        self.back.hide()
        # self.next_response.hide()

    def read_directory(self, elem: str) -> None:
        """Read directory file and print text on labal opinion"""
        os.chdir(os.path.dirname(__file__))
        self.main_text.clear()
        directory = elem.split(",")
        print(directory[1])
        with open(directory[1], "r", encoding="utf-8") as f:
            text = f.read()
        text = text.split("\n")
        spisok = []
        print(text[1])

        for element in text:
            for i in range(1, (len(element) // 100) + 1):
                if element[100 * i - 1] != " ":
                    j = 100 * i - 1
                    while element[j] != " ":
                        j = j - 1
                    element = element[:j] + "\n" + element[j:]
                else:
                    element = element[:100 * i - 1] + "\n" + element[100 * i - 1:]
            spisok.append(element)
        self.main_text.setText(
            spisok[1] + "\n" + spisok[2] + "\n" + spisok[3] + "\n" + spisok[4] + "\n" + spisok[5] + "\n")

    def start_iterator_click(self):
        self.button_defult()
        self.button_first.hide()
        self.button_second.hide()
        self.button_three.hide()
        # self.start_iterator.hide()
        self.one_star.show()
        self.two_star.show()
        self.three_star.show()
        self.four_star.show()
        self.five_star.show()

    def button_defult(self):
        self.button_first.setText("Первый скрипт")  # вписываем текст
        self.button_second.setText("Второй скрипт")
        self.button_three.setText("Третий скрипт")
        self.start_iterator.setText("Запустить итератор")
        self.one_star.setText("***1***")
        self.two_star.setText("***2***")
        self.three_star.setText("***3***")
        self.four_star.setText("***4***")
        self.five_star.setText("***5***")
        # self.next_response.setText("Следующий отзыв")
        self.back.setText("Выйти в меню")

        self.button_first.setFixedSize(150, 30)  # обновляем размер кнопок под текст
        self.button_second.setFixedSize(150, 30)
        self.button_three.setFixedSize(150, 30)
        self.start_iterator.setFixedSize(150, 30)
        # self.five_star.setFixedSize(100, 30)
        self.five_star.setGeometry(100, 30, 100, 30)
        self.four_star.setGeometry(100, 30, 100, 30)
        self.three_star.setGeometry(100, 30, 100, 30)
        self.two_star.setGeometry(100, 30, 100, 30)
        self.one_star.setGeometry(100, 30, 100, 30)
        # self.next_response.adjustSize()
        self.back.adjustSize()

        self.button_first.move(50, 50)  # размещаем кнопки
        self.button_second.move(300, 50)
        self.button_three.move(550, 50)
        self.start_iterator.move(800, 50)
        self.five_star.move(825, 100)
        self.four_star.move(825, 150)
        self.three_star.move(825, 200)
        self.two_star.move(825, 250)
        self.one_star.move(825, 300)
        self.back.move(150, 50)
        # self.next_response.move(750, 50)

        self.one_star.hide()
        self.two_star.hide()
        self.three_star.hide()
        self.four_star.hide()
        self.five_star.hide()
        #  self.next_response.hide()
        self.back.hide()

    def __init__(self) -> None:
        super(Window, self).__init__()
        if not os.path.isfile("C:\\Users\\Солнышко\\PycharmProjects\\Laba_python\\Dataset\\test_csv.csv"):
            dirlist = QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")
            first_script.first_script(dirlist)
        self.button_first = QtWidgets.QPushButton(self)  # создаем кнопочки
        self.button_second = QtWidgets.QPushButton(self)
        self.button_three = QtWidgets.QPushButton(self)
        self.start_iterator = QtWidgets.QPushButton(self)
        self.one_star = QtWidgets.QPushButton(self)
        self.two_star = QtWidgets.QPushButton(self)
        self.three_star = QtWidgets.QPushButton(self)
        self.four_star = QtWidgets.QPushButton(self)
        self.five_star = QtWidgets.QPushButton(self)
        # self.next_response = QtWidgets.QPushButton(self)
        self.back = QtWidgets.QPushButton(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setStyleSheet(
            "border-style: solid;"
            "border-width: 1px;"
            "border-color: black; "
        )
        self.main_text.setAlignment(QtCore.Qt.AlignLeft)
        self.main_text.setFixedSize(990, 490)
        self.main_text.move(0, 100)
        self.main_text.adjustSize()
        self.main_text.setText("uhjgghjkhgbhjnh")
        self.main_text.setFont(QFont("Times", 11))
        self.main_text.hide()

        self.button_defult()

        self.button_first.clicked.connect(self.button_first_click)
        self.button_second.clicked.connect(self.button_second_click)
        self.button_three.clicked.connect(self.button_three_click)
        self.start_iterator.clicked.connect(self.start_iterator_click)
        self.one_star.clicked.connect(self.one_star_click)
        self.two_star.clicked.connect(self.two_star_click)
        self.three_star.clicked.connect(self.three_star_click)
        self.four_star.clicked.connect(self.four_star_click)
        self.five_star.clicked.connect(self.five_star_click)
        # self.next_response.clicked.connect(self.next_response_click)
        self.back.clicked.connect(self.back_click)

        self.iterat_1 = iterator_and_function.Iterator("C:\\Users\\Солнышко\\PycharmProjects\\Laba_python\\Dataset\\test_csv.csv", 1)
        self.iterat_2 = iterator_and_function.Iterator("C:\\Users\\Солнышко\\PycharmProjects\\Laba_python\\Dataset\\test_csv.csv", 2)
        self.iterat_3 = iterator_and_function.Iterator("C:\\Users\\Солнышко\\PycharmProjects\\Laba_python\\Dataset\\test_csv.csv", 3)
        self.iterat_4 = iterator_and_function.Iterator("C:\\Users\\Солнышко\\PycharmProjects\\Laba_python\\Dataset\\test_csv.csv", 4)
        self.iterat_5 = iterator_and_function.Iterator("C:\\Users\\Солнышко\\PycharmProjects\\Laba_python\\Dataset\\test_csv.csv", 5)


def application() -> None:
    """"Start aplication mainwindow"""
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize(1000, 600)
    window.setObjectName("MainWindow")
    # window.setStyleSheet("#MainWindow{border-image:url(C:\Games\Phon.jpg}")
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
