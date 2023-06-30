# Manipulación de fechas y horas
# datetime

import datetime

ahora = datetime.datetime.now()
print(ahora)

futuro = ahora + datetime.timedelta(days=10)

print(futuro)
