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
        lista.append(valor)
        if len(lista) > 5:
            lista.pop(0)
        fig, graf = plt.subplots(2,2, figsize=(10,4))
        ax = graf[0,0]
        bx = graf[0,1]
        cx = graf[1,0]
        dx = graf[1,1]
        
        #GRAFICO 1
        grafico = ax.bar(range(len(lista)),lista)
        ax.set_ylim(0,400)
        print(lista)
        for _grafico, _lista in zip(grafico, lista):
            ax.text(_grafico.get_x() + _grafico.get_width()/2,
                    _lista + 1,
                    str(_lista),
                    ha='center', va='bottom', fontsize=10, color='black') 
            
        ax.set_xlabel('Sensor')
        ax.set_ylabel('Valores')
        ax.set_title('Grafico de barras con OpenCV')
        
        #GRAFICO 2
        valornuevo = 400 - valor 
        bx.pie([valor,valornuevo], labels=["GRAFICO 2","Restante"], 
               autopct="%1.1f%%")
        bx.set_title('Grafico de barras con OpenCV')
        grafico2 = dx.bar(range(len(lista)),lista)
        dx.set_ylim(0,400)
        print(lista)
        for _grafico, _lista in zip(grafico2, lista):
            ax.text(_grafico.get_x() + _grafico.get_width()/2,
                    _lista + 1,
                    str(_lista),
                    ha='center', va='bottom', fontsize=10, color='black') 
            
        dx.set_xlabel('Sensor')
        dx.set_ylabel('Valores')
        dx.set_title('Grafico de barras con OpenCV')
        
        #GRAFICO 3
        valornuevo = 400 - valor 
        cx.pie([valor,valornuevo], labels=["GRAFICO 3","Restante"], 
               autopct="%1.1f%%")
        cx.set_title('Grafico de barras con OpenCV')
       
        
       #pintamos el grafico
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