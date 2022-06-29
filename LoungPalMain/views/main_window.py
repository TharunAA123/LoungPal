# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\~~OPERATION AIRONE~~\MVM\~Grade 12\Cse\LoungPal\Frontend\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from views.cell import MapCell
from model.sql_operations import SqlOperations

class Ui_MainWindow(object):
    
    def __init__(self):
        self._rows = 0
        self._columns = 0
        self._sql_operations = SqlOperations()
        self._location_dict = self.load_locations()
        self._location_cell_dict = {}
        
        
    def load_locations(self):
        return self._sql_operations.get_all_locations()    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1168, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.grid = QtWidgets.QHBoxLayout()
        self.grid.setObjectName("grid")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(10, 74, 41, 16))
        self.label_7.setObjectName("label_7")
        self.new_pwd_inp = QtWidgets.QLineEdit(self.groupBox_5)
        self.new_pwd_inp.setGeometry(QtCore.QRect(90, 110, 131, 20))
        self.new_pwd_inp.setText("")
        self.new_pwd_inp.setObjectName("new_pwd_inp")
        self.new_userid_inp = QtWidgets.QLineEdit(self.groupBox_5)
        self.new_userid_inp.setGeometry(QtCore.QRect(90, 72, 131, 20))
        self.new_userid_inp.setText("")
        self.new_userid_inp.setObjectName("new_userid_inp")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(10, 112, 61, 16))
        self.label_8.setObjectName("label_8")
        self.signup_button = QtWidgets.QPushButton(self.groupBox_5)
        self.signup_button.setGeometry(QtCore.QRect(80, 150, 75, 31))
        self.signup_button.setObjectName("signup_button")
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(9, 42, 71, 16))
        self.label_9.setObjectName("label_9")
        self.user_name_inp = QtWidgets.QLineEdit(self.groupBox_5)
        self.user_name_inp.setGeometry(QtCore.QRect(89, 40, 131, 20))
        self.user_name_inp.setText("")
        self.user_name_inp.setObjectName("user_name_inp")
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(10, 39, 41, 16))
        self.label.setObjectName("label")
        self.pwd_inp = QtWidgets.QLineEdit(self.groupBox_4)
        self.pwd_inp.setGeometry(QtCore.QRect(80, 74, 141, 21))
        self.pwd_inp.setText("")
        self.pwd_inp.setObjectName("pwd_inp")
        self.user_id_inp = QtWidgets.QLineEdit(self.groupBox_4)
        self.user_id_inp.setGeometry(QtCore.QRect(80, 37, 141, 20))
        self.user_id_inp.setText("")
        self.user_id_inp.setObjectName("user_id_inp")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 77, 61, 16))
        self.label_3.setObjectName("label_3")
        self.login_button = QtWidgets.QPushButton(self.groupBox_4)
        self.login_button.setGeometry(QtCore.QRect(80, 110, 75, 31))
        self.login_button.setObjectName("login_button")
        self.status_label = QtWidgets.QLabel(self.groupBox_4)
        self.status_label.setGeometry(QtCore.QRect(20, 170, 211, 20))
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(14, 101, 71, 20))
        self.label_2.setObjectName("label_2")
        self.search_button = QtWidgets.QPushButton(self.groupBox_3)
        self.search_button.setGeometry(QtCore.QRect(14, 146, 75, 23))
        self.search_button.setObjectName("search_button")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(14, 64, 47, 13))
        self.label_4.setObjectName("label_4")
        self.source_dropdn = QtWidgets.QComboBox(self.groupBox_3)
        self.source_dropdn.setGeometry(QtCore.QRect(80, 61, 180, 22))
        self.source_dropdn.setObjectName("source_dropdn")
        #self.source_dropdn.addItem("")
        #self.source_dropdn.setItemText(0, "")
        self.dest_dropdn = QtWidgets.QComboBox(self.groupBox_3)
        self.dest_dropdn.setGeometry(QtCore.QRect(80, 101, 180, 22))
        self.dest_dropdn.setObjectName("dest_dropdn")
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.grid.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.map_layout = QtWidgets.QGridLayout()
        self.map_layout.setObjectName("map_layout")
        self.gridLayout_4.addLayout(self.map_layout, 0, 0, 1, 1)
        self.grid.addWidget(self.groupBox)
        self.grid.setStretch(0, 1)
        self.grid.setStretch(1, 3)
        self.gridLayout.addLayout(self.grid, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1168, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.groupBox.setEnabled(False)
        self.groupBox_3.setEnabled(False)
        
        self.init_signals()
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    def init_signals(self):
        self.login_button.clicked.connect(self.onLoginClick)
        self.signup_button.clicked.connect(self.onSignupClick)
        self.source_dropdn.activated.connect(self.onSourceSelect)
        self.dest_dropdn.activated.connect(self.onDestinationSelect)
        self.search_button.clicked.connect(self.onSearchClick)


        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_5.setTitle(_translate("MainWindow", "New User Sign up"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>User ID</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Password</p></body></html>"))
        self.signup_button.setText(_translate("MainWindow", "Sign up"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>User Name</p></body></html>"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Registered User Login"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>User ID</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Password</p></body></html>"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Search Route"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Destination</p></body></html>"))
        self.search_button.setText(_translate("MainWindow", "Show Route"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Source</p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Terminal layout"))
        
        
        for pos, service in self._location_dict.items():
            self._rows = pos[0] if pos[0] > self._rows else self._rows
            self._columns = pos[1] if pos[1] > self._columns else self._columns
            map_cell = MapCell(pos[0], pos[1], service[0], service[1], service[2])
            map_cell_widget = map_cell.getCell()
            if service[0] not in "EMPTY":
                self.source_dropdn.addItem(service[0], map_cell)
                self.dest_dropdn.addItem(service[0], map_cell)
            
            
            self.map_layout.addWidget(map_cell_widget, pos[0], pos[1])
            self._location_cell_dict[service[1]] = map_cell
            
    def onLoginClick(self):
        x = self._sql_operations.login_request(self.user_id_inp.text(), self.pwd_inp.text())

        if x[0]:
            self.groupBox.setEnabled(True)
            self.groupBox_3.setEnabled(True)
        else:
            self.groupBox.setEnabled(False)
            self.groupBox_3.setEnabled(False)

        self.status_label.setText(x[1]) 
        
        for key,value in self._location_cell_dict.items():
            value.remove_highlight(is_source=True,is_destination=True,is_path=True)
        
    def onSignupClick(self):
        x = self._sql_operations.signup(self.user_name_inp.text(), self.new_userid_inp.text(), self.new_pwd_inp.text())     
        
        self.status_label.setText(x)
        
    def onSourceSelect(self):
        for count in range(self.source_dropdn.count()):
            self.source_dropdn.itemData(count).remove_highlight(is_source=True)
            #self.source_dropdn.itemData(count).remove_highlight(is_path=True)
            
        for key,value in self._location_cell_dict.items():
            value.remove_highlight(is_path=True)
            
        selected_cell = self.source_dropdn.currentData()
        selected_cell.__class__ = MapCell
        selected_cell.highlight(is_source=True)
    
    def onDestinationSelect(self):#new part 1
        for count in range(self.source_dropdn.count()):
            self.dest_dropdn.itemData(count).remove_highlight(is_destination=True)
            #self.dest_dropdn.itemData(count).remove_highlight(is_path=True)
            
        for key,value in self._location_cell_dict.items():
            value.remove_highlight(is_path=True)    
            
        selected_cell = self.dest_dropdn.currentData()
        selected_cell.__class__ = MapCell
        selected_cell.highlight(is_destination=True)    
            
            
    def onSearchClick(self):
        destination_cell = self.dest_dropdn.currentData()
        source_cell = self.source_dropdn.currentData()
        destination_cell.__class__ = MapCell
        source_cell.__class__ = MapCell
        route_list = self._sql_operations.get_route(source_cell.get_service_no(),
                                                    destination_cell.get_service_no())
        #print(route_list)
        
        
        if route_list:
            
            for route in route_list:
                path_cell = self._location_cell_dict[route]
                path_cell.highlight(is_path=True)
            
        else:
            print("Route not found")
            
