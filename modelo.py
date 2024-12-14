class Modelo:
    __valor_actual: str = ""
    __limpiar_antes: bool = True

    def limpiar_valor_actual(self):
        self.__valor_actual = ""

    def remover_ultimo_caracter(self):
        self.__valor_actual = self.__valor_actual[:-1]

    def presionar_igual(self):
        current_screen_value: str = self.__valor_actual
        if current_screen_value:
            try:
                resultado = eval(current_screen_value)
                self.__valor_actual = str(resultado)
                self.__limpiar_antes = True
            except Exception as error:
                print(error)
                self.__valor_actual = "Error"
                self.__limpiar_antes = True

    def presionar_otro_boton(self, simbolo):
        if self.__limpiar_antes:
            self.limpiar_valor_actual()
            self.__limpiar_antes = False

        if simbolo in "+-*/" and not self.__valor_actual:
            return

        if (
            simbolo in "+-*/"
            and self.__valor_actual
            and self.__valor_actual[-1] in "+-*/"
        ):
            return
        self.__valor_actual += simbolo

    @property
    def valor_actual(self) -> str:
        return self.__valor_actual
