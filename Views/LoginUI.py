from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from functools import partial
from Window import Routing
from Window import Transfer
from Lib.Messages import Messages


# #////////////////////////////EVENTS///////////////////////////
from Controllers.AuthenticationController import Auth


def login(window, ui : "Ui_MainWindow"):

    data = {
        "email" : getEmail(ui),
        "password" : getPassword(ui),
    }

    result = Auth.Login(data)

    if not result:
        Routing.Refresh(window)
    else:
        Messages.push(Messages.Type.SUCCESS, "You logged in successfully")
        if Auth.CheckAdminCredentials():
            Routing.Redirect(window, "adminHome")
        else:
            Routing.Redirect(window, "userHome")




#get inputs

def getEmail(ui : "Ui_MainWindow") -> str:
    return ui.lineEditEmail.text().strip()


def getPassword(ui : "Ui_MainWindow") -> str:
    return ui.lineEditPassword.text().strip()





#//////////////////////////////UI//////////////////////////////



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 328)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 521, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.mainGLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.mainGLayout.setContentsMargins(5, 0, 5, 5)
        self.mainGLayout.setSpacing(20)
        self.mainGLayout.setObjectName("mainGLayout")
        self.btnHLayout = QtWidgets.QHBoxLayout()
        self.btnHLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.btnHLayout.setContentsMargins(-1, 0, -1, -1)
        self.btnHLayout.setSpacing(20)
        self.btnHLayout.setObjectName("btnHLayout")

        self.btnForgetPassword = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.btnForgetPassword.setFont(font)
        self.btnForgetPassword.setObjectName("btnForgetPassword")
        self.btnHLayout.addWidget(self.btnForgetPassword)





        self.btnLogin = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")

        self.btnLogin.clicked.connect( partial(login, MainWindow, self  ) )



        self.btnHLayout.addWidget(self.btnLogin)
        self.mainGLayout.addLayout(self.btnHLayout, 4, 0, 1, 3)
        self.lblPassword = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPassword.sizePolicy().hasHeightForWidth())
        self.lblPassword.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblPassword.setFont(font)
        self.lblPassword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblPassword.setObjectName("lblPassword")
        self.mainGLayout.addWidget(self.lblPassword, 2, 0, 1, 1)
        self.lblAdminEmail = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAdminEmail.sizePolicy().hasHeightForWidth())
        self.lblAdminEmail.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblAdminEmail.setFont(font)
        self.lblAdminEmail.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblAdminEmail.setObjectName("lblAdminEmail")
        self.mainGLayout.addWidget(self.lblAdminEmail, 1, 0, 1, 1)



        self.lineEditPassword = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditPassword.sizePolicy().hasHeightForWidth())
        self.lineEditPassword.setSizePolicy(sizePolicy)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setClearButtonEnabled(True)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.mainGLayout.addWidget(self.lineEditPassword, 2, 1, 1, 2)



        self.lineEditEmail = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditEmail.sizePolicy().hasHeightForWidth())
        self.lineEditEmail.setSizePolicy(sizePolicy)
        self.lineEditEmail.setInputMask("")
        self.lineEditEmail.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditEmail.setClearButtonEnabled(True)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.mainGLayout.addWidget(self.lineEditEmail, 1, 1, 1, 2)



        self.lblTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle.sizePolicy().hasHeightForWidth())
        self.lblTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.mainGLayout.addWidget(self.lblTitle, 0, 0, 1, 3)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnForgetPassword.setText(_translate("MainWindow", "Forget Password"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.lblPassword.setText(_translate("MainWindow", "Password: "))
        self.lblAdminEmail.setText(_translate("MainWindow", "Email: "))
        self.lineEditPassword.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.lineEditEmail.setPlaceholderText(_translate("MainWindow", "Enter your email address"))
        self.lblTitle.setText(_translate("MainWindow", "Login Page"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()



    sys.exit(app.exec_())
