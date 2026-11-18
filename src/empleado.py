class Empleado:
    def __init__(self, nombre: str, id_empleado: str):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.alertas_recibidas = []

    def recibir_alerta(self, alerta: dict) -> None:
        self.alertas_recibidas.append(alerta)

