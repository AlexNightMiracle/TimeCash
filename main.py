from untitled import *
import sys
import os
import time

from qt_material import apply_stylesheet

class createMainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(createMainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.stat = False

        self.ui.pushButton.clicked.connect(self.ChangeStat)

        self.timer = QtCore.QTimer()

        #alltime = str(f'{21}:{21}:{21}')
        #self.ui.lcdNumber_2.display(alltime)

    def ChangeStat(self):
        if(self.stat == False):
            self.stat = True
            self.startTime = time.time()

            self.timer.timeout.connect(self.TimerFunc)
            self.timer.start(1000)
        else:
            self.stat = False

        print(self.stat)

    def TimerFunc(self):
        if self.stat == True:
            time_r = int(time.time() - self.startTime)

            hours = time_r // 3600
            minutes = (time_r % 3600) // 60
            seconds = time_r % 60

            if hours > 99:
                self.stat = False
            else:
                hours_s = str(hours)
                minutes_s = str(minutes)
                second_s = str(seconds)

                time_s = str(f'{hours}:{minutes}:{seconds}')
                cash = (hours * self.ui.spinBox.value()) + (minutes * (self.ui.spinBox.value()) / 60) + (seconds * (self.ui.spinBox.value()) / 3600)
                #cash = round(cash)
                #cash = str(cash)
                #print(cash)
                #self.ui.lcdNumber_2.display(time_s)
                self.ui.lineEdit.setText(time_s)
                self.ui.lineEdit_2.setText(f'%.2f'%cash)
                #print(time_s)

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = createMainWindow()
    apply_stylesheet(app, theme="dark_cyan.xml")
    stylesheet = app.styleSheet()
    with open('custom_buttons.css') as file: app.setStyleSheet(stylesheet + file.read().format(**os.environ))
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
