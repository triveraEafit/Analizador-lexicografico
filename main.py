import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import re


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




    
}


def analizador_lexicografico(cadena):
    
    palabras_espanol = re.findall(r'\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+\b', cadena)

    
    emojis = re.findall(r':\)|:\(|:D|;\)|:P|xD|:-\)|:-\(|\(y\)|\(n\)|<3|\\m/|:-O|:O|:-\||:\||:\*|>:\(|\^\^|:-\]',
                        cadena)

    return palabras_espanol, emojis

def mostrar_interfaz():
    def procesar():
        
        cadena = entrada_texto.get("1.0", 'end-1c')

        
        palabras_espanol, emojis = analizador_lexicografico(cadena)

        
        salida_texto.delete("1.0", tk.END)
        salida_texto.insert(tk.END, f"Cadena de salida:\n\n")

        
        contador_palabras = 0
        contador_emojis = 0

        
        for palabra in re.split(
                r'(:\)|:\(|:D|;\)|:P|xD|:-\)|:-\(|\(y\)|\(n\)|<3|\\m/|:-O|:O|:-\||:\||:\*|>:\(|\^\^|:-\])|(\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+\b)',
                cadena):
            if palabra and palabra in emojis:
                
                ruta_emoji = EMOJI_PATHS.get(palabra, "png")
                cargar_y_mostrar_emoji(palabra, ruta_emoji)
                contador_emojis += 1
                
                salida_texto.insert(tk.END, " ")
            elif palabra and re.match(r'\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+\b', palabra):
                
                salida_texto.insert(tk.END, palabra + " ")  a
                contador_palabras += 1

        
        salida_texto.insert(tk.END, '\n')

        
        salida_texto.insert(tk.END, f"\nPalabras en español identificadas: {contador_palabras}\n")
        salida_texto.insert(tk.END, f"Emojis identificados: {contador_emojis}\n")

        
        cargar_y_mostrar_imagen()
    
    def cargar_y_mostrar_emoji(emoji, ruta_emoji):
        try:
            
            imagen_emoji = Image.open(ruta_emoji)
            imagen_emoji = imagen_emoji.resize((50, 50))  

            
            emoji_tk = ImageTk.PhotoImage(imagen_emoji)

            
            label_emoji = tk.Label(salida_texto, image=emoji_tk)
            label_emoji.image = emoji_tk  
            label_emoji.image_tk = emoji_tk  
            label_emoji.pack(side=tk.LEFT)

            
            salida_texto.window_create(tk.END, window=label_emoji)

        except FileNotFoundError:
            salida_texto.insert(tk.END, f"Emoji no encontrado: {emoji}\n")

 


    def cargar_y_mostrar_imagen():
        try:
            
            ruta_imagen = "png"

            
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((200, 200), Image.ANTIALIAS) 

            
            imagen_tk = ImageTk.PhotoImage(imagen)

            
            label_imagen = tk.Label(salida_texto, image=imagen_tk)
            label_imagen.image = imagen_tk  
            label_imagen.image_tk = imagen_tk  
            label_imagen.pack(side=tk.LEFT)

        except FileNotFoundError:
            salida_texto.insert(tk.END, "Imagen no encontrada\n")

    
    ventana = tk.Tk()
    ventana.title("Analizador Lexicográfico")
    logo = tk.PhotoImage(file="logo_eafit_completo.png")
    w1 = tk.Label(ventana, image=logo).pack(side="right")

    escudo = tk.PhotoImage(file="Presidential_Seal_of_Colombia_(2).svg.png")
    w2 = tk.Label(ventana, image=escudo).pack(side="left")



    
    entrada_texto = scrolledtext.ScrolledText(ventana, width=40, height=10)
    entrada_texto.pack(padx=10, pady=10)

 
    boton_procesar = tk.Button(ventana, text="Procesar", command=procesar)
    boton_procesar.pack(pady=5)

   
    salida_texto = scrolledtext.ScrolledText(ventana, width=40, height=15)
    salida_texto.pack(padx=10, pady=10)
    ventana.mainloop()


mostrar_interfaz()
