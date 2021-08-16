import tkinter as tk
from tkinter import * 
import pyautogui
import time

#Añadir control de tiempo para que entre a las clases automaticamente

#Ventana n.1
ventana = Tk()
ventana.geometry("200x300")
ventana.title("Clases automaticas")
ventana.resizable(0, 0)
ventana.config(bg="gray")


'''
EN CASO DE HABER USADO UNA SEGUNDA VENTANA  
def segundaVentana():
    ventana2 = Toplevel(ventana)
    ventana2.geometry("200x300")

    nota_Ventana2 = Label(ventana2, text="Esta es la ventana para entrar por")
    nota_Ventana2.place(x=0, y=0)
    nota_Ventana3 = Label(ventana2, text="segunda vez, despues de salir de una")
    nota_Ventana3.place(x=0, y=20)

    #Botones para entrar por segunda vez a una clase
    botonCalculo2 = Button(ventana2, text="Calculo diferencial")
    botonCalculo2.place(x=40, y=50)

    botonProbabilidad2 = Button(ventana2, text="Probabilidad y Estadistica")
    botonProbabilidad2.place(x=40, y=80)

    botonIngles2 = Button(ventana2, text="Ingles")
    botonIngles2.place(x=40, y=110)

    botonComputacion2 = Button(ventana2, text="Computacion")
    botonComputacion2.place(x=40, y=140)

    botonQuimica2 = Button(ventana2, text="Quimica")
    botonQuimica2.place(x=40, y=170)

    botonFisica2 = Button(ventana2, text="Fisica")
    botonFisica2.place(x=40, y=200)
'''

#Funciones para cada una de as clases al entrar por primera vez
def entrada_Meet():
    pyautogui.hotkey("win", "r")
    pyautogui.typewrite("msedge https://classroom.google.com//u/3/h")
    pyautogui.press("enter")
    time.sleep(4.5)

def ultimoPaso():
    pyautogui.moveTo(410, 605)
    pyautogui.click()
    pyautogui.moveTo(485, 610)
    pyautogui.click()
    pyautogui.moveTo(980, 467, 2)
    pyautogui.click()


def calculo_diferencial(): #primera
    entrada_Meet()
    pyautogui.moveTo(50, 251, 1)
    pyautogui.click(clicks=1, button="left")
    pyautogui.moveTo(400, 276, 2)
    pyautogui.click()
    time.sleep(6)
    ultimoPaso()

def probabilidad_y_estadistica(): #segunda
    entrada_Meet()
    pyautogui.moveTo(400, 251, 1)
    pyautogui.click(clicks=1, button="left")
    pyautogui.moveTo(400, 276, 2)
    pyautogui.click()
    time.sleep(6)
    ultimoPaso()

def ingles(): #tercera
    entrada_Meet()
    pyautogui.moveTo(715, 250, 1)
    pyautogui.click(clicks=1, button="left")
    pyautogui.moveTo(400, 276, 2)
    pyautogui.click()
    time.sleep(6)
    ultimoPaso()

def computacion(): #cuarta
    entrada_Meet()
    pyautogui.moveTo(1030, 250, 1)
    pyautogui.click(clicks=1, button="left")
    pyautogui.moveTo(400, 246, 2)
    pyautogui.click()
    time.sleep(6)
    ultimoPaso()

def quimica(): #quinta
    entrada_Meet()
    pyautogui.moveTo(50, 559, 1)
    pyautogui.click(clicks=1, button="left")
    pyautogui.moveTo(400, 276, 2)
    pyautogui.click()
    time.sleep(6)
    ultimoPaso()

def fisica(): #sexta
    entrada_Meet()
    pyautogui.moveTo(380, 559, 1)
    pyautogui.click(clicks=1, button="left")
    pyautogui.moveTo(400, 276, 2)
    pyautogui.click()
    time.sleep(6)
    ultimoPaso()

#Botones para entrar por primera vez
claseCalculo = Button(ventana, text="Calculo Diferencial", bg="red", command=calculo_diferencial)
claseCalculo.place(x=25, y=30)

claseProbabilidad = Button(ventana, text="Probabilidad y Estadistica", bg="blue", command=probabilidad_y_estadistica)
claseProbabilidad.place(x=25, y=60)

claseIngles = Button(ventana, text="Inglés", bg="yellow", command=ingles)
claseIngles.place(x=25, y=90)

claseComputacion = Button(ventana, text="Computacion", bg="white", command=computacion)
claseComputacion.place(x=25, y=120)

claseQuimica = Button(ventana, text="Quimica", bg="purple", command=quimica)
claseQuimica.place(x=25, y=150)

claseFisica = Button(ventana, text="Fisica", bg="green", command=fisica)
claseFisica.place(x=25, y=180)

nota = Label(ventana, text="Al dar click sobre cualquier clase", bg="gray")
nota2 = Label(ventana, text="esta te llevara a la clase seleccionada", bg="gray")
nota2.place(x=0, y=250)
nota.place(x=0, y=230)


clases = Label(ventana, text="Clases:", bd=2, bg="gray", font="Elefant 14")
clases.pack()

'''
segundaNota = Label(ventana, text="Si ya estas en la ventana donde te")
segundaNota.place(x=0, y=270)
terceraNota = Label(ventana, text="saliste de tu clase, entra al siguiente boton")
terceraNota.place(x=0, y=290)

botonVentana2 = Button(ventana, text="Segunda vez", command=segundaVentana)
botonVentana2.place(x=50, y=315)
'''


ventana.mainloop()

#pruebas