# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'core/synthesis/structure_synthesis/structure_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from core.QtModules import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(430, 654)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/number.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.edges_label = QtWidgets.QLabel(Form)
        self.edges_label.setObjectName("edges_label")
        self.horizontalLayout_4.addWidget(self.edges_label)
        self.edges_text = QtWidgets.QLineEdit(Form)
        self.edges_text.setReadOnly(True)
        self.edges_text.setObjectName("edges_text")
        self.horizontalLayout_4.addWidget(self.edges_text)
        self.expr_copy = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expr_copy.setIcon(icon1)
        self.expr_copy.setObjectName("expr_copy")
        self.horizontalLayout_4.addWidget(self.expr_copy)
        self.expr_add_collection = QtWidgets.QPushButton(Form)
        self.expr_add_collection.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/collections.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.expr_add_collection.setIcon(icon2)
        self.expr_add_collection.setObjectName("expr_add_collection")
        self.horizontalLayout_4.addWidget(self.expr_add_collection)
        self.from_mechanism_button = QtWidgets.QPushButton(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/merge_from.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.from_mechanism_button.setIcon(icon3)
        self.from_mechanism_button.setAutoDefault(True)
        self.from_mechanism_button.setDefault(True)
        self.from_mechanism_button.setObjectName("from_mechanism_button")
        self.horizontalLayout_4.addWidget(self.from_mechanism_button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.main_splitter = QtWidgets.QSplitter(Form)
        self.main_splitter.setOrientation(QtCore.Qt.Vertical)
        self.main_splitter.setObjectName("main_splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.main_splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nj_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nj_label.setObjectName("nj_label")
        self.gridLayout.addWidget(self.nj_label, 0, 1, 1, 1)
        self.nl_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nl_label.setObjectName("nl_label")
        self.gridLayout.addWidget(self.nl_label, 0, 0, 1, 1)
        self.nl_input = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.nl_input.setMinimum(4)
        self.nl_input.setObjectName("nl_input")
        self.gridLayout.addWidget(self.nl_input, 2, 0, 1, 1)
        self.nj_input = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.nj_input.setMinimum(4)
        self.nj_input.setObjectName("nj_input")
        self.gridLayout.addWidget(self.nj_input, 2, 1, 1, 1)
        self.dof_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dof_label.setObjectName("dof_label")
        self.gridLayout.addWidget(self.dof_label, 0, 2, 1, 1)
        self.dof = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.dof.setEnabled(False)
        self.dof.setMinimum(-99)
        self.dof.setProperty("value", 1)
        self.dof.setObjectName("dof")
        self.gridLayout.addWidget(self.dof, 2, 2, 1, 1)
        self.keep_dof = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.keep_dof.setChecked(True)
        self.keep_dof.setObjectName("keep_dof")
        self.gridLayout.addWidget(self.keep_dof, 0, 3, 1, 1)
        self.graph_degenerate = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_degenerate.sizePolicy().hasHeightForWidth())
        self.graph_degenerate.setSizePolicy(sizePolicy)
        self.graph_degenerate.setObjectName("graph_degenerate")
        self.graph_degenerate.addItem("")
        self.graph_degenerate.addItem("")
        self.graph_degenerate.addItem("")
        self.gridLayout.addWidget(self.graph_degenerate, 2, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.number_synthesis_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.number_synthesis_button.setAutoDefault(True)
        self.number_synthesis_button.setObjectName("number_synthesis_button")
        self.horizontalLayout_2.addWidget(self.number_synthesis_button)
        self.assortment_clear_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assortment_clear_button.sizePolicy().hasHeightForWidth())
        self.assortment_clear_button.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.assortment_clear_button.setIcon(icon4)
        self.assortment_clear_button.setObjectName("assortment_clear_button")
        self.horizontalLayout_2.addWidget(self.assortment_clear_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.link_assortment_list = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.link_assortment_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.link_assortment_list.setIndentation(10)
        self.link_assortment_list.setObjectName("link_assortment_list")
        self.verticalLayout_2.addWidget(self.link_assortment_list)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.main_splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graph_engine_text = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.graph_engine_text.setObjectName("graph_engine_text")
        self.horizontalLayout.addWidget(self.graph_engine_text)
        self.graph_engine = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.graph_engine.setObjectName("graph_engine")
        self.horizontalLayout.addWidget(self.graph_engine)
        self.reload_atlas = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.reload_atlas.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/data_update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reload_atlas.setIcon(icon5)
        self.reload_atlas.setObjectName("reload_atlas")
        self.horizontalLayout.addWidget(self.reload_atlas)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.graph_link_as_node = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.graph_link_as_node.setObjectName("graph_link_as_node")
        self.horizontalLayout.addWidget(self.graph_link_as_node)
        self.graph_show_label = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.graph_show_label.setChecked(True)
        self.graph_show_label.setObjectName("graph_show_label")
        self.horizontalLayout.addWidget(self.graph_show_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.structure_synthesis_all_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.structure_synthesis_all_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.structure_synthesis_all_button.setAutoDefault(True)
        self.structure_synthesis_all_button.setObjectName("structure_synthesis_all_button")
        self.horizontalLayout_5.addWidget(self.structure_synthesis_all_button)
        self.structure_synthesis_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.structure_synthesis_button.setObjectName("structure_synthesis_button")
        self.horizontalLayout_5.addWidget(self.structure_synthesis_button)
        self.structure_list_clear_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.structure_list_clear_button.sizePolicy().hasHeightForWidth())
        self.structure_list_clear_button.setSizePolicy(sizePolicy)
        self.structure_list_clear_button.setIcon(icon4)
        self.structure_list_clear_button.setObjectName("structure_list_clear_button")
        self.horizontalLayout_5.addWidget(self.structure_list_clear_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.structure_list = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.structure_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.structure_list.setIconSize(QtCore.QSize(200, 200))
        self.structure_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.structure_list.setViewMode(QtWidgets.QListView.IconMode)
        self.structure_list.setUniformItemSizes(True)
        self.structure_list.setObjectName("structure_list")
        self.verticalLayout_3.addWidget(self.structure_list)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.time_title_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.time_title_label.setObjectName("time_title_label")
        self.horizontalLayout_6.addWidget(self.time_title_label)
        self.time_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_6.addWidget(self.time_label)
        self.paint_time_title_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.paint_time_title_label.setObjectName("paint_time_title_label")
        self.horizontalLayout_6.addWidget(self.paint_time_title_label)
        self.paint_time_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.paint_time_label.setObjectName("paint_time_label")
        self.horizontalLayout_6.addWidget(self.paint_time_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.save_atlas = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_atlas.setIcon(icon6)
        self.save_atlas.setObjectName("save_atlas")
        self.horizontalLayout_6.addWidget(self.save_atlas)
        self.save_edges = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/save_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_edges.setIcon(icon7)
        self.save_edges.setObjectName("save_edges")
        self.horizontalLayout_6.addWidget(self.save_edges)
        self.edges2atlas_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/edges_to_atlas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edges2atlas_button.setIcon(icon8)
        self.edges2atlas_button.setIconSize(QtCore.QSize(40, 16))
        self.edges2atlas_button.setObjectName("edges2atlas_button")
        self.horizontalLayout_6.addWidget(self.edges2atlas_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.main_splitter)

        self.retranslateUi(Form)
        self.graph_degenerate.setCurrentIndex(1)
        self.graph_engine.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.edges_label.setText(_translate("Form", "Edge set:"))
        self.expr_copy.setStatusTip(_translate("Form", "Copy expression."))
        self.expr_add_collection.setStatusTip(_translate("Form", "Add to collection."))
        self.from_mechanism_button.setStatusTip(_translate("Form", "Analyze current mechanism from canvas."))
        self.nj_label.setToolTip(_translate("Form", "Number of joints"))
        self.nj_label.setText(_translate("Form", "NJ (?)"))
        self.nl_label.setToolTip(_translate("Form", "Number of links"))
        self.nl_label.setText(_translate("Form", "NL (?)"))
        self.dof_label.setToolTip(_translate("Form", "Degree of freedom"))
        self.dof_label.setText(_translate("Form", "DOF (?)"))
        self.keep_dof.setStatusTip(_translate("Form", "Keep the degrees of freedom when adjusting numbers."))
        self.keep_dof.setText(_translate("Form", "Keep the DOF"))
        self.graph_degenerate.setItemText(0, _translate("Form", "Only degenerate"))
        self.graph_degenerate.setItemText(1, _translate("Form", "No degenerate"))
        self.graph_degenerate.setItemText(2, _translate("Form", "All"))
        self.number_synthesis_button.setStatusTip(_translate("Form", "Find the possible number of different joints."))
        self.number_synthesis_button.setText(_translate("Form", "Number Synthesis"))
        self.link_assortment_list.headerItem().setText(0, _translate("Form", "Link Assortment / Contracted Link Assortment"))
        self.graph_engine_text.setText(_translate("Form", "Engine: "))
        self.graph_engine.setStatusTip(_translate("Form", "Layout engine from NetworkX."))
        self.reload_atlas.setToolTip(_translate("Form", "Re-layout"))
        self.graph_link_as_node.setStatusTip(_translate("Form", "Show the edges as nodes."))
        self.graph_link_as_node.setText(_translate("Form", "Link as node"))
        self.graph_show_label.setText(_translate("Form", "Show labels"))
        self.structure_synthesis_all_button.setStatusTip(_translate("Form", "Find the structure of mechanism from all numbers."))
        self.structure_synthesis_all_button.setText(_translate("Form", "Find All"))
        self.structure_synthesis_button.setText(_translate("Form", "Find by Assortment"))
        self.time_title_label.setText(_translate("Form", "Find in:"))
        self.paint_time_title_label.setText(_translate("Form", "Painted in:"))
        self.save_atlas.setStatusTip(_translate("Form", "Save the atlas to image file."))
        self.save_atlas.setText(_translate("Form", "Save as image"))
        self.save_edges.setStatusTip(_translate("Form", "Save the edges of atlas to text file."))
        self.save_edges.setText(_translate("Form", "Save as list"))
        self.edges2atlas_button.setStatusTip(_translate("Form", "Load the edges data from text file, then save them to image files."))


import icons_rc
