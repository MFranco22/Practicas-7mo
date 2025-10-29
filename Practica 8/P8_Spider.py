import cv2
import matplotlib.pyplot as plt
import numpy as np
import serial
import json
aux = 0
lista = []
puerto = serial.Serial("COM7", 115200)

plt.ion()

while True:
    try:
        linea = puerto.readline().decode().strip()
        if not linea:
            continue
        objeto = json.loads(linea)
        print(objeto)
        valor = objeto["values"]
        fig, ax = plt.subplots()
        #grafico = ax.plot(lista)
        ax.set_ylim(0,400)
        valornuevo = 400 - valor 
        ax.pie([valor,valornuevo], labels=["Potenciometro","Restante"], 
               autopct="%1.1f%%")
        #ax.set_xlabel('Sensor')
        #ax.set_ylabel('Valores')
        ax.set_title('Grafico de barras con OpenCV')

        fig.canvas.draw()
        img = np.array(fig.canvas.buffer_rgba())
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imshow('Grafico con OpenCV', img)
        #cv2.waitKey(1)
        plt.close(fig)   
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    except json.JSONDecodeError:
        print('Error de json')
        
    except Exception as e:
        print('Error', e)
        break

puerto.close()   
cv2.destroyAllWindows()