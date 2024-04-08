import unittest
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

class TestMainWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.window = MainWindow()

    def test_calculate(self):
        self.window.lineEdit.setText("5")
        self.window.lineEdit_2.setText("10")
        self.window.comboBox.setCurrentIndex(0)

        self.window.calculate()

        self.assertEqual(self.window.label_4.text(), "5.0")
        self.assertEqual(self.window.label_5.text(), "10.0")
        self.assertEqual(self.window.label_6.text(), "1x1")
        self.assertEqual(self.window.label_7.text(), "50.0")
        self.assertEqual(self.window.label_8.text(), "50")

    def test_add_to_table(self):
        self.window.label_4.setText("5")
        self.window.label_5.setText("10")
        self.window.label_6.setText("1x1")
        self.window.label_7.setText("50.0")
        self.window.label_8.setText("50")

        self.window.add_to_table()

        self.assertEqual(self.window.tableView.model()._data[0][1], 5.0)
        self.assertEqual(self.window.tableView.model()._data[0][2], 10.0)
        self.assertEqual(self.window.tableView.model()._data[0][3], "1x1")
        self.assertEqual(self.window.tableView.model()._data[0][4], 50.0)
        self.assertEqual(self.window.tableView.model()._data[0][5], 50)

    def test_clear_table(self):
        self.window.clear_table()

        self.assertEqual(len(self.window.tableView.model()._data), 0)
    
    def tearDown(self):
        self.window.close()
        del self.window

    @classmethod
    def tearDownClass(cls):
        del cls.app

if __name__ == '__main__':
    unittest.main()
