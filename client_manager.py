import sys, socket, subprocess, pickle, os, time, threading, pickle
import typing
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, pyqtSignal, QThread, QObject

qtcreator_file  = "client_manager.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

def write(data:dict, isForClient:bool=False):
    if isForClient:
        with open('data.pkl', 'wb') as f:
            pickle.dump(data, f)
    else:
        with open('ServData.pkl', 'wb') as f:
            pickle.dump(data, f)

def read(isForClient:bool=False) -> dict:   
    if isForClient:
        with open('data.pkl', 'rb') as f:
            return pickle.load(f)
    else: 
        with open('ServData.pkl', 'rb') as f:
            return pickle.load(f)
    
class Worker(QObject):
    nextStep = pyqtSignal()
    finished = pyqtSignal()
    step = 0
    lastStep = 9

    def __init__(self, IP1:list, IP2:list, comboBox:QtWidgets.QComboBox) -> None:
        QObject.__init__(self)
        self.IP1 = IP1
        self.IP2 = IP2
        self.comboBox = comboBox

    def run(self):
        socket.setdefaulttimeout(2)
        for ping in range(int(self.IP1[3]),int(self.IP2[3])):
            self.step += 1
            self.nextStep.emit()

            address = self.IP1[0] + "." + self.IP1[1] + "." + self.IP1[2] + "." + str(ping)
            res = os.system(f"ping -n 1 -w 100 {address}")
            print(res)
            if res == 0:
                # print( "ping to", address, "OK")
                self.step -= 1
                threading.Thread(target=(lambda: self.get_hostname(address))).start()
                print("A")
            elif res == 1:
                print("no response from", address)
            else:
                print("ping to", address, "failed!")

        self.finished.emit()
    
    def get_hostname(self, address):
        try:
            self.comboBox.addItems([socket.gethostbyaddr(address)[0]])
        except:
            self.comboBox.addItems([address])
        self.step += 1

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # write({"IP1":"111111","IP2":"111111","port":"1"})
        self.data = read()

        self.IP1.setText(self.data["IP1"][0] + "." + self.data["IP1"][1] + "." + self.data["IP1"][2] + "." + self.data["IP1"][3])
        self.IP2.setText(self.data["IP2"][0] + "." + self.data["IP2"][1] + "." + self.data["IP2"][2] + "." + self.data["IP2"][3])
        self.HostPort.setText(str(self.data["port"]))

        self.setFixedSize(self.size())

        self.Port.setPlaceholderText(str(self.data["port"]))
        self.Host.setPlaceholderText(socket.gethostbyname(socket.gethostname()) + f"   ({socket.gethostname()})")
        self.Cancel.clicked.connect(app.quit)
        self.Scan.clicked.connect(self.scan)
        self.Change.clicked.connect(self.change)

        
        self.method:QtWidgets.QComboBox
        self.method.currentIndexChanged.connect(lambda: self.stack.setCurrentIndex(not self.method.currentIndex()))
        self.method.currentIndexChanged.connect(lambda: self.IP.setFocus())

        self.Help.triggered.connect(lambda: os.system("python3 ./Help.py"))
        

        self.IP1.returnPressed.connect(lambda: self.IP2.setFocus())
        self.IP2.returnPressed.connect(self.setip)

        self.HostPort.returnPressed.connect(self.setport)

        self.SetPort.clicked.connect(self.setport)
        self.SetIP.clicked.connect(self.setip)
        
    def scan(self):

        progress = QtWidgets.QProgressDialog('Work in progress', 'Cancel', 0, abs(int(self.data["IP1"][3]) - int(self.data["IP2"][3])) - 1, self)
        progress.setWindowTitle("Generating files...")
        progress.setWindowModality(Qt.WindowModal)
        progress.show()
        progress.setValue(0)

        self.thread = QThread()
        worker = Worker(self.data["IP1"],self.data["IP2"],self.comboBox)
        worker.moveToThread(self.thread)

        self.thread.started.connect(worker.run)

        worker.nextStep.connect(lambda: progress.setValue(worker.step))
        worker.finished.connect(lambda: progress.cancel())

        worker.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        worker.finished.connect(worker.deleteLater)

        self.thread.start()

        self.ID.setPlaceholderText(str(read(1)["ID"]))

    def change(self):
        data:dict = {}
        data["ID"] = self.ID.text()
        data["port"] = self.Port.placeholderText()
        data["host"] = socket.gethostbyname(socket.gethostname())
        write(data, 1)
        print(data)
        os.system(f"scp data.pkl boite@{self.comboBox.currentText()}:client")
        os.system(f"ssh boite@({self.comboBox.currentText()} ")
        QtWidgets.QMessageBox.information(self,"info","The client has been set!\nPlease restart the client program")


    def setip(self):
        try :
            self.data["IP1"]:list = self.IP1.text().split(".")
            self.data["IP2"]:list = self.IP2.text().split(".")
            IP1 = self.data["IP1"]
            IP2 = self.data["IP2"]
            if (len(IP1) != 4 or len(IP2) != 4):
                raise Exception("incorrect ipv4 format")
            if IP1[0] != IP2[0] or IP1[1] != IP2[1] or IP1[2] != IP2[2]:
                raise Exception("You can only vary the last number")
            for i in IP1:
                int(i)
            for i in IP2:
                int(i)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self,"uh oh",f"could not set the IP range.\n{e}")
            return
        write(self.data)

        QtWidgets.QMessageBox.information(self,"info","The IP range has been set!")

    def setport(self):
        try :
            self.data["port"]:int = int(self.HostPort.text())
        except Exception as e:
            QtWidgets.QMessageBox.critical(self,"uh oh",f"could not set the port.\n{e}")
            return
        write(self.data)
        self.Port.setPlaceholderText(str(self.data["port"]))

        QtWidgets.QMessageBox.information(self,"info","The Port has been set!\nPlease reastart the server program.")

    def test(self):
        print("test")
        self.HostPort:QtWidgets.QLineEdit
        self.HostPort.setFocus()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp(app)
    window.show()
    sys.exit(app.exec_())
    