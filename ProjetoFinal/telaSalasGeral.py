from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from sqlite3 import Error

from ProjetoFinal.telaCadastrarSala import telaCadastrarSalas
from ProjetoFinal.telaSala import telaSala


def telaSalas():
    class TelaSalas:
        def __init__(self, janela_salas_geral):
            self.busca_componentes = None
            self.pag = 1
            self.telaSalasGeral = janela_salas_geral
            self.telaSalasGeral.title('Salas')
            self.telaSalasGeral.iconbitmap('icone.ico')
            self.telaSalasGeral.geometry('1440x750+50+10')
            self.telaSalasGeral['bg'] = '#F5F5F5'
            self.telaSalasGeral.resizable(width=False, height=False)

            self.header = tk.Frame(self.telaSalasGeral, bg='#004AAD', height=95)
            self.header.place(relx=0, relwidth=1, rely=0, relheight=0.08)
            self.footer = tk.Frame(self.telaSalasGeral, bg='#004AAD', height=95)
            self.footer.place(relx=0, relwidth=1, rely=0.92, relheight=0.08)

            self.logo = tk.PhotoImage(file=r'..\ProjetoFinal\logo_simbolo.png')
            self.rotuloLogo = tk.Label(self.telaSalasGeral, image=self.logo, bg='#F5F5F5')
            self.rotuloLogo.place(relx=0.025, rely=0.09)

            self.titulo = tk.Label(self.telaSalasGeral, text='Salas', font='Inter 28 bold', bg='#F5F5F5')
            self.titulo.place(relx=0.115, rely=0.095)

            self.botaoCadastro = tk.Button(self.telaSalasGeral, bg='#F59714', text='Cadastrar nova sala', relief='flat',
                                           font='Inter 16 bold', fg='#F5F5F5', height=1, width=20, command= lambda: telaCadastrarSalas())
            self.botaoCadastro.place(relx=0.75, relwidth=0.22, rely=0.15)

            self.filtro = tk.PhotoImage(file=r'..\ProjetoFinal\filtro.png')
            self.rotuloFiltro = tk.Label(self.telaSalasGeral, image=self.filtro, bg='#F5F5F5')
            self.rotuloFiltro.place(relx=0.025, rely=0.2)
            self.textoFiltro = tk.Label(self.telaSalasGeral, text='Filtrar', font='Inter 20', bg='#F5F5F5')
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
            self.caixaSelecao.bind("<<ComboboxSelected>>")
            self.caixaSelecao.place(relx=0.145, rely=0.713)

            self.pesquisar = tk.Button(self.telaSalasGeral, text='Pesquisar', font='Inter 12 bold', fg='white',
                                       bg='#004AAD', command=self.pesquisar)
            self.pesquisar.place(relx=0.08, rely=0.8)

            # resultado sala 1

            self.frameSalas1 = tk.Frame(self.telaSalasGeral, relief='solid', borderwidth=0.5, width=250, height=350)
            self.frameSalas1.place(relx=0.32, relwidth=0.65, rely=0.29, relheight=0.15)
            self.botaoSala1 = tk.Button(self.telaSalasGeral)
            self.rotuloSala1 = tk.Label(self.telaSalasGeral, text='', font='Inter 19 bold')
            self.rotuloSala1.place(relx=0.35, rely=0.30)
            self.obsSala1 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.obsSala1.place(relx=0.35, rely=0.35)
            self.iconePcs1 = tk.PhotoImage(file=r'..\ProjetoFinal\computador.png')
            self.label_iconePcs1 = tk.Label(self.telaSalasGeral, image=self.iconePcs1)
            self.label_iconePcs1.place(relx=0.35, rely=0.39)
            self.nroPCsSala1 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.nroPCsSala1.place(relx=0.38, rely=0.39)
            self.iconePessoas1 = tk.PhotoImage(file=r'..\ProjetoFinal\pessoas2.png')
            self.label_iconePessoas1 = tk.Label(self.telaSalasGeral, image=self.iconePessoas1)
            self.label_iconePessoas1.place(relx=0.45, rely=0.39)
            self.nroCadeirasSala1 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.nroCadeirasSala1.place(relx=0.47, rely=0.39)
            self.andarpoloSala1 = tk.Label(self.telaSalasGeral, text='', font='Inter 16')
            self.andarpoloSala1.place(relx=0.45, rely=0.305)

            self.sinalDispManhaSala1 = tk.Label(self.telaSalasGeral, text='', width=3, height=1)
            self.dispManhaSala1 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.sinalDispManhaSala1.place(relx=0.73, rely=0.305)
            self.dispManhaSala1.place(relx=0.75, rely=0.305)
            self.sinalDispTardeSala1 = tk.Label(self.telaSalasGeral, text='', width=3, height=1)
            self.dispTardeSala1 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.sinalDispTardeSala1.place(relx=0.73, rely=0.35)
            self.dispTardeSala1.place(relx=0.75, rely=0.347)
            self.sinalDispNoiteSala1 = tk.Label(self.telaSalasGeral, text='', width=3, height=1)
            self.dispNoiteSala1 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.sinalDispNoiteSala1.place(relx=0.73, rely=0.395)
            self.dispNoiteSala1.place(relx=0.751, rely=0.39)

            # resultado sala 2

            self.frameSalas2 = tk.Frame(self.telaSalasGeral, relief='solid', borderwidth=0.5, width=250, height=350)
            self.frameSalas2.place(relx=0.32, relwidth=0.65, rely=0.46, relheight=0.15)
            self.botaoSala2 = tk.Button(self.telaSalasGeral)
            self.rotuloSala2 = tk.Label(self.telaSalasGeral, text='', font='Inter 19 bold')
            self.rotuloSala2.place(relx=0.35, rely=0.47)
            self.obsSala2 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.obsSala2.place(relx=0.35, rely=0.52)
            self.iconePcs2 = tk.PhotoImage(file=r'..\ProjetoFinal\computador.png')
            self.label_iconePcs2 = tk.Label(self.telaSalasGeral, image=self.iconePcs2)
            self.label_iconePcs2.place(relx=0.35, rely=0.56)
            self.nroPCsSala2 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.nroPCsSala2.place(relx=0.38, rely=0.56)
            self.iconePessoas2 = tk.PhotoImage(file=r'..\ProjetoFinal\pessoas2.png')
            self.label_iconePessoas2 = tk.Label(self.telaSalasGeral, image=self.iconePessoas2)
            self.label_iconePessoas2.place(relx=0.45, rely=0.56)
            self.nroCadeirasSala2 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.nroCadeirasSala2.place(relx=0.47, rely=0.56)
            self.andarpoloSala2 = tk.Label(self.telaSalasGeral, text='', font='Inter 16')
            self.andarpoloSala2.place(relx=0.45, rely=0.475)

            self.sinalDispManhaSala2 = tk.Label(self.telaSalasGeral, text='', width=3, height=1)
            self.dispManhaSala2 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.sinalDispManhaSala2.place(relx=0.73, rely=0.475)
            self.dispManhaSala2.place(relx=0.75, rely=0.475)
            self.sinalDispTardeSala2 = tk.Label(self.telaSalasGeral, text='', width=3, height=1)
            self.dispTardeSala2 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.sinalDispTardeSala2.place(relx=0.73, rely=0.52)
            self.dispTardeSala2.place(relx=0.75, rely=0.517)
            self.sinalDispNoiteSala2 = tk.Label(self.telaSalasGeral, text='', width=3, height=1)
            self.dispNoiteSala2 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.sinalDispNoiteSala2.place(relx=0.73, rely=0.565)
            self.dispNoiteSala2.place(relx=0.751, rely=0.56)

            # resultado sala 3

            self.frameSalas3 = tk.Frame(self.telaSalasGeral, relief='solid', borderwidth=0.5, width=250, height=350)
            self.frameSalas3.place(relx=0.32, relwidth=0.65, rely=0.63, relheight=0.15)
            self.botaoSala3 = tk.Button(self.telaSalasGeral)
            self.rotuloSala3 = tk.Label(self.telaSalasGeral, text='', font='Inter 19 bold')
            self.rotuloSala3.place(relx=0.35, rely=0.64)
            self.obsSala3 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.obsSala3.place(relx=0.35, rely=0.69)
            self.iconePcs3 = tk.PhotoImage(file=r'..\ProjetoFinal\computador.png')
            self.label_iconePcs3 = tk.Label(self.telaSalasGeral, image=self.iconePcs3)
            self.label_iconePcs3.place(relx=0.35, rely=0.73)
            self.nroPCsSala3 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.nroPCsSala3.place(relx=0.38, rely=0.73)
            self.iconePessoas3 = tk.PhotoImage(file=r'..\ProjetoFinal\pessoas2.png')
            self.label_iconePessoas3 = tk.Label(self.telaSalasGeral, image=self.iconePessoas3)
            self.label_iconePessoas3.place(relx=0.45, rely=0.73)
            self.nroCadeirasSala3 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.nroCadeirasSala3.place(relx=0.47, rely=0.73)
            self.andarpoloSala3 = tk.Label(self.telaSalasGeral, text='', font='Inter 16')
            self.andarpoloSala3.place(relx=0.45, rely=0.645)

            self.sinalDispManhaSala3 = tk.Label(self.telaSalasGeral, text='', width=3, height=1)
            self.dispManhaSala3 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.sinalDispManhaSala3.place(relx=0.73, rely=0.645)
            self.dispManhaSala3.place(relx=0.75, rely=0.645)
            self.sinalDispTardeSala3 = tk.Label(self.telaSalasGeral, text='', width=3, height=1)
            self.dispTardeSala3 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.sinalDispTardeSala3.place(relx=0.73, rely=0.69)
            self.dispTardeSala3.place(relx=0.75, rely=0.687)
            self.sinalDispNoiteSala3 = tk.Label(self.telaSalasGeral, text='', width=3, height=1)
            self.dispNoiteSala3 = tk.Label(self.telaSalasGeral, text='', font='Inter 15')
            self.sinalDispNoiteSala3.place(relx=0.73, rely=0.736)
            self.dispNoiteSala3.place(relx=0.751, rely=0.73)

            self.botaoProx = tk.Button(self.telaSalasGeral, text='>', command=lambda: self.exibir(salas, pag='>'))
            self.botaoProx.place(relx=0.63, relwidth=0.05, rely=0.79, relheight=0.05)
            self.botaoAnte = tk.Button(self.telaSalasGeral, text='<', command=lambda: self.exibir(salas, pag='<'))
            self.botaoAnte.place(relx=0.58, relwidth=0.05, rely=0.79, relheight=0.05)

            sql = 'SELECT * FROM salas order by nome'
            salas = comandosSQL(sql)
            self.exibir(salas)

        def exibir(self, salas, pag = 0):

            if self.busca_componentes != None:
                salas = self.busca_componentes
            if pag == '>':
                self.pag = self.pag + 1
            elif pag == '<':
                self.pag = self.pag - 1
            else:
                pass
            pag = self.pag
            # print(salas)
            if pag < 1:
                self.pag = 1
                pag = 1
            if pag != 1:
                self.limpar()
            if len(salas) < 1:
                pass
            else:
                contadorsala = 0
                salastemp = salas[((3 * pag) - 3):(3 * pag)]  # Isso pega os três resultados da pagina atual
                for v in salastemp:
                    nnsala = v[0]
                    nnpolo = v[1]
                    nnandar = v[2]
                    nncadeira = v[3]
                    nncomputador = v[4]
                    nntelevisor = v[5]
                    nntelaretratil = v[6]
                    nnprojetor = v[8]
                    nnquadro = v[9]
                    nnarcondicionado = v[10]
                    nnmanha = v[11]
                    nntarde = v[12]
                    nnnoite = v[13]
                    contadorsala += 1
                    if contadorsala == 1:
                        self.rotuloSala1.config(text=nnsala)
                        self.obsSala1.config(text='Nenhuma observacao inserida')
                        self.nroPCsSala1.config(text=nncomputador)
                        self.nroCadeirasSala1.config(text=nncadeira)
                        self.andarpoloSala1.config(text=f'{nnandar}, {nnpolo}')
                        self.dispManhaSala1.config(text='Manhã')
                        self.dispTardeSala1.config(text='Tarde')
                        self.dispNoiteSala1.config(text='Noite')

                        self.nnsala1 = nnsala
                        self.nnpolo1 = nnpolo
                        self.nnandar1 = nnandar
                        self.nncadeira1 = nncadeira
                        self.nncomputador1 = nncomputador
                        self.nntelevisor1 = nntelevisor
                        self.nntelaretratil1 = nntelaretratil
                        self.nnprojetor1 = nnprojetor
                        self.nnquadro1 = nnquadro
                        self.nnarcondicionado1 = nnarcondicionado
                        self.nnmanha1 = nnmanha
                        self.nntarde1 = nntarde
                        self.nnnoite1 = nnnoite

                        self.botaoSala1.configure(
                            command=lambda: telaSala(self.nnsala1, self.nnpolo1, self.nnandar1, self.nncadeira1,
                                                     self.nncomputador1, self.nntelevisor1, self.nntelaretratil1,
                                                     self.nnprojetor1, self.nnquadro1, self.nnarcondicionado1,
                                                     self.nnmanha1, self.nntarde1, self.nnnoite1))
                        self.botaoSala1.place(relx=0.321, relwidth=0.649, rely=0.291, relheight=0.148)

                        if nnmanha == 1:
                            self.sinalDispManhaSala1.config(bg='red')
                        if nntarde == 1:
                            self.sinalDispTardeSala1.config(bg='red')
                        if nnnoite == 1:
                            self.sinalDispNoiteSala1.config(bg='red')
                        if nnmanha == 0:
                            self.sinalDispManhaSala1.config(bg='green')
                        if nntarde == 0:
                            self.sinalDispTardeSala1.config(bg='green')
                        if nnnoite == 0:
                            self.sinalDispNoiteSala1.config(bg='green')


                    elif contadorsala == 2:
                        self.rotuloSala2.config(text=nnsala)
                        self.obsSala2.config(text='Nenhuma observacao inserida')
                        self.nroPCsSala2.config(text=nncomputador)
                        self.nroCadeirasSala2.config(text=nncadeira)
                        self.andarpoloSala2.config(text=f'{nnandar}, {nnpolo}')
                        self.dispManhaSala2.config(text='Manhã')
                        self.dispTardeSala2.config(text='Tarde')
                        self.dispNoiteSala2.config(text='Noite')

                        self.nnsala2 = nnsala
                        self.nnpolo2 = nnpolo
                        self.nnandar2 = nnandar
                        self.nncadeira2 = nncadeira
                        self.nncomputador2 = nncomputador
                        self.nntelevisor2 = nntelevisor
                        self.nntelaretratil2 = nntelaretratil
                        self.nnprojetor2 = nnprojetor
                        self.nnquadro2 = nnquadro
                        self.nnarcondicionado2 = nnarcondicionado
                        self.nnmanha2 = nnmanha
                        self.nntarde2 = nntarde
                        self.nnnoite2 = nnnoite

                        self.botaoSala2.configure(
                            command=lambda: telaSala(self.nnsala2, self.nnpolo2, self.nnandar2, self.nncadeira2,
                                                     self.nncomputador2, self.nntelevisor2, self.nntelaretratil2,
                                                     self.nnprojetor2, self.nnquadro2, self.nnarcondicionado2,
                                                     self.nnmanha2, self.nntarde2, self.nnnoite2))
                        self.botaoSala2.place(relx=0.321, relwidth=0.649, rely=0.461, relheight=0.148)


                        if nnmanha == 1:
                            self.sinalDispManhaSala2.config(bg='red')
                        if nntarde == 1:
                            self.sinalDispTardeSala2.config(bg='red')
                        if nnnoite == 1:
                            self.sinalDispNoiteSala2.config(bg='red')
                        if nnmanha == 0:
                            self.sinalDispManhaSala2.config(bg='green')
                        if nntarde == 0:
                            self.sinalDispTardeSala2.config(bg='green')
                        if nnnoite == 0:
                            self.sinalDispNoiteSala2.config(bg='green')

                    elif contadorsala == 3:
                        self.rotuloSala3.config(text=nnsala)
                        self.obsSala3.config(text='Nenhuma observacao inserida')
                        self.nroPCsSala3.config(text=nncomputador)
                        self.nroCadeirasSala3.config(text=nncadeira)
                        self.andarpoloSala3.config(text=f'{nnandar}, {nnpolo}')
                        self.dispManhaSala3.config(text='Manhã')
                        self.dispTardeSala3.config(text='Tarde')
                        self.dispNoiteSala3.config(text='Noite')

                        self.nnsala3 = nnsala
                        self.nnpolo3 = nnpolo
                        self.nnandar3 = nnandar
                        self.nncadeira3 = nncadeira
                        self.nncomputador3 = nncomputador
                        self.nntelevisor3 = nntelevisor
                        self.nntelaretratil3 = nntelaretratil
                        self.nnprojetor3 = nnprojetor
                        self.nnquadro3 = nnquadro
                        self.nnarcondicionado3 = nnarcondicionado
                        self.nnmanha3 = nnmanha
                        self.nntarde3 = nntarde
                        self.nnnoite3 = nnnoite

                        self.botaoSala3.configure(
                            command=lambda: telaSala(self.nnsala3, self.nnpolo3, self.nnandar3, self.nncadeira3,
                                                     self.nncomputador3, self.nntelevisor3, self.nntelaretratil3,
                                                     self.nnprojetor3, self.nnquadro3, self.nnarcondicionado3,
                                                     self.nnmanha3, self.nntarde3, self.nnnoite3))
                        self.botaoSala3.place(relx=0.321, relwidth=0.649, rely=0.632, relheight=0.148)


                        if nnmanha == 1:
                            self.sinalDispManhaSala3.config(bg='red')
                        if nntarde == 1:
                            self.sinalDispTardeSala3.config(bg='red')
                        if nnnoite == 1:
                            self.sinalDispNoiteSala3.config(bg='red')
                        if nnmanha == 0:
                            self.sinalDispManhaSala3.config(bg='green')
                        if nntarde == 0:
                            self.sinalDispTardeSala3.config(bg='green')
                        if nnnoite == 0:
                            self.sinalDispNoiteSala3.config(bg='green')

            # ----------------------------

        def pesquisar(self):
            cod = ''
            cadeiras = self.campoCadeira.get()
            mesas = self.campoMesa.get()
            pcs = self.campoPC.get()
            projetor = self.campoProjetor.get()
            televisor = self.campoTelevisor.get()
            quadro = self.campoQuadro.get()
            tela = self.campoTela.get()
            ar = self.campoAr.get()
            turno = self.horarioDisponivel(cod)

            if self.campoCadeira.get() == '':
                cadeiras = 0
            if self.campoMesa.get() == '':
                mesas = 0
            if self.campoPC.get() == '':
                pcs = 0
            if self.campoProjetor.get() == '':
                projetor = 0
            if self.campoTelevisor.get() == '':
                televisor = 0
            if self.campoQuadro.get() == '':
                quadro = 0
            if self.campoTela.get() == '':
                tela = 0
            if self.campoAr.get() == '':
                ar = 0
            if turno == 0 or turno == '':
                turno = ''

            sql = f'SELECT * FROM salas WHERE cadeiras>={cadeiras} AND mesas>={mesas} AND computadores>={pcs} AND televisores>={televisor} AND tela_retratil>={tela} AND projetores>={projetor} AND quadros>={quadro} AND ar_condicionado>={ar} {turno};'
            salas = comandosSQL(sql)
            print(comandosSQL(sql))
            self.limpar()
            componentes = str(cadeiras) + str(mesas) + str(pcs) + str(projetor) + str(televisor) + str(quadro) + str(
                tela) + str(ar) + str(turno)
            print(componentes, type(componentes))
            if componentes == 0:
                self.busca_componentes = None
            else:
                self.busca_componentes = salas
            self.exibir(salas)

        def horarioDisponivel(self, cod):
            if self.caixaSelecao.get() == 'Manhã':
                cod = 'AND ocupado_manha = 0'
            elif self.caixaSelecao.get() == 'Tarde':
                cod = 'AND ocupado_tarde = 0'
            elif self.caixaSelecao.get() == 'Noite':
                cod = 'AND ocupado_noite = 0'
            return cod

        def limpar(self):
            self.rotuloSala1.config(text='')
            self.obsSala1.config(text='')
            self.nroPCsSala1.config(text='')
            self.nroCadeirasSala1.config(text='')
            self.andarpoloSala1.config(text='')
            self.dispManhaSala1.config(text='')
            self.dispTardeSala1.config(text='')
            self.dispNoiteSala1.config(text='')
            self.sinalDispManhaSala1.config(bg='#F5F5F5')
            self.sinalDispTardeSala1.config(bg='#F5F5F5')
            self.sinalDispNoiteSala1.config(bg='#F5F5F5')

            self.rotuloSala2.config(text='')
            self.obsSala2.config(text='')
            self.nroPCsSala2.config(text='')
            self.nroCadeirasSala2.config(text='')
            self.andarpoloSala2.config(text='')
            self.dispManhaSala2.config(text='')
            self.dispTardeSala2.config(text='')
            self.dispNoiteSala2.config(text='')
            self.sinalDispManhaSala2.config(bg='#F5F5F5')
            self.sinalDispTardeSala2.config(bg='#F5F5F5')
            self.sinalDispNoiteSala2.config(bg='#F5F5F5')

            self.rotuloSala3.config(text='')
            self.obsSala3.config(text='')
            self.nroPCsSala3.config(text='')
            self.nroCadeirasSala3.config(text='')
            self.andarpoloSala3.config(text='')
            self.dispManhaSala3.config(text='')
            self.dispTardeSala3.config(text='')
            self.dispNoiteSala3.config(text='')
            self.sinalDispManhaSala3.config(bg='#F5F5F5')
            self.sinalDispTardeSala3.config(bg='#F5F5F5')
            self.sinalDispNoiteSala3.config(bg='#F5F5F5')

    def conexaoBanco():
        caminho = 'Modelo Banco de dados\\bancoDedados.db'
        conexao = None

        try:
            conexao = sqlite3.connect(caminho)
            print('Conexao aceita')
        except Error as ex:
            print('Erro de conexão:', ex)
        return conexao

    def comandosSQL(sql):
        c = conexao.cursor()
        c.execute(sql)
        return c.fetchall()

    conexao = conexaoBanco()
    janela_salas_geral = tk.Toplevel()
    objetoSalasGeral = TelaSalas(janela_salas_geral)
    janela_salas_geral.mainloop()
    conexao.close()

telaSalas()