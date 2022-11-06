from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from sqlite3 import Error
from tkinter import messagebox


def telaCadastrarProfessores():
    class TelaCadastroProfessores:
        def __init__(self, janela_professores_cadastro, conexao):
            self.conexao = conexao
            self.cadastrar_professores = janela_professores_cadastro
            self.cadastrar_professores.title('Cadastrar Salas')  # Trocar o título da janela
            self.cadastrar_professores.iconbitmap('icone.ico')  # Verificar se tem o ícone no seu arquivo
            self.cadastrar_professores.geometry('890x650+300+10')
            self.cadastrar_professores['bg'] = '#F5F5F5'
            self.cadastrar_professores.resizable(width=False, height=False)

            self.label_superior = tk.Label(self.cadastrar_professores, bg='#004AAD')
            self.label_superior.place(relx=0, relwidth=1, relheight=0.08, rely=0)

            # Logo do senac
            self.senac_logo = tk.PhotoImage(file=r'..\ProjetoFinal\logo_simbolo.png')
            self.senac_tituloPag = tk.Label(self.cadastrar_professores, text='Cadastro Professores',
                                            font='Inter 26 bold', bg='#F5F5F5')
            self.label_senac_logo = tk.Label(self.cadastrar_professores, image=self.senac_logo, bg = '#F5F5F5')
            self.label_senac_logo.place(relx=0.05, rely=0.13)
            self.senac_tituloPag.place(relx=0.19, rely=0.15)

            # Entradas

            self.nome_professor = tk.Label(self.cadastrar_professores, bg='#F5F5F5', text='Nome:', font='Inter 17 bold',
                                           anchor='w')
            self.nome_professor.place(relx=0.1, relwidth=0.1, rely=0.33, relheight=0.040)
            self.entrada_nome_professor = tk.Entry(self.cadastrar_professores, bg='#D9D9D9')
            self.entrada_nome_professor.place(relx=0.20, relwidth=0.65, rely=0.33, relheight=0.040)

            self.label_email = tk.Label(self.cadastrar_professores, bg='#F5F5F5', text='E-mail:', font='Inter 17 bold',
                                        anchor='w')
            self.label_email.place(relx=0.1, relwidth=0.1, rely=0.41, relheight=0.04)
            self.entrada_email = tk.Entry(self.cadastrar_professores, bg='#D9D9D9')
            self.entrada_email.place(relx=0.20, relwidth=0.28, rely=0.41, relheight=0.04)

            self.label_CPF = tk.Label(self.cadastrar_professores, bg='#F5F5F5', text='CPF:', font='Inter 17 bold',
                                      anchor='w')
            self.label_CPF.place(relx=0.1, relwidth=0.1, rely=0.49, relheight=0.04)
            self.entrada_CPF = tk.Entry(self.cadastrar_professores, bg='#D9D9D9')
            self.entrada_CPF.place(relx=0.2, relwidth=0.28, rely=0.49, relheight=0.04)

            self.label_fone = tk.Label(self.cadastrar_professores, bg='#F5F5F5', text='Fone:', font='Inter 17 bold',
                                       anchor='w')
            self.label_fone.place(relx=0.49, relwidth=0.1, rely=0.41, relheight=0.04)
            self.entrada_fone = tk.Entry(self.cadastrar_professores, bg='#D9D9D9')
            self.entrada_fone.place(relx=0.57, relwidth=0.28, rely=0.41, relheight=0.04)

            self.label_conhecimento = tk.Label(self.cadastrar_professores, bg='#F5F5F5',
                                               text='Conhecimentos do(a) professor(a):',
                                               font='Inter 17 bold', anchor='w')
            self.label_conhecimento.place(relx=0.1, relwidth=0.5, rely=0.57, relheight=0.04)
            self.entrada_conhecimento = tk.Entry(self.cadastrar_professores, bg='#D9D9D9')
            self.entrada_conhecimento.place(relx=0.57, relwidth=0.286, rely=0.57, relheight=0.04)

            self.botao_cadastrar_cadastrar_professor = tk.Button(self.cadastrar_professores, text='Cadastrar',
                                                                 fg='white',
                                                                 bg='#004AAD', font='Inter 17 bold',
                                                                 relief=FLAT, command=lambda: self.cadastrarProf())
            self.botao_cadastrar_cadastrar_professor.place(relx=0.40, relwidth=0.15, rely=0.75, relheight=0.08)

            self.label_inferior = tk.Label(self.cadastrar_professores, bg='#004AAD')
            self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)

        def cadastrarProf(self):
            try:
                if self.entrada_nome_professor.get() == '' and self.entrada_CPF.get() == '' and self.entrada_email.get() and self.entrada_fone.get() and self.entrada_conhecimento.get():
                    messagebox.showerror('Atenção!', 'Preencha todos os campos!')
                else:
                    c = self.conexao.cursor()
                    sql = "INSERT INTO professor (nome, cpf, email, telefone, conhecimento) VALUES ('" + self.entrada_nome_professor.get() + "', '" + self.entrada_CPF.get() + "','" + self.entrada_email.get() + "', '" + self.entrada_fone.get() + "', '" + self.entrada_conhecimento.get() + "')"
                    c.execute(sql)
                    self.conexao.commit()
                    messagebox.showinfo('Caixa de Mensagem', 'Dados Inseridos com sucesso!')
            except Error as ex:
                print('Não inseriu', ex)

    # ------------------ Fora da Classe ------------------

    def conexaoBanco():
        caminho = 'Modelo Banco de dados\\bancoDedados.db'
        conexao = None
        try:
            conexao = sqlite3.connect(caminho)
            print('Conexao aceita')
        except Error as ex:
            print('Erro de conexão:', ex)
        return conexao

    janela_professores_cadastro = tk.Toplevel()
    conexao = conexaoBanco()
    objeto = TelaCadastroProfessores(janela_professores_cadastro, conexao)
    janela_professores_cadastro.mainloop()
    conexao.close()


