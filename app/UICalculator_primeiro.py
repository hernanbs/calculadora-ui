# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UICalculator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("app\\Calculator\\")
from calculadora import Calculadora

class Ui_Dialog(object):
    numberUsed = ''

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(384, 358)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 361, 321))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 341, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_calc = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.txt_calc.setObjectName("txt_calc")
        self.horizontalLayout.addWidget(self.txt_calc)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txt_result = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.txt_result.setObjectName("txt_result")
        self.horizontalLayout.addWidget(self.txt_result)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(10, 110, 341, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 130, 338, 174))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_sub = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_sub.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_sub.setObjectName("btn_sub")
        self.gridLayout.addWidget(self.btn_sub, 1, 3, 1, 1)
        self.btn_two = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_two.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_two.setObjectName("btn_two")
        self.gridLayout.addWidget(self.btn_two, 0, 1, 1, 1)
        self.btn_six = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_six.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_six.setObjectName("btn_six")
        self.gridLayout.addWidget(self.btn_six, 1, 2, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_mult.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_mult.setObjectName("btn_mult")
        self.gridLayout.addWidget(self.btn_mult, 2, 3, 1, 1)
        self.btn_zero = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_zero.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_zero.setObjectName("btn_zero")
        self.gridLayout.addWidget(self.btn_zero, 3, 1, 1, 1)
        self.btn_equal = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_equal.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_equal.setObjectName("btn_equal")
        self.gridLayout.addWidget(self.btn_equal, 3, 2, 1, 1)
        self.btn_five = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_five.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_five.setObjectName("btn_five")
        self.gridLayout.addWidget(self.btn_five, 1, 1, 1, 1)
        self.btn_one = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_one.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_one.setObjectName("btn_one")
        self.gridLayout.addWidget(self.btn_one, 0, 0, 1, 1)
        self.btn_eight = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_eight.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_eight.setObjectName("btn_eight")
        self.gridLayout.addWidget(self.btn_eight, 2, 1, 1, 1)
        self.btn_sum = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_sum.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_sum.setObjectName("btn_sum")
        self.gridLayout.addWidget(self.btn_sum, 0, 3, 1, 1)
        self.btn_four = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_four.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_four.setObjectName("btn_four")
        self.gridLayout.addWidget(self.btn_four, 1, 0, 1, 1)
        self.btn_divide = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_divide.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_divide.setObjectName("btn_divide")
        self.gridLayout.addWidget(self.btn_divide, 3, 3, 1, 1)
        self.btn_three = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_three.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_three.setObjectName("btn_three")
        self.gridLayout.addWidget(self.btn_three, 0, 2, 1, 1)
        self.btn_nine = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_nine.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_nine.setObjectName("btn_nine")
        self.gridLayout.addWidget(self.btn_nine, 2, 2, 1, 1)
        self.btn_seven = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_seven.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_seven.setObjectName("btn_seven")
        self.gridLayout.addWidget(self.btn_seven, 2, 0, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_clear.setMinimumSize(QtCore.QSize(71, 31))
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Calculadora"))
        self.txt_calc.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1+1</p></body></html>"))
        self.label.setText(_translate("Dialog", ">>>>"))
        self.btn_sub.setText(_translate("Dialog", "-"))
        self.btn_two.setText(_translate("Dialog", "2"))
        self.btn_six.setText(_translate("Dialog", "6"))
        self.btn_mult.setText(_translate("Dialog", "*"))
        self.btn_zero.setText(_translate("Dialog", "0"))
        self.btn_equal.setText(_translate("Dialog", "="))
        self.btn_five.setText(_translate("Dialog", "5"))
        self.btn_one.setText(_translate("Dialog", "1"))
        self.btn_eight.setText(_translate("Dialog", "8"))
        self.btn_sum.setText(_translate("Dialog", "+"))
        self.btn_four.setText(_translate("Dialog", "4"))
        self.btn_divide.setText(_translate("Dialog", "/"))
        self.btn_three.setText(_translate("Dialog", "3"))
        self.btn_nine.setText(_translate("Dialog", "9"))
        self.btn_seven.setText(_translate("Dialog", "7"))
        self.btn_clear.setText(_translate("Dialog", "C"))

    def setOperator(self, op):
        self.operator = op

    def getOperator(self):
        return self.operator

    def getNumberUsed(self):
        return int(self.numberUsed)
    
    def setNumberUsed(self, txt_number):
        self.numberUsed += txt_number

    def clearNumberUsed(self):
        self.numberUsed = ''

    def getCalculator(self):
        return self.objCalc

    def One(self):
        self.setNumberUsed('1')

    def Two(self):
        self.setNumberUsed('2')

    def Three(self):
        self.setNumberUsed('3')

    def Four(self):
        self.setNumberUsed('4')

    def Five(self):
        self.setNumberUsed('5')

    def Six(self):
        self.setNumberUsed('6') 

    def Seven(self):
        self.setNumberUsed('7')

    def Eight(self):
        self.setNumberUsed('8')

    def Nine(self):
        self.setNumberUsed('9')

    def Zero(self):
        self.setNumberUsed('0')

    def Clear(self):
        print('clear')
        self.arrayNum.append('c')
        print(self.arrayNum.pop()) 
        # self.arrayNum.pop()

    def Sum(self):
        print('sum')
        self.arrayNum.append(self.getNumberUsed())
        self.clearNumberUsed()
        self.arrayOperator.append('+')
        print("Numeros: " + str(self.arrayNum))
        print("Operação: " + str(self.arrayOperator))

    def Sub(self):
        print('subtraction')
        self.arrayNum.append(self.getNumberUsed())
        self.clearNumberUsed()
        self.arrayOperator.append('-')
        print("Numeros: " + str(self.arrayNum))
        print("Operação: " + str(self.arrayOperator))

    def Mult(self):
        print('multiplication')
        self.arrayNum.append(self.getNumberUsed())
        self.clearNumberUsed()
        self.arrayOperator.append('*')
        print("Numeros: " + str(self.arrayNum))
        print("Operação: " + str(self.arrayOperator))

    def Divide(self):
        print('divide')
        self.arrayNum.append(self.getNumberUsed())
        self.clearNumberUsed()
        self.arrayOperator.append('/')
        print("Numeros: " + str(self.arrayNum))
        print("Operação: " + str(self.arrayOperator)) 

    def Equal(self):
        print('equal')
        self.arrayNum.append(self.getNumberUsed())
        self.clearNumberUsed()
        # self.arrayOperator.append('=')
        print(self.arrayNum)
        print(self.arrayOperator)    
        self.executeCalc()
        self.txt_calc = ''
        # variavel = " ".join(str(i) for i in self.arrayNum) // colocar resultado em txt_calc widget

    def executeCalc(self):
        resultado = self.calculateTwoItens(self.arrayNum[0], self.arrayNum[1], self.arrayOperator[0])
        self.arrayNum.pop(0)
        self.arrayNum.pop(0)
        self.arrayOperator.pop(0)
        print("resultado :: ")
        print(resultado)
        self.arrayNum.insert(0,resultado)
            

    def calculateTwoItens(self, itemA, itemB, operator):
        self.getCalculator().setNum1(itemA)
        self.getCalculator().setNum2(itemB)
        return self.selectOperator(operator)


    def selectOperator(self, operator):
        return {
            '+': self.getCalculator().sumOp(),
            '-': self.getCalculator().subtract(),
            '/': self.getCalculator().divide(),
            '*': self.getCalculator().multiple()
        }[operator]

    def initBtn(self):
        self.objCalc = Calculadora()
        self.arrayNum = []
        self.arrayOperator = []
        print('testando init')
        self.btn_one.clicked.connect(self.One)
        self.btn_two.clicked.connect(self.Two)
        self.btn_three.clicked.connect(self.Three)
        self.btn_four.clicked.connect(self.Four)
        self.btn_five.clicked.connect(self.Five)
        self.btn_six.clicked.connect(self.Six)
        self.btn_seven.clicked.connect(self.Seven)
        self.btn_eight.clicked.connect(self.Eight)
        self.btn_nine.clicked.connect(self.Nine)
        self.btn_zero.clicked.connect(self.Zero)

        self.btn_clear.clicked.connect(self.Clear)
        self.btn_divide.clicked.connect(self.Divide)
        self.btn_equal.clicked.connect(self.Equal)
        self.btn_mult.clicked.connect(self.Mult)
        self.btn_sub.clicked.connect(self.Sub)
        self.btn_sum.clicked.connect(self.Sum)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    obj_calc = Calculadora()
    ui.setOperator('')
    ui.initBtn()
    sys.exit(app.exec_())

