from tkinter import *
import tkinter as tk
from tkinter import ttk
from telaCadastrarProfessor import telaCadastrarProfessores


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
            self.caixa_selecao_area_conhecimento.place(relx=0.17, relwidth=0.2, rely=0.285)

            # botão
            self.botao_cadastrar_novo_professor = tk.Button(self.professores, text='Cadastrar novo professor',
                                                            font='Inter 17 bold', fg='white', bg='#F59714', relief=FLAT,
                                                            command=lambda: self.cadastrar_professores())
            self.botao_cadastrar_novo_professor.place(relx=0.7, rely=0.2)

        def selecionar(self):
            pass

        def cadastrar_professores(self):
            telaCadastrarProfessores()

    janela_professores_geral = tk.Toplevel()
    objetoProfessoresGeral = TelaProfessores(janela_professores_geral)
    janela_professores_geral.mainloop()

