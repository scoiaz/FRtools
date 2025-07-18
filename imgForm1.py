# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import cv2
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow,  QFileDialog, QListWidgetItem
from Ui_imgForm1 import Ui_MainWindow


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
    def on_btnOpenImg_clicked(self):
        """
        Slot documentation goes here.
        """

    @pyqtSlot()
    def on_btnFindImages_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot()
    def on_btnSaveName_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot(QListWidgetItem)
    def on_listImages_itemActivated(self, item):
        """
        Slot documentation goes here.

        @param item DESCRIPTION
        @type QListWidgetItem
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot(QListWidgetItem)
    def on_listFaces_itemActivated(self, item):
        """
        Slot documentation goes here.

        @param item DESCRIPTION
        @type QListWidgetItem
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot(QListWidgetItem)
    def on_listImages_itemClicked(self, item):
        """
        Slot documentation goes here.

        @param item DESCRIPTION
        @type QListWidgetItem
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot(QListWidgetItem, QListWidgetItem)
    def on_listImages_currentItemChanged(self, current, previous):
        """
        Slot documentation goes here.

        @param current DESCRIPTION
        @type QListWidgetItem
        @param previous DESCRIPTION
        @type QListWidgetItem
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot(str)
    def on_listImages_currentTextChanged(self, currentText):
        """
        Slot documentation goes here.

        @param currentText DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot(int)
    def on_listImages_currentRowChanged(self, currentRow):
        """
        Slot documentation goes here.

        @param currentRow DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot(QModelIndex)
    def on_listFaces_clicked(self, index):
        """
        Slot documentation goes here.

        @param index DESCRIPTION
        @type QModelIndex
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot(QListWidgetItem)
    def on_listFaces_itemClicked(self, item):
        """
        Slot documentation goes here.

        @param item DESCRIPTION
        @type QListWidgetItem
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot(QListWidgetItem, QListWidgetItem)
    def on_listFaces_currentItemChanged(self, current, previous):
        """
        Slot documentation goes here.

        @param current DESCRIPTION
        @type QListWidgetItem
        @param previous DESCRIPTION
        @type QListWidgetItem
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot(int)
    def on_listFaces_currentRowChanged(self, currentRow):
        """
        Slot documentation goes here.

        @param currentRow DESCRIPTION
        @type int
        """
        # TODO: not implemented yet
        raise NotImplementedError
