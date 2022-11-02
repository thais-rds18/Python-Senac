from tkinter import *
import tkinter as tk
from tkinter import ttk
from telaCadastrarSala import telaCadastrarSalas


def telaSalas():
    class TelaSalas:
        def __init__(self, janela_salas_geral):
            self.telaSalasGeral = janela_salas_geral
            self.telaSalasGeral.title('Salas')
            self.telaSalasGeral.iconbitmap('icone.ico')
            self.telaSalasGeral.geometry('1440x750+50+10')
            self.telaSalasGeral.resizable(width=False, height=False)

            self.header = tk.Frame(self.telaSalasGeral, bg='#004AAD', height=95)
            self.header.place(relx=0, relwidth=1, rely=0, relheight=0.08)
            self.footer = tk.Frame(self.telaSalasGeral, bg='#004AAD', height=95)
            self.footer.place(relx=0, relwidth=1, rely=0.92, relheight=0.08)

            self.logo = tk.PhotoImage(file=r'..\ProjetoFinal\logo_simbolo.png')
            self.rotuloLogo = tk.Label(self.telaSalasGeral, image=self.logo)
            self.rotuloLogo.place(relx=0.025, rely=0.09)

            self.titulo = tk.Label(self.telaSalasGeral, text='Salas', font='Inter 28 bold')
            self.titulo.place(relx=0.115, rely=0.095)

            self.botaoCadastro = tk.Button(self.telaSalasGeral, bg='#F59714', text='Cadastrar nova sala', relief='flat',
                                           font='Inter 16 bold', fg='#F5F5F5', height=1, width=20,command=lambda: telaCadastrarSalas())
            self.botaoCadastro.place(relx=0.75, relwidth=0.22, rely=0.15)

            self.filtro = tk.PhotoImage(file=r'..\ProjetoFinal\filtro.png')
            self.rotuloFiltro = tk.Label(self.telaSalasGeral, image=self.filtro)
            self.rotuloFiltro.place(relx=0.025, rely=0.2)
            self.textoFiltro = tk.Label(self.telaSalasGeral, text='Filtrar', font='Inter 20')
            self.textoFiltro.place(relx=0.07, rely=0.21)
            self.lateralFiltro = tk.Frame(self.telaSalasGeral, relief='solid', borderwidth=0.5, width=250, height=350)
            self.lateralFiltro.place(relx=0.025, relwidth=0.2, rely=0.29, relheight=0.6)

            self.rotuloCadeira = tk.Label(self.telaSalasGeral, text='Cadeiras (mín.):', font='Inter 12')
            self.rotuloCadeira.place(relx=0.035, rely=0.315)
            self.campoCadeira = tk.Entry(self.telaSalasGeral, width=10)
            self.campoCadeira.place(relx=0.145, rely=0.318)

            self.rotuloMesa = tk.Label(self.telaSalasGeral, text='Mesas (mín.):', font='Inter 12')
            self.rotuloMesa.place(relx=0.035, rely=0.365)
            self.campoMesa = tk.Entry(self.telaSalasGeral, width=10)
            self.campoMesa.place(relx=0.145, rely=0.368)

            self.rotuloPC = tk.Label(self.telaSalasGeral, text='PCs (mín.):', font='Inter 12')
            self.rotuloPC.place(relx=0.035, rely=0.410)
            self.campoPC = tk.Entry(self.telaSalasGeral, width=10)
            self.campoPC.place(relx=0.145, rely=0.413)

            self.rotuloProjetor = tk.Label(self.telaSalasGeral, text='Projetores (mín.):', font='Inter 12')
            self.rotuloProjetor.place(relx=0.035, rely=0.460)
            self.campoProjetor = tk.Entry(self.telaSalasGeral, width=10)
            self.campoProjetor.place(relx=0.145, rely=0.463)

            self.rotuloTelevisor = tk.Label(self.telaSalasGeral, text='Televisores (mín.):', font='Inter 12')
            self.rotuloTelevisor.place(relx=0.035, rely=0.510)
            self.campoTelevisor = tk.Entry(self.telaSalasGeral, width=10)
            self.campoTelevisor.place(relx=0.145, rely=0.513)

            self.rotuloQuadro = tk.Label(self.telaSalasGeral, text='Quadros (mín.):', font='Inter 12')
            self.rotuloQuadro.place(relx=0.035, rely=0.560)
            self.campoQuadro = tk.Entry(self.telaSalasGeral, width=10)
            self.campoQuadro.place(relx=0.145, rely=0.563)

            self.rotuloTela = tk.Label(self.telaSalasGeral, text='Tela retrátil (mín.):', font='Inter 12')
            self.rotuloTela.place(relx=0.035, rely=0.610)
            self.campoTela = tk.Entry(self.telaSalasGeral, width=10)
            self.campoTela.place(relx=0.145, rely=0.613)

            self.rotuloAr = tk.Label(self.telaSalasGeral, text='Ar-condic. (mín.):', font='Inter 12')
            self.rotuloAr.place(relx=0.035, rely=0.660)
            self.campoAr = tk.Entry(self.telaSalasGeral, width=10)
            self.campoAr.place(relx=0.145, rely=0.663)

            self.rotuloDisponivel = tk.Label(self.telaSalasGeral, text='Disponivel em: ', font='Inter 12')
            self.rotuloDisponivel.place(relx=0.035, rely=0.710)
            self.caixaSelecao = ttk.Combobox(self.telaSalasGeral, values=['Manhã', 'Tarde', 'Noite'], width=10)
            self.caixaSelecao.current()
            self.caixaSelecao.bind("<<ComboboxSelected>>", self.selecionar)
            self.caixaSelecao.place(relx=0.145, rely=0.713)

            self.pesquisar = tk.Button(self.telaSalasGeral, text='Pesquisar', font='Inter 12 bold', fg='white', bg='#004AAD')
            self.pesquisar.place(relx=0.08, rely=0.8)

            # Teste para exibição das salas

            self.frameSalas1 = tk.Frame(self.telaSalasGeral, relief='solid', borderwidth=0.5, width=250, height=350)
            self.frameSalas1.place(relx=0.32, relwidth=0.65, rely=0.29, relheight=0.15)
            self.rotuloSala1 = tk.Label(self.telaSalasGeral, text='Sala 1', font='Inter 19 bold')
            self.rotuloSala1.place(relx=0.35, rely=0.30)
            self.obsSala1 = tk.Label(self.telaSalasGeral, text='Obs: Todos Intel Core i7', font='Inter 15')
            self.obsSala1.place(relx=0.35, rely=0.35)
            self.nroPCsSala1 = tk.Label(self.telaSalasGeral, text='20', font='Inter 15')
            self.nroPCsSala1.place(relx=0.35, rely=0.39)
            self.nroCadeirasSala1 = tk.Label(self.telaSalasGeral, text='20', font='Inter 15')
            self.nroCadeirasSala1.place(relx=0.40, rely=0.39)
            self.andarpoloSala1 = tk.Label(self.telaSalasGeral, text='4º andar, Recife Sede', font='Inter 16')
            self.andarpoloSala1.place(relx=0.45, rely=0.305)
            self.dispManhaSala1 = tk.Label(self.telaSalasGeral, text='Manhã', font='Inter 15')
            self.dispManhaSala1.place(relx=0.75, rely=0.305)
            self.dispTardeSala1 = tk.Label(self.telaSalasGeral, text='Tarde', font='Inter 15')
            self.dispTardeSala1.place(relx=0.75, rely=0.35)
            self.dispNoiteSala1 = tk.Label(self.telaSalasGeral, text='Noite', font='Inter 15')
            self.dispNoiteSala1.place(relx=0.751, rely=0.39)

            self.frameSalas2 = tk.Frame(self.telaSalasGeral, relief='solid', borderwidth=0.5, width=250, height=350)
            self.frameSalas2.place(relx=0.32, relwidth=0.65, rely=0.46, relheight=0.15)
            self.rotuloSala2 = tk.Label(self.telaSalasGeral, text='Sala 2', font='Inter 19 bold')
            self.rotuloSala2.place(relx=0.35, rely=0.47)
            self.obsSala2 = tk.Label(self.telaSalasGeral, text='Obs: Todos Intel Core i5', font='Inter 15')
            self.obsSala2.place(relx=0.35, rely=0.52)
            self.nroPCsSala2 = tk.Label(self.telaSalasGeral, text='20', font='Inter 15')
            self.nroPCsSala2.place(relx=0.35, rely=0.56)
            self.nroCadeirasSala2 = tk.Label(self.telaSalasGeral, text='20', font='Inter 15')
            self.nroCadeirasSala2.place(relx=0.40, rely=0.56)
            self.andarpoloSala2 = tk.Label(self.telaSalasGeral, text='5º andar, Recife Sede', font='Inter 16')
            self.andarpoloSala2.place(relx=0.45, rely=0.475)
            self.dispManhaSala2 = tk.Label(self.telaSalasGeral, text='Manhã', font='Inter 15')
            self.dispManhaSala2.place(relx=0.75, rely=0.475)
            self.dispTardeSala2 = tk.Label(self.telaSalasGeral, text='Tarde', font='Inter 15')
            self.dispTardeSala2.place(relx=0.75, rely=0.52)
            self.dispNoiteSala2 = tk.Label(self.telaSalasGeral, text='Noite', font='Inter 15')
            self.dispNoiteSala2.place(relx=0.751, rely=0.56)

            self.frameSalas3 = tk.Frame(self.telaSalasGeral, relief='solid', borderwidth=0.5, width=250, height=350)
            self.frameSalas3.place(relx=0.32, relwidth=0.65, rely=0.63, relheight=0.15)
            self.rotuloSala3 = tk.Label(self.telaSalasGeral, text='Sala 2', font='Inter 19 bold')
            self.rotuloSala3.place(relx=0.35, rely=0.64)
            self.obsSala3 = tk.Label(self.telaSalasGeral, text='Obs: Todos Intel Core i5', font='Inter 15')
            self.obsSala3.place(relx=0.35, rely=0.69)
            self.nroPCsSala3 = tk.Label(self.telaSalasGeral, text='20', font='Inter 15')
            self.nroPCsSala3.place(relx=0.35, rely=0.73)
            self.nroCadeirasSala3 = tk.Label(self.telaSalasGeral, text='20', font='Inter 15')
            self.nroCadeirasSala3.place(relx=0.40, rely=0.73)
            self.andarpoloSala3 = tk.Label(self.telaSalasGeral, text='5º andar, Recife Sede', font='Inter 16')
            self.andarpoloSala3.place(relx=0.45, rely=0.645)
            self.dispManhaSala3 = tk.Label(self.telaSalasGeral, text='Manhã', font='Inter 15')
            self.dispManhaSala3.place(relx=0.75, rely=0.645)
            self.dispTardeSala3 = tk.Label(self.telaSalasGeral, text='Tarde', font='Inter 15')
            self.dispTardeSala3.place(relx=0.75, rely=0.69)
            self.dispNoiteSala3 = tk.Label(self.telaSalasGeral, text='Noite', font='Inter 15')
            self.dispNoiteSala3.place(relx=0.751, rely=0.73)

            # ----------------------------

        def selecionar(self):
            pass

        def pesquisar(self):
            pass


    janela_salas_geral = tk.Toplevel()
    objetoSalasGeral = TelaSalas(janela_salas_geral)
    janela_salas_geral.mainloop()


