import datetime
import time
import os

while(True):
    os.system('clear') # Se limpia la pantalla
    dt = datetime.datetime.now()
    print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
    time.sleep(1) # Esperar un 1 segundo