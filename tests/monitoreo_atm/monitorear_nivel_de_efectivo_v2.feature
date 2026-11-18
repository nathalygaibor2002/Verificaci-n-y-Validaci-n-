# language: es
Característica:Monitorear el nivel de efectivo y alerta cuando se necesita reabastecimiento.
Escenario: Alertar por capacidad baja
        Dado que tengo la siguiente capacidad de efectivo en el cajero A:
          | denominación | capacidad_minima | capacidad_actual |
          | $10          | 500              | 400              |
          | $20          | 1000             | 800              |
        Cuando el sistema evalúa los niveles de efectivo del cajero A
        Entonces se envía una alerta de reabastecimiento al empleado con los datos del cajero A
        Y el mensaje "Se requiere 100 billetes de $10 y 200 billetes de $20 para reabastecer el cajero A"