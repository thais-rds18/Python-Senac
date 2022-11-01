from tkinter import *
import tkinter as tk
from tkinter import ttk


def telaEditarProfessores():
    class TelaEditarProfessores:
        def __init__(self, janela_professores_edicao):
            self.editar_professores = janela_professores_edicao
            self.editar_professores.title('Cadastrar Salas')  # Trocar o título da janela
            self.editar_professores.iconbitmap('icone.ico')  # Verificar se tem o ícone no seu arquivo
            self.editar_professores.geometry('1440x750+50+10')
            self.editar_professores['bg'] = '#F5F5F5'
            self.editar_professores.resizable(width=False, height=False)

            self.label_superior = tk.Label(self.editar_professores, bg='#004AAD')
            self.label_superior.place(relx=0, relwidth=1, relheight=0.08, rely=0)

            # Logo do senac
            self.senac_logo = tk.PhotoImage(file=r'..\ProjetoFinal\logo_simbolo.png')
            self.senac_tituloPag = tk.Label(self.editar_professores, text='Editar Professores',
                                            font='Inter 26 bold')
            self.label_senac_logo = tk.Label(self.editar_professores, image=self.senac_logo)
            self.label_senac_logo.place(relx=0.1, rely=0.13)
            self.senac_tituloPag.place(relx=0.19, rely=0.15)

            # Entradas

            self.nome_professor = tk.Label(self.editar_professores, bg='#F5F5F5', text='Nome:', font='Inter 17 bold',
                                           anchor='w')
            self.nome_professor.place(relx=0.16, relwidth=0.08, rely=0.33, relheight=0.035)
            self.entrada_nome_professor = tk.Entry(self.editar_professores, bg='#D9D9D9')
            self.entrada_nome_professor.place(relx=0.23, relwidth=0.588, rely=0.33, relheight=0.035)

            self.label_email = tk.Label(self.editar_professores, bg='#F5F5F5', text='E-mail:', font='Inter 17 bold',
                                        anchor='w')
            self.label_email.place(relx=0.16, relwidth=0.075, rely=0.4, relheight=0.035)
            self.entrada_email = tk.Entry(self.editar_professores, bg='#D9D9D9')
            self.entrada_email.place(relx=0.23, relwidth=0.25, rely=0.4, relheight=0.035)

            self.label_CPF = tk.Label(self.editar_professores, bg='#F5F5F5', text='CPF:', font='Inter 17 bold',
                                      anchor='w')
            self.label_CPF.place(relx=0.16, relwidth=0.12, rely=0.47, relheight=0.035)
            self.entrada_CPF = tk.Entry(self.editar_professores, bg='#D9D9D9')
            self.entrada_CPF.place(relx=0.23, relwidth=0.25, rely=0.47, relheight=0.035)

            self.label_fone = tk.Label(self.editar_professores, bg='#F5F5F5', text='Fone:', font='Inter 17 bold',
                                       anchor='w')
            self.label_fone.place(relx=0.515, relwidth=0.057, rely=0.4, relheight=0.035)
            self.entrada_fone = tk.Entry(self.editar_professores, bg='#D9D9D9')
            self.entrada_fone.place(relx=0.576, relwidth=0.239, rely=0.4, relheight=0.035)

            self.label_conhecimento = tk.Label(self.editar_professores, bg='#F5F5F5',
                                               text='Insira conhecimento do(a) professor(a):',
                                               font='Inter 17 bold', anchor='w')
            self.label_conhecimento.place(relx=0.16, relwidth=0.35, rely=0.54, relheight=0.035)
            self.entrada_conhecimento = tk.Entry(self.editar_professores, bg='#D9D9D9')
            self.entrada_conhecimento.place(relx=0.53, relwidth=0.286, rely=0.54, relheight=0.035)

            self.botao_pesquisar_cadastrar_professor = tk.Button(self.editar_professores, text='Pesquisar', fg='white',
                                                                 bg='#F59714', font='Inter 17 bold',
                                                                 relief=FLAT)
            self.botao_pesquisar_cadastrar_professor.place(relx=0.57, relwidth=0.12, rely=0.75, relheight=0.07)

            self.botao_cadastrar_cadastrar_professor = tk.Button(self.editar_professores, text='Editar',
                                                                 fg='white',
                                                                 bg='#004AAD', font='Inter 17 bold',
                                                                 relief=FLAT)
            self.botao_cadastrar_cadastrar_professor.place(relx=0.3, relwidth=0.12, rely=0.75, relheight=0.07)

            self.label_inferior = tk.Label(self.editar_professores, bg='#004AAD')
            self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)

        def editar(self):
            pass

    janela_professores_edicao = tk.Toplevel()
    objetoSalasGeral = TelaEditarProfessores(janela_professores_edicao)
    janela_professores_edicao.mainloop()
