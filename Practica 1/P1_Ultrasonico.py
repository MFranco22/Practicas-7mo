
import serial
import time

def leer():
    n = 0
    while(True):
        datos = conexion.readline().strip()
        if datos != "":
            lista.append(datos)
            print(lista)
           # print(datos[1:])        
        n += 1
        if n >50:
            break
        time.sleep(0.1) #para no sobrecargar el Buffer
        
    lista =[]     

    conexion = serial.Serial('COM7', 115200, timeout = 1)

    if __name__=='_main_':
        leer()
        conexion.close()