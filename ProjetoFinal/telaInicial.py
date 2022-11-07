from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from sqlite3 import Error
from tkinter import messagebox
from tkcalendar import DateEntry
from ProjetoFinal.telaCadastrarCurso import telaCadastrarCurso
from ProjetoFinal.telaCadastrarUsuario import telaCadastrarUsuario
from ProjetoFinal.telaProfessoresGeral import telaProfessores
from ProjetoFinal.telaSalasGeral import telaSalas


class Inicio:
    def __init__(self, janela, conexao):
        self.conexao = conexao
        self.janela_login = janela
        self.janela_login.title('Tela de Acesso')
        self.janela_login.iconbitmap('icone.ico')
        self.janela_login.geometry('1440x750+50+10')
        self.janela_login['bg'] = '#F5F5F5'  # BOTÃO LARANJA #DE8708
        self.janela_login.resizable(False, False)

        self.label_superior = tk.Label(self.janela_login, bg='#004AAD', fg='white', font='Inter 20 bold')
        self.label_superior.place(relx=0, relwidth=1, relheight=0.08, rely=0)

        self.imagem = tk.PhotoImage(file=r'..\ProjetoFinal\logosenac.png')
        self.label_logoSenac = tk.Label(self.janela_login, image=self.imagem, bg='#F5F5F5')
        self.label_logoSenac.place(relx=0.44, rely=0.12, relheight=0.25, relwidth=0.18)

        self.label_login = tk.Label(self.janela_login, text='Login:', font='Inter 17 bold', bg='#F5F5F5')
        self.label_login.place(relx=0.30, rely=0.45, relheight=0.05, relwidth=0.06)
        self.entrada_login = tk.Entry(self.janela_login, bg='lightgray', font='Inter 17')
        self.entrada_login.place(relx=0.40, rely=0.45, relheight=0.05, relwidth=0.30)

        self.label_senha = tk.Label(self.janela_login, text='Senha:', font='Inter 17 bold', bg='#F5F5F5')
        self.label_senha.place(relx=0.30, rely=0.53, relheight=0.05, relwidth=0.07)
        self.entrada_senha = tk.Entry(self.janela_login, bg='lightgray', font='Inter 17', show='*')
        self.entrada_senha.place(relx=0.40, rely=0.53, relheight=0.05, relwidth=0.30)

        self.mensagem_acesso = tk.Label(self.janela_login, text='', bg='#F5F5F5', font='Verdana 16')
        self.mensagem_acesso.place(relx=0.43, rely=0.62, relheight=0.05, relwidth=0.25)

        self.botao_entrar = tk.Button(self.janela_login, text='ENTRAR', font='Inter 17 bold', fg='white', bg='#DE8708',
                                      relief=GROOVE, command=lambda: self.login_inicial())
        self.botao_entrar.place(relx=0.36, rely=0.70, relheight=0.08, relwidth=0.10)
        # self.botao_entrar.bind('<Return>', self.enter_confirmar)
        # self.botao_entrar.bind('<Any-Button>', self.clique_confirmar)

        self.botao_cadastrar = tk.Button(self.janela_login, text='CADASTRAR', font='Inter 17 bold', fg='white',
                                         bg='#004AAD', relief=GROOVE, command=lambda: telaCadastrarUsuario())
        self.botao_cadastrar.place(relx=0.58, rely=0.70, relheight=0.08, relwidth=0.15)
        # self.botao_cadastrar.bind('<Return>') receberá a função para cadastrar futuramente
        # self.botao_cadastrar.bind('<Any-Button>') receberá a função para cadastrar futuramente

        self.botao_esqueci_senha = tk.Button(self.janela_login, text='Esqueci minha senha', font='Verdana 16',
                                             fg='#004AAD', bg='#F5F5F5', relief=FLAT, command=lambda : self.esqueciSenha())
        self.botao_esqueci_senha.place(relx=0.43, rely=0.83, relheight=0.05, relwidth=0.20)
        # self.label_esqueci_senha.bind('<Return>') receberá a função para cadastrar futuramente
        # self.botao_esqueci_senha.bind('<Any-Button>') receberá a função para cadastrar futuramente

        self.label_inferior = tk.Label(self.janela_login, bg='#004AAD')
        self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)

    def esqueciSenha(self):
        pass

    def telaInicial(self):
        self.janela_login.destroy()
        self.janela01 = Tk()
        self.inicial = self.janela01
        self.inicial.title('Cadastro de Salas')  # Trocar o título da janela
        self.inicial.iconbitmap('icone.ico')  # Verificar se tem o ícone no seu arquivo
        self.inicial.geometry('1440x750+50+10')
        self.inicial['bg'] = '#F5F5F5'
        self.inicial.resizable(width=False, height=False)

        self.label_superior = tk.Label(self.inicial, bg='#004AAD')
        self.label_superior.place(relx=0, relwidth=1, relheight=0.08, rely=0)

        self.botao_cadastrar_novo_curso = tk.Button(self.inicial, bg='#004AAD', text='Cadastrar novo curso',
                                                    font='Inter 20 bold', fg='white', width=17, command=lambda: telaCadastrarCurso())
        self.botao_cadastrar_novo_curso.place(relx=0.03, rely=0.16)

        self.imagem = tk.PhotoImage(file=r'..\ProjetoFinal\logosenac.png')
        self.recebe = tk.Label(self.inicial, image=self.imagem, bg='#F5F5F5')
        self.recebe.place(rely=0.2, relx=0.42)

        self.label_boas_vindas = tk.Label(self.inicial, font='Inter 24 bold', bg='#F5F5F5', text='Olá, Administrador')
        self.label_boas_vindas.place(rely=0.50, relx=0.40)

        self.botao_Salas = tk.Button(self.inicial, text='SALAS', font='Inter 17 bold', fg='white', bg='orange',
                                     width=13,
                                     relief=FLAT, command=lambda: telaSalas())
        self.botao_Salas.place(rely=0.65, relx=0.3)

        self.botao_Professores = tk.Button(self.inicial, text='PROFESSORES', font='Inter 17 bold', fg='white',
                                           bg='orange',
                                           width=17, relief=FLAT, command=lambda: telaProfessores())
        self.botao_Professores.place(rely=0.65, relx=0.55)

        self.label_inferior = tk.Label(self.inicial, bg='#004AAD')
        self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)

        self.inicial.mainloop()

    def login_inicial(self):
        c = self.conexao.cursor()
        sql = "SELECT * FROM login WHERE usuario = '" + self.entrada_login.get() + "' AND senha = '" + self.entrada_senha.get() + "'"
        c.execute(sql)
        if c.fetchall():
            self.telaInicial()
        else:
            messagebox.showerror('Error', 'Senha ou Usuario incorreto!')
        c.close()


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

janela = tk.Tk()
conexao = conexaoBanco()
objeto = Inicio(janela, conexao)
janela.mainloop()
conexao.close()