import datetime
import os
from time import ctime
import ntplib

server= "time-e-g.nist.gov"

t1 = datetime.datetime.now()
print ("\nInicio de la Petición: %s" % t1)

print("\nObteniendo la hora del servidor NTP:")
cl= ntplib.NTPClient()
resp= cl.request(server)
hact= datetime.datetime.strptime(ctime(resp.tx_time), "%a %b %d %H:%M:%S %Y")
print("Respuesta de " + server +  ": " + str(hact))

t2 = datetime.datetime.now()
print ("\nLlegada de la Petición: %s" % t2)

aj= (t2-t1)/2
print("\nAjuste: "+str(aj))

horan= hact+aj
print("Hora: "+str(horan))
print("\nAjustando tiempo:")
cmnd= 'date -u "'+str(horan.strftime("%m%d%H%M%Y.%S"))+'"'
os.system(cmnd)