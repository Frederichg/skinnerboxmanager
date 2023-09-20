import sys
from PyQt5 import QtWidgets, uic, QtCore

qtcreator_file  = "Help.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.treeWidget:QtWidgets.QTreeWidget
        self.stackedWidget:QtWidgets.QStackedWidget

        root = self.treeWidget.invisibleRootItem()
        Items:dict = {}
        for i in range(root.childCount()):
            Items[root.child(i).text(0)] = len(Items)
            for j in range(root.child(i).childCount()):
                Items[root.child(i).child(j).text(0)] = len(Items)

        self.treeWidget.itemSelectionChanged.connect(lambda: self.loadAllMessages(Items))
    
    def loadAllMessages(self, Items:dict):
        getSelected:QtWidgets.QTreeWidgetItem = self.treeWidget.selectedItems()[0]
        if getSelected:
            self.stackedWidget.setCurrentIndex(Items[getSelected.text(0)] + 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())