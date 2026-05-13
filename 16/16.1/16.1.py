import sys
import traceback
from logging import exception

sys.excepthook = lambda type, value, tback: traceback.print_exception(type, value, tback)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon,QFontDatabase
from qwerty import Ui_MainWindow
from currency_converter import CurrencyConverter
class CorrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CorrencyConv, self).__init__()

        font_id = QFontDatabase.addApplicationFont("digiface.ttf")
        if font_id == -1:
            print("Ошибка: Не удалось загрузить шрифт!")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ini_ui()
    def ini_ui(self):
        self.setWindowTitle ("Ковертатор лаве")
        self.setWindowIcon(QIcon("WEWEW.png"))


        self.ui.INV.setPlaceholderText(' Из валюты ')
        self.ui.inmon.setPlaceholderText('Сколько')
        self.ui.outv.setPlaceholderText('В валюту')
        self.ui.outmon.setPlaceholderText('Итого')
        self.ui.jmay.clicked.connect(self.convert)

    def convert(self):
        try:
            c=CurrencyConverter(fallback_on_missing_rate=True)
            inv=self.ui.INV.text().upper()
            outv=self.ui.outv.text().upper()
            inmon=float(self.ui.inmon.text())

            outmon=round(c.convert(inmon, "%s" % (inv), "%s" % (outv)),2)

            self.ui.outmon.setText(str(outmon))
        except ValueError:
            self.ui.outmon.setText('ошибка числа')
        except Exception as e:
            self.ui.outmon.setText('ошибка валюты')
            print(f'ошибка{e}')

app = QtWidgets.QApplication([])
application = CorrencyConv()
application.show()
sys.exit(app.exec_())
