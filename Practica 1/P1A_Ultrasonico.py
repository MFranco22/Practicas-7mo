import time
import serial 
from tkinter import *
from tkinter import messagebox

class Principal():
    def _init_(self):
        self.ven = Tk()
        self.ven.geometry("400x200")
        self.conexion= None
        self.n = 0
        self.lista = []
       
        
    def recibir(self):
        iniciado = False
        while True:
            datos = self.conexion.readline().strip()
            if not datos:
                continue
            texto = datos.decode('utf-8', errors='ignore')
            if "ESP32" in texto:
                iniciado = True
                continue
            if iniciado:
                print(datos)
                self.mensaje.config(text=f"{texto}")
                self.ven.update_idletasks()  #recargar o actualiza la ventana
            self.n += 1
            if self.n > 20:
                self.conexion.close()
                break
            time.sleep(0.1)


        
    def inicio(self):
        try:
            self.conexion = serial.Serial('COM3', 115200, timeout=1)
            messagebox.showinfo("Exito","Si se conecto...")
            
        except:
            messagebox.showerror("Error","Error al conectar")
        self.mensaje = Label(self.ven, text="Hola")
        self.mensaje.place(x=10,y=10)
        Button(self.ven, text="Aceptar", command=self.recibir).place(x=10,y=30)
        Button(self.ven, text="Cerrar", command=self.cerrar).place(x=70,y=30)
        self.ven.mainloop()
        
        
    def cerrar(self):
        self.conexion.close()
        self.ven.destroy()

if __name__== '__main__':
    app = Principal()
    app.inicio()