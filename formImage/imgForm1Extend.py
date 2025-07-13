    # -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot,  Qt,  QModelIndex
from PyQt5.QtWidgets import QMainWindow,  QFileDialog, QListWidgetItem
from PyQt5.QtGui import QPixmap
from Ui_imgForm1 import Ui_MainWindow
from faceRecognition import FRImage # , FRFace

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_btnFindImages_clicked(self):
        """
        Slot documentation goes here.
        """
        self.listImages.clear()
        self.listFaces.clear()
        # Select Images for processing
        self.imgPath = QFileDialog.getOpenFileNames(directory="~/Pictures/FR")
        self.FRImage = []
        FRImage.InstanceCount = 0
        self.FRImage.clear()
        n = 0
        for i in self.imgPath[0]:
            self.FRImage.append( FRImage() )
            self.FRImage[n].Open(i)
            print(n, self.FRImage[n].InstanceID)
            self.FRImage[n].FindFaces(n)
            n += 1
        
        # Display Image List
        for i in range(0, len(self.FRImage)):
            self.listImages.addItem(self.FRImage[i].FilePath)
                

    @pyqtSlot()
    def on_btnSaveName_clicked(self):
        """
        Slot documentation goes here.
        """

    @pyqtSlot(QListWidgetItem)
    def on_listImages_itemActivated(self, item):
        """
        Slot documentation goes here.

        @param item DESCRIPTION
        @type QListWidgetItem
        """
        
        
    @pyqtSlot(QListWidgetItem)
    def on_listFaces_itemActivated(self, item):
        """
        Slot documentation goes here.

        @param item DESCRIPTION
        @type QListWidgetItem
        """
        self.lblFaceImage.setPixmap(QPixmap(item.text()).scaled(181, 181, Qt.KeepAspectRatio, Qt.SmoothTransformation))



    @pyqtSlot(QListWidgetItem)
    def on_listImages_itemClicked(self, item):
        """
        Slot documentation goes here.

        @param item DESCRIPTION
        @type QListWidgetItem
        """
           

        print('Cliked', item,  item.text() )

    @pyqtSlot(QListWidgetItem, QListWidgetItem)
    def on_listImages_currentItemChanged(self, current, previous):
        """
        Slot documentation goes here.

        @param current DESCRIPTION
        @type QListWidgetItem
        @param previous DESCRIPTION
        @type QListWidgetItem
        """
        print('Item Changed', current,  previous )

    @pyqtSlot(str)
    def on_listImages_currentTextChanged(self, currentText):
        """
        Slot documentation goes here.

        @param currentText DESCRIPTION
        @type str
        """
        self.lblMainImage.setPixmap(QPixmap(currentText).scaled(181, 181, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        print('Text Changed', currentText )

    @pyqtSlot(int)
    def on_listImages_currentRowChanged(self, currentRow):
        """
        Slot documentation goes here.

        @param currentRow DESCRIPTION
        @type int
        """
        self.listFaces.clear()
        
        i = currentRow
        for n in range(0, len(self.FRImage[i].Faces)-1):
            self.listFaces.addItem(self.FRImage[i].Faces[n].FilePath)

        print('Row Changed', currentRow )

    @pyqtSlot(QModelIndex)
    def on_listFaces_clicked(self, index):
        """
        Slot documentation goes here.

        @param index DESCRIPTION
        @type QModelIndex
        """

    @pyqtSlot(QListWidgetItem)
    def on_listFaces_itemClicked(self, item):
        """
        Slot documentation goes here.

        @param item DESCRIPTION
        @type QListWidgetItem
        """

    @pyqtSlot(QListWidgetItem, QListWidgetItem)
    def on_listFaces_currentItemChanged(self, current, previous):
        """
        Slot documentation goes here.

        @param current DESCRIPTION
        @type QListWidgetItem
        @param previous DESCRIPTION
        @type QListWidgetItem
        """

    @pyqtSlot(int)
    def on_listFaces_currentRowChanged(self, currentRow):
        """
        Slot documentation goes here.

        @param currentRow DESCRIPTION
        @type int
        """
