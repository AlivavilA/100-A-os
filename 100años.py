# Programa que te avisa en que año cumpliras los 100 años
import datetime

nombre = input('¿Como te llamas?: ')
años = input('¿Cuantos años tienes?: ')
veces = input('¿Cual es tu numero favorito?: ')
veces = int(veces)

años =int(años)

year=int(datetime.date.today().year)

año = year - años


cien = año + 100
years = cien - year
cien = str(cien)
years=str(years)

resumen = nombre + " en " + years + " años cumpliras los 100 años, este año sera el " + cien + ".\n"
repetir = resumen * veces

print(repetir)
