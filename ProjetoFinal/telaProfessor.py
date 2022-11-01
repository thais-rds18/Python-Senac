from tkinter import *
import tkinter as tk
from tkinter import ttk

from telaEditarSala import telaEditarSala


def telaProfessor():
    class TelaProfessor:
        def __init__(self, prof_individual):
            self.professor_individual = prof_individual
            self.professor_individual.title('Professor Individual')
            self.professor_individual.iconbitmap('icone.ico')
            self.professor_individual.geometry('1440x750+50+10')
            self.professor_individual.resizable(False, False)

            self.label_superior = tk.Label(self.professor_individual, bg='#004AAD', height=95)
            self.label_superior.place(relx=0, relwidth=1, rely=0, relheight=0.08)

            self.senac_logo = tk.PhotoImage(file=r'..\ProjetoFinal\logo_simbolo.png')
            self.label_senac_logo = tk.Label(self.professor_individual, image=self.senac_logo)
            self.label_senac_logo.place(relx=0.1, rely=0.11)
            self.label_titulo_salas = tk.Label(self.professor_individual, text='Professores', font='Inter 28 bold',
                                               bg='#F5F5F5')
            self.label_titulo_salas.place(relx=0.19, rely=0.13)

            self.botao_voltar_prof_indiviual = tk.Button(self.professor_individual, text='Voltar',
                                                         font='Inter 17 bold', fg='white', bg='#004AAD', relief=FLAT)
            self.botao_voltar_prof_indiviual.place(relx=0.8, relwidth=0.1, rely=0.15)

            self.icone_editar = tk.PhotoImage(file=r'..\ProjetoFinal\editar.png')
            self.label_icone_editar = tk.Label(self.professor_individual, image=self.icone_editar)
            self.btn_editar = tk.Button(self.professor_individual, text='Editar',
                                        font='Inter 13', relief=FLAT,
                                        fg='black', width=6, command=lambda: self.editar_prof())
            self.label_icone_editar.place(relx=0.73, rely=0.85)
            self.btn_editar.place(relx=0.75, rely=0.85)

            self.icone_excluir = tk.PhotoImage(file=r'..\ProjetoFinal\lixeira.png')
            self.label_icone_excluir = tk.Label(self.professor_individual, image=self.icone_excluir)
            self.label_icone_excluir.place(relx=0.81, rely=0.85)
            self.btn_excluir = tk.Button(self.professor_individual, text='Excluir',
                                         font='Inter 13',
                                         fg='red', width=6, relief=FLAT, command=lambda: self.excluir_prof())
            self.btn_excluir.place(relx=0.83, rely=0.85)

            self.label_inferior = tk.Label(self.professor_individual, bg='#004AAD', height=95)
            self.label_inferior.place(relx=0, relwidth=1, rely=0.92, relheight=0.08)

        def editar_prof(self):
            telaEditarSala()

        def excluir_prof(self):
            pass

        def botao_voltar_professor_individual(self):
            pass

    prof_individual = tk.Toplevel()
    objetoProfIndividual = TelaProfessor(prof_individual)
    prof_individual.mainloop()

