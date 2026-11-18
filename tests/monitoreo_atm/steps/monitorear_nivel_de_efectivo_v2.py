import behave.runner
from behave import *
from behave.api.step_matchers import use_step_matcher
from src.cajero import Cajero
from src.casete import Casete
from src.empleado import Empleado
from src.sistema_monitoreo import SistemaMonitoreo

use_step_matcher("parse")


@step("que tengo la siguiente capacidad de efectivo en el cajero A:")
def step_impl(context: behave.runner.Context):
    context.casetes = {}
    for row in context.table:
        denominacion = int(row["denominación"].replace("$", ""))
        capacidad_minima = int(row["capacidad_minima"])
        capacidad_actual = int(row["capacidad_actual"])
        context.casetes[denominacion] = {
            "capacidad_minima": capacidad_minima,
            "capacidad_actual": capacidad_actual
        }


@step("el sistema evalúa los niveles de efectivo del cajero A")
def step_impl(context: behave.runner.Context):
    cajero = Cajero("A")
    for denom, datos in context.casetes.items():
        cajero.agregar_casete(Casete(
            denominacion=denom,
            capacidad_minima=datos["capacidad_minima"],
            capacidad_actual=datos["capacidad_actual"],
        ))

    empleado = Empleado("Empleado ATM", "EMP-001")
    sistema = SistemaMonitoreo()
    context.alerta_enviada = sistema.evaluar_niveles(cajero, empleado)
    if context.alerta_enviada:
        context.mensaje_alerta = empleado.alertas_recibidas[0]["mensaje"]


@step("se envía una alerta de reabastecimiento al empleado con los datos del cajero A")
def step_impl(context: behave.runner.Context):
    assert context.alerta_enviada is True, "No se envió la alerta de reabastecimiento"


@step('el mensaje "{mensaje_esperado}"')
def step_impl(context: behave.runner.Context, mensaje_esperado: str):
    assert context.mensaje_alerta == mensaje_esperado, (
        f"Mensaje esperado: '{mensaje_esperado}', pero se obtuvo: '{context.mensaje_alerta}'"
    )