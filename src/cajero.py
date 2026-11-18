from .casete import Casete


class Cajero:
    def __init__(self, identificador: str):
        self.identificador = identificador
        self.casetes: dict[int, Casete] = {}

    def agregar_casete(self, casete: Casete) -> None:
        self.casetes[casete.denominacion] = casete

