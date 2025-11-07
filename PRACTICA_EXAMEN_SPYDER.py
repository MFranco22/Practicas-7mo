import cv2
import matplotlib.pyplot as plt
import numpy as np
import serial
import json

lista = []
lista2 = []
lista3 = []
lista4 = []
puerto = serial.Serial("COM7",115200, timeout=1)

plt.ion()

while True:
    try:
        linea = puerto.readline().decode().strip()
        if not linea:
            continue
        objeto = json.loads(linea)
        etiqueta = objeto["Labels"]
        valor = objeto["values"]
        print(objeto)
        
        if etiqueta == "Potenciometro":
            lista.append(valor)
            if len(lista) > 100:
                lista.pop(0)
                
        elif etiqueta == "Fotocelda":
            lista2.append(valor)
            if len(lista2) > 100:
                lista2.pop(0)
                
        elif etiqueta == "Humedad":
            lista3.append(valor)
            if len(lista3) > 100:
                lista3.pop(0)
        
        elif etiqueta == "Ultrasonico":
            lista4.append(valor)
            if len(lista4) > 100:
                lista4.pop(0)
                
        # Solo graficar si hay datos en los sensores
        #if len(lista) == 0 or len(lista2) == 0 or len(lista3) == 0 or len(lista4) == 0:
            #continue
        # ✅ Solo graficar si hay al menos 1 valor en alguna lista
        if not (lista or lista2 or lista3 or lista4):
            continue
          
            
        #fig, (ax, bx, cx) = plt.subplots(1, 3, figsize=(10,4))
        fig, graf = plt.subplots(2,2, figsize=(10,4))
        ax = graf[0,0]
        bx = graf[0,1]
        cx = graf[1,0]
        dx = graf[1,1]

        #GRAFICO 1: Grafico de barras POTENCIOMETRO
        grafico = ax.bar(range(len(lista)),(lista))
        ax.set_title("Potenciómetro")
        ax.set_ylim(0, 450)        
        
        for _graficos,_lista in zip(grafico,lista):           #Este for es para poner los valores encima de las barras
            ax.text(_graficos.get_x() + _graficos.get_width() / 2, 
            _lista + 1,
            str(_lista), ha='center', 
            va='bottom', fontsize=10, color='black')
            
        # --- GRAFICO 2: Fotocelda ---
        if lista2:
            grafico2 = lista2[-1]
            restante = max(0, 400 - grafico2)
            bx.pie([grafico2, restante],
                   labels=["Fotocelda", "Restante"],
                   autopct="%1.1f%%")
            bx.set_title("Fotocelda")

        
        #GRAFICO 3: Barras FOTOCELDA
        grafico3 = cx.bar(range(len(lista3)),(lista3))
        cx.set_title("FOTOCELDA")
        cx.set_ylim(0, 450)        
        
        for _graficos,_lista in zip(grafico3,lista3):           #Este for es para poner los valores encima de las barras
            cx.text(_graficos.get_x() + _graficos.get_width() / 2, 
            _lista + 1,
            str(_lista), ha='center', 
            va='bottom', fontsize=10, color='black')
            
            
        # --- GRAFICO 4: ULTRASONICO ---
        grafico4 = lista4[-1]
        restante = max(0, 400 - grafico4)
        dx.pie([grafico4, restante],
               labels=["Ultrasonico", "Restante"],
               autopct="%1.1f%%")
        dx.set_title("ULTRASONICO")
         
            
        fig.canvas.draw()
        img = np.array(fig.canvas.buffer_rgba())
        img = cv2.cvtColor(img,cv2.COLOR_RGBA2BGR)
        cv2.imshow("Grafico de barras",img)
        cv2.waitKey(1)
        plt.close(fig)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break    
    except json.JSONDecodeError:
            print("Error al decodificar JSON")
    except Exception as e:
            print("Error inesperado:", e)
            break
puerto.close()
cv2.destroyAllWindows()