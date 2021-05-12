# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1210, 883)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.movieGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.movieGroupBox.sizePolicy().hasHeightForWidth())
        self.movieGroupBox.setSizePolicy(sizePolicy)
        self.movieGroupBox.setObjectName("movieGroupBox")
        self.horizontalLayout.addWidget(self.movieGroupBox)
        self.rangeGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.rangeGroupBox.setObjectName("rangeGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.rangeGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.maxSpinBox = QtWidgets.QSpinBox(self.rangeGroupBox)
        self.maxSpinBox.setMinimumSize(QtCore.QSize(70, 0))
        self.maxSpinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.maxSpinBox.setMaximum(100000)
        self.maxSpinBox.setProperty("value", 1000)
        self.maxSpinBox.setObjectName("maxSpinBox")
        self.verticalLayout_2.addWidget(self.maxSpinBox)
        self.rangeSliderWidget = QtWidgets.QWidget(self.rangeGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rangeSliderWidget.sizePolicy().hasHeightForWidth())
        self.rangeSliderWidget.setSizePolicy(sizePolicy)
        self.rangeSliderWidget.setMinimumSize(QtCore.QSize(45, 0))
        self.rangeSliderWidget.setMaximumSize(QtCore.QSize(45, 16777215))
        self.rangeSliderWidget.setObjectName("rangeSliderWidget")
        self.verticalLayout_2.addWidget(self.rangeSliderWidget)
        self.minSpinBox = QtWidgets.QSpinBox(self.rangeGroupBox)
        self.minSpinBox.setMinimumSize(QtCore.QSize(70, 0))
        self.minSpinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minSpinBox.setMaximum(100000)
        self.minSpinBox.setProperty("value", 100)
        self.minSpinBox.setObjectName("minSpinBox")
        self.verticalLayout_2.addWidget(self.minSpinBox)
        self.horizontalLayout.addWidget(self.rangeGroupBox)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.locs1Label = QtWidgets.QLabel(self.groupBox)
        self.locs1Label.setObjectName("locs1Label")
        self.verticalLayout.addWidget(self.locs1Label)
        self.locs1TableWidget = QtWidgets.QTableWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locs1TableWidget.sizePolicy().hasHeightForWidth())
        self.locs1TableWidget.setSizePolicy(sizePolicy)
        self.locs1TableWidget.setMaximumSize(QtCore.QSize(16777215, 210))
        self.locs1TableWidget.setShowGrid(True)
        self.locs1TableWidget.setObjectName("locs1TableWidget")
        self.locs1TableWidget.setColumnCount(0)
        self.locs1TableWidget.setRowCount(0)
        self.locs1TableWidget.horizontalHeader().setVisible(False)
        self.locs1TableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.locs1TableWidget.horizontalHeader().setStretchLastSection(True)
        self.locs1TableWidget.verticalHeader().setVisible(False)
        self.locs1TableWidget.verticalHeader().setDefaultSectionSize(20)
        self.verticalLayout.addWidget(self.locs1TableWidget)
        self.locs2Label = QtWidgets.QLabel(self.groupBox)
        self.locs2Label.setObjectName("locs2Label")
        self.verticalLayout.addWidget(self.locs2Label)
        self.locs2TableWidget = QtWidgets.QTableWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locs2TableWidget.sizePolicy().hasHeightForWidth())
        self.locs2TableWidget.setSizePolicy(sizePolicy)
        self.locs2TableWidget.setShowGrid(True)
        self.locs2TableWidget.setObjectName("locs2TableWidget")
        self.locs2TableWidget.setColumnCount(0)
        self.locs2TableWidget.setRowCount(0)
        self.locs2TableWidget.horizontalHeader().setVisible(False)
        self.locs2TableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.locs2TableWidget.horizontalHeader().setStretchLastSection(True)
        self.locs2TableWidget.verticalHeader().setVisible(False)
        self.locs2TableWidget.verticalHeader().setDefaultSectionSize(20)
        self.verticalLayout.addWidget(self.locs2TableWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nmPerPixLabel = QtWidgets.QLabel(self.centralwidget)
        self.nmPerPixLabel.setObjectName("nmPerPixLabel")
        self.horizontalLayout_2.addWidget(self.nmPerPixLabel)
        self.nmPerPixelSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.nmPerPixelSpinBox.setMaximum(1000.0)
        self.nmPerPixelSpinBox.setProperty("value", 160.0)
        self.nmPerPixelSpinBox.setObjectName("nmPerPixelSpinBox")
        self.horizontalLayout_2.addWidget(self.nmPerPixelSpinBox)
        self.frameLabel = QtWidgets.QLabel(self.centralwidget)
        self.frameLabel.setMinimumSize(QtCore.QSize(140, 0))
        self.frameLabel.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frameLabel.setObjectName("frameLabel")
        self.horizontalLayout_2.addWidget(self.frameLabel)
        self.xyiLabel = QtWidgets.QLabel(self.centralwidget)
        self.xyiLabel.setMinimumSize(QtCore.QSize(150, 0))
        self.xyiLabel.setMaximumSize(QtCore.QSize(0, 16777215))
        self.xyiLabel.setScaledContents(False)
        self.xyiLabel.setObjectName("xyiLabel")
        self.horizontalLayout_2.addWidget(self.xyiLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.fileLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileLabel.sizePolicy().hasHeightForWidth())
        self.fileLabel.setSizePolicy(sizePolicy)
        self.fileLabel.setMinimumSize(QtCore.QSize(300, 0))
        self.fileLabel.setMaximumSize(QtCore.QSize(300, 16777215))
        self.fileLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fileLabel.setObjectName("fileLabel")
        self.horizontalLayout_2.addWidget(self.fileLabel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1210, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Movie = QtWidgets.QAction(MainWindow)
        self.actionLoad_Movie.setObjectName("actionLoad_Movie")
        self.actionLoad_Locs2 = QtWidgets.QAction(MainWindow)
        self.actionLoad_Locs2.setObjectName("actionLoad_Locs2")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionLoad_Locs1 = QtWidgets.QAction(MainWindow)
        self.actionLoad_Locs1.setObjectName("actionLoad_Locs1")
        self.actionCapture = QtWidgets.QAction(MainWindow)
        self.actionCapture.setObjectName("actionCapture")
        self.menuFile.addAction(self.actionLoad_Movie)
        self.menuFile.addAction(self.actionLoad_Locs1)
        self.menuFile.addAction(self.actionLoad_Locs2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionCapture)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Visualizer"))
        self.movieGroupBox.setTitle(_translate("MainWindow", "Movie"))
        self.rangeGroupBox.setTitle(_translate("MainWindow", "Contrast"))
        self.groupBox.setTitle(_translate("MainWindow", "Localization Fit Parameters"))
        self.locs1Label.setText(_translate("MainWindow", "Localizations 1 Results"))
        self.locs2Label.setText(_translate("MainWindow", "Localizations 2 Results"))
        self.nmPerPixLabel.setText(_translate("MainWindow", "nm per pixel:"))
        self.frameLabel.setText(_translate("MainWindow", "NA"))
        self.xyiLabel.setText(_translate("MainWindow", "NA"))
        self.fileLabel.setText(_translate("MainWindow", "NA"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Movie.setText(_translate("MainWindow", "Load Movie"))
        self.actionLoad_Locs2.setText(_translate("MainWindow", "Load Localizations 2"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionLoad_Locs1.setText(_translate("MainWindow", "Load Localizations 1"))
        self.actionCapture.setText(_translate("MainWindow", "Frame Capture"))
