from .cajero import Cajero
from .empleado import Empleado


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
                "mensaje": mensaje,
            }
            empleado.recibir_alerta(alerta)
            return True
        return False

