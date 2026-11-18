class Casete:
    def __init__(self, denominacion: int, capacidad_minima: int, capacidad_actual: int):
        self.denominacion = denominacion
        self.capacidad_minima = capacidad_minima
        self.capacidad_actual = capacidad_actual

    def calcular_faltante(self) -> int:
        if self.capacidad_actual < self.capacidad_minima:
            return self.capacidad_minima - self.capacidad_actual
        return 0

