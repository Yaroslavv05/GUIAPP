from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt


'''
Цей клас TableModel є підкласом QAbstractTableModel і використовується для створення моделі таблиці у фреймворку PySide6. 
У конструкторі він приймає дані для заповнення таблиці (data) і заголовки стовпців (headers). 
Методи rowCount та columnCount повертають кількість рядків і стовпців у таблиці відповідно. Метод data використовується для отримання даних для певної клітинки таблиці за її індексом, 
а метод headerData - для отримання заголовків стовпців.
'''

class TableModel(QAbstractTableModel):
    def __init__(self, data=None, headers=None):
        super().__init__()
        self._data = data or []
        self._headers = headers or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._data[0]) if self._data else 0

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if section < len(self._headers):
                return self._headers[section]
        return super().headerData(section, orientation, role)
