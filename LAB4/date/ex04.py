#екі күннің айырмасын секунд түрінде есептеу
import datetime
d1 = datetime.datetime.now()
print(d1)
d2 = datetime.datetime(2024, 2, 12)
print(d2)
dif = d1-d2
print(dif.total_seconds()) #секундқа айналдырадыa