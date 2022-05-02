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
        self.toolButton.setGeometry(QtCore.QRect(780, 480, 40, 20))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.clicked.connect(self.browse_file_event)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 470, 250, 40))
        self.label.setObjectName("label")

        self.path = QtWidgets.QLineEdit(self)
        self.path.setGeometry(QtCore.QRect(270, 470, 500, 40))
        self.path.setObjectName("path")
        self.path.setDisabled(True)
        self.path.setPlaceholderText("Path to the XML file...")

        self.error_label = QtWidgets.QLabel(self)
        self.error_label.setGeometry(QtCore.QRect(20, 500, 990, 40))
        self.error_label.setStyleSheet("color: red")
        self.error_label.setObjectName("error_label")

        self.clearButton = QtWidgets.QPushButton(self)
        self.clearButton.setGeometry(QtCore.QRect(60, 270, 100, 50))
        self.clearButton.setObjectName("clearButton")
        self.clearButton.clicked.connect(self.clear_expression)

        self.plusButton = QtWidgets.QPushButton(self)
        self.plusButton.setGeometry(QtCore.QRect(220, 270, 50, 50))
        self.plusButton.setObjectName("plusButton")
        self.plusButton.clicked.connect(self.add_plus_symbol_event)

        self.minusButton = QtWidgets.QPushButton(self)
        self.minusButton.setGeometry(QtCore.QRect(320, 270, 50, 50))
        self.minusButton.setObjectName("minusButton")
        self.minusButton.clicked.connect(self.add_minus_symbol_event)

        self.timesButton = QtWidgets.QPushButton(self)
        self.timesButton.setGeometry(QtCore.QRect(420, 270, 50, 50))
        self.timesButton.setObjectName("timesButton")
        self.timesButton.clicked.connect(self.add_times_symbol_event)

        self.divButton = QtWidgets.QPushButton(self)
        self.divButton.setGeometry(QtCore.QRect(520, 270, 50, 50))
        self.divButton.setObjectName("divButton")
        self.divButton.clicked.connect(self.add_div_symbol_event)

        self.pwrButton = QtWidgets.QPushButton(self)
        self.pwrButton.setGeometry(QtCore.QRect(620, 270, 50, 50))
        self.pwrButton.setObjectName("pwrButton")
        self.pwrButton.clicked.connect(self.add_pwr_symbol_event)

        self.sqrtButton = QtWidgets.QPushButton(self)
        self.sqrtButton.setGeometry(QtCore.QRect(720, 270, 50, 50))
        self.sqrtButton.setObjectName("sqrtButton")
        self.sqrtButton.clicked.connect(self.add_sqrt_symbol_event)

        self.computeButton = QtWidgets.QPushButton(self)
        self.computeButton.setGeometry(QtCore.QRect(820, 270, 100, 50))
        self.computeButton.setObjectName("computeButton")
        self.computeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.computeButton.clicked.connect(self.compute_event)

        self.writeEquation = QtWidgets.QTextEdit(self)
        self.writeEquation.setObjectName("writeEquation")
        self.writeEquation.setEnabled(True)
        self.writeEquation.setGeometry(QtCore.QRect(130, 40, 830, 200))

        self.equation_label = QtWidgets.QLabel(self)
        self.equation_label.setGeometry(QtCore.QRect(30, 40, 250, 40))
        self.equation_label.setObjectName("equation_label")

        self.result_label = QtWidgets.QTextEdit(self)
        self.result_label.setEnabled(False)
        self.result_label.setGeometry(QtCore.QRect(130, 370, 250, 40))
        self.result_label.setObjectName("result_label")

        self.computed_result_label = QtWidgets.QLabel(self)
        self.computed_result_label.setGeometry(QtCore.QRect(30, 370, 250, 40))
        self.computed_result_label.setObjectName("computed_result_label")

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

    def add_pwr_symbol_event(self):
        self.add_symbol("^")

    def add_div_symbol_event(self):
        self.add_symbol("/")

    def add_symbol(self, symbol):
        self.writeEquation.setText(self.writeEquation.toPlainText() + f"{symbol}")

    def clear_expression(self):
        self.path.setText("")
        self.writeEquation.setText("")
        self.result_label.setText("")

    def show_equation(self, file_path):
        try:
            if len(file_path) > 0:
                self.is_from_file = True
                self.expression = parse(file_path)
                self.writeEquation.setText(self.expression)
                self.compute_event()
        except Exception as e:
            self.error_label.setText(str(e))

    def compute_event(self):
        try:
            if len(self.writeEquation.toPlainText()) == 0:
                return
            if self.is_from_file:
                self.is_from_file = False
            else:
                self.path.setText("")
            result = evaluate(self.writeEquation.toPlainText())
            self.result_label.setText(f"{result}")
            write(result)
            self.error_label.setText("")
        except Exception as e:
            self.error_label.setText(str(e))

    def retranslate_ui(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.computeButton.setText(_translate("Dialog", "Compute"))
        self.clearButton.setText(_translate("MainWindow", "Clear", None))
        self.plusButton.setText(_translate("MainWindow", "+", None))
        self.minusButton.setText(_translate("MainWindow", "-", None))
        self.timesButton.setText(_translate("MainWindow", "*", None))
        self.pwrButton.setText(_translate("MainWindow", "^", None))
        self.divButton.setText(_translate("MainWindow", "/", None))
        self.sqrtButton.setText(_translate("MainWindow", "\u221a", None))
        self.label.setText(_translate("MainWindow", "Import Equations XML", None))
        self.equation_label.setText(_translate("MainWindow", "Equation", None))
        self.computed_result_label.setText(_translate("MainWindow", "Result", None))
        self.error_label.setText(_translate("MainWindow", "", None))
