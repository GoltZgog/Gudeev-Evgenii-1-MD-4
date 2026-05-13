import sys
import traceback
import subprocess
from logging import exception


sys.excepthook = lambda type, value, tback: traceback.print_exception(type, value, tback)
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QIcon,QFontDatabase
from PyQt5.QtCore import QThread, pyqtSignal
from wisper import Ui_MainWindow
from currency_converter import CurrencyConverter

class gaf(QThread):

    ls=pyqtSignal(str)
    fs=pyqtSignal()

    def __init__(self,inv,outv):
        super().__init__()

        self.inv = inv
        self.outv = outv

    def run(self):
        cmd=["whisper", self.inv, "--output_dir" ,self.outv]
	
        import os
        my_env=os.environ.copy()
        my_env["PYTHONIOENCODING"] = "utf-8"

        try:
            process=subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
		        errors="replace",
                bufsize=1,
                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0,
                env=my_env)

            for line in process.stdout:
                if line:
                    self.ls.emit(line.strip())

            process.wait()

            if process.returncode == 0:
                self.ls.emit("\n✅ Готово! Файлы сохранены.")
            else:
                self.ls.emit(f"\n❌ Ошибка! Код завершения: {process.returncode}")

        except FileNotFoundError:
            self.ls.emit("❌ Ошибка: Whisper не установлен или не добавлен в PATH.")

        except Exception as e:
            self.ls.emit(f"❌ Произошла ошибка: {str(e)}")

        finally:
            self.fs.emit()

class priv(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(priv, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("Ковертатор аудио в txt")

        self.inv.setPlaceholderText("выберите файл")
        self.outv.setPlaceholderText("выберите путь сохранения")
        self.worker = None

        self.jmayv.clicked.connect(self.nach)
        self.jmayo.clicked.connect(self.skach)
        self.jmay.clicked.connect(self.guf)

    def nach(self):
        file,_=QtWidgets.QFileDialog.getOpenFileName(
            self,"выбери файл","","Audio/Video Files (*.mp3 *.wav *.m4a *.mp4 *.mkv);;All Files (*)")
        if file:
            self.inv.setText(file)

    def ul(self,text):
        self.tv.append(text)
        sb=self.tv.verticalScrollBar()
        sb.setValue(sb.maximum())

    def skach(self):
        asa = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения")
        if asa:
            self.outv.setText(asa)
    def guf(self):
        inv=self.inv.text().strip()
        outv=self.outv.text().strip()

        if not inv or not outv:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Укажите файл и папку для сохранения!")
            return

        self.jmay.setEnabled(False)

        self.tv.clear()
        self.ul(f"Запуск перевода...\nФайл: {inv}\nСохранение в: {outv}\n---")

        self.worker = gaf(inv,outv)
        self.worker.ls.connect(self.ul)
        self.worker.fs.connect(self.on_finished)
        self.worker.start()

    def on_finished(self):
        self.jmay.setEnabled(True)


app = QtWidgets.QApplication([])
application = priv()
application.show()
sys.exit(app.exec_())