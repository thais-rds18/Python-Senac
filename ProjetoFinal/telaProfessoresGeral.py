from tkinter import *
import tkinter as tk
from tkinter import ttk
from telaCadastrarProfessor import telaCadastrarProfessores
from teste import testeprofs


def telaProfessores():
    class TelaProfessores:
        def __init__(self, janela_professores_geral):
            self.professores = janela_professores_geral
            self.professores.title('Professores')
            self.professores.iconbitmap('icone.ico')
            self.professores.geometry('1440x750+50+10')
            self.professores['bg'] = '#F5F5F5'
            self.professores.resizable(width=False, height=False)

            # barra de rolagem
            self.barraLateral = tk.Scrollbar(self.professores, orient=VERTICAL)
            self.barraLateral.pack(side=RIGHT, fill=Y)

            # label azul cima e baixo
            self.label_cima = tk.Label(self.professores, bg='#004AAD')
            self.label_cima.place(relx=0, relwidth=1, relheight=0.08, rely=0)

            self.label_baixo = tk.Label(self.professores, bg='#004AAD')
            self.label_baixo.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)

            # Base da janela

            self.logo_senac = tk.PhotoImage(file='logo_simbolo.png')
            self.label_logo_senac = tk.Label(self.professores, image=self.logo_senac, bg='#F5F5F5', relief=FLAT)
            self.label_logo_senac.place(relx=0.025, rely=0.09)
            self.titulo_professores = tk.Label(self.professores, text='Professores', font='Inter 28 bold', bg='#F5F5F5')
            self.titulo_professores.place(relx=0.115, rely=0.095)

            # Filtros
            # checkbox
            self.checkbox_ordem_alfabetica = tk.Checkbutton(self.professores, text='Ordem alfabética', font='Inter 12',
                                                            bg='#F5F5F5')
            self.checkbox_ordem_alfabetica.place(relx=0.036, rely=0.225)
            self.caixa_selecao_area_conhecimento = ttk.Combobox(self.professores, values=[], width=10)

            # caixa de seleção
            self.imagem_filtro = tk.PhotoImage(file=r'..\ProjetoFinal\filtro2.png')
            self.label_imagem_filtro = tk.Label(self.professores, image=self.imagem_filtro, bg='#F5F5F5')
            self.label_imagem_filtro.place(relx=0.027, rely=0.27)

            self.label_area_conhecimento = tk.Label(self.professores, text='Área de conhecimento:', font='Inter 12',
                                                    bg='#F5F5F5')
            self.label_area_conhecimento.place(relx=0.0528, rely=0.285)

            self.caixa_selecao_area_conhecimento.current()
            self.caixa_selecao_area_conhecimento.bind("<<ComboboxSelected>>", self.selecionar())
            self.caixa_selecao_area_conhecimento.place(relx=0.027, relwidth=0.2, rely=0.33)

            # botão
            self.botao_cadastrar_novo_professor = tk.Button(self.professores, text='Cadastrar novo professor',
                                                            font='Inter 17 bold', fg='white', bg='#F59714', relief=FLAT,
                                                            command=lambda: self.cadastrar_professores())
            self.botao_cadastrar_novo_professor.place(relx=0.7, rely=0.2)

            # Teste para exibição das salas

            self.frameProf1 = tk.Frame(self.professores, relief='solid', borderwidth=0.5, width=250, height=350)
            self.frameProf1.place(relx=0.32, relwidth=0.65, rely=0.29, relheight=0.15)
            self.imgBotaoProf1 = tk.PhotoImage(file='botaosala.png')
            self.botaoProf1 = tk.Button(self.professores, image=self.imgBotaoProf1)
            # self.botaoProf1.place(relx=0.321, relwidth=0.649, rely=0.291, relheight=0.148)
            self.nomeProf1 = tk.Label(self.professores, text='', font='Inter 19 bold')
            self.nomeProf1.place(relx=0.35, rely=0.30)
            self.espProf1 = tk.Label(self.professores, text='', font='Inter 15')
            self.espProf1.place(relx=0.35, rely=0.35)
            self.foneProf1 = tk.Label(self.professores, text='', font='Inter 15')
            self.foneProf1.place(relx=0.35, rely=0.39)
            self.emailProf1 = tk.Label(self.professores, text='', font='Inter 15')
            self.emailProf1.place(relx=0.48, rely=0.39)
            self.cpfProf1 = tk.Label(self.professores, text='', font='Inter 16')
            self.cpfProf1.place(relx=0.45, rely=0.305)
            self.dispManhaProf1 = tk.Label(self.professores, text='', font='Inter 15')
            self.dispManhaProf1.place(relx=0.75, rely=0.305)
            self.dispTardeProf1 = tk.Label(self.professores, text='', font='Inter 15')
            self.dispTardeProf1.place(relx=0.75, rely=0.35)
            self.dispNoiteProf1 = tk.Label(self.professores, text='', font='Inter 15')
            self.dispNoiteProf1.place(relx=0.751, rely=0.39)

            self.frameProf2 = tk.Frame(self.professores, relief='solid', borderwidth=0.5, width=250, height=350)
            self.frameProf2.place(relx=0.32, relwidth=0.65, rely=0.46, relheight=0.15)
            self.imgBotaoProf2 = tk.PhotoImage(file='botaosala.png')
            self.botaoProf2 = tk.Button(self.professores, image=self.imgBotaoProf2)
            # self.botaoProf2.place(relx=0.321, relwidth=0.649, rely=0.461, relheight=0.148)
            self.nomeProf2 = tk.Label(self.professores, text='', font='Inter 19 bold')
            self.nomeProf2.place(relx=0.35, rely=0.47)
            self.espProf2 = tk.Label(self.professores, text='', font='Inter 15')
            self.espProf2.place(relx=0.35, rely=0.52)
            self.nroPCsProf2 = tk.Label(self.professores, text='', font='Inter 15')
            self.nroPCsProf2.place(relx=0.35, rely=0.56)
            self.emailProf2 = tk.Label(self.professores, text='', font='Inter 15')
            self.emailProf2.place(relx=0.48, rely=0.56)
            self.cpfProf2 = tk.Label(self.professores, text='', font='Inter 16')
            self.cpfProf2.place(relx=0.45, rely=0.475)
            self.dispManhaProf2 = tk.Label(self.professores, text='', font='Inter 15')
            self.dispManhaProf2.place(relx=0.75, rely=0.475)
            self.dispTardeProf2 = tk.Label(self.professores, text='', font='Inter 15')
            self.dispTardeProf2.place(relx=0.75, rely=0.52)
            self.dispNoiteProf2 = tk.Label(self.professores, text='', font='Inter 15')
            self.dispNoiteProf2.place(relx=0.751, rely=0.56)

            self.frameProf3 = tk.Frame(self.professores, relief='solid', borderwidth=0.5, width=250, height=350)
            self.frameProf3.place(relx=0.32, relwidth=0.65, rely=0.63, relheight=0.15)
            self.imgBotaoProf3 = tk.PhotoImage(file='botaosala.png')
            self.botaoProf3 = tk.Button(self.professores, image=self.imgBotaoProf3)
            # self.botaoProf3.place(relx=0.321, relwidth=0.649, rely=0.632, relheight=0.148)
            self.nomeProf3 = tk.Label(self.professores, text='', font='Inter 19 bold')
            self.nomeProf3.place(relx=0.35, rely=0.64)
            self.espProf3 = tk.Label(self.professores, text='', font='Inter 15')
            self.espProf3.place(relx=0.35, rely=0.69)
            self.nroPCsProf3 = tk.Label(self.professores, text='', font='Inter 15')
            self.nroPCsProf3.place(relx=0.35, rely=0.73)
            self.emailProf3 = tk.Label(self.professores, text='', font='Inter 15')
            self.emailProf3.place(relx=0.48, rely=0.73)
            self.cpfProf3 = tk.Label(self.professores, text='', font='Inter 16')
            self.cpfProf3.place(relx=0.45, rely=0.645)
            self.dispManhaProf3 = tk.Label(self.professores, text='', font='Inter 15')
            self.dispManhaProf3.place(relx=0.75, rely=0.645)
            self.dispTardeProf3 = tk.Label(self.professores, text='', font='Inter 15')
            self.dispTardeProf3.place(relx=0.75, rely=0.69)
            self.dispNoiteProf3 = tk.Label(self.professores, text='', font='Inter 15')
            self.dispNoiteProf3.place(relx=0.751, rely=0.73)

            profs = testeprofs()
            if len(profs) < 1:
                pass
            else:
                contadorprof = 0
                for v in profs.values():
                    nnnome = v[0]
                    nncpf = v[1]
                    nnemail = v[2]
                    nnfone = v[3]
                    nnesp = v[4]
                    contadorprof += 1
                    if contadorprof == 1:
                        self.nomeProf1.config(text=nnnome)
                        self.espProf1.config(text=nnesp)
                        self.foneProf1.config(text=nnfone)
                        self.emailProf1.config(text=nnemail)
                        self.cpfProf1.config(text=nncpf)
                        self.botaoProf1.place(relx=0.321, relwidth=0.649, rely=0.291, relheight=0.148)
                    elif contadorprof == 2:
                        self.nomeProf2.config(text=nnnome)
                        self.espProf2.config(text=nnesp)
                        self.foneProf2.config(text=nnfone)
                        self.emailProf2.config(text=nnemail)
                        self.cpfProf2.config(text=nncpf)
                        self.botaoSala2.place(relx=0.321, relwidth=0.649, rely=0.461, relheight=0.148)
                    elif contadorprof == 3:
                        self.nomeProf3.config(text=nnnome)
                        self.espProf3.config(text=nnesp)
                        self.foneProf3.config(text=nnfone)
                        self.emailProf3.config(text=nnemail)
                        self.cpfProf3.config(text=nncpf)
                        self.botaoSala3.place(relx=0.321, relwidth=0.649, rely=0.632, relheight=0.148)

            # ----------------------------

        def selecionar(self):
            pass

        def cadastrar_professores(self):
            telaCadastrarProfessores()

    janela_professores_geral = tk.Toplevel()
    objetoProfessoresGeral = TelaProfessores(janela_professores_geral)
    janela_professores_geral.mainloop()

