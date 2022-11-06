from tkinter import *
import tkinter as tk
from tkinter import ttk

from telaEditarSala import telaEditarSala


def telaSala():
    class TelaSala:
        def __init__(self, sala_individual):
            self.sala_individual = sala_individual
            self.sala_individual.title('Sala Individual')
            self.sala_individual.iconbitmap('icone.ico')
            self.sala_individual.geometry('1440x750+50+10')
            self.sala_individual.resizable(False, False)

            self.label_superior = tk.Label(self.sala_individual, bg='#004AAD', height=95)
            self.label_superior.place(relx=0, relwidth=1, rely=0, relheight=0.08)

            self.senac_logo = tk.PhotoImage(file=r'..\ProjetoFinal\logo_simbolo.png')
            self.label_senac_logo = tk.Label(self.sala_individual, image=self.senac_logo)
            self.label_senac_logo.place(relx=0.1, rely=0.11)
            self.label_titulo_salas = tk.Label(self.sala_individual, text='Salas', font='Inter 28 bold', bg='#F5F5F5')
            self.label_titulo_salas.place(relx=0.19, rely=0.13)

            self.botao_voltar_sala_indiviual = tk.Button(self.sala_individual, text='Voltar',
                                                         font='Inter 17 bold', fg='white', bg='#004AAD',
                                                         relief=FLAT)
            self.botao_voltar_sala_indiviual.place(relx=0.8, relwidth=0.1, rely=0.15)

            self.label_inferior = tk.Label(self.sala_individual, bg='#004AAD', height=95)
            self.label_inferior.place(relx=0, relwidth=1, rely=0.92, relheight=0.08)

            self.icone_editar = tk.PhotoImage(file=r'..\ProjetoFinal\editar.png')
            self.label_icone_editar = tk.Label(self.sala_individual, image=self.icone_editar)
            self.label_icone_editar.place(relx=0.73, rely=0.85)
            self.btn_editar = tk.Button(self.sala_individual, text='Editar',
                                        font='Inter 13', relief=FLAT,
                                        fg='black', width=6, command=lambda: self.editar_sala())
            self.btn_editar.place(relx=0.75, rely=0.85)

            self.icone_excluir = tk.PhotoImage(file=r'..\ProjetoFinal\lixeira.png')
            self.label_icone_excluir = tk.Label(self.sala_individual, image=self.icone_excluir)
            self.label_icone_excluir.place(relx=0.81, rely=0.85)
            self.btn_excluir = tk.Button(self.sala_individual, text='Excluir',
                                         font='Inter 13',
                                         fg='red', width=6, relief=FLAT, command=lambda: self.excluir_sala())
            self.btn_excluir.place(relx=0.83, rely=0.85)

        def editar_sala(self):
            telaEditarSala()

        def excluir_sala(self):
            pass

    sala_individual = tk.Toplevel()
    objetoSalasGeral = TelaSala(sala_individual)
    sala_individual.mainloop()

telaSala()