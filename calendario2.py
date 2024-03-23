"""
Esta es otra forma de crear un calendario atravez de un bucle for y en idioma español

"""

import calendar
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

year = int(input("Ingrese un año: "))

for month in range(1, 13):
    x = calendar.month(year, month)
    print(x)