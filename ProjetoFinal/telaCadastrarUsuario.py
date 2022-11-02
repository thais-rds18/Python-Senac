from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
import sqlite3
from sqlite3 import Error
from tkinter import messagebox

class Janela_Cadastrar_Usuario:
    def __init__(self, janela, conexao):
        self.conexao = conexao
        self.janela_cadastrar_usuario = janela
        self.janela_cadastrar_usuario.title('Cadastrar Usuário')  # Trocar o título da janela
        # self.janela08.iconbitmap('icone.ico')  # Verificar se tem o ícone no seu arquivo
        self.janela_cadastrar_usuario.geometry('890x650+300+10')
        self.janela_cadastrar_usuario['bg'] = '#F5F5F5'
        self.janela_cadastrar_usuario.resizable(width=False, height=False)

        self.label_superior = tk.Label(self.janela_cadastrar_usuario, bg='#004AAD')
        self.label_superior.place(relx=0, relwidth=1, relheight=0.08, rely=0)

        self.senac_logo = tk.PhotoImage(file='logo_simbolo.png')
        self.label_senac_logo = tk.Label(self.janela_cadastrar_usuario, image=self.senac_logo, bg='#F5F5F5')
        self.label_senac_logo.place(relx=0.02, rely=0.09)

        self.label_Cadastro_usuario = tk.Label(self.janela_cadastrar_usuario, text='Cadastro Usuário', bg='#F5F5F5',
                                               font='Inter 28 bold')
        self.label_Cadastro_usuario.place(relx=0.15, relwidth=0.40, rely=0.08, relheight=0.15)

        self.label_usuario = tk.Label(self.janela_cadastrar_usuario, text='Nome:', font='Inter 17 bold', bg='#F5F5F5')
        self.label_usuario.place(relx=0.01, relwidth=0.10, rely=0.25, relheight=0.05)
        self.entrada_usuario = tk.Entry(self.janela_cadastrar_usuario, font='Inter 17', bg='#D9D9D9')
        self.entrada_usuario.place(relx=0.13, relwidth=0.75, rely=0.25, relheight=0.05)

        self.label_email = tk.Label(self.janela_cadastrar_usuario, text='E-mail:', font='Inter 17 bold', bg='#F5F5F5')
        self.label_email.place(relx=0.01, relwidth=0.10, rely=0.35, relheight=0.05)
        self.entrada_email = tk.Entry(self.janela_cadastrar_usuario, font='Inter 17',  bg='#D9D9D9')
        self.entrada_email.place(relx=0.13, relwidth=0.75, rely=0.35, relheight=0.05)

        self.label_cpf = tk.Label(self.janela_cadastrar_usuario, text='CPF:', font='Inter 17 bold', bg='#F5F5F5')
        self.label_cpf.place(relx=0.01, relwidth=0.07, rely=0.45, relheight=0.05)
        self.entrada_cpf = tk.Entry(self.janela_cadastrar_usuario, font='Inter 17', bg='#D9D9D9')
        self.entrada_cpf.place(relx=0.13, relwidth=0.35, rely=0.45, relheight=0.05)

        self.label_nascimento = tk.Label(self.janela_cadastrar_usuario, text='Data Nasc.:', font='Inter 17 bold', bg='#F5F5F5')
        self.label_nascimento.place(relx=0.50, relwidth=0.15, rely=0.45, relheight=0.05)
        self.entrada_nascimento = DateEntry(self.janela_cadastrar_usuario, locale='pt_BR', dateformat='DD/MM/YYYY', font='Inter 17', bg='#D9D9D9')
        self.entrada_nascimento.place(relx=0.67, relwidth=0.21, rely=0.45, relheight=0.05)

        self.label_senha = tk.Label(self.janela_cadastrar_usuario, text='Senha:', font='Inter 17 bold',
                                    bg='#F5F5F5')
        self.label_senha.place(relx=0.01, relwidth=0.10, rely=0.55, relheight=0.05)
        self.entrada_senha = tk.Entry(self.janela_cadastrar_usuario, font='Inter 17', bg='#D9D9D9')
        self.entrada_senha.place(relx=0.13, relwidth=0.75, rely=0.55, relheight=0.05)

        self.label_confirmar_senha = tk.Label(self.janela_cadastrar_usuario, text='Confirmar Senha:', font='Inter 17 bold',
                                    bg='#F5F5F5')
        self.label_confirmar_senha.place(relx=0.01, relwidth=0.23, rely=0.65, relheight=0.05)
        self.entrada_confirmar_senha = tk.Entry(self.janela_cadastrar_usuario, text='Inter 17', bg='#D9D9D9')
        self.entrada_confirmar_senha.place(relx=0.25, relwidth=0.63, rely=0.65, relheight=0.05)

        self.botao_cadastrar = tk.Button(self.janela_cadastrar_usuario, text='Cadastrar', font='Inter 17 bold', fg='white', bg='#004AAD', command=lambda: self.cadastrarUsuario())
        self.botao_cadastrar.place(relx=0.43, relwidth=0.15, rely=0.78, relheight=0.10)

        self.label_inferior = tk.Label(self.janela_cadastrar_usuario, bg='#004AAD')
        self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)


    def cadastrarUsuario(self):
        try:
            if self.entrada_usuario.get() and self.entrada_cpf.get() == '' and self.entrada_email.get() == '' and self.entrada_nascimento.get() == '' and self.entrada_senha.get() == '' and self.entrada_confirmar_senha.get() == '':
                messagebox.showerror('Atenção!', 'Preencha todos os campos!')
            else:
                c = self.conexao.cursor()
                sql = "INSERT INTO login (usuario, cpf, email, nascimento, senha, confirmar_senha) VALUES ( '" + self.entrada_usuario.get() + "', '" + self.entrada_cpf.get() + "','" + self.entrada_email.get()+ "', '" + self.entrada_nascimento.get() + "', '" + self.entrada_senha.get() + "', '" + self.entrada_confirmar_senha.get() + "')"
                c.execute(sql)
                self.conexao.commit()
                messagebox.showinfo('Caixa de Mensagem', 'Dados Inseridos com sucesso!')
        except Error as ex:
            print('Não inseriu', ex)



#------------------ Fora da Classe ------------------

def conexaoBanco():
    caminho = 'Modelo Banco de dados\\bancoDedados.db'
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
        print('Conexao aceita')
    except Error as ex:
        print('Erro de conexão:', ex)
    return conexao

janela = Tk()
conexao = conexaoBanco()
objeto = Janela_Cadastrar_Usuario(janela, conexao)
janela.mainloop()
conexao.close()