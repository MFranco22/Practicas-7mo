
import serial
import time
from tkinter import *
from tkinter import messagebox

class Principal():
    def __init__(self):
        self.ven = Tk()
        self.ven.geometry("400x200")
        self.ven.title("Sensor Ultrasonico")

        self.conexion = None  # Inicialmente sin conexión

        # Botón para conectar
        Button(self.ven, text="Conectar", command=self.conectar).place(x=20, y=50)

        # Botón para recibir datos
        Button(self.ven, text="Recibir datos", command=self.recibir).place(x=120, y=50)

        self.mensaje = Label(self.ven, text="Estado: Desconectado", fg="red") #inicializa con desconectado
        self.mensaje.place(x=20, y=20)

    def conectar(self):
        try:
            self.conexion = serial.Serial('COM7', 115200, timeout=1)
            time.sleep(2)
            messagebox.showinfo("Éxito", "✅ Conectado al Arduino")
            self.mensaje.config(text="Estado: Conectado", fg="green") #AQUI cambia el texto a conectado
        except Exception as e:                                       #exepcion e para guardar el motivo del error
            messagebox.showerror("Error", f"❌ No se pudo conectar\n{e}") # f para mostrar el error

    def recibir(self):
        if self.conexion is None:
            messagebox.showwarning("Atención", "Primero debes conectar el Arduino.")
            return

        lista = []
        n = 0

        try:
            while n < 5:
                if self.conexion.in_waiting > 0:
                    datos = self.conexion.readline().decode('utf-8').strip()
                    if datos != "":
                        lista.append(datos)
                        print("Distancia:", datos, "cm")
                        self.mensaje.config(text=f"Distancia: {datos} cm")
                n += 1
                self.ven.update()  # Actualiza la interfaz
                time.sleep(0.1)

            print("Lectura terminada.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error:\n{e}")

    def inicio(self):
        self.ven.mainloop()
        if self.conexion:
            self.conexion.close()

if __name__ == '__main__':
    app = Principal()
    app.inicio()
