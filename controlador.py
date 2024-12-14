from modelo import Modelo
from vista import Vista


class Controlador:
    def __init__(self, modelo: Modelo, vista: Vista):
        self.__modelo = modelo
        self.__vista = vista
        self.__enlazar_con_vista()

    def __enlazar_con_vista(self):
        for simbolo, boton in self.__vista.mapa_botones.items():
            boton.clicked.connect(
                lambda _, simbolo=simbolo: self.manejador_click(simbolo)
            )

    def manejador_click(self, simbolo):
        if simbolo == "CLEAR":
            self.__modelo.limpiar_valor_actual()
        elif simbolo == "DEL":
            self.__modelo.remover_ultimo_caracter()
        elif simbolo == "=":
            self.__modelo.presionar_igual()
        else:
            self.__modelo.presionar_otro_boton(simbolo)

        self.__actualizar_display()

    def __actualizar_display(self):
        self.__vista.display.setText(self.__modelo.valor_actual)
