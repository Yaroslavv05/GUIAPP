from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow
from tablemodel import TableModel
from database import Database
from PySide6.QtWidgets import QHeaderView
from PySide6.QtCore import Slot
import math
import logging
logger = logging.getLogger(__name__)

figures = {
    "1x1": (1, 1),
    "3x5": (3, 5),
    "5x5": (5, 5),
    "7x7": (7, 7),
    "5x10": (5, 10)
}

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.calculate)
        self.pushButton_2.clicked.connect(self.add_to_table)
        self.pushButton_3.clicked.connect(self.clear_table)

        headers = ['ID', 'Сторона A', 'Сторона B', 'Вибрана фігура', 'Площа', 'Кількість фігур']
        self.model = TableModel(headers=headers)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  

        self.db = Database()
        self.load_data_from_db()

        self.row_id = self.get_last_id() + 1

    def load_data_from_db(self):
        self.model._data = self.db.fetch_all()
        self.model.layoutChanged.emit()

    def get_last_id(self):
        last_id = self.db.get_last_id()
        return last_id if last_id is not None else 0

    @Slot()
    def calculate(self):
        try:
            side_a = float(self.lineEdit.text())
            side_b = float(self.lineEdit_2.text())
            figure = self.comboBox.currentText()

            if side_a <= 0 or side_b <= 0:
                raise ValueError("Сторони повинні бути більше 0")

            area = side_a * side_b
            count_figures = math.floor(area / (figures[figure][0] * figures[figure][1]))

            self.label_4.setText(str(side_a))
            self.label_5.setText(str(side_b))
            self.label_6.setText(figure)
            self.label_7.setText(str(area))
            self.label_8.setText(str(count_figures))

        except ValueError as e:
            logger.error(e)
            QMessageBox.critical(self, "Помилка", str(e))


    @Slot()
    def add_to_table(self):
        try:
            side_a = float(self.label_4.text())
            side_b = float(self.label_5.text())
            figure = self.label_6.text()
            area = float(self.label_7.text())
            count_figures = int(self.label_8.text())

            self.db.insert_data(side_a, side_b, figure, area, count_figures)

            self.model._data.append([self.row_id, side_a, side_b, figure, area, count_figures])
            self.model.layoutChanged.emit()

            self.row_id += 1
        except Exception as e:
            logger.error(e)

    @Slot()
    def clear_table(self):
        try:
            self.db.clear_table()
            self.model._data = []
            self.model.layoutChanged.emit()
            self.row_id = 0
        except Exception as e:
            logger.error(e)
