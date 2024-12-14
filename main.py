from PyQt5.QtWidgets import QApplication

from vista import Vista
from modelo import Modelo
from controlador import Controlador

app = QApplication([])
windows = Vista("Mi calculadora")
modelo = Modelo()
controlador = Controlador(modelo, windows)

windows.show()
app.exec_()