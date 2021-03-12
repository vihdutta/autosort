from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from autosort import copyfromdirs, srcdirs
import threading
import time

class WorkerSignals(QtCore.QObject):
    result = QtCore.pyqtSignal(object)

class Worker(QtCore.QRunnable):
    def __init__(self, metadata, replace, sortmethod, destdir):
        super().__init__()
        self.signals = WorkerSignals()
        self.metadata = metadata
        self.replace = replace
        self.sortmethod = sortmethod
        self.destdir = destdir

    @QtCore.pyqtSlot()
    def run(self):
        function = copyfromdirs(self.metadata, self.replace, self.sortmethod, self.destdir)
        for statement in function:
            self.signals.result.emit(statement)

class Ui_MainWindow(object):
    def __init__(self, *args, **kwargs):
        self.threadpool = QtCore.QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("background-color: rgb(55, 57, 67);")
        self.background.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background.setFrameShadow(QtWidgets.QFrame.Plain)
        self.background.setObjectName("background")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.background)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.replace_button = QtWidgets.QRadioButton(self.background)
        self.replace_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.replace_button.setFont(font)
        self.replace_button.setStyleSheet("QRadioButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(143, 129, 89);\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QRadioButton:hover{\n"
"    background-color: rgb(168, 151, 105);\n"
"}\n"
"\n"
"QRadioButton:pressed{\n"
"    background-color: rgb(116, 104, 72);\n"
"}\n"
"\n"
"QRadioButton:indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton:indicator:checked {\n"
"    background-color: rgb(143, 129, 89);\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton:indicator:unchecked {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid white;\n"
"}")
        self.replace_button.setObjectName("replace_button")
        self.nonExclusiveButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.nonExclusiveButtonGroup.setObjectName("nonExclusiveButtonGroup")
        self.nonExclusiveButtonGroup.setExclusive(False)
        self.nonExclusiveButtonGroup.addButton(self.replace_button)
        self.gridLayout_3.addWidget(self.replace_button, 4, 2, 1, 1)
        self.run_button = QtWidgets.QPushButton(self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy)
        self.run_button.setMinimumSize(QtCore.QSize(250, 80))
        self.run_button.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(24)
        self.run_button.setFont(font)
        self.run_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.run_button.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(143, 129, 89);\n"
"    border-radius: 20px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(168, 151, 105);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(116, 104, 72);\n"
"}")
        self.run_button.setAutoDefault(False)
        self.run_button.setFlat(False)
        self.run_button.setObjectName("run_button")
        self.gridLayout_3.addWidget(self.run_button, 8, 2, 1, 1)
        self.destinationdisplay = QtWidgets.QLineEdit(self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.destinationdisplay.sizePolicy().hasHeightForWidth())
        self.destinationdisplay.setSizePolicy(sizePolicy)
        self.destinationdisplay.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.destinationdisplay.setFont(font)
        self.destinationdisplay.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.destinationdisplay.setStyleSheet("color: rgb(198, 208, 221);\n"
"background-color: rgb(61, 63, 72);\n"
"border-radius: 10px;\n"
"padding-right: 10px;")
        self.destinationdisplay.setInputMask("")
        self.destinationdisplay.setText("")
        self.destinationdisplay.setMaxLength(32767)
        self.destinationdisplay.setCursorPosition(0)
        self.destinationdisplay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.destinationdisplay.setReadOnly(True)
        self.destinationdisplay.setObjectName("destinationdisplay")
        self.gridLayout_3.addWidget(self.destinationdisplay, 13, 1, 1, 2)
        self.destination_button = QtWidgets.QPushButton(self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.destination_button.sizePolicy().hasHeightForWidth())
        self.destination_button.setSizePolicy(sizePolicy)
        self.destination_button.setMinimumSize(QtCore.QSize(250, 50))
        self.destination_button.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(20)
        self.destination_button.setFont(font)
        self.destination_button.setMouseTracking(False)
        self.destination_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.destination_button.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(143, 129, 89);\n"
"    border-radius: 15px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(168, 151, 105);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(116, 104, 72);\n"
"}")
        self.destination_button.setAutoDefault(False)
        self.destination_button.setFlat(False)
        self.destination_button.setObjectName("destination_button")
        self.gridLayout_3.addWidget(self.destination_button, 7, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 14, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 8, 3, 1, 1)
        self.metadata_button = QtWidgets.QRadioButton(self.background)
        self.metadata_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.metadata_button.setFont(font)
        self.metadata_button.setStyleSheet("QRadioButton {\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(143, 129, 89);\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QRadioButton:hover{\n"
"\n"
"    background-color: rgb(168, 151, 105);\n"
"}\n"
"\n"
"QRadioButton:pressed{\n"
"    \n"
"    \n"
"    background-color: rgb(116, 104, 72);\n"
"}\n"
"\n"
"QRadioButton:indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton:indicator:checked {\n"
"    background-color: rgb(143, 129, 89);\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QRadioButton:indicator:unchecked {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid white;\n"
"}")
        self.metadata_button.setObjectName("metadata_button")
        self.nonExclusiveButtonGroup.addButton(self.metadata_button)
        self.gridLayout_3.addWidget(self.metadata_button, 5, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(250, 0))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid white;\n"
"    outline: none;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(143, 129, 89);\n"
"    selection-background-color: rgb(168, 151, 105);\n"
"  }\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.organization_box = QtWidgets.QComboBox(self.groupBox)
        self.organization_box.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(12)
        self.organization_box.setFont(font)
        self.organization_box.setStyleSheet("QComboBox{\n"
"    background-color: rgb(143, 129, 89);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: white;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"")
        self.organization_box.setObjectName("organization_box")
        self.organization_box.addItem("")
        self.organization_box.addItem("")
        self.organization_box.addItem("")
        self.gridLayout_6.addWidget(self.organization_box, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 3, 2, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.background)
        self.scrollArea.setMinimumSize(QtCore.QSize(260, 0))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("/* Scroll Bar Stuff*/\n"
"\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: rgb(61, 63, 72);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(143, 129, 89);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(168, 151, 105);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(116, 104, 72);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(61, 63, 72);\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"/*bottom*/\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(61, 63, 72);\n"
"    height: 15px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidget = QtWidgets.QWidget()
        self.scrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 260, 308))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidget.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidget.setSizePolicy(sizePolicy)
        self.scrollAreaWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidget.setAutoFillBackground(False)
        self.scrollAreaWidget.setStyleSheet("")
        self.scrollAreaWidget.setObjectName("scrollAreaWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.console = QtWidgets.QTextEdit(self.scrollAreaWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        self.console.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.console.setFont(font)
        self.console.setToolTipDuration(-1)
        self.console.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.console.setStyleSheet("QTextEdit{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(61, 63, 72);\n"
"    border-radius: 20px;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"    padding-top: 10px;\n"
"    padding-bottom: 10px;\n"
"}\n"
"")
        self.console.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.console.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.console.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.console.setMarkdown("")
        self.console.setPlaceholderText("")
        self.console.setObjectName("console")
        self.gridLayout.addWidget(self.console, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidget)
        self.gridLayout_3.addWidget(self.scrollArea, 2, 1, 7, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 1, 1)
        self.source_button = QtWidgets.QPushButton(self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_button.sizePolicy().hasHeightForWidth())
        self.source_button.setSizePolicy(sizePolicy)
        self.source_button.setMinimumSize(QtCore.QSize(250, 50))
        self.source_button.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(20)
        self.source_button.setFont(font)
        self.source_button.setMouseTracking(False)
        self.source_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.source_button.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(143, 129, 89);\n"
"    border-radius: 15px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(168, 151, 105);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(116, 104, 72);\n"
"}")
        self.source_button.setAutoDefault(False)
        self.source_button.setFlat(False)
        self.source_button.setObjectName("source_button")
        self.gridLayout_3.addWidget(self.source_button, 6, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 5, 0, 1, 1)
        self.sourcedisplay = QtWidgets.QLineEdit(self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourcedisplay.sizePolicy().hasHeightForWidth())
        self.sourcedisplay.setSizePolicy(sizePolicy)
        self.sourcedisplay.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sourcedisplay.setFont(font)
        self.sourcedisplay.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sourcedisplay.setStyleSheet("color: rgb(198, 208, 221);\n"
"background-color: rgb(61, 63, 72);\n"
"border-radius: 10px;\n"
"padding-right: 10px;")
        self.sourcedisplay.setInputMask("")
        self.sourcedisplay.setText("")
        self.sourcedisplay.setMaxLength(32767)
        self.sourcedisplay.setCursorPosition(0)
        self.sourcedisplay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sourcedisplay.setReadOnly(True)
        self.sourcedisplay.setObjectName("sourcedisplay")
        self.gridLayout_3.addWidget(self.sourcedisplay, 12, 1, 1, 2)
        self.gridLayout_2.addWidget(self.background, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.replace_button, self.metadata_button)
        MainWindow.setTabOrder(self.metadata_button, self.destination_button)
        MainWindow.setTabOrder(self.destination_button, self.run_button)
        MainWindow.setTabOrder(self.run_button, self.console)
        MainWindow.setTabOrder(self.console, self.scrollArea)


    def source_button_click(self):
        sourcedir = QFileDialog.getExistingDirectory()
        srcdirs.append(sourcedir)
        srcdirsstring = ', '.join(srcdirs)
        self.sourcedisplay.setText(srcdirsstring)
    

    def destination_button_click(self):
        self.destdir = QFileDialog.getExistingDirectory()
        self.destinationdisplay.setText(self.destdir)


    def run_button_click(self):
        organization = self.organization_box.currentText()

        if organization == 'One folder organization':
            sortmethod = 1
        elif organization == 'Multi-folder organization':
            sortmethod = 2
        else:
            sortmethod = 0

        replace = self.replace_button.isChecked()
        metadata = self.metadata_button.isChecked()

        if not srcdirs:
            nosourceerror = QMessageBox()
            nosourceerror.setWindowTitle('Error')
            nosourceerror.setText('Source directory field cannot be empty.')
            nosourceerror.setIcon(QMessageBox.Critical)
            nosourceerror.exec_()
        try:
            worker = Worker(metadata, replace, sortmethod, self.destdir)
            worker.signals.result.connect(self.statement_returner)
            self.threadpool.start(worker)
        except AttributeError:
            nodestinationerror = QMessageBox()
            nodestinationerror.setWindowTitle('Error')
            nodestinationerror.setText('Destination directory field cannot be empty.')
            nodestinationerror.setIcon(QMessageBox.Critical)
            nodestinationerror.exec_()
        
    def statement_returner(self, statement):
        self.console.append(statement)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "autosort"))
        self.replace_button.setText(_translate("MainWindow", "Replace duplicate files"))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.destinationdisplay.setPlaceholderText(_translate("MainWindow", "Destination Directory"))
        self.destination_button.setText(_translate("MainWindow", "Destination"))
        self.metadata_button.setText(_translate("MainWindow", "Preserve file metadata"))
        self.organization_box.setItemText(0, _translate("MainWindow", "No organization"))
        self.organization_box.setItemText(1, _translate("MainWindow", "One folder organization"))
        self.organization_box.setItemText(2, _translate("MainWindow", "Multi-folder organization"))
        self.console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI Light\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:131073;\"><br /></p></body></html>"))
        self.source_button.setText(_translate("MainWindow", "Source"))
        self.sourcedisplay.setPlaceholderText(_translate("MainWindow", "Source Directory"))

        self.source_button.clicked.connect(self.source_button_click)
        self.destination_button.clicked.connect(self.destination_button_click)
        self.run_button.clicked.connect(self.run_button_click)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
