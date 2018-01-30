# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/桌面/Pyslvs-PyQt5/core/synthesis/DimensionalSynthesis/Algorithm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(527, 636)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/DimensionalSynthesis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pointNum = QtWidgets.QLabel(self.horizontalWidget)
        self.pointNum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pointNum.setObjectName("pointNum")
        self.horizontalLayout_2.addWidget(self.pointNum)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.Point_list = QtWidgets.QListWidget(self.horizontalWidget)
        self.Point_list.setObjectName("Point_list")
        self.verticalLayout_2.addWidget(self.Point_list)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.X_coordinate = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.X_coordinate.setMinimum(-9999.99)
        self.X_coordinate.setMaximum(9999.99)
        self.X_coordinate.setObjectName("X_coordinate")
        self.horizontalLayout_8.addWidget(self.X_coordinate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_6 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)
        self.Y_coordinate = QtWidgets.QDoubleSpinBox(self.horizontalWidget)
        self.Y_coordinate.setMinimum(-9999.99)
        self.Y_coordinate.setMaximum(9999.99)
        self.Y_coordinate.setObjectName("Y_coordinate")
        self.horizontalLayout_12.addWidget(self.Y_coordinate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.horizontalWidget)
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.horizontalWidget_2)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_2.addWidget(self.horizontalWidget_2)
        self.horizontalLayout_13.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.clearAll = QtWidgets.QPushButton(self.horizontalWidget)
        self.clearAll.setAutoDefault(False)
        self.clearAll.setObjectName("clearAll")
        self.verticalLayout_3.addWidget(self.clearAll)
        self.pathAdjust = QtWidgets.QPushButton(self.horizontalWidget)
        self.pathAdjust.setObjectName("pathAdjust")
        self.verticalLayout_3.addWidget(self.pathAdjust)
        self.line_5 = QtWidgets.QFrame(self.horizontalWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        self.series = QtWidgets.QPushButton(self.horizontalWidget)
        self.series.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/formula.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.series.setIcon(icon1)
        self.series.setAutoDefault(False)
        self.series.setObjectName("series")
        self.verticalLayout_3.addWidget(self.series)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.importCSV = QtWidgets.QPushButton(self.horizontalWidget)
        self.importCSV.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/CSV.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importCSV.setIcon(icon2)
        self.importCSV.setIconSize(QtCore.QSize(20, 20))
        self.importCSV.setObjectName("importCSV")
        self.horizontalLayout.addWidget(self.importCSV)
        self.importXLSX = QtWidgets.QPushButton(self.horizontalWidget)
        self.importXLSX.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/excel_2013.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importXLSX.setIcon(icon3)
        self.importXLSX.setIconSize(QtCore.QSize(20, 20))
        self.importXLSX.setObjectName("importXLSX")
        self.horizontalLayout.addWidget(self.importXLSX)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.close_path = QtWidgets.QPushButton(self.horizontalWidget)
        self.close_path.setObjectName("close_path")
        self.verticalLayout_3.addWidget(self.close_path)
        self.line_6 = QtWidgets.QFrame(self.horizontalWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_3.addWidget(self.line_6)
        self.moveUp = QtWidgets.QPushButton(self.horizontalWidget)
        self.moveUp.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveUp.setIcon(icon4)
        self.moveUp.setAutoDefault(False)
        self.moveUp.setObjectName("moveUp")
        self.verticalLayout_3.addWidget(self.moveUp)
        self.moveDown = QtWidgets.QPushButton(self.horizontalWidget)
        self.moveDown.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moveDown.setIcon(icon5)
        self.moveDown.setAutoDefault(False)
        self.moveDown.setObjectName("moveDown")
        self.verticalLayout_3.addWidget(self.moveDown)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.add = QtWidgets.QPushButton(self.horizontalWidget)
        self.add.setMaximumSize(QtCore.QSize(40, 16777215))
        self.add.setAutoDefault(False)
        self.add.setObjectName("add")
        self.horizontalLayout_11.addWidget(self.add)
        self.remove = QtWidgets.QPushButton(self.horizontalWidget)
        self.remove.setMaximumSize(QtCore.QSize(40, 16777215))
        self.remove.setAutoDefault(False)
        self.remove.setObjectName("remove")
        self.horizontalLayout_11.addWidget(self.remove)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addWidget(self.horizontalWidget)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_7.addWidget(self.line_2)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.horizontalLayout_14.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Ax = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.Ax.setMaximumSize(QtCore.QSize(70, 16777215))
        self.Ax.setMinimum(-1000000.0)
        self.Ax.setMaximum(1000000.0)
        self.Ax.setSingleStep(10.0)
        self.Ax.setObjectName("Ax")
        self.horizontalLayout_3.addWidget(self.Ax)
        self.Ay = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.Ay.setMaximumSize(QtCore.QSize(70, 16777215))
        self.Ay.setMinimum(-1000000.0)
        self.Ay.setMaximum(1000000.0)
        self.Ay.setSingleStep(10.0)
        self.Ay.setObjectName("Ay")
        self.horizontalLayout_3.addWidget(self.Ay)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.Ar = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.Ar.setMaximum(10000.0)
        self.Ar.setSingleStep(10.0)
        self.Ar.setObjectName("Ar")
        self.verticalLayout_9.addWidget(self.Ar)
        self.horizontalLayout_14.addLayout(self.verticalLayout_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.line_4 = QtWidgets.QFrame(self.groupBox)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_7.addWidget(self.line_4)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_11.addWidget(self.label_3)
        self.horizontalLayout_15.addLayout(self.verticalLayout_11)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Bx = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.Bx.setMaximumSize(QtCore.QSize(70, 16777215))
        self.Bx.setMinimum(-1000000.0)
        self.Bx.setMaximum(1000000.0)
        self.Bx.setSingleStep(10.0)
        self.Bx.setObjectName("Bx")
        self.horizontalLayout_5.addWidget(self.Bx)
        self.By = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.By.setMaximumSize(QtCore.QSize(70, 16777215))
        self.By.setMinimum(-1000000.0)
        self.By.setMaximum(1000000.0)
        self.By.setSingleStep(10.0)
        self.By.setObjectName("By")
        self.horizontalLayout_5.addWidget(self.By)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.Br = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.Br.setMaximum(10000.0)
        self.Br.setSingleStep(10.0)
        self.Br.setObjectName("Br")
        self.verticalLayout_10.addWidget(self.Br)
        self.horizontalLayout_15.addLayout(self.verticalLayout_10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16.addWidget(self.groupBox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalGroupBox = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.verticalGroupBox)
        self.horizontalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Result_list = QtWidgets.QListWidget(self.verticalGroupBox)
        self.Result_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Result_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Result_list.setObjectName("Result_list")
        self.horizontalLayout_6.addWidget(self.Result_list)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Result_chart = QtWidgets.QPushButton(self.verticalGroupBox)
        self.Result_chart.setObjectName("Result_chart")
        self.verticalLayout_6.addWidget(self.Result_chart)
        self.Result_load_settings = QtWidgets.QPushButton(self.verticalGroupBox)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/dataupdate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Result_load_settings.setIcon(icon6)
        self.Result_load_settings.setObjectName("Result_load_settings")
        self.verticalLayout_6.addWidget(self.Result_load_settings)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.deleteButton = QtWidgets.QPushButton(self.verticalGroupBox)
        self.deleteButton.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon7)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout_6.addWidget(self.deleteButton)
        self.mergeButton = QtWidgets.QPushButton(self.verticalGroupBox)
        self.mergeButton.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/merge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mergeButton.setIcon(icon8)
        self.mergeButton.setObjectName("mergeButton")
        self.verticalLayout_6.addWidget(self.mergeButton)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout.addWidget(self.verticalGroupBox)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.profile_label = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.profile_label.setWordWrap(True)
        self.profile_label.setObjectName("profile_label")
        self.horizontalLayout_7.addWidget(self.profile_label)
        self.load_profile = QtWidgets.QToolButton(self.verticalGroupBox_2)
        self.load_profile.setObjectName("load_profile")
        self.horizontalLayout_7.addWidget(self.load_profile)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.line = QtWidgets.QFrame(self.verticalGroupBox_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.verticalWidget = QtWidgets.QWidget(self.verticalGroupBox_2)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.type0 = QtWidgets.QRadioButton(self.verticalWidget)
        self.type0.setChecked(False)
        self.type0.setObjectName("type0")
        self.verticalLayout_5.addWidget(self.type0)
        self.type1 = QtWidgets.QRadioButton(self.verticalWidget)
        self.type1.setObjectName("type1")
        self.verticalLayout_5.addWidget(self.type1)
        self.type2 = QtWidgets.QRadioButton(self.verticalWidget)
        self.type2.setChecked(True)
        self.type2.setObjectName("type2")
        self.verticalLayout_5.addWidget(self.type2)
        self.verticalLayout_4.addWidget(self.verticalWidget)
        self.advanceButton = QtWidgets.QPushButton(self.verticalGroupBox_2)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/properties.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.advanceButton.setIcon(icon9)
        self.advanceButton.setObjectName("advanceButton")
        self.verticalLayout_4.addWidget(self.advanceButton)
        self.line_3 = QtWidgets.QFrame(self.verticalGroupBox_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.label_7 = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.timeShow = QtWidgets.QLabel(self.verticalGroupBox_2)
        self.timeShow.setObjectName("timeShow")
        self.verticalLayout_4.addWidget(self.timeShow)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.verticalGroupBox_2)
        self.horizontalLayout_16.addLayout(self.verticalLayout)
        self.verticalLayout_12.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.timePanel = QtWidgets.QWidget(Form)
        self.timePanel.setObjectName("timePanel")
        self.timePanelLayout = QtWidgets.QHBoxLayout(self.timePanel)
        self.timePanelLayout.setContentsMargins(6, 0, 6, 0)
        self.timePanelLayout.setObjectName("timePanelLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.timePanel)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        self.portText = QtWidgets.QLineEdit(self.timePanel)
        self.portText.setObjectName("portText")
        self.horizontalLayout_9.addWidget(self.portText)
        self.timePanelLayout.addLayout(self.horizontalLayout_9)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.timePanelLayout.addItem(spacerItem4)
        self.GenerateZMQ = QtWidgets.QPushButton(self.timePanel)
        self.GenerateZMQ.setEnabled(False)
        self.GenerateZMQ.setMinimumSize(QtCore.QSize(120, 0))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/ZeroMQ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GenerateZMQ.setIcon(icon10)
        self.GenerateZMQ.setAutoDefault(True)
        self.GenerateZMQ.setObjectName("GenerateZMQ")
        self.timePanelLayout.addWidget(self.GenerateZMQ)
        self.GenerateLocal = QtWidgets.QPushButton(self.timePanel)
        self.GenerateLocal.setEnabled(False)
        self.GenerateLocal.setMinimumSize(QtCore.QSize(120, 0))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/local.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GenerateLocal.setIcon(icon11)
        self.GenerateLocal.setAutoDefault(True)
        self.GenerateLocal.setObjectName("GenerateLocal")
        self.timePanelLayout.addWidget(self.GenerateLocal)
        self.horizontalLayout_4.addWidget(self.timePanel)
        self.verticalLayout_12.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("Form", "Path"))
        self.pointNum.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aa00;\">0</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "x: "))
        self.label_6.setText(_translate("Form", "y: "))
        self.clearAll.setStatusTip(_translate("Form", "Clear all points."))
        self.clearAll.setText(_translate("Form", "Clear All"))
        self.pathAdjust.setStatusTip(_translate("Form", "Process path data, such as moving or scaling."))
        self.pathAdjust.setText(_translate("Form", "Adjust ..."))
        self.series.setToolTip(_translate("Form", "Formula"))
        self.series.setStatusTip(_translate("Form", "Generat points from formula."))
        self.importCSV.setToolTip(_translate("Form", "CSV"))
        self.importCSV.setStatusTip(_translate("Form", "Import path from CSV format."))
        self.importXLSX.setToolTip(_translate("Form", "Microsoft Excel"))
        self.importXLSX.setStatusTip(_translate("Form", "Import path from Microsoft Excel format."))
        self.close_path.setText(_translate("Form", "Close path"))
        self.add.setText(_translate("Form", "+"))
        self.remove.setText(_translate("Form", "-"))
        self.label_2.setText(_translate("Form", "Driver (A): "))
        self.Ar.setPrefix(_translate("Form", "±"))
        self.label_3.setText(_translate("Form", "Follower (B): "))
        self.Br.setPrefix(_translate("Form", "±"))
        self.verticalGroupBox.setTitle(_translate("Form", "Results"))
        self.Result_chart.setStatusTip(_translate("Form", "Fitness / Time chart"))
        self.Result_chart.setText(_translate("Form", "Chart"))
        self.Result_load_settings.setText(_translate("Form", "Load"))
        self.deleteButton.setStatusTip(_translate("Form", "Delete this result."))
        self.deleteButton.setText(_translate("Form", "Delete"))
        self.mergeButton.setStatusTip(_translate("Form", "Merge this result to canvas."))
        self.mergeButton.setText(_translate("Form", "Merge"))
        self.verticalGroupBox_2.setTitle(_translate("Form", "Options"))
        self.load_profile.setText(_translate("Form", "..."))
        self.type0.setText(_translate("Form", "Genetic Algorithm"))
        self.type1.setText(_translate("Form", "Firefly Algorithm"))
        self.type2.setText(_translate("Form", "Differential Evolution"))
        self.advanceButton.setText(_translate("Form", "Advance ..."))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Time spent: </span></p></body></html>"))
        self.timeShow.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">[N/A]</span></p></body></html>"))
        self.label.setText(_translate("Form", "ZMQ filter: "))
        self.portText.setStatusTip(_translate("Form", "LAN screening."))
        self.portText.setText(_translate("Form", "tcp://*:8000"))
        self.GenerateZMQ.setStatusTip(_translate("Form", "Calculated by the zmq servers."))
        self.GenerateZMQ.setText(_translate("Form", "Synthesis"))
        self.GenerateLocal.setStatusTip(_translate("Form", "Calculated on the local side."))
        self.GenerateLocal.setText(_translate("Form", "Synthesis"))

import icons_rc
import preview_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

