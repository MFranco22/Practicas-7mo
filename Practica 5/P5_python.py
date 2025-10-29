
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

#BARRAS
ejesx = ['A','B','C','D']
ejesy = []

for i in range(1,5):
    ejesy.append(random.randint(1,100))

print(ejesy)    
fig, ax = plt.subplots()
grafico = ax.bar(ejesx, ejesy, color = 'skyBlue')

#MOSTRAR ARRIBA DE LAS BARRAS EL VALOR
for grafico, ejesy in zip(grafico, ejesy):
    ax.text(grafico.get_x() + grafico.get_width()/2,
            ejesy + 1,
            str(ejesy),
            ha='center',
            va='bottom',
            fontsize= 10, color='black')
    
ax.set_xlabel('Ejes X')
ax.set_ylabel('Ejes X')
ax.set_title('Grafico de barras con OpenCv')

fig.canvas.draw()
img = np.array(fig.canvas.buffer_rgba())
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imshow('Grafico con OpenCv', img)
cv2.waitKey(0)
cv2.destroyAllWindows()