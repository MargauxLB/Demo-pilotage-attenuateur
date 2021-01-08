from PyQt5.QtWidgets import QDialog, QApplication,QMainWindow
from essai import Ui_Dialog
import sys
import Attenuateur


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.SendButton_click)
        self.show()
    def SendButton_click(self):
        att = Attenuateur.Attenuateur()
        if len(self.ui.entryvalue.text()) == 0:
            return

        port = self.ui.entryportcom.text()
        ip = self.ui.entryip.text()

        try:
            value = float(self.ui.entryvalue.text())
            if len(port) != 0:
                att.connexion_serial(port)

            if len(ip) != 0:
                att.connexion_network(ip)
            print(value)

            att.set_value(value)
        except Attenuateur.AttenuateurSerialException:
            self.ui.Error.setText('Serial port error')
        except Attenuateur.AttenuateurNetworkException:
            self.ui.Error.setText('Network error')
        except ValueError:
            self.ui.Error.setText('Value error')
        except:
            self.ui.Error.setText('Unknown error')
        else:
            self.ui.Error.setText('Ok')

        att.close()



app=QApplication(sys.argv)
w=AppWindow()
w.show()
sys.exit(app.exec_())