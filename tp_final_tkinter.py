import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import subprocess

def salir():
    ventana.destroy()

def librerias_python():
    messagebox.showinfo("Librerías Python", "Ejercicio sobre Librerías Python")

def ejecutar_script_matriz_36():
    try:
        resultado = subprocess.check_output(["python", "Matriz_36.py"], text=True)
        text_resultado.delete(1.0, tk.END)  # Limpiar el contenido anterior
        text_resultado.insert(tk.END, resultado)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al ejecutar el script: {e}")
        
def ejecutar_script_matriz_triangular():
    try:
        resultado = subprocess.check_output(["python", "Matriz_Triangular.py"], text=True)
        text_resultado.delete(1.0, tk.END)  # Limpiar el contenido anterior
        text_resultado.insert(tk.END, resultado)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al ejecutar el script: {e}")
        
def ejecutar_script_planilla_ventas():
    try:
        resultado = subprocess.check_output(["python", "Planilla_de_Datos_de_Ventas.py"], text=True)
        text_resultado.delete(1.0, tk.END)  # Limpiar el contenido anterior
        text_resultado.insert(tk.END, resultado)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al ejecutar el script: {e}")
        
def ejecutar_script_planilla_acciones():
    try:
        resultado = subprocess.check_output(["python", "Planilla_De_Resultado_De_Acciones.py"], text=True)
        text_resultado.delete(1.0, tk.END)  # Limpiar el contenido anterior
        text_resultado.insert(tk.END, resultado)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al ejecutar el script: {e}")

def ejecutar_script_datos_encuestados():
    try:
        resultado = subprocess.check_output(["python", "Carga_datos_encuestados.py"], text=True)
        text_resultado.delete(1.0, tk.END)  # Limpiar el contenido anterior
        text_resultado.insert(tk.END, resultado)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al ejecutar el script: {e}")
        
def ejecutar_script_datos_en_orden():
    try:
        resultado = subprocess.check_output(["python", "Datos_Ordenados.py"], text=True)
        text_resultado.delete(1.0, tk.END)  # Limpiar el contenido anterior
        text_resultado.insert(tk.END, resultado)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al ejecutar el script: {e}")
        
def ejecutar_script_distribucion_notas():
    try:
        resultado = subprocess.check_output(["python", "Distribución_de _notas.py"], text=True)
        text_resultado.delete(1.0, tk.END)  # Limpiar el contenido anterior
        text_resultado.insert(tk.END, resultado)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al ejecutar el script: {e}")
        
def encuestas():
    messagebox.showinfo("Encuestas", "Ejercicio sobre Encuestas")

def ayuda():
    messagebox.showinfo("Ayuda", "Ejercicio sobre Ayuda")

def derechos_de_desarrollo():
    mensaje = "La aplicación fue creada por un equipo de estudiantes capacitados, encabezado por [Alexander Ortega], en colaboración con [Matias Juri, Gonzalo Zordan y Thomas Gutierrez]. Este grupo experto combinó habilidades técnicas avanzadas, experiencia en desarrollo de software y una profunda comprensión de las necesidades del profesor para llevar a cabo el trabajo, diseño y ejecución de la aplicación de manera exitosa."
    messagebox.showinfo("A cerca de ...", mensaje)

def matriz_36_elementos():
    matriz = np.random.random((6, 6))
    messagebox.showinfo("Matriz de 36 Elementos", f"Matriz:\n{matriz}")

def matriz_inferior_triangular():
    matriz = np.tril(np.random.random((6, 6)))
    messagebox.showinfo("Matriz Inferior Triangular", f"Matriz:\n{matriz}")

def planilla_datos_ventas():
    messagebox.showinfo("Planilla de Datos de Ventas", "Funcionalidad de Planilla de Datos de Ventas")

def Planilla_de_Resultado_de_Acciones():
    messagebox.showinfo("Planilla de Resultado de Acciones", "Funcionalidad de Planilla de Resultado de Acciones")

def distribucion_notas():
    messagebox.showinfo("Distribución de Notas", "Funcionalidad de Distribución de Notas")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("TP Final")
ventana.geometry("600x800")

# Cargar la imagen con Pillow
imagen_pillow = Image.open("imagen_trabajo.png")
imagen_fondo = ImageTk.PhotoImage(imagen_pillow)

# Crear un widget Label para mostrar la imagen
label_fondo = tk.Label(ventana, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Crear un botón de salir
boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(pady=20)

# Crear un widget Text para mostrar el resultado
text_resultado = tk.Text(ventana, height=10, width=75)
text_resultado.pack(padx=10, pady=10)

# Definir las funciones para cada opción del menú
def menu_librerias():
    librerias_python()

def menu_encuestas():
    encuestas()

def menu_ayuda():
    ayuda()

# Crear la barra de menú
barra_menu = tk.Menu(ventana)

# Crear la opción "Librerías Python" en el menú
menu_librerias_opcion = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Librerías Python", menu=menu_librerias_opcion)

# Agregar subopción "Matrices con Numpy"
menu_matrices_opcion = tk.Menu(menu_librerias_opcion, tearoff=0)
menu_librerias_opcion.add_cascade(label="Matrices con Numpy", menu=menu_matrices_opcion)

# Subopciones de "Matrices con Numpy"
menu_matrices_opcion.add_command(label="Matriz de 36 Elementos", command=ejecutar_script_matriz_36)
menu_matrices_opcion.add_command(label="Matriz Inferior Triangular", command=ejecutar_script_matriz_triangular)

# Agregar subopción "Dataframes con Pandas"
menu_dataframes_opcion = tk.Menu(menu_librerias_opcion, tearoff=0)
menu_librerias_opcion.add_cascade(label="Dataframes con Pandas", menu=menu_dataframes_opcion)

# Subopciones de "Dataframes con Pandas"
menu_dataframes_opcion.add_command(label="Planilla de Datos de Ventas", command=ejecutar_script_planilla_ventas)
menu_dataframes_opcion.add_command(label="Planilla de Resultado de Acciones", command=ejecutar_script_planilla_acciones)

# Agregar subopción "Gráficos con Matplotlib"
menu_matplotlib_opcion = tk.Menu(menu_librerias_opcion, tearoff=0)
menu_librerias_opcion.add_cascade(label="Gráficos con Matplotlib", menu=menu_matplotlib_opcion)

# Subopciones de "Gráficos con Matplotlib"
menu_matplotlib_opcion.add_command(label="Distribución de Notas", command=ejecutar_script_distribucion_notas)

# Crear la opción "Encuestas" en el menú
menu_encuestas_opcion = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Encuestas", menu=menu_encuestas_opcion)
menu_encuestas_opcion.add_command(label="Carga datos de Encuestados y Muestra", command=ejecutar_script_datos_encuestados)
menu_encuestas_opcion.add_command(label="Datos Encuesta Ordenados", command=ejecutar_script_datos_en_orden)

# Crear la opción "Ayuda" en el menú
menu_ayuda_opcion = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda_opcion)
menu_ayuda_opcion.add_command(label="A cerca de ...", command=derechos_de_desarrollo)

# Configurar la ventana para utilizar la barra de menú
ventana.config(menu=barra_menu)

# Ejecutar el bucle principal
ventana.mainloop()
