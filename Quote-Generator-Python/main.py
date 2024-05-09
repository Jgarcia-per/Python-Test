import tkinter as tk
import requests
from threading import Thread
from deep_translator import GoogleTranslator

# Variables del api
api = 'http://api.quotable.io/random'
quotes = []
quotes_number = 0

# Variables de la ventana
window = tk.Tk()
window.geometry('1200x260')
window.title('Generador de Frases!')
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.configure(bg='black')

# Precargar
def preload_quotes():
    global quotes

    print('----- Cargando mas Frases -----')
    for x in range(10):
        random_quote = requests.get(api).json()
        text = random_quote['content']
        translator = GoogleTranslator(source='en', target='es')
        content_es = translator.translate(text)
        author = random_quote['author']
        quote = content_es + '\n\n' + "Por " + author
        print(content_es)
    
        quotes.append(quote)
    print ('----- Finalizado el cargado de frases -----')

preload_quotes()

# Cargar nueva
def get_random_quote():
    global quotes_label
    global quotes
    global quotes_number

    quotes_label.configure(text=quotes[quotes_number])
    quotes_number = quotes_number + 1
    print(quotes_number)

    if quotes_number == 10:
        quotes_number = 0
        preload_quotes()

# Estilos de la ventana
quotes_label = tk.Label(window,
                        text='Presione el boton para generar una frase!',
                        height=6,
                        pady=10,
                        wraplength=800,
                        font=('Helvetica',14),
                        bg='black',
                        fg='white',)
quotes_label.grid(row=0,
                  column=0,
                  stick='WE',
                  padx=20,
                  pady=10)

# boton en la ventana
button = tk.Button(text='Generar',
                   command=get_random_quote,
                   bg='#b300b3',
                   fg='black',
                   activebackground='#330033',
                   activeforeground='white',
                   font=('Helvetica', 14))
button.grid(row=1,
            column=0,
            stick='WE',
            padx=20,
            pady=10)

# estar en bucle
if __name__ == '__main__':
    window.mainloop()