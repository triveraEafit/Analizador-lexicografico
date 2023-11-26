import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import re

# Diccionario de correspondencia entre emojis y sus rutas de archivo
EMOJI_PATHS = {
    ":)": "png/006-feliz-1.png",
    ":(": "png/009-triste.png",
    ":D": "png/005-sonriente.png",
    ";)": "png/018-guino.png",
    ":P": "png/025-nerd.png ",
    "xD": "png/010-risa.png",
    ":-)": "png/006-feliz-1.png",
    ":-(": "png/009-triste.png",
    "(y)": "png/045-como.png",
    "(n)": "png/028-pulgares-abajo.png",
    "<3": "png/corazon.png",
    "\\m/": "png/027-fresco.png",
    ":-O": "png/055-sorpresa.png",
    ":O": "png/004-conmocionado.png",
    ":-|": "png/indiferencia1.png",
    ":|": "png/75404.png",
    ":*": "png/kisspng-smiley-emoticon-kiss-emoji-clip-art-kiss-smiley-transparent-background-5a75415d9cfd16.7358352615176338856431.jpg",
    ">:(": "png/037-jurar.png",
    "^^": "png/038-sonriente-1.png",
    ":-]": "png/052-obrero.png",




    # Agrega más emojis según sea necesario
}

# Función para analizar lexicográficamente la cadena de texto
def analizador_lexicografico(cadena):
    # Expresión regular para identificar palabras en español
    palabras_espanol = re.findall(r'\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+\b', cadena)

    # Expresión regular para identificar emojis
    emojis = re.findall(r':\)|:\(|:D|;\)|:P|xD|:-\)|:-\(|\(y\)|\(n\)|<3|\\m/|:-O|:O|:-\||:\||:\*|>:\(|\^\^|:-\]',
                        cadena)

    return palabras_espanol, emojis
# Función para mostrar la interfaz gráfica
def mostrar_interfaz():
    def procesar():
        # Obtener la cadena de texto ingresada
        cadena = entrada_texto.get("1.0", 'end-1c')

        # Analizar lexicográficamente la cadena
        palabras_espanol, emojis = analizador_lexicografico(cadena)

        # Mostrar resultados en la interfaz gráfica
        salida_texto.delete("1.0", tk.END)
        salida_texto.insert(tk.END, f"Cadena de salida:\n\n")

        # Inicializar contadores
        contador_palabras = 0
        contador_emojis = 0

        # Iterar sobre la cadena original y mostrar texto con imágenes
        # Iterar sobre la cadena original y mostrar texto con imágenes
        for palabra in re.split(
                r'(:\)|:\(|:D|;\)|:P|xD|:-\)|:-\(|\(y\)|\(n\)|<3|\\m/|:-O|:O|:-\||:\||:\*|>:\(|\^\^|:-\])|(\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+\b)',
                cadena):
            if palabra and palabra in emojis:
                # Si la palabra es un emoji, obtener la ruta y mostrar la imagen
                ruta_emoji = EMOJI_PATHS.get(palabra, "png")
                cargar_y_mostrar_emoji(palabra, ruta_emoji)
                contador_emojis += 1
                # Agregar un espacio después del emoji
                salida_texto.insert(tk.END, " ")
            elif palabra and re.match(r'\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+\b', palabra):
                # Si la palabra no es un emoji y es una palabra en español, mostrar el texto
                salida_texto.insert(tk.END, palabra + " ")  # Agregar un espacio después de la palabra
                contador_palabras += 1

        # Agregar una nueva línea en la salida
        salida_texto.insert(tk.END, '\n')

        # Mostrar la cantidad de palabras y emojis identificados
        salida_texto.insert(tk.END, f"\nPalabras en español identificadas: {contador_palabras}\n")
        salida_texto.insert(tk.END, f"Emojis identificados: {contador_emojis}\n")

        # Agregar una imagen a la interfaz
        cargar_y_mostrar_imagen()
    # Función para cargar y mostrar un emoji
    def cargar_y_mostrar_emoji(emoji, ruta_emoji):
        try:
            # Cargar la imagen del emoji
            imagen_emoji = Image.open(ruta_emoji)
            imagen_emoji = imagen_emoji.resize((50, 50))  # O Image.BICUBIC como método de interpolación

            # Convertir la imagen a formato Tkinter
            emoji_tk = ImageTk.PhotoImage(imagen_emoji)

            # Crear un label para mostrar la imagen
            label_emoji = tk.Label(salida_texto, image=emoji_tk)
            label_emoji.image = emoji_tk  # Evitar que la imagen sea eliminada por el recolector de basura
            label_emoji.image_tk = emoji_tk  # Mantener una referencia adicional
            label_emoji.pack(side=tk.LEFT)

            # Insertar emoji en el widget Text
            salida_texto.window_create(tk.END, window=label_emoji)

        except FileNotFoundError:
            salida_texto.insert(tk.END, f"Emoji no encontrado: {emoji}\n")

    # ...

    # Función para cargar y mostrar una imagen
    def cargar_y_mostrar_imagen():
        try:
            # Ruta de la imagen (reemplaza 'ruta_de_la_imagen.jpg' con la ruta correcta)
            ruta_imagen = "png"

            # Cargar la imagen
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((200, 200), Image.ANTIALIAS)  # Ajustar tamaño según necesidades

            # Convertir la imagen a formato Tkinter
            imagen_tk = ImageTk.PhotoImage(imagen)

            # Crear un label para mostrar la imagen
            label_imagen = tk.Label(salida_texto, image=imagen_tk)
            label_imagen.image = imagen_tk  # Evitar que la imagen sea eliminada por el recolector de basura
            label_imagen.image_tk = imagen_tk  # Mantener una referencia adicional
            label_imagen.pack(side=tk.LEFT)

        except FileNotFoundError:
            salida_texto.insert(tk.END, "Imagen no encontrada\n")

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Analizador Lexicográfico")
    logo = tk.PhotoImage(file="logo_eafit_completo.png")
    w1 = tk.Label(ventana, image=logo).pack(side="right")

    escudo = tk.PhotoImage(file="Presidential_Seal_of_Colombia_(2).svg.png")
    w2 = tk.Label(ventana, image=escudo).pack(side="left")



    # Crear una caja de texto para ingresar la cadena
    entrada_texto = scrolledtext.ScrolledText(ventana, width=40, height=10)
    entrada_texto.pack(padx=10, pady=10)

    # Crear un botón para procesar la cadena
    boton_procesar = tk.Button(ventana, text="Procesar", command=procesar)
    boton_procesar.pack(pady=5)

    # Crear una caja de texto para mostrar los resultados
    salida_texto = scrolledtext.ScrolledText(ventana, width=40, height=15)
    salida_texto.pack(padx=10, pady=10)

    # Iniciar el bucle de eventos de la interfaz gráfica
    ventana.mainloop()

# Llamar a la función para mostrar la interfaz gráfica
mostrar_interfaz()
