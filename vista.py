from PyQt5.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
)
from PyQt5.QtGui import QFont

CALC_KEYBOARD = [
    ["(", ")", "CLEAR", "DEL"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "+"],
    [".", "0", "=", "-"],
]

DISPLAY_FONT = QFont("Arial", 22)
KEYBOARD_FONT = QFont("Arial", 16)


class Vista(QWidget):
    __display: QLineEdit
    __mapa_botones: dict[str, QPushButton] = {}

    def __init__(self, titulo, parent=None):
        QWidget.__init__(self, parent)
        QWidget.setWindowTitle(self, titulo)
        self.__crear_vista()

    def __crear_vista(self):
        # Crear el display con fuente grande
        self.__display = QLineEdit()
        self.__display.setReadOnly(True)
        self.__display.setFont(DISPLAY_FONT)  # Fuente grande para el display
        self.__display.setMinimumHeight(50)  # Altura mínima del display

        contenedor_principal = QVBoxLayout()
        contanedor_teclado = QGridLayout()

        # Crear botones con fuente grande y ajuste de tamaño
        for i, row in enumerate(CALC_KEYBOARD):
            for j, key_data in enumerate(row):
                # Inicializar valores predeterminados
                x, y, col_span, row_span, simbolo = i, j, 1, 1, key_data

                # Crear el botón  C#
                boton = QPushButton(simbolo)
                boton.setFont(KEYBOARD_FONT)  # Fuente grande para los botones
                boton.setMinimumSize(70, 70)  # Tamaño más grande para los botones

                # Mapear el botón con su símbolo
                self.__mapa_botones[simbolo] = boton

                # Agregar el botón al contenedor del teclado
                contanedor_teclado.addWidget(boton, x, y, col_span, row_span)

        # Agregar el display y el teclado al layout principal
        contenedor_principal.addWidget(self.__display)
        contenedor_principal.addLayout(contanedor_teclado)
        self.setLayout(contenedor_principal)

    @property
    def display(self) -> QLineEdit:
        return self.__display

    @property
    def mapa_botones(self) -> dict[str, QPushButton]:
        return self.__mapa_botones
