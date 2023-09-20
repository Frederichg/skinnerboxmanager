#python -m PyQt5.uic.pyuic -x trial.ui -o trial.py

import sys, os, logging, pickle
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time import sleep
from tcp_classes import *

# ui file
qtcreator_file  = "untitled2.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

# setup to print messages
logging.basicConfig(format="%(message)s", level=logging.INFO)

# read from pkl files
def read() -> dict:    
    with open('ServData.pkl', 'rb') as f:
        return pickle.load(f)
    

# Worker object, this is where all the info for a client is kept
# has an infinite loop that requests the runtime variables and to check the connection
class Worker(QObject):
    NEW_DICT = pyqtSignal()
    NEW_ID = pyqtSignal()
    finished = pyqtSignal()
    DICT:dict
    ID:int
    serv:server
    cmd:command

    def run(self):
        self.ID = self.serv.connect()
        self.NEW_ID.emit()
        while True: 
            # self.get_dict()
            sleep(0.1)
            if self.stat():
                break
            sleep(0.1)

    def get_dict(self):
        self.cmd = command("stat",4)
        self.serv.send(self.cmd,self.ID)
        self.DICT = self.serv.receive_dict(self.ID)
        self.NEW_DICT.emit()

    def stat(self):
        self.cmd = command("stat",0)
        stat = self.serv.send(self.cmd,self.ID)
        if stat == -1:
            self.finished.emit()
            return 1

class Frame():
    def __init__(self, window, frame_index:int, ID:int, tab:QtWidgets.QWidget) -> None:

        self.frame_index = frame_index

        self.tab = tab

        self.serv:server = window.serv

        self.ID = ID

        self.frame = window.findChild(QtWidgets.QGroupBox, "verticalGroupBox").findChild(QtWidgets.QFrame, f'frame_{frame_index}')
        self.frame.setEnabled(True)

        self.frame_text["b_name"] = f'box{self.ID}'
        self.frame_text["p_name"] = f"psychopy{self.ID}"

        self.setFrame("stopped")

        self.frame.findChild(QtWidgets.QPushButton, f'pushButton_{frame_index}_1').clicked.connect(lambda: self.start(ID,tab))
        self.frame.findChild(QtWidgets.QPushButton, f'pushButton_{frame_index}_2').clicked.connect(lambda: self.stop(ID,tab))
        self.frame.findChild(QtWidgets.QPushButton, f'pushButton_{frame_index}_3').clicked.connect(lambda: window.transfer(ID))

        self.frame.findChild(QtWidgets.QLineEdit, f'lineEdit_{frame_index}_3').returnPressed.connect(lambda: self.start(ID, tab))

        tab.Play.clicked.connect(lambda: self.start(ID,tab))
        tab.Stop.clicked.connect(lambda: self.stop(ID,tab))
        tab.Transfer.clicked.connect(lambda: window.transfer(ID))

        tab.Feeder.clicked.connect(lambda: self.serv.send(command("test",0),ID,tab))
        tab.FP_light.clicked.connect(lambda: self.serv.send(command("test",1),ID,tab))
        tab.H_light.clicked.connect(lambda: self.serv.send(command("test",2),ID,tab))
        tab.Screen.clicked.connect(lambda: self.serv.send(command("test",3),ID,tab))


    def setFrame(self, status):
        #frame
        # self.frame_text["b_name"] = f'box{self.ID}'
        # self.frame_text["p_name"] = f"psychopy{self.ID}"

        frame_index = self.frame_index

        frame:QtWidgets.QFrame = window.findChild(QtWidgets.QGroupBox, "verticalGroupBox").findChild(QtWidgets.QFrame, f'frame_{frame_index}')
        self.frame = frame
        frame.setEnabled(True)

        params = self.frame_status[status]

        frame.findChild(QtWidgets.QLineEdit, f'lineEdit_{frame_index}_1').setEnabled(params[0])
        frame.findChild(QtWidgets.QLineEdit, f'lineEdit_{frame_index}_2').setEnabled(params[1])
        frame.findChild(QtWidgets.QLineEdit, f'lineEdit_{frame_index}_3').setEnabled(params[2])

        frame.findChild(QtWidgets.QPushButton, f'pushButton_{frame_index}_1').setEnabled(params[3])
        frame.findChild(QtWidgets.QPushButton, f'pushButton_{frame_index}_2').setEnabled(params[4])
        frame.findChild(QtWidgets.QPushButton, f'pushButton_{frame_index}_3').setEnabled(params[5])

        frame.findChild(QtWidgets.QProgressBar, f'progressBar_{frame_index}').setEnabled(params[6])

        frame.findChild(QtWidgets.QLineEdit, f'lineEdit_{frame_index}_1').setText(self.frame_text["b_name"])
        frame.findChild(QtWidgets.QLineEdit, f'lineEdit_{frame_index}_2').setText(self.frame_text["p_name"])
        frame.findChild(QtWidgets.QLineEdit, f'lineEdit_{frame_index}_3').setText(self.frame_text["p_#"])

        frame.findChild(QtWidgets.QPushButton, f'pushButton_{frame_index}_1').setText(self.frame_text["s/p"])
        frame.findChild(QtWidgets.QPushButton, f'pushButton_{frame_index}_2').setText(self.frame_text["stop"])
        frame.findChild(QtWidgets.QPushButton, f'pushButton_{frame_index}_3').setText(self.frame_text["transfer"])

        frame.findChild(QtWidgets.QProgressBar, f'progressBar_{frame_index}').setValue(self.frame_text["progress"])

        # tab
        self.tab.Play.setText(self.frame_text["s/p"])

        self.tab.B_name.setText(self.frame_text["b_name"])
        self.tab.P_name.setText(self.frame_text["p_name"])
        self.tab.Par_name.setText(self.frame_text["p_#"])

        self.tab.Play.setEnabled(params[3])
        self.tab.Stop.setEnabled(params[4])
        self.tab.Transfer.setEnabled(params[5])

        self.tab.progressBar.setEnabled(params[6])


    def start(self, ID:int,tab):
        if self.serv.send(command("stat",0),ID,tab) == 2:
            self.frame_text["s/p"] = "Start"
            self.setFrame("paused")
            self.serv.send(command("stat",2),ID,tab)
        else:
            line = self.frame.findChild(QtWidgets.QLineEdit, f'lineEdit_{self.frame_index}_3')
            text = line.text()
            if text == "":
                text = self.tab.Par_name.text()
            self.frame_text["p_#"] = text
            # self.frame_text["s/p"] = "Pause"
            self.setFrame("running")
            self.serv.send(command("stat",3),ID,tab)
            self.serv.send(command(str(text),0),ID,tab)

    def stop(self, ID:int,tab):
        self.frame_text["s/p"] = "Start"
        self.frame_text["p_#"] = ""
        self.setFrame("stopped")
        self.serv.send(command("stat",1),ID,tab)

    def remove(self):
        self.frame_text["b_name"] = ""
        self.frame_text["p_name"] = ""
        self.frame_text["p_#"] = ""
        self.frame_text["s/p"] = "Start"

        self.setFrame("disconnected")


    frame_status = {
        # [Box name, program Name, participant #, start/pause, stop, transfer, progress]
        "running" : [1,1,0,0,1,0,0],
        "stopped" : [1,1,1,1,0,0,0],
        "paused" : [1,1,0,1,1,0,1],
        "disconnected" : [0,0,0,0,0,0,0]
    }

    frame_text = {
        "b_name" : "",
        "p_name" : "",
        "p_#" : "",
        "s/p" : "Start",
        "stop" : "Stop",
        "transfer" : "Transfer",
        "progress" : 0
    }
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):

    frames = []
    threads = []
    Runtimes = {
        "x" : 3
    }

    def __init__(self, port:int):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.serv = server(port)

        self.add_button.clicked.connect(self.mkThread)
        self.Help.triggered.connect(lambda: os.system("python3 ./Help.py"))
        self.Client_Manager.triggered.connect(lambda: os.system("python3 ./client_manager.py"))

    def mkThread(self):

        self.add_button.setEnabled(False)

        thread = QThread()
        worker = Worker()
        worker.moveToThread(thread)

        thread.started.connect(worker.run)
        worker.finished.connect(thread.quit)
        worker.finished.connect(lambda: self.disconnect(worker.ID))

        thread.finished.connect(thread.deleteLater)
        worker.NEW_ID.connect(lambda: self.add_tab(worker.ID))
        worker.NEW_DICT.connect(lambda: exec(f"window.setTableData({worker.DICT},window.home.findChild(QtWidgets.QWidget, \"tab{worker.ID}\").Runtime)"))

        self.threads.append(thread)
        worker.serv = self.serv
        thread.start()

    def disconnect(self,ID):
        index = self.home.indexOf(self.home.findChild(QtWidgets.QWidget, f"tab{ID}"))
        self.home.removeTab(index)
        frame:Frame = self.frames[index-1]
        frame.remove()
        self.frames.remove(frame)

    def add_tab(self, ID:int):

        tab = uic.loadUi("tab.ui")
        tab.setObjectName(f'tab{ID}')
        self.home.addTab(tab, f'box{ID}')

        self.frames.append(Frame(self,len(self.frames) + 1,ID, tab))

        self.BoxCount.setText(f'{len(self.frames)}')
        self.add_button.setEnabled(True)

        tab.Send.clicked.connect(lambda: self.send_command_through_gui(tab, ID))
        tab.Command:QtWidgets.QLineEdit
        tab.Command.returnPressed.connect(lambda: self.send_command_through_gui(tab, ID))

    def send_command_through_gui(self, tab, ID):
        text:str = tab.Command.text()
        text = text.split(" ")
        try:
            self.serv.send(command(text[0],int(text[1])),ID,tab)
        except:
            return


    def transfer(self, ID:int):
        message = QtWidgets.QMessageBox(self)
        message.setIcon(1)
        message.setText("would you like to Upload or Download files?")
        message.addButton("Upload",QtWidgets.QMessageBox.YesRole)
        message.addButton("Download",QtWidgets.QMessageBox.NoRole)
        return_value = message.exec()
        if not return_value:
            f = QtWidgets.QFileDialog.getOpenFileNames(self,'Open file','c:\\',"Python / data files (*.py *.xlsx)")
            if f[0] != '':
                for file in f[0]:
                    self.serv.send(command("file",1),ID)
                    self.serv.send_file(file, ID)

    def setTableData(self, data:dict, table:QtWidgets.QTableWidget): 
        if data != -1:
            horHeaders = []
            for n, key in enumerate(sorted(data.keys())):
                horHeaders.append(key)
                for m, item in enumerate(str(data[key])):
                    newitem = QtWidgets.QTableWidgetItem(item)
                    table.setItem(m, n, newitem)
            while table.columnCount() <= n:
                table.insertColumn(0)
            table.setHorizontalHeaderLabels(horHeaders)

    def test(self):
        print("test")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    port = int(read()["port"])
    window = MyApp(port)
    window.show()
    sys.exit(app.exec_())