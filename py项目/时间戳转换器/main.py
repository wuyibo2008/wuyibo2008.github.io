from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
import time,sys
class Stats:
    def __init__(self):
        self.ui = QUiLoader().load('main.ui')
        self.ui.c_t_zhuan.clicked.connect(self.c_t)
        self.ui.t_c_zhuan.clicked.connect(self.t_c)
        self.ui.pushButton_3.clicked.connect(self.z_x)

    def z_x(self):
        xianzai = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        method = self.ui.comboBox_2.currentText()
        if method == '10位-秒级':
            mm = str(int(time.time()))          
            self.ui.lineEdit_5.setText(xianzai)
            self.ui.lineEdit_6.setText(mm)
           
        if method == '13位-毫秒级': 
            self.ui.lineEdit_5.setText(xianzai)
            choice = QMessageBox.question(
                self.ui,
                '确认',
                'Python转13位时间戳并不准确\n💡建议转换后不作为重要信息💡\n是否继续？')
            if choice == QMessageBox.Yes:
                mm = str(int(round(time.time() * 1000)))
                self.ui.lineEdit_6.setText(mm)
            if choice == QMessageBox.No:
                self.ui.lineEdit_5.clear()
    def t_c(self):
        try:
            method = self.ui.comboBox_2.currentText()
            text = self.ui.lineEdit_5.text()
            if text != '':
                if method == '10位-秒级':
                    mm=str(int(time.mktime(time.strptime(text, "%Y-%m-%d %H:%M:%S"))))
                    self.ui.lineEdit_6.setText(mm)
                if method == '13位-毫秒级':
                    choice = QMessageBox.question(
                        self.ui,
                        '确认',
                        'Python转13位时间戳并不准确\n💡建议转换后不作为重要信息💡\n是否继续？')
                    if choice == QMessageBox.Yes:
                        mm=(int(time.mktime(time.strptime(text, "%Y-%m-%d %H:%M:%S"))))
                        mm*=1000
                        self.ui.lineEdit_6.setText(str(mm))
                    if choice == QMessageBox.No:
                        self.ui.lineEdit_5.clear()
            else :
                QMessageBox.warning(
                self.ui,
                '请输入',
                '时间不能为空')
        except:
            QMessageBox.critical(
                self.ui,
                '错误',
                '转换错误，可能的错误:\n💡1.格式没有按照:\nxxxx(年份)-xx(月份)-xx(日) xx(小时*24制):xx(分):xx(秒)\n💡2.输入不为数字\n💡3.时间的冒号为中文字符\n💡4.年份过远，10位转换可尝试13位')
            self.ui.lineEdit_5.clear()

    def c_t(self):
        try:
            method = self.ui.comboBox.currentText()
            text = self.ui.lineEdit.text()
            if text != '':
                if method == '10位-秒级':
                    timeArray = time.localtime(int(text))
                    mm = (time.strftime("%Y-%m-%d %H:%M:%S", timeArray))
                    print(text)
                    self.ui.lineEdit_2.setText(mm)
                if method == '13位-毫秒级':
                    choice = QMessageBox.question(
                        self.ui,
                        '确认',
                        'Python转13位时间戳并不准确\n💡建议转换后不作为重要信息💡\n是否继续？')

                    if choice == QMessageBox.Yes:
                        text=int(text)
                        text/=1000
                        timeArray = time.localtime(int(text))
                        mm = (time.strftime("%Y-%m-%d %H:%M:%S", timeArray))
                        self.ui.lineEdit_2.setText(mm)
                    if choice == QMessageBox.No:
                        self.ui.lineEdit.clear()
                    
            else :
                QMessageBox.warning(
                self.ui,
                '请输入',
                '时间戳不能为空')
        except:
            QMessageBox.critical(
                self.ui,
                '错误',
                '转换错误，可能的错误:\n1.时间戳超过10位\n2.输入不为数字')
            self.ui.lineEdit.clear()

app = QApplication([])
stats = Stats()
stats.ui.show()
sys.exit(app.exec_())