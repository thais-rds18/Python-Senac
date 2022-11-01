from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry

class Janela_Cadastrar_Usuario:
    def __init__(self, janela):
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

        self.label_nome = tk.Label(self.janela_cadastrar_usuario, text='Nome:', font='Inter 17 bold', bg='#F5F5F5')
        self.label_nome.place(relx=0.01, relwidth=0.10, rely=0.25, relheight=0.05)
        self.entrada_nome = tk.Entry(self.janela_cadastrar_usuario, font='Inter 17', bg='#D9D9D9')
        self.entrada_nome.place(relx=0.13, relwidth=0.75, rely=0.25, relheight=0.05)

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
        self.entrada_nasciento = DateEntry(self.janela_cadastrar_usuario, locale='pt_BR', dateformat='DD/MM/YYYY', font='Inter 17', bg='#D9D9D9')
        self.entrada_nasciento.place(relx=0.67, relwidth=0.21, rely=0.45, relheight=0.05)

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


        self.botao_cadastrar = tk.Button(self.janela_cadastrar_usuario, text='Cadastrar', font='Inter 17 bold', fg='white', bg='#004AAD')
        self.botao_cadastrar.place(relx=0.43, relwidth=0.15, rely=0.78, relheight=0.10)








        self.label_inferior = tk.Label(self.janela_cadastrar_usuario, bg='#004AAD')
        self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)


janela = Tk()
objetoJanela = Janela_Cadastrar_Usuario(janela)
janela.mainloop()