import sys
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from main_ui import Ui_MainWindow
import dataController as dc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        actorList = dc.getActorAll()
        for actor in actorList:
            actorId, actorName, actorStatus = actor
            checkBox = QCheckBox(actorName)
            checkBox.setChecked(bool(actorStatus))
            checkBox.stateChanged.connect(lambda state, id=actorId, name=actorName, checkbox=checkBox: self.updateStatus(id, name, checkbox.isChecked()))
            item_widget = QListWidgetItem()
            self.ui.listActor.addItem(item_widget)
            self.ui.listActor.setItemWidget(item_widget, checkBox)

        self.ui.btnAdd.clicked.connect(self.addList)
        self.ui.btnEdit.clicked.connect(self.editList)
        self.ui.btnRemove.clicked.connect(self.removeList)
        self.ui.btnClear.clicked.connect(self.clearList)
    
    def updateStatus(self, id, name, status):
        dc.updateActor(id, name, status)
    
    def addList(self):
        text, ok = QInputDialog.getText(self, "Add a actor", "New actor:")
        if ok and text:
            dc.insertActor(text, 0)
            checkBox = QCheckBox(text)
            checkBox.setChecked(bool(0))
            checkBox.stateChanged.connect(lambda state, id=dc.getActorId(text), name=text, checkbox=checkBox: self.updateStatus(id, name, checkbox.isChecked()))
            item_widget = QListWidgetItem()
            self.ui.listActor.addItem(item_widget)
            self.ui.listActor.setItemWidget(item_widget, checkBox)

    def editList(self):
        currentRow = self.ui.listActor.currentRow()
        item = self.ui.listActor.item(currentRow)
        cbItem = self.ui.listActor.itemWidget(item)
        text, ok = QInputDialog.getText(self, "Edit a actor", "New actor:", QLineEdit.Normal, cbItem.text())
        if ok and text:
            dc.updateActor(dc.getActorId(cbItem.text()), text, cbItem.isChecked())
            cbItem.setText(text)

    def removeList(self):
        currentRow = self.ui.listActor.currentRow()
        item = self.ui.listActor.item(currentRow)
        cbItem = self.ui.listActor.itemWidget(item)
        if currentRow >= 0:
            actorId = dc.getActorId(cbItem.text())
            dc.deleteActor(actorId)
            currentItem = self.ui.listActor.takeItem(currentRow)
            del currentItem

    def clearList(self):
        self.ui.listActor.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()