from os.path import expanduser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QGraphicsDropShadowEffect

from application.controller import PageWindow

from application.input_parser import parse
from application.output_printer import write
from application.arithmetic_tree import evaluate


class MainPage(PageWindow):

    def __init__(self):
        super().__init__()
        self.expression = ''
        self.ok = 1
        self.setupUi()
        self.is_from_file = False

    def setupUi(self):
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.toolButton = QtWidgets.QToolButton(self)
        self.toolButton.setGeometry(QtCore.QRect(950, 380, 40, 20))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.clicked.connect(self.browse_file_event)

        self.computeButton = QtWidgets.QPushButton(self)
        self.computeButton.setGeometry(QtCore.QRect(1020, 370, 100, 40))
        self.computeButton.setObjectName("computeButton")
        self.computeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.computeButton.clicked.connect(self.compute_event)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(130, 370, 250, 40))
        self.label.setObjectName("label")

        self.path = QtWidgets.QLineEdit(self)
        self.path.setGeometry(QtCore.QRect(370, 370, 560, 40))
        self.path.setObjectName("path")
        self.path.setDisabled(True)
        self.path.setPlaceholderText("Path to the XML file...")

        self.plusButton = QtWidgets.QPushButton(self)
        self.plusButton.setGeometry(QtCore.QRect(470, 270, 50, 50))
        self.plusButton.setObjectName("plusButton")
        self.plusButton.clicked.connect(self.add_plus_symbol_event)

        self.minusButton = QtWidgets.QPushButton(self)
        self.minusButton.setGeometry(QtCore.QRect(570, 270, 50, 50))
        self.minusButton.setObjectName("minusButton")
        self.minusButton.clicked.connect(self.add_minus_symbol_event)

        self.timesButton = QtWidgets.QPushButton(self)
        self.timesButton.setGeometry(QtCore.QRect(670, 270, 50, 50))
        self.timesButton.setObjectName("timesButton")
        self.timesButton.clicked.connect(self.add_times_symbol_event)

        self.sqrtButton = QtWidgets.QPushButton(self)
        self.sqrtButton.setGeometry(QtCore.QRect(770, 270, 50, 50))
        self.sqrtButton.setObjectName("sqrtButton")
        self.sqrtButton.clicked.connect(self.add_sqrt_symbol_event)

        self.writeEquation = QtWidgets.QTextEdit(self)
        self.writeEquation.setObjectName("writeEquation")
        self.writeEquation.setEnabled(True)
        self.writeEquation.setGeometry(QtCore.QRect(100, 40, 1100, 200))

        self.readEquation = QtWidgets.QTextEdit(self)
        self.readEquation.setObjectName("readEquation")
        self.readEquation.setEnabled(False)
        self.readEquation.setGeometry(QtCore.QRect(100, 500, 1100, 200))

        self.result_label = QtWidgets.QLabel(self)
        self.result_label.setGeometry(QtCore.QRect(130, 670, 250, 40))
        self.result_label.setObjectName("result_label")

        self.retranslate_ui(self)

    # setupUi

    def browse_file_event(self):
        """
        opens browser to choose path to image file
        """
        self.path.setText("")
        # opens a file dialog for the format
        file_path = QFileDialog.getOpenFileName(None, 'Select a file:', expanduser("~"),
                                                filter="All files (*.*);;XML (*.xml)")
        self.path.setText(file_path[0])
        self.show_equation(file_path[0])

    def add_plus_symbol_event(self):
        self.add_symbol("+")

    def add_minus_symbol_event(self):
        self.add_symbol("-")

    def add_sqrt_symbol_event(self):
        self.add_symbol("√")

    def add_times_symbol_event(self):
        self.add_symbol("*")

    def add_symbol(self, symbol):
        self.writeEquation.setText(self.writeEquation.toPlainText() + f"{symbol}")

    def show_equation(self, file_path):
        if len(file_path) > 0:
            self.is_from_file = True
            self.expression = parse(file_path)
            self.writeEquation.setText(self.expression)
            self.compute_event()

    def compute_event(self):
        if self.is_from_file:
            self.is_from_file = False
        else:
            self.path.setText("")
        result = evaluate(self.writeEquation.toPlainText())
        self.result_label.setText(f"Result: {result}")
        write(result)

    def retranslate_ui(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.computeButton.setText(_translate("Dialog", "Compute"))
        self.plusButton.setText(_translate("MainWindow", "+", None))
        self.minusButton.setText(_translate("MainWindow", "-", None))
        self.timesButton.setText(_translate("MainWindow", "*", None))
        self.sqrtButton.setText(_translate("MainWindow", "\u221a", None))
        self.label.setText(_translate("MainWindow", "Import Equations XML File", None))
