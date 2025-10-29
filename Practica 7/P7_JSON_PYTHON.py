import cv2
import matplotlib.pyplot as plt
import numpy as np
import serial
import json

lista = []
puerto = serial.Serial("COM7", 115200)

plt.ion()

while True:
    try:
        linea = puerto.readline().decode().strip()
        if not linea:
            continue
        objeto =json.loads(linea)
        print(objeto)
        
    #LISTAAAAAA
        valor = objeto["values"]
        lista.append(valor)
        if len(lista) > 100:
            lista.pop(0)      
        fig, ax = plt.subplots()
        
        ax.set_xlabel('Sensor')
        ax.set_ylabel('Valores')
        ax.set_title('Grafico de barras con OpenCv')

        fig.canvas.draw()
        img = np.array(fig.canvas.buffer_rgba())
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imshow('Grafico con OpenCv', img)
        cv2.waitKey(1)
        plt.close(fig)
            
        if cv2.waitKey(25) & 0xFF == ord('q'): #cerrar el puerto para que ya no se envien datos
            puerto.close()
            break
                    
    except json.JSONDecodeError:
         print('Error de Json')
    except Exception as e:
        print('Error', e)
        break
    
puerto.close()
cv2.destroyWindow()