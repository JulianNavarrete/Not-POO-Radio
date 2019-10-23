# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login_designer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 440)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 430, 420))
        self.groupBox.setObjectName("groupBox")
        self.userLabel = QtWidgets.QLabel(self.groupBox)
        self.userLabel.setGeometry(QtCore.QRect(32, 30, 70, 32))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(14)
        self.userLabel.setFont(font)
        self.userLabel.setObjectName("userLabel")
        self.passLabel = QtWidgets.QLabel(self.groupBox)
        self.passLabel.setGeometry(QtCore.QRect(20, 70, 100, 32))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(14)
        self.passLabel.setFont(font)
        self.passLabel.setObjectName("passLabel")
        self.lineEditUser = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditUser.setGeometry(QtCore.QRect(140, 30, 260, 32))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditUser.setFont(font)
        self.lineEditUser.setObjectName("lineEditUser")
        self.lineEditPass = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditPass.setGeometry(QtCore.QRect(140, 70, 260, 32))
        self.lineEditPass.setObjectName("lineEditPass")
        self.keepLogged = QtWidgets.QCheckBox(self.groupBox)
        self.keepLogged.setGeometry(QtCore.QRect(150, 120, 230, 32))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(14)
        self.keepLogged.setFont(font)
        self.keepLogged.setObjectName("keepLogged")
        self.loginInvitedButton = QtWidgets.QPushButton(self.groupBox)
        self.loginInvitedButton.setGeometry(QtCore.QRect(85, 230, 260, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(14)
        self.loginInvitedButton.setFont(font)
        self.loginInvitedButton.setObjectName("loginInvitedButton")
        self.noteInvited = QtWidgets.QLabel(self.groupBox)
        self.noteInvited.setGeometry(QtCore.QRect(30, 280, 360, 62))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(14)
        self.noteInvited.setFont(font)
        self.noteInvited.setObjectName("noteInvited")
        self.loginButton = QtWidgets.QPushButton(self.groupBox)
        self.loginButton.setGeometry(QtCore.QRect(260, 170, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(14)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.forgetPassButton = QtWidgets.QPushButton(self.groupBox)
        self.forgetPassButton.setGeometry(QtCore.QRect(30, 170, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(14)
        self.forgetPassButton.setFont(font)
        self.forgetPassButton.setObjectName("forgetPassButton")
        self.createAccountButton = QtWidgets.QPushButton(self.groupBox)
        self.createAccountButton.setGeometry(QtCore.QRect(220, 360, 170, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(14)
        self.createAccountButton.setFont(font)
        self.createAccountButton.setObjectName("createAccountButton")
        self.dontHaveAcc = QtWidgets.QLabel(self.groupBox)
        self.dontHaveAcc.setGeometry(QtCore.QRect(30, 350, 170, 62))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(14)
        self.dontHaveAcc.setFont(font)
        self.dontHaveAcc.setObjectName("dontHaveAcc")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Inicio de sesión"))
        self.groupBox.setTitle(_translate("Dialog", "Ingresa con tu cuenta"))
        self.userLabel.setText(_translate("Dialog", "Usuario:"))
        self.passLabel.setText(_translate("Dialog", "Contraseña:"))
        self.keepLogged.setText(_translate("Dialog", "Mantener sesión iniciada"))
        self.loginInvitedButton.setText(_translate("Dialog", "Iniciar como Invitado"))
        self.noteInvited.setText(_translate("Dialog", "Nota: al iniciar como invitado no estatá \n"
"disponible el guardado en la nube"))
        self.loginButton.setText(_translate("Dialog", "Iniciar sesión"))
        self.forgetPassButton.setText(_translate("Dialog", "Olvidé mi contraseña"))
        self.createAccountButton.setText(_translate("Dialog", "Crear una cuenta"))
        self.dontHaveAcc.setText(_translate("Dialog", "¿No tienes cuenta?"))

# Función main
if __name__ == "__main__":

    # Importamos librería sys
    import sys

    # Crea el objeto de la Aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Crea el diálogo
    Dialog = QtWidgets.QDialog()

    # Crea un objeto de la clase Definida
    ui = Ui_Dialog()

    # LLama al objeto pasando como parámetro el Diálogo
    ui.setupUi(Dialog)

    # Muestra el Diálogo
    Dialog.show()

    # Ejecuta la aplicación y su valor de finalización lo usa para salir
    sys.exit(app.exec_())
