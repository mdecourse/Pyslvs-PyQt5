# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/Pyslvs-PyQt5/core/panel/run_Triangle_Solver_directionItem.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(604, 142)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Type = QtWidgets.QComboBox(Form)
        self.Type.setObjectName("Type")
        self.Type.addItem("")
        self.Type.addItem("")
        self.horizontalLayout_3.addWidget(self.Type)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.p1Layout = QtWidgets.QHBoxLayout()
        self.p1Layout.setObjectName("p1Layout")
        self.p1Option = QtWidgets.QComboBox(self.widget_2)
        self.p1Option.setObjectName("p1Option")
        self.p1Option.addItem("")
        self.p1Option.addItem("")
        self.p1Layout.addWidget(self.p1Option)
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.p1 = QtWidgets.QComboBox(self.widget)
        self.p1.setObjectName("p1")
        self.horizontalLayout.addWidget(self.p1)
        self.x1 = QtWidgets.QDoubleSpinBox(self.widget)
        self.x1.setObjectName("x1")
        self.horizontalLayout.addWidget(self.x1)
        self.y1 = QtWidgets.QDoubleSpinBox(self.widget)
        self.y1.setObjectName("y1")
        self.horizontalLayout.addWidget(self.y1)
        self.p1Layout.addWidget(self.widget)
        self.verticalLayout.addLayout(self.p1Layout)
        self.p2Layout = QtWidgets.QHBoxLayout()
        self.p2Layout.setObjectName("p2Layout")
        self.p2Option = QtWidgets.QComboBox(self.widget_2)
        self.p2Option.setObjectName("p2Option")
        self.p2Option.addItem("")
        self.p2Option.addItem("")
        self.p2Layout.addWidget(self.p2Option)
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.p2 = QtWidgets.QComboBox(self.widget_6)
        self.p2.setObjectName("p2")
        self.horizontalLayout_2.addWidget(self.p2)
        self.x2 = QtWidgets.QDoubleSpinBox(self.widget_6)
        self.x2.setObjectName("x2")
        self.horizontalLayout_2.addWidget(self.x2)
        self.y2 = QtWidgets.QDoubleSpinBox(self.widget_6)
        self.y2.setObjectName("y2")
        self.horizontalLayout_2.addWidget(self.y2)
        self.p2Layout.addWidget(self.widget_6)
        self.verticalLayout.addLayout(self.p2Layout)
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.len1Layout = QtWidgets.QHBoxLayout()
        self.len1Layout.setObjectName("len1Layout")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.len1Layout.addWidget(self.label)
        self.len1 = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.len1.setMinimum(0.01)
        self.len1.setProperty("value", 10.0)
        self.len1.setObjectName("len1")
        self.len1Layout.addWidget(self.len1)
        self.verticalLayout_3.addLayout(self.len1Layout)
        self.len2Layout = QtWidgets.QHBoxLayout()
        self.len2Layout.setObjectName("len2Layout")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.len2Layout.addWidget(self.label_2)
        self.len2 = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.len2.setMinimum(0.01)
        self.len2.setProperty("value", 10.0)
        self.len2.setObjectName("len2")
        self.len2Layout.addWidget(self.len2)
        self.verticalLayout_3.addLayout(self.len2Layout)
        self.angleLayout = QtWidgets.QHBoxLayout()
        self.angleLayout.setObjectName("angleLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.angleLayout.addWidget(self.label_3)
        self.angle = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.angle.setMinimum(0.01)
        self.angle.setProperty("value", 30.0)
        self.angle.setObjectName("angle")
        self.angleLayout.addWidget(self.angle)
        self.verticalLayout_3.addLayout(self.angleLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.addWidget(self.widget_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Type.setItemText(0, _translate("Form", "PLAP"))
        self.Type.setItemText(1, _translate("Form", "PLLP"))
        self.p1Option.setItemText(0, _translate("Form", "Existed Point"))
        self.p1Option.setItemText(1, _translate("Form", "Customize Point"))
        self.p2Option.setItemText(0, _translate("Form", "Existed Point"))
        self.p2Option.setItemText(1, _translate("Form", "Customize Point"))
        self.label.setText(_translate("Form", "Length1"))
        self.label_2.setText(_translate("Form", "Length2"))
        self.label_3.setText(_translate("Form", "Angle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

