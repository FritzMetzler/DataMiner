from matplotlib.pyplot import text
import views.eda as eda
from views.eda import abrir_ventana_secundaria
import tkinter as tk
from tkinter import ttk





root = tk.Tk()
root.config(width=800, height=500)
root.resizable(False, False)
root.title("BITMINER")
"""
Apartado de creacion de botones

"""

EDA__button = ttk.Button(
    root,
    text="EDA",
    command=abrir_ventana_secundaria
)

EDA__button.place(x=100, y=100)

ADC__button = ttk.Button(
    root,
    text="ADC",
    command=abrir_ventana_secundaria
)

ADC__button.place(x=100, y=150)

PCA__button = ttk.Button(
    root,
    text="PCA",
    command=abrir_ventana_secundaria
)

PCA__button.place(x=100, y=200)

clustering__button = ttk.Button(
    root,
    text="Clustering",
    command=abrir_ventana_secundaria
)

clustering__button.place(x=200, y=100)

AsociationRules__button = ttk.Button(
    root,
    text="AR",
    command=abrir_ventana_secundaria
)

AsociationRules__button .place(x=200, y=150)

woods__button = ttk.Button(
    root,
    text="Woods",
    command=abrir_ventana_secundaria
)

woods__button.place(x=200, y=200)

"""
Apartado de dataframe widged de visualizacion
"""



root.mainloop()