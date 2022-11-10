from tkinter import *
import tkinter as tk
from tkinter import ttk

from telaEditarSala import telaEditarSala


def telaSala(nnsala, nnpolo, nnandar, nncadeira, nncomputador, nntelevisor, nntelaretratil, nnprojetor,
             nnquadro, nnarcondicionado, nnmanha, nntarde, nnnoite):
    class TelaSala:
        def __init__(self, sala_individual):
            self.sala_individual = sala_individual
            self.sala_individual.title('Sala Individual')
            self.sala_individual.iconbitmap('icone.ico')
            self.sala_individual.geometry('1440x750+50+10')
            self.sala_individual['bg']='#F5F5F5'
            self.sala_individual.resizable(False, False)

            self.label_superior = tk.Label(self.sala_individual, bg='#004AAD', height=95)
            self.label_superior.place(relx=0, relwidth=1, rely=0, relheight=0.08)

            self.senac_logo = tk.PhotoImage(file=r'..\ProjetoFinal\logo_simbolo.png')
            self.label_senac_logo = tk.Label(self.sala_individual, image=self.senac_logo, bg='#F5F5F5')
            self.label_senac_logo.place(relx=0.1, rely=0.11)
            self.label_titulo_salas = tk.Label(self.sala_individual, text='Salas', font='Inter 28 bold', bg='#F5F5F5')
            self.label_titulo_salas.place(relx=0.19, rely=0.13)

            self.botao_voltar_sala_indiviual = tk.Button(self.sala_individual, text='Voltar',
                                                         font='Inter 17 bold', fg='white', bg='#004AAD',
                                                         relief=FLAT, command=lambda: self.sala_individual.destroy())
            self.botao_voltar_sala_indiviual.place(relx=0.8, relwidth=0.1, rely=0.15)

            self.label_titulo_sala = tk.Label(self.sala_individual, text=nnsala, font='Inter 24 bold', bg='#F5F5F5')
            self.label_titulo_sala.place(relx=0.1, rely=0.25)
            self.andarpoloSala = tk.Label(self.sala_individual, text=f'{nnandar}, {nnpolo}', font='Inter 22',
                                          bg='#F5F5F5')
            self.andarpoloSala.place(relx=0.18, rely=0.25)

            self.iconePessoas = tk.PhotoImage(file=r'..\ProjetoFinal\pessoas.png')
            self.label_iconePessoas = tk.Label(self.sala_individual, image=self.iconePessoas, bg='#F5F5F5')
            self.label_iconePessoas.place(relx=0.11, rely=0.40)
            self.nroCadeiras = tk.Label(self.sala_individual, text=f'{nncadeira} pessoas', font='Inter 17',
                                        bg='#F5F5F5')
            self.nroCadeiras.place(relx=0.16, rely=0.40)

            self.iconePcs = tk.PhotoImage(file=r'..\ProjetoFinal\computador.png')
            self.label_iconePcs = tk.Label(self.sala_individual, image=self.iconePcs, bg='#F5F5F5')
            self.label_iconePcs.place(relx=0.11, rely=0.45)
            self.nroPcsSala = tk.Label(self.sala_individual, text=f'{nncomputador} computadores', font='Inter 17',
                                       bg='#F5F5F5')
            self.nroPcsSala.place(relx=0.16, rely=0.45)

            self.iconeTelevisor = tk.PhotoImage(file=r'..\ProjetoFinal\tv.png')
            self.label_iconeTelevisor = tk.Label(self.sala_individual, image=self.iconeTelevisor, bg='#F5F5F5')
            self.label_iconeTelevisor.place(relx=0.11, rely=0.50)
            self.nroTvs = tk.Label(self.sala_individual, text=f'{nntelevisor} televisores', font='Inter 17',
                                   bg='#F5F5F5')
            self.nroTvs.place(relx=0.16, rely=0.50)

            self.iconeTela = tk.PhotoImage(file=r'..\ProjetoFinal\tela retratil.png')
            self.label_iconeTela = tk.Label(self.sala_individual, image=self.iconeTela, bg='#F5F5F5')
            self.label_iconeTela.place(relx=0.11, rely=0.55)
            self.nroTela = tk.Label(self.sala_individual, text=f'{nntelaretratil} telas retratil', font='Inter 17',
                                    bg='#F5F5F5')
            self.nroTela.place(relx=0.16, rely=0.55)

            self.iconeProjetor = tk.PhotoImage(file=r'..\ProjetoFinal\projetor.png')
            self.label_iconeProjetor = tk.Label(self.sala_individual, image=self.iconeProjetor, bg='#F5F5F5')
            self.label_iconeProjetor.place(relx=0.11, rely=0.60)
            self.nroProjetor = tk.Label(self.sala_individual, text=f'{nnprojetor} projetores', font='Inter 17',
                                        bg='#F5F5F5')
            self.nroProjetor.place(relx=0.16, rely=0.60)

            self.iconeQuadro = tk.PhotoImage(file=r'..\ProjetoFinal\quadro.png')
            self.label_iconeQuadro = tk.Label(self.sala_individual, image=self.iconeQuadro, bg='#F5F5F5')
            self.label_iconeQuadro.place(relx=0.11, rely=0.65)
            self.nroQuadro = tk.Label(self.sala_individual, text=f'{nnquadro} quadro', font='Inter 17', bg='#F5F5F5')
            self.nroQuadro.place(relx=0.16, rely=0.65)

            self.iconeArCondicionado = tk.PhotoImage(file=r'..\ProjetoFinal\ar condicionado.png')
            self.label_iconeArCondicionado = tk.Label(self.sala_individual, image=self.iconeArCondicionado,
                                                      bg='#F5F5F5')
            self.label_iconeArCondicionado.place(relx=0.11, rely=0.60)
            self.nroArCondicionado = tk.Label(self.sala_individual, text=f'{nnarcondicionado} ar-condicionado',
                                              font='Inter 17', bg='#F5F5F5')
            self.nroArCondicionado.place(relx=0.16, rely=0.60)

            self.sinalDispManhaSala = tk.Label(self.sala_individual, text='', width=3, height=1, bg='#F5F5F5')
            self.dispManhaSala = tk.Label(self.sala_individual, text='Manhã', font='Inter 15', bg='#F5F5F5')
            self.sinalDispManhaSala.place(relx=0.63, rely=0.305)
            self.dispManhaSala.place(relx=0.65, rely=0.305)
            self.sinalDispTardeSala = tk.Label(self.sala_individual, text='', width=3, height=1, bg='#F5F5F5')
            self.dispTardeSala = tk.Label(self.sala_individual, text='Tarde', font='Inter 15', bg='#F5F5F5')
            self.sinalDispTardeSala.place(relx=0.63, rely=0.35)
            self.dispTardeSala.place(relx=0.65, rely=0.347)
            self.sinalDispNoiteSala = tk.Label(self.sala_individual, text='', width=3, height=1, bg='#F5F5F5')
            self.dispNoiteSala = tk.Label(self.sala_individual, text='Noite', font='Inter 15', bg='#F5F5F5')
            self.sinalDispNoiteSala.place(relx=0.63, rely=0.395)
            self.dispNoiteSala.place(relx=0.651, rely=0.39)

            if nnmanha == 1:
                self.sinalDispManhaSala.config(bg='red')
            if nntarde == 1:
                self.sinalDispTardeSala.config(bg='red')
            if nnnoite == 1:
                self.sinalDispNoiteSala.config(bg='red')
            if nnmanha == 0:
                self.sinalDispManhaSala.config(bg='green')
            if nntarde == 0:
                self.sinalDispTardeSala.config(bg='green')
            if nnnoite == 0:
                self.sinalDispNoiteSala.config(bg='green')

            self.label_inferior = tk.Label(self.sala_individual, bg='#004AAD', height=95)
            self.label_inferior.place(relx=0, relwidth=1, rely=0.92, relheight=0.08)

            self.icone_editar = tk.PhotoImage(file=r'..\ProjetoFinal\editar.png')
            self.label_icone_editar = tk.Label(self.sala_individual, image=self.icone_editar, bg='#F5F5F5')
            self.label_icone_editar.place(relx=0.73, rely=0.85)
            self.btn_editar = tk.Button(self.sala_individual, text='Editar',
                                        font='Inter 13', relief=FLAT,bg='#F5F5F5',
                                        fg='black', width=6, command=lambda: self.editar_sala())
            self.btn_editar.place(relx=0.75, rely=0.85)

            self.icone_excluir = tk.PhotoImage(file=r'..\ProjetoFinal\lixeira.png')
            self.label_icone_excluir = tk.Label(self.sala_individual, image=self.icone_excluir, bg='#F5F5F5')
            self.label_icone_excluir.place(relx=0.81, rely=0.85)
            self.btn_excluir = tk.Button(self.sala_individual, text='Excluir',
                                         font='Inter 13', bg='#F5F5F5',
                                         fg='red', width=6, relief=FLAT, command=lambda: self.excluir_sala())
            self.btn_excluir.place(relx=0.83, rely=0.85)

        def editar_sala(self):
            telaEditarSala()

        def excluir_sala(self):
            pass

    sala_individual = tk.Toplevel()
    objetoSalasGeral = TelaSala(sala_individual)
    sala_individual.mainloop()
