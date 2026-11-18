class Empleado:
    def __init__(self, nombre: str, id_empleado: str):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.alertas_recibidas = []

    def recibir_alerta(self, alerta: dict):
        self.alertas_recibidas.append(alerta)


class Casete:
    def __init__(self, denominacion: int, capacidad_minima: int, capacidad_actual: int):
        self.denominacion = denominacion
        self.capacidad_minima = capacidad_minima
        self.capacidad_actual = capacidad_actual

    def calcular_faltante(self) -> int:
        if self.capacidad_actual < self.capacidad_minima:
            return self.capacidad_minima - self.capacidad_actual
        return 0


class Cajero:
    def __init__(self, identificador: str):
        self.identificador = identificador
        self.casetes: dict[int, Casete] = {}

    def agregar_casete(self, casete: Casete):
        self.casetes[casete.denominacion] = casete


class SistemaMonitoreo:
    def evaluar_niveles(self, cajero: Cajero, empleado: Empleado) -> bool:
        faltante_10 = cajero.casetes[10].calcular_faltante() if 10 in cajero.casetes else 0
        faltante_20 = cajero.casetes[20].calcular_faltante() if 20 in cajero.casetes else 0

        if faltante_10 > 0 or faltante_20 > 0:
            mensaje = (
                f"Se requiere {faltante_10} billetes de $10 y "
                f"{faltante_20} billetes de $20 para reabastecer el cajero {cajero.identificador}"
            )
            alerta = {
                "cajero": cajero.identificador,
                "mensaje": mensaje
            }
            empleado.recibir_alerta(alerta)
            return True
        return False
"""Compatibilidad con importaciones existentes.

Las clases viven ahora en módulos independientes dentro de ``src``.
"""

from .cajero import Cajero
from .casete import Casete
from .empleado import Empleado
from .sistema_monitoreo import SistemaMonitoreo

__all__ = ["Cajero", "Casete", "Empleado", "SistemaMonitoreo"]