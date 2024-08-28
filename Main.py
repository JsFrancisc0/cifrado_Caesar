import tkinter as tk
from tkinter import messagebox

# Este es el alfabeto con el que se inicia por defecto
alfabeto = 'abcdefghijklmnopqrstuvwxyz'


# Función para encriptar el texto
def encriptar():
    texto_original = entrada_texto.get("1.0", tk.END).strip()
    clave = entrada_clave.get()
    if not clave.isdigit():
        messagebox.showerror("Error", "La clave debe ser un número entero!")
        return
    clave = int(clave)

    texto_cifrado = ''
    for letra in texto_original:
        letra = letra.lower()
        if letra != ' ':
            index = alfabeto.find(letra)
            if index == -1:
                texto_cifrado += letra # Esto es para dejar los caracteres que no estan en el afabeto sin encriptar
            else:
                index_c = (index + clave) % len(alfabeto) # Aqui uso el operador mod para mantener el indice dentro del rango
                texto_cifrado += alfabeto[index_c]
        else:
            texto_cifrado += ' ' # Esto es para mantener los espacios

    salida_texto.delete("1.0", tk.END)
    salida_texto.insert(tk.END, texto_cifrado)


# Función para desencriptar el texto
def desencriptar():
    texto_cifrado = entrada_texto.get("1.0", tk.END).strip()
    clave = entrada_clave.get()
    if not clave.isdigit():
        messagebox.showerror("Error", "La clave debe ser un número entero!")
        return
    clave = int(clave)

    texto_original = ''
    for letra in texto_cifrado:
        letra = letra.lower()
        if letra != ' ':
            index = alfabeto.find(letra)
            if index == -1:
                texto_original += letra
            else:
                index_c = (index - clave) % len(alfabeto)
                texto_original += alfabeto[index_c]
        else:
            texto_original += ' '

    salida_texto.delete("1.0", tk.END)
    salida_texto.insert(tk.END, texto_original)


# Función para abrir la ventana de edición del alfabeto
def editar_alfabeto():
    def guardar_alfabeto():
        global alfabeto
        nuevo_alfabeto = entrada_nuevo_alfabeto.get().strip()
        if nuevo_alfabeto:
            alfabeto = nuevo_alfabeto
            messagebox.showinfo("Éxito", "Alfabeto actualizado correctamente")
            ventana_editar_alfabeto.destroy()
        else:
            messagebox.showerror("Error", "El alfabeto no puede estar vacío")

    ventana_editar_alfabeto = tk.Toplevel(ventana)
    ventana_editar_alfabeto.title("Editar Alfabeto")

    etiqueta_actual = tk.Label(ventana_editar_alfabeto, text="Alfabeto actual:")
    etiqueta_actual.pack()

    etiqueta_alfabeto = tk.Label(ventana_editar_alfabeto, text=alfabeto)
    etiqueta_alfabeto.pack()

    etiqueta_nuevo = tk.Label(ventana_editar_alfabeto, text="Nuevo alfabeto:")
    etiqueta_nuevo.pack()

    entrada_nuevo_alfabeto = tk.Entry(ventana_editar_alfabeto, width=50)
    entrada_nuevo_alfabeto.pack()

    boton_guardar = tk.Button(ventana_editar_alfabeto, text="Guardar", command=guardar_alfabeto)
    boton_guardar.pack()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cifrado César")

# Crear los botones, cuadros de texto etc
etiqueta_titulo = tk.Label(ventana, text="Cifrado César")
etiqueta_titulo.pack()

entrada_texto = tk.Text(ventana, height=10, width=40)
entrada_texto.pack()

etiqueta_clave = tk.Label(ventana, text="clave de desplazamiento")
etiqueta_clave.pack()

entrada_clave = tk.Entry(ventana)
entrada_clave.pack()

boton_encriptar = tk.Button(ventana, text="Encriptar", command=encriptar)
boton_encriptar.pack(side=tk.LEFT, padx=20, pady=10)

boton_desencriptar = tk.Button(ventana, text="Desencriptar", command=desencriptar)
boton_desencriptar.pack(side=tk.RIGHT, padx=20, pady=10)

salida_texto = tk.Text(ventana, height=10, width=40)
salida_texto.pack()

# Botón para editar el alfabeto
boton_editar_alfabeto = tk.Button(ventana, text="Editar alfabeto", command=editar_alfabeto)
boton_editar_alfabeto.pack(pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
