from PyQt5 import QtWidgets, QtGui, QtCore
from final1 import Ui_MainWindow
from final1money1 import money1

#('./onnxruntime_providers_shared.dll','onnxruntime\\capi'),('./common.onnx','ddddocr')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        self.roll1=0
        self.ui.radioButton.toggled.connect(self.roll11)
        self.ui.radioButton_2.toggled.connect(self.roll12)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton.clicked.connect(self.startClicked)
        self.ui.pushButton_2.clicked.connect(self.stopClicked)

    #按開始
    def startClicked(self):
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(True)
        print("You clicked starttttt")
        self.combobox1=self.ui.comboBox.currentIndex()
        if self.combobox1==0:
            self.money1=money1(t=self.roll1,y=50,u=20)
            self.money1.start()#開始程序


#######
    #按停止
    def stopClicked(self):
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton.setEnabled(True)
        print(f"You clicked stoppppp")
        if self.combobox1==0:
            self.money1.terminate()#終止程序


    #打幣選加倍
    def roll11(self):
        self.roll1=10
    def roll12(self):
        self.roll1=20


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())