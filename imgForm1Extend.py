    # -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot,  Qt,  QModelIndex,  QDir
from PyQt5.QtWidgets import QMainWindow,  QFileDialog, QListWidgetItem
from PyQt5.QtGui import QPixmap
from Ui_imgForm1 import Ui_MainWindow
from faceRecognition import FRImage # , FRFace

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    activeImageID = 0
    activeFaceID = 0
    
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """

        super().__init__(parent)
        self.setupUi(self)
        
        self.Dialog = QFileDialog()
        self.imgDir = QDir()
        self.imgDir.setPath("~scoiaz/Pictures/FR/")
        self.Dialog.setDirectory(self.imgDir)


    @pyqtSlot()
    def on_btnFindImages_clicked(self):
        """
        Slot documentation goes here.
        """
        self.listImages.clear()
        self.listFaces.clear()
        # Select Images for processing
        
        self.imgPath = self.Dialog.getOpenFileNames(
            self, 
            "Select one or more image files!",
            "/home/Pictures/FR/",  
            "Images (*.png *.xpm *.jpg)")
        self.FRImage = []
        FRImage.InstanceCount = 0
        self.FRImage.clear()
        n = 0
        for i in self.imgPath[0]:
            self.FRImage.append( FRImage() )
            self.FRImage[n].Open(i)
            self.FRImage[n].FindFaces(n)
            n += 1
        
        # Display Image List
        for i in range(0, len(self.FRImage)):
            self.listImages.addItem(self.FRImage[i].FilePath)
        
        MainWindow.activeFaceID = 0
        MainWindow.on_listImages_currentRowChanged(self,  0)

    @pyqtSlot()
    def on_btnSaveName_clicked(self):
        """
        Slot documentation goes here.
        """

    @pyqtSlot(str)
    def on_listImages_currentTextChanged(self, currentText):
        """
        Slot documentation goes here.

        @param currentText DESCRIPTION
        @type str
        """

        
    @pyqtSlot(str)
    def on_listFaces_currentTextChanged(self, currentText):
        """
        Slot documentation goes here.

        @param currentText DESCRIPTION
        @type str
        """
        self.lblFaceImage.setPixmap(self.FRImage[MainWindow.activeImageID].Faces[0].imgPixmap.scaled(181, 181, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.lblFaceImage.setPixmap(QPixmap(currentText).scaled(181, 181, Qt.KeepAspectRatio, Qt.SmoothTransformation))

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
        
        MainWindow.activeImageID = self.FRImage[i].InstanceID
        
        print(i, currentRow)
        self.lblMainImage.setPixmap(self.FRImage[i].ImgPixmap.scaled(181, 181, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.lblFaceImage.setPixmap(self.FRImage[i].Faces[0].imgPixmap.scaled(181, 181, Qt.KeepAspectRatio, Qt.SmoothTransformation))


    @pyqtSlot(QListWidgetItem)
    def on_listFaces_itemClicked(self, item):
        """
        Slot documentation goes here.

        @param item DESCRIPTION
        @type QListWidgetItem
        """

    @pyqtSlot(int)
    def on_listFaces_currentRowChanged(self, currentRow):
        """
        Slot documentation goes here.

        @param currentRow DESCRIPTION
        @type int
        """
