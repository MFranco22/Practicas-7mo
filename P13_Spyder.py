# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 13:28:56 2025

@author: migue
"""
import cv2
import socket
import numpy as np

ipesp32 = "192.168.16.117"
puerto = 12345

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.connect((ipesp32,puerto))

lista = []

while True:
    try:
        dato = servidor.recv(1024).decode().strip()
        if not dato:
            continue
        print(dato)
        lista.append(dato)
        if len(lista) >=10:
            break
        
    except Exception as e:
        print("error")
    
servidor.close