from tkinter import *
from tkinter import ttk
from PegaDados import PegaData
import threading

class Interface:
    def execute(self):
        window = Tk()
        window.title('dyst app')
        window.geometry('700x500+100+0')
        
        self.text_distancia = Label(window, text='0')
        self.text_distancia.pack()

        label_from = Label(window, text='De: ')
        label_from.pack()

        self.input_from = ttk.Entry(window)
        self.input_from.pack()

        label_for = Label(window, text='Para: ')
        label_for.pack()

        self.input_for = ttk.Entry(window)
        self.input_for.pack()

        botao_calc_dist = ttk.Button(
            window, 
            text='Calcular Distância',
            command=lambda: threading.Thread(target=self.pega).start())
        
        botao_calc_dist.pack()

        btn_ver_imagem = ttk.Button(window, text='Visualizar')
        btn_ver_imagem.pack()

        # ! mantem a janela aberta: 
        mainloop() 

    def pega(self):
        partida = 'fortaleza'
        chegada = 'jericoacoara'
        distancia = PegaData().pega(partida, chegada)
        self.text_distancia.config(text=distancia)
        # print(distancia)

Interface().execute()