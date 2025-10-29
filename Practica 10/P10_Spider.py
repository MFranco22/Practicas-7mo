import cv2
import matplotlib.pyplot as plt
import numpy as np
import serial
import json

lista = []
puerto = serial.Serial("COM7",115200)

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
        figura, [ax1,bx1] = plt.subplots(1,2, figsize=(10,5))
        
        #GRAFICO 1: Grafico de barras
        grafico = ax1.bar(range(len(lista)),(lista))
        ax1.set_ylim(0, 450)        
        
        for _graficos,_lista in zip(grafico,lista):           #Este for es para poner los valores encima de las barras
            ax1.text(_graficos.get_x() + _graficos.get_width() / 2, 
            _lista + 1,
            str(_lista), ha='center', 
            va='bottom', fontsize=10, color='black')
            
        #GRAFICO 2: Grafico de Pastel
        valorNuevo = 450 - valor
        bx1.pie([valor,valorNuevo],labels=["Valor","valorNuevo"],
                autopct="%1.1f%%")
        bx1.set_title("Grafico de Pastel con OpenCV")
   
        figura.canvas.draw()
        img = np.array(figura.canvas.buffer_rgba())
        img = cv2.cvtColor(img,cv2.COLOR_RGBA2BGR)
        cv2.imshow("Grafico de barras",img)
        cv2.waitKey(1)
        plt.close(figura)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break    
    except json.JSONDecodeError:
            print("Error al decodificar JSON")
    except Exception as e:
            print("Error inesperado:", e)
            break
puerto.close()
cv2.destroyAllWindows()