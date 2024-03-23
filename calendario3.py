"""
En este calendario al usuario se le solicitara un año y un mes especifico

"""

import calendar
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

year = int(input("Ingrese un año: "))
month = int(input("Ingrese un mes (en número): "))

x = calendar.month(year, month)
print(x)
