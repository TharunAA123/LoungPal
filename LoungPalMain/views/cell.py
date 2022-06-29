# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\~~OPERATION AIRONE~~\MVM\~Grade 12\Cse\LoungPal\Frontend\cell.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class MapCell(object):
    
    def __init__(self, row, column, name, unique_id, service_no):
        self._row = row
        self._column = column
        self._name = name
        self._unique_id = unique_id
        self._serv_no = service_no

        self.set_highlight_colors()

        self._is_source_select = False
        self._is_destination_select = False
        self._is_path = False
    
    def set_highlight_colors(self):#new part 2
        self.focus_in_source_color = "background-color: rgb(255,87,90); border: solid rgb(0, 255, 17);"
        self.focus_in_destination_color = "background-color: rgb(3,253,252); border: solid rgb(0, 255, 17);"#rgb(215,238,16)
        self.focus_in_path_color = "background-color: rgb(215,238,16); border: solid rgb(0, 255, 17);"
        self.focus_out_color = "background-color: rgb(202,214,240); border: solid rgb(66,110,199); "

    def init_highlight(self):
        self._is_source_select = False
        self._is_destination_select = False
        self._is_path = False
        self.gridLayoutWidget.setStyleSheet(self.focus_out_color)   
        
    def highlight(self, is_source=False, is_destination=False, is_path=False):
        self._is_destination_select = is_destination
        self._is_source_select = is_source
        self._is_path = is_path
        if self._is_destination_select:
            self.gridLayoutWidget.setStyleSheet(self.focus_in_destination_color)
        if self._is_source_select:
            self.gridLayoutWidget.setStyleSheet(self.focus_in_source_color)
        if self._is_path:
            self.gridLayoutWidget.setStyleSheet(self.focus_in_path_color)
    
            
    def remove_highlight(self, is_source=False, is_destination=False, is_path=False):
        if self._is_path and is_path:
            self.gridLayoutWidget.setStyleSheet(self.focus_out_color)
            self._is_path = False
        if self._is_destination_select and is_destination:
            self.gridLayoutWidget.setStyleSheet(self.focus_out_color)
            self._is_destination_select = False
        if self._is_source_select and is_source:
            self.gridLayoutWidget.setStyleSheet(self.focus_out_color)
            self._is_source_select = False        
    
    def getCell(self):
        self.gridLayoutWidget = QtWidgets.QWidget()
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 130, 160, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.serv_name = QtWidgets.QLabel(self.gridLayoutWidget)
        if self._name in "EMPTY":
            self.serv_name.setText(" ")
        else:    
            self.serv_name.setText(self._name)
        self.serv_name.setObjectName("serv_name")
        self.gridLayout.addWidget(self.serv_name, 0, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 3)
        self.gridLayout.setRowStretch(1, 2)

        #QtCore.QMetaObject.connectSlotsByName()
        self.gridLayoutWidget.setStyleSheet("background-color: rgb(202,214,240); border: solid rgb(66,110,199); ")
        self.init_highlight()
        return self.gridLayoutWidget
    
    def get_service_no(self):
        return self._serv_no

    
    



