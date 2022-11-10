from distutils.cmd import Command
from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from sqlite3 import Error
from tkinter import messagebox
from tkcalendar import DateEntry


class Inicio:
    def __init__(self, janela, conexao):
        self.conexao = conexao
        self.janela_login = janela
        self.pag = 1
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

        self.botao_cadastrar = tk.Button(self.janela_login, text='CADASTRAR', font='Inter 17 bold', fg='white',
                                         bg='#004AAD', relief=GROOVE, command=lambda: telaCadastrarUsuario())
        self.botao_cadastrar.place(relx=0.58, rely=0.70, relheight=0.08, relwidth=0.15)

        self.botao_esqueci_senha = tk.Button(self.janela_login, text='Esqueci minha senha', font='Verdana 16',
                                             fg='#004AAD', bg='#F5F5F5', relief=FLAT, command=lambda: self.telaRecuperarSenha())
        self.botao_esqueci_senha.place(relx=0.43, rely=0.83, relheight=0.05, relwidth=0.20)

        self.label_inferior = tk.Label(self.janela_login, bg='#004AAD')
        self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)


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
                                                    font='Inter 20 bold', fg='white', width=17,
                                                    command=lambda: telaCadastrarCurso())
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

    def telaRecuperarSenha(self):
        class Janela_Recuperar_Senha:
            def __init__(self, janela_recuperar):
                self.janela_recuperar_senha = janela_recuperar
                self.janela_recuperar_senha.title('Recuperação de Senha')  # Trocar o título da janela
                self.janela_recuperar_senha.iconbitmap('icone.ico')  # Verificar se tem o ícone no seu arquivo
                self.janela_recuperar_senha.geometry('690x550+300+10')
                self.janela_recuperar_senha['bg'] = '#F5F5F5'
                self.janela_recuperar_senha.resizable(width=False, height=False)

                self.label_superior = tk.Label(self.janela_recuperar_senha, bg='#004AAD')
                self.label_superior.place(relx=0, relwidth=1, relheight=0.08, rely=0)

                self.senac_logo = tk.PhotoImage(file='logo_simbolo.png')
                self.label_senac_logo = tk.Label(self.janela_recuperar_senha, image=self.senac_logo, bg='#F5F5F5')
                self.label_senac_logo.place(relx=0.02, rely=0.09)

                self.label_Recuperar_senha = tk.Label(self.janela_recuperar_senha, text='Recuperar Senha', bg='#F5F5F5',
                                                      font='Inter 24 bold')
                self.label_Recuperar_senha.place(relx=0.18, relwidth=0.40, rely=0.08, relheight=0.15)

                self.label_cpf = tk.Label(self.janela_recuperar_senha, text='CPF:', font='Inter 17 bold', bg='#F5F5F5')
                self.label_cpf.place(relx=0.15, relwidth=0.10, rely=0.35, relheight=0.05)
                self.entrada_cpf = tk.Entry(self.janela_recuperar_senha, font='Inter 17', bg='#D9D9D9')
                self.entrada_cpf.place(relx=0.28, relwidth=0.50, rely=0.35, relheight=0.05)

                self.label_email = tk.Label(self.janela_recuperar_senha, text='E-mail:', font='Inter 17 bold',
                                            bg='#F5F5F5')
                self.label_email.place(relx=0.15, relwidth=0.12, rely=0.45, relheight=0.05)
                self.entrada_email = tk.Entry(self.janela_recuperar_senha, font='Inter 17', bg='#D9D9D9')
                self.entrada_email.place(relx=0.28, relwidth=0.50, rely=0.45, relheight=0.05)

                self.botao_enviar = tk.Button(self.janela_recuperar_senha, text='Enviar', font='Inter 17 bold',
                                              fg='white', bg='#004AAD', command=lambda: self.enviar_email())
                self.botao_enviar.place(relx=0.43, relwidth=0.20, rely=0.60, relheight=0.10)

                self.label_inferior = tk.Label(self.janela_recuperar_senha, bg='#004AAD')
                self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)


            def enviar_email(self):
                cpf = self.entrada_cpf.get()
                email = self.entrada_email.get()
                print(cpf, email)
                # sql = f'SELECT * FROM salas WHERE cpf={cpf}

        janela = tk.Toplevel()
        objetoJanela = Janela_Recuperar_Senha(janela)
        janela.mainloop()

    def login_inicial(self):
        c = self.conexao.cursor()
        sql = "SELECT * FROM login WHERE usuario = '" + self.entrada_login.get() + "' AND senha = '" + self.entrada_senha.get() + "'"
        c.execute(sql)
        if c.fetchall():
            self.telaInicial()
        else:
            messagebox.showerror('Error', 'Senha ou email incorreto!')
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


def telaCadastrarUsuario():
    class Janela_Cadastrar_Usuario:
        def __init__(self, janela, conexao):
            self.conexao = conexao
            self.janela_cadastrar_usuario = janela
            self.janela_cadastrar_usuario.title('Cadastrar Usuário')  # Trocar o título da janela
            self.janela_cadastrar_usuario.iconbitmap('icone.ico')  # Verificar se tem o ícone no seu arquivo
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

            self.label_usuario = tk.Label(self.janela_cadastrar_usuario, text='Nome:', font='Inter 17 bold',
                                          bg='#F5F5F5')
            self.label_usuario.place(relx=0.01, relwidth=0.10, rely=0.25, relheight=0.05)
            self.entrada_usuario = tk.Entry(self.janela_cadastrar_usuario, font='Inter 17', bg='#D9D9D9')
            self.entrada_usuario.place(relx=0.13, relwidth=0.75, rely=0.25, relheight=0.05)

            self.label_email = tk.Label(self.janela_cadastrar_usuario, text='E-mail:', font='Inter 17 bold',
                                        bg='#F5F5F5')
            self.label_email.place(relx=0.01, relwidth=0.10, rely=0.35, relheight=0.05)
            self.entrada_email = tk.Entry(self.janela_cadastrar_usuario, font='Inter 17', bg='#D9D9D9')
            self.entrada_email.place(relx=0.13, relwidth=0.75, rely=0.35, relheight=0.05)

            self.label_cpf = tk.Label(self.janela_cadastrar_usuario, text='CPF:', font='Inter 17 bold', bg='#F5F5F5')
            self.label_cpf.place(relx=0.01, relwidth=0.07, rely=0.45, relheight=0.05)
            self.entrada_cpf = tk.Entry(self.janela_cadastrar_usuario, font='Inter 17', bg='#D9D9D9')
            self.entrada_cpf.place(relx=0.13, relwidth=0.35, rely=0.45, relheight=0.05)

            self.label_nascimento = tk.Label(self.janela_cadastrar_usuario, text='Data Nasc.:', font='Inter 17 bold',
                                             bg='#F5F5F5')
            self.label_nascimento.place(relx=0.50, relwidth=0.15, rely=0.45, relheight=0.05)
            self.entrada_nascimento = DateEntry(self.janela_cadastrar_usuario, locale='pt_BR', dateformat='DD/MM/YYYY',
                                                font='Inter 17', bg='#D9D9D9')
            self.entrada_nascimento.place(relx=0.67, relwidth=0.21, rely=0.45, relheight=0.05)

            self.label_senha = tk.Label(self.janela_cadastrar_usuario, text='Senha:', font='Inter 17 bold',
                                        bg='#F5F5F5')
            self.label_senha.place(relx=0.01, relwidth=0.10, rely=0.55, relheight=0.05)
            self.entrada_senha = tk.Entry(self.janela_cadastrar_usuario, font='Inter 17', bg='#D9D9D9', show='*')
            self.entrada_senha.place(relx=0.13, relwidth=0.75, rely=0.55, relheight=0.05)

            self.label_confirmar_senha = tk.Label(self.janela_cadastrar_usuario, text='Confirmar Senha:',
                                                  font='Inter 17 bold',
                                                  bg='#F5F5F5')
            self.label_confirmar_senha.place(relx=0.01, relwidth=0.23, rely=0.65, relheight=0.05)
            self.entrada_confirmar_senha = tk.Entry(self.janela_cadastrar_usuario, bg='#D9D9D9', show='*')
            self.entrada_confirmar_senha.place(relx=0.25, relwidth=0.63, rely=0.65, relheight=0.05)

            self.botao_cadastrar = tk.Button(self.janela_cadastrar_usuario, text='Cadastrar', font='Inter 17 bold',
                                             fg='white', bg='#004AAD', command=lambda: self.cadastrarUsuario())
            self.botao_cadastrar.place(relx=0.43, relwidth=0.15, rely=0.78, relheight=0.10)

            self.label_inferior = tk.Label(self.janela_cadastrar_usuario, bg='#004AAD')
            self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)

        def cadastrarUsuario(self):
            try:
                if self.entrada_usuario.get() == '' or self.entrada_cpf.get() == '' or self.entrada_email.get() == '' or self.entrada_nascimento.get() == '' or self.entrada_senha.get() == '' or self.entrada_confirmar_senha.get() == '':
                    messagebox.showerror('Atenção!', 'Preencha todos os campos!')

                elif self.entrada_senha.get() != self.entrada_confirmar_senha.get():
                    messagebox.showerror('Atenção!', 'Senha e Confirmar senha nao conferem!')

                else:
                    c = self.conexao.cursor()
                    sql = "INSERT INTO login (usuario, cpf, email, nascimento, senha, confirmar_senha) VALUES ( '" + self.entrada_usuario.get() + "', '" + self.entrada_cpf.get() + "','" + self.entrada_email.get() + "', '" + self.entrada_nascimento.get() + "', '" + self.entrada_senha.get() + "', '" + self.entrada_confirmar_senha.get() + "')"
                    c.execute(sql)
                    self.conexao.commit()
                    messagebox.showinfo('Caixa de Mensagem', 'Dados Inseridos com sucesso!')
            except Error as ex:
                print('Não inseriu', ex)

    conexao = conexaoBanco()
    janela_usuario_cadastro = tk.Toplevel()
    objetoUsuario = Janela_Cadastrar_Usuario(janela_usuario_cadastro, conexao)
    janela_usuario_cadastro.mainloop()
    conexao.close()


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

        def exibir(self, salas, pag=0):
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
                    nnmesa = v[7]
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
                        self.nnmesa1 = nnmesa
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
                        self.nnmesa2 = nnmesa
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
                        self.nnmesa3 = nnmesa
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


    def comandosSQL(sql):
        c = conexao.cursor()
        c.execute(sql)
        return c.fetchall()

    conexao = conexaoBanco()
    janela_salas_geral = tk.Toplevel()
    objetoSalasGeral = TelaSalas(janela_salas_geral)
    janela_salas_geral.mainloop()
    conexao.close()


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
            var1 = tk.IntVar()
            self.checkbox_ordem_alfabetica = tk.Checkbutton(self.professores, text='Ordem alfabética', font='Inter 12',
                                                            variable=var1, onvalue=1, offvalue=0, bg='#F5F5F5',
                                                            command=lambda: self.exibirProf(self.filtrarProfs(var1)))
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
            self.caixa_selecao_area_conhecimento.bind("<<ComboboxSelected>>")
            self.caixa_selecao_area_conhecimento.place(relx=0.027, relwidth=0.2, rely=0.33)

            # botão
            self.botao_cadastrar_novo_professor = tk.Button(self.professores, text='Cadastrar novo professor',
                                                            font='Inter 17 bold', fg='white', bg='#F59714', relief=FLAT,
                                                            command=lambda: telaCadastrarProfessores())
            self.botao_cadastrar_novo_professor.place(relx=0.7, rely=0.2)

            # Teste para exibição das salas

            self.frameProf1 = tk.Frame(self.professores, relief='solid', borderwidth=0.5, width=250, height=350)
            self.frameProf1.place(relx=0.32, relwidth=0.65, rely=0.29, relheight=0.15)
            self.botaoProf1 = tk.Button(self.professores)
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
            self.botaoProf2 = tk.Button(self.professores)
            self.nomeProf2 = tk.Label(self.professores, text='', font='Inter 19 bold')
            self.nomeProf2.place(relx=0.35, rely=0.47)
            self.espProf2 = tk.Label(self.professores, text='', font='Inter 15')
            self.espProf2.place(relx=0.35, rely=0.52)
            self.foneProf2 = tk.Label(self.professores, text='', font='Inter 15')
            self.foneProf2.place(relx=0.35, rely=0.56)
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
            self.botaoProf3 = tk.Button(self.professores)
            self.nomeProf3 = tk.Label(self.professores, text='', font='Inter 19 bold')
            self.nomeProf3.place(relx=0.35, rely=0.64)
            self.espProf3 = tk.Label(self.professores, text='', font='Inter 15')
            self.espProf3.place(relx=0.35, rely=0.69)
            self.foneProf3 = tk.Label(self.professores, text='', font='Inter 15')
            self.foneProf3.place(relx=0.35, rely=0.73)
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

            self.exibirProf(self.filtrarProfs(var1))

        def filtrarProfs(self, var1):
            sql = ''
            if var1.get() == 1:
                sql = 'SELECT * From professor order by nome'

            elif var1.get() == 0:
                sql = 'SELECT * From professor'

            profs = comandosSQL(sql)
            return profs

        def exibirProf(self, profs):
            if len(profs) < 1:
                pass
            else:
                contadorprof = 0
                for v in profs:
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
                        self.botaoProf2.place(relx=0.321, relwidth=0.649, rely=0.461, relheight=0.148)
                    elif contadorprof == 3:
                        self.nomeProf3.config(text=nnnome)
                        self.espProf3.config(text=nnesp)
                        self.foneProf3.config(text=nnfone)
                        self.emailProf3.config(text=nnemail)
                        self.cpfProf3.config(text=nncpf)
                        self.botaoProf3.place(relx=0.321, relwidth=0.649, rely=0.632, relheight=0.148)

    def comandosSQL(sql):
        c = conexao.cursor()
        c.execute(sql)
        return c.fetchall()

    conexao = conexaoBanco()
    janela_professores_geral = tk.Toplevel()
    objetoProfessoresGeral = TelaProfessores(janela_professores_geral)
    janela_professores_geral.mainloop()
    conexao.close()


def telaCadastrarSalas():
    class TelaCadastroSalas:
        def __init__(self, janela_salas_cadastro, conexao):
            self.conexao = conexao
            self.cadastrar_salas = janela_salas_cadastro
            self.cadastrar_salas.title('Cadastrar Salas')  # Trocar o título da janela
            self.cadastrar_salas.iconbitmap('icone.ico')  # Verificar se tem o ícone no seu arquivo
            self.cadastrar_salas.geometry('890x650+300+10')
            self.cadastrar_salas['bg'] = '#F5F5F5'
            self.cadastrar_salas.resizable(width=False, height=False)

            self.label_superior = tk.Label(self.cadastrar_salas, bg='#004AAD')
            self.label_superior.place(relx=0, relwidth=1, relheight=0.08, rely=0)

            self.senac_logo = tk.PhotoImage(file=r'..\ProjetoFinal\logo_simbolo.png')
            self.senac_tituloPag = tk.Label(self.cadastrar_salas, text='Cadastrar Salas', font='Inter 26 bold',
                                            bg='#F5F5F5')
            self.label_senac_logo = tk.Label(self.cadastrar_salas, image=self.senac_logo, bg='#F5F5F5')
            self.label_senac_logo.place(relx=0.0, rely=0.13)
            self.senac_tituloPag.place(relx=0.15, rely=0.15)

            # Entradas
            self.label_polo = tk.Label(self.cadastrar_salas, bg='#F5F5F5', text='Polo:', font='Inter 17 bold',
                                       anchor='w')
            self.label_polo.place(relx=0.513, relwidth=0.16, rely=0.23, relheight=0.035)
            self.entrada_polo = ttk.Combobox(self.cadastrar_salas, width=12,
                                             values=['Faculdade Senac', 'Recife Sede', 'Aprendizagem'])
            self.entrada_polo.current()
            self.entrada_polo.place(relx=0.6, relwidth=0.213, rely=0.23, relheight=0.035)

            self.label_nome_sala = tk.Label(self.cadastrar_salas, bg='#F5F5F5', text='Nome:', font='Inter 17 bold',
                                            anchor='w')
            self.label_nome_sala.place(relx=0.05, relwidth=0.16, rely=0.33, relheight=0.035)
            self.entrada_nome_sala = tk.Entry(self.cadastrar_salas, bg='#D9D9D9')
            self.entrada_nome_sala.place(relx=0.22, relwidth=0.24, rely=0.33, relheight=0.035)

            self.label_cadeiras = tk.Label(self.cadastrar_salas, bg='#F5F5F5', text='Cadeiras:', font='Inter 17 bold',
                                           anchor='w')
            self.label_cadeiras.place(relx=0.05, relwidth=0.16, rely=0.4, relheight=0.035)
            self.entrada_cadeiras = tk.Entry(self.cadastrar_salas, bg='#D9D9D9')
            self.entrada_cadeiras.place(relx=0.242, relwidth=0.218, rely=0.4, relheight=0.035)

            self.label_computadores = tk.Label(self.cadastrar_salas, bg='#F5F5F5', text='Computadores:',
                                               font='Inter 17 bold',
                                               anchor='w')
            self.label_computadores.place(relx=0.05, relwidth=0.20, rely=0.47, relheight=0.035)
            self.entrada_computadores = tk.Entry(self.cadastrar_salas, bg='#D9D9D9')
            self.entrada_computadores.place(relx=0.286, relwidth=0.174, rely=0.47, relheight=0.035)

            self.label_televisores = tk.Label(self.cadastrar_salas, bg='#F5F5F5', text='Televisores:',
                                              font='Inter 17 bold',
                                              anchor='w')
            self.label_televisores.place(relx=0.05, relwidth=0.16, rely=0.54, relheight=0.035)
            self.entrada_televisores = tk.Entry(self.cadastrar_salas, bg='#D9D9D9')
            self.entrada_televisores.place(relx=0.263, relwidth=0.197, rely=0.54, relheight=0.035)

            self.label_Tela_retratil = tk.Label(self.cadastrar_salas, bg='#F5F5F5', text='Tela retrátil:',
                                                font='Inter 17 bold',
                                                anchor='w')
            self.label_Tela_retratil.place(relx=0.05, relwidth=0.16, rely=0.61, relheight=0.035)
            self.entrada_Tela_retratil = tk.Entry(self.cadastrar_salas, bg='#D9D9D9')
            self.entrada_Tela_retratil.place(relx=0.263, relwidth=0.197, rely=0.61, relheight=0.035)

            self.label_andar = tk.Label(self.cadastrar_salas, bg='#F5F5F5', text='Andar:', font='Inter 17 bold',
                                        anchor='w')
            self.label_andar.place(relx=0.515, relwidth=0.1, rely=0.33, relheight=0.035)
            self.entrada_andar = tk.Entry(self.cadastrar_salas, bg='#D9D9D9')
            self.entrada_andar.place(relx=0.69, relwidth=0.2417, rely=0.33, relheight=0.035)

            self.label_mesas = tk.Label(self.cadastrar_salas, bg='#F5F5F5', text='Mesas:', font='Inter 17 bold',
                                        anchor='w')
            self.label_mesas.place(relx=0.515, relwidth=0.1, rely=0.4, relheight=0.035)
            self.entrada_mesas = tk.Entry(self.cadastrar_salas, bg='#D9D9D9')
            self.entrada_mesas.place(relx=0.69, relwidth=0.240, rely=0.4, relheight=0.035)

            self.label_projetores = tk.Label(self.cadastrar_salas, bg='#F5F5F5', text='Projetores:',
                                             font='Inter 17 bold', anchor='w')
            self.label_projetores.place(relx=0.515, relwidth=0.14, rely=0.47, relheight=0.039)
            self.entrada_projetores = tk.Entry(self.cadastrar_salas, bg='#D9D9D9')
            self.entrada_projetores.place(relx=0.725, relwidth=0.205, rely=0.47, relheight=0.035)

            self.label_quadros = tk.Label(self.cadastrar_salas, bg='#F5F5F5', text='Quadros:', font='Inter 17 bold',
                                          anchor='w')
            self.label_quadros.place(relx=0.515, relwidth=0.14, rely=0.54, relheight=0.035)
            self.entrada_quadros = tk.Entry(self.cadastrar_salas, bg='#D9D9D9')
            self.entrada_quadros.place(relx=0.71, relwidth=0.221, rely=0.54, relheight=0.035)

            self.label_ar_condicionado = tk.Label(self.cadastrar_salas, bg='#F5F5F5', text='Ar-condicionado:',
                                                  font='Inter 17 bold',
                                                  anchor='w')
            self.label_ar_condicionado.place(relx=0.515, relwidth=0.23, rely=0.61, relheight=0.035)
            self.entrada_ar_condicionado = tk.Entry(self.cadastrar_salas, bg='#D9D9D9')
            self.entrada_ar_condicionado.place(relx=0.772, relwidth=0.157, rely=0.61, relheight=0.035)

            self.botao_cadastrar_cadastrar_sala = tk.Button(self.cadastrar_salas, text='Cadastrar', fg='white',
                                                            bg='#004AAD',
                                                            font='Inter 17 bold',
                                                            relief=FLAT, command=lambda: self.cadastrar())
            self.botao_cadastrar_cadastrar_sala.place(relx=0.42, relwidth=0.16, rely=0.75, relheight=0.09)
            self.botao_cadastrar_cadastrar_sala.bind('<Any-Button>')

            self.label_inferior = tk.Label(self.cadastrar_salas, bg='#004AAD')
            self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)

        def cadastrar(self):
            try:
                if self.entrada_nome_sala.get() == '' or self.entrada_cadeiras.get() == '' or self.entrada_computadores.get() == '' or self.entrada_televisores.get() == '' or self.entrada_Tela_retratil.get() == '' or self.entrada_polo.get() == '' or self.entrada_mesas.get() == '' or self.entrada_projetores.get() == '' or self.entrada_quadros.get() == '' or self.entrada_ar_condicionado.get() == '' or self.entrada_andar.get() == '':
                    messagebox.showerror('Atenção!', 'Preencha todos os campos!')
                else:
                    c = self.conexao.cursor()
                    sql = "INSERT INTO salas (nome, cadeiras, computadores, televisores, tela_retratil, polo, mesas, projetores, quadros, ar_condicionado, andar, ocupado_manha, ocupado_tarde, ocupado_noite ) VALUES ( '" + self.entrada_nome_sala.get() + "', '" + self.entrada_cadeiras.get() + "','" + self.entrada_computadores.get() + "', '" + self.entrada_televisores.get() + "', '" + self.entrada_Tela_retratil.get() + "', '" + self.entrada_polo.get() + "' , '" + self.entrada_mesas.get() + "', '" + self.entrada_projetores.get() + "', '" + self.entrada_quadros.get() + "', '" + self.entrada_ar_condicionado.get() + "', '" + self.entrada_andar.get() + "', 0, 0, 0)"
                    c.execute(sql)
                    self.conexao.commit()
                    messagebox.showinfo('Caixa de Mensagem', 'Dados Inseridos com sucesso!')
            except Error as ex:
                print('Não inseriu', ex)

    conexao = conexaoBanco()
    janela_salas_cadastro = tk.Toplevel()
    objetoSalasGeral = TelaCadastroSalas(janela_salas_cadastro, conexao)
    janela_salas_cadastro.mainloop()
    conexao.close()


def telaCadastrarCurso():
    class Cadastrar_Curso:
        def __init__(self, janela_cadastrar_curso, conexao):
            # Base da janela
            self.conexao = conexao
            self.janela_cadastrar_curso = janela_cadastrar_curso
            self.janela_cadastrar_curso.title('Editar Salas')  # Trocar o título da janela
            self.janela_cadastrar_curso.iconbitmap('icone.ico')  # Verificar se tem o ícone no seu arquivo
            self.janela_cadastrar_curso.geometry('890x650+300+10')
            self.janela_cadastrar_curso['bg'] = '#F5F5F5'
            self.janela_cadastrar_curso.resizable(width=False, height=False)

            self.label_superior = tk.Label(self.janela_cadastrar_curso, bg='#004AAD')
            self.label_superior.place(relx=0, relwidth=1, relheight=0.08, rely=0)

            self.senac_logo = tk.PhotoImage(file='logo_simbolo.png')
            self.label_senac_logo = tk.Label(self.janela_cadastrar_curso, image=self.senac_logo, bg='#F5F5F5')
            self.label_senac_logo.place(relx=0.032, rely=0.09)

            self.label_Cadastro_Curso = tk.Label(self.janela_cadastrar_curso, text='Cadastro Curso', bg='#F5F5F5',
                                                 font='Inter 28 bold')
            self.label_Cadastro_Curso.place(relx=0.15, relwidth=0.40, rely=0.10, relheight=0.15)

            # Entradas
            self.label_nome = tk.Label(self.janela_cadastrar_curso, bg='#F5F5F5', text='Nome:', font='Inter 17 bold',
                                       anchor='w')
            self.label_nome.place(relx=0.05, relwidth=0.08, rely=0.25, relheight=0.05)
            self.entrada_nome = tk.Entry(self.janela_cadastrar_curso, bg='#D9D9D9', font='Inter 17')
            self.entrada_nome.place(relx=0.15, relwidth=0.40, rely=0.25, relheight=0.045)

            self.label_Hora_Total = tk.Label(self.janela_cadastrar_curso, text='Carga Horária Total:', bg='#F5F5F5',
                                             font='Inter 17 bold',
                                             anchor='w')
            self.label_Hora_Total.place(relx=0.05, relwidth=0.30, rely=0.35, relheight=0.05)
            self.entrada_Hora_Total = tk.Entry(self.janela_cadastrar_curso, bg='#D9D9D9', font='Inter 17')
            self.entrada_Hora_Total.place(relx=0.37, relwidth=0.17, rely=0.35, relheight=0.045)

            self.label_Hora_Diaria = tk.Label(self.janela_cadastrar_curso, text='Carga Horária Diária:', bg='#F5F5F5',
                                              font='Inter 17 bold', anchor='w')
            self.label_Hora_Diaria.place(relx=0.05, relwidth=0.30, rely=0.45, relheight=0.05)
            self.entrada_Hora_Diaria = tk.Entry(self.janela_cadastrar_curso, bg='#D9D9D9', font='Inter 17')
            self.entrada_Hora_Diaria.place(relx=0.37, relwidth=0.17, rely=0.45, relheight=0.045)

            self.label_Turno = tk.Label(self.janela_cadastrar_curso, bg='#F5F5F5', text='Turno:', font='Inter 17 bold',
                                        anchor='w')
            self.label_Turno.place(relx=0.56, relwidth=0.09, rely=0.25, relheight=0.05)
            self.entrada_Turno = ttk.Combobox(self.janela_cadastrar_curso, values=[" ", "Manhã", "Tarde", "Noite"],
                                              font='Inter 17')
            self.entrada_Turno.current(0)
            self.entrada_Turno.bind("<<ComboboxSelected>>")
            self.entrada_Turno.place(relx=0.66, relwidth=0.29, rely=0.25, relheight=0.045)

            self.label_inicio = tk.Label(self.janela_cadastrar_curso, bg='#F5F5F5', text='Início:',
                                         font='Inter 17 bold', anchor='w')
            self.label_inicio.place(relx=0.56, relwidth=0.09, rely=0.35, relheight=0.05)
            self.entrada_inicio = DateEntry(self.janela_cadastrar_curso, locale='pt_BR', dateformat='DD/MM/YYYY',
                                            font='Inter 17')
            self.entrada_inicio.place(relx=0.66, relwidth=0.28, rely=0.35, relheight=0.045)

            self.label_fim = tk.Label(self.janela_cadastrar_curso, bg='#F5F5F5', text='Fim:', font='Inter 17 bold',
                                      anchor='w')
            self.label_fim.place(relx=0.56, relwidth=0.08, rely=0.45, relheight=0.05)
            self.entrada_fim = DateEntry(self.janela_cadastrar_curso, locale='pt_BR', dateformat='DD/MM/YYYY',
                                         font='Inter 17')
            self.entrada_fim.place(relx=0.66, relwidth=0.28, rely=0.45, relheight=0.045)

            self.label_CPF_professor = tk.Label(self.janela_cadastrar_curso, bg='#F5F5F5', text='CPF do Professor:',
                                                font='Inter 16 bold', anchor='w')
            self.label_CPF_professor.place(relx=0.05, relwidth=0.21, rely=0.55, relheight=0.035)
            self.entrada_CPF_professor = tk.Entry(self.janela_cadastrar_curso, bg='#D9D9D9', font='Inter 17')
            self.entrada_CPF_professor.place(relx=0.28, relwidth=0.25, rely=0.55, relheight=0.045)

            self.label_Sala = tk.Label(self.janela_cadastrar_curso, bg='#F5F5F5', text='Nome Sala:',
                                       font='Inter 16 bold', anchor='w')
            self.label_Sala.place(relx=0.56, relwidth=0.21, rely=0.55, relheight=0.035)
            self.entrada_Sala = tk.Entry(self.janela_cadastrar_curso, bg='#D9D9D9', font='Inter 17')
            self.entrada_Sala.place(relx=0.70, relwidth=0.25, rely=0.55, relheight=0.045)

            self.label_polo = tk.Label(self.janela_cadastrar_curso, bg='#F5F5F5', text='Polo:',
                                       font='Inter 16 bold', anchor='w')
            self.label_polo.place(relx=0.05, relwidth=0.21, rely=0.65, relheight=0.035)
            self.entrada_polo = ttk.Combobox(self.janela_cadastrar_curso,
                                             values=[" ", "Faculdade Senac", "Recife Sede", "Aprendizagem"],
                                             font='Inter 17')
            self.entrada_polo.current(0)
            self.entrada_polo.bind("<<ComboboxSelected>>")
            self.entrada_polo.place(relx=0.15, relwidth=0.39, rely=0.65, relheight=0.045)

            self.label_andar = tk.Label(self.janela_cadastrar_curso, bg='#F5F5F5', text='Andar:',
                                        font='Inter 16 bold', anchor='w')
            self.label_andar.place(relx=0.56, relwidth=0.21, rely=0.65, relheight=0.035)
            self.entrada_andar = ttk.Combobox(self.janela_cadastrar_curso,
                                              values=[" ", "1", "2", "3", "4", "5", "6", "7"],
                                              font='Inter 17')
            self.entrada_andar.current(0)
            self.entrada_andar.bind('<<ComboboxSelected>>')
            self.entrada_andar.place(relx=0.66, relwidth=0.25, rely=0.65, relheight=0.045)

            self.botao_cadastrar_cadastrar_curso = tk.Button(self.janela_cadastrar_curso, text='Cadastrar', fg='white',
                                                             bg='#004AAD',
                                                             font='Inter 17 bold',
                                                             relief=FLAT, command=lambda: self.cadastrarCurso())
            self.botao_cadastrar_cadastrar_curso.place(relx=0.42, relwidth=0.15, rely=0.79, relheight=0.07)

            self.label_inferior = tk.Label(self.janela_cadastrar_curso, bg='#004AAD')
            self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)

        def cadastrarCurso(self):
            turno = ''
            try:
                if self.entrada_nome.get() == '' or self.entrada_Hora_Total.get() == '' or self.entrada_Hora_Diaria.get() == '' or self.entrada_inicio.get() == '' or self.entrada_fim.get() == '' or self.entrada_CPF_professor.get() == '' or self.entrada_Sala.get() == '' or self.entrada_polo.get() == '' or self.entrada_andar.get() == '' or self.entrada_Turno.get() == '':
                    messagebox.showerror('Atenção!', 'Preencha todos os campos!')
                else:
                    c = self.conexao.cursor()
                    sql = "INSERT INTO curso (nome, hora_total, hora_diaria, entrada_inicio, entrada_fim, CPF_professor, nomeSala, polo, andar) VALUES ( '" + self.entrada_nome.get() + "', '" + self.entrada_Hora_Total.get() + "','" + self.entrada_Hora_Diaria.get() + "', '" + self.entrada_inicio.get() + "', '" + self.entrada_fim.get() + "', '" + self.entrada_CPF_professor.get() + "' , '" + self.entrada_Sala.get() + "', '" + self.entrada_polo.get() + "', '" + self.entrada_andar.get() + "');"
                    sql2 = self.turno(turno)
                    c.execute(sql)
                    c.execute(sql2)
                    self.conexao.commit()
                    messagebox.showinfo('Caixa de Mensagem', 'Dados Inseridos com sucesso!')
            except Error as ex:
                print('Não inseriu', ex)

        def turno(self, turno):
            self.entrada_Turno.get()
            if self.entrada_Turno.get() == 'Manhã':
                turno = "UPDATE salas SET ocupado_manha = True WHERE nome = '" + self.entrada_Sala.get() + "' AND polo = '" + self.entrada_polo.get() + "' AND andar = '" + self.entrada_andar.get() + "';"

            if self.entrada_Turno.get() == 'Tarde':
                turno = f"UPDATE salas SET ocupado_tarde = True WHERE nome = '" + self.entrada_Sala.get() + "' AND polo = '" + self.entrada_polo.get() + "' AND andar = '" + self.entrada_andar.get() + "';"

            if self.entrada_Turno.get() == 'Noite':
                turno = f"UPDATE salas SET ocupado_noite = True WHERE nome = '" + self.entrada_Sala.get() + "' AND polo = '" + self.entrada_polo.get() + "' AND andar = '" + self.entrada_andar.get() + "';"

            return turno

    janela_cadastrar_curso = tk.Toplevel()
    conexao = conexaoBanco()
    objetoCadastrarCurso = Cadastrar_Curso(janela_cadastrar_curso, conexao)
    janela_cadastrar_curso.mainloop()
    conexao.close()


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
            self.label_senac_logo = tk.Label(self.cadastrar_professores, image=self.senac_logo, bg='#F5F5F5')
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
                if self.entrada_nome_professor.get() == '' or self.entrada_CPF.get() == '' or self.entrada_email.get() or self.entrada_fone.get() or self.entrada_conhecimento.get():
                    messagebox.showerror('Atenção!', 'Preencha todos os campos!')
                else:
                    c = self.conexao.cursor()
                    sql = "INSERT INTO professor (nome, cpf, email, telefone, conhecimento) VALUES ('" + self.entrada_nome_professor.get() + "', '" + self.entrada_CPF.get() + "','" + self.entrada_email.get() + "', '" + self.entrada_fone.get() + "', '" + self.entrada_conhecimento.get() + "')"
                    c.execute(sql)
                    self.conexao.commit()
                    messagebox.showinfo('Caixa de Mensagem', 'Dados Inseridos com sucesso!')
            except Error as ex:
                print('Não inseriu', ex)

    janela_professores_cadastro = tk.Toplevel()
    conexao = conexaoBanco()
    objeto = TelaCadastroProfessores(janela_professores_cadastro, conexao)
    janela_professores_cadastro.mainloop()
    conexao.close()


def telaSala(nnsala, nnpolo, nnandar, nncadeira,nncomputador, nntelevisor, nntelaretratil, nnprojetor, nnquadro, nnarcondicionado, nnmanha, nntarde, nnnoite):
        class TelaSala:
            def __init__(self, sala_individual):
                self.sala_individual = sala_individual
                self.sala_individual.title('Sala Individual')
                self.sala_individual.iconbitmap('icone.ico')
                self.sala_individual.geometry('1440x750+50+10')
                self.sala_individual['bg'] = '#F5F5F5'
                self.sala_individual.resizable(False, False)

                self.label_superior = tk.Label(self.sala_individual, bg='#004AAD', height=95)
                self.label_superior.place(relx=0, relwidth=1, rely=0, relheight=0.08)

                self.senac_logo = tk.PhotoImage(file=r'..\ProjetoFinal\logo_simbolo.png')
                self.label_senac_logo = tk.Label(self.sala_individual, image=self.senac_logo, bg='#F5F5F5')
                self.label_senac_logo.place(relx=0.1, rely=0.11)
                self.label_titulo_salas = tk.Label(self.sala_individual, text='Salas', font='Inter 28 bold',
                                                   bg='#F5F5F5')
                self.label_titulo_salas.place(relx=0.19, rely=0.13)

                self.botao_voltar_sala_indiviual = tk.Button(self.sala_individual, text='Voltar',
                                                             font='Inter 17 bold', fg='white', bg='#004AAD',
                                                             relief=FLAT,
                                                             command=lambda: self.sala_individual.destroy())
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
                self.nroQuadro = tk.Label(self.sala_individual, text=f'{nnquadro} quadro', font='Inter 17',
                                          bg='#F5F5F5')
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
                                            font='Inter 13', relief=FLAT, bg='#F5F5F5',
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
                pass

            def excluir_sala(self):
                pass

        sala_individual = tk.Toplevel()
        objetoSalasGeral = TelaSala(sala_individual)
        sala_individual.mainloop()

janela = tk.Tk()
conexao = conexaoBanco()
objeto = Inicio(janela, conexao)
janela.mainloop()
conexao.close()
