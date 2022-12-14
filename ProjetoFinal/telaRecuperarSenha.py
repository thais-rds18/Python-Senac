from tkinter import *
import tkinter as tk


def telaRecuperarSenha():
    class Janela_Recuperar_Senha:
        def __init__(self, janela):
            self.janela_recuperar_senha = janela
            self.janela_recuperar_senha.title('Recuperação de Senha')  # Trocar o título da janela
            self.janela_recuperar_senha.iconbitmap('icone.ico')  # Verificar se tem o ícone no seu arquivo
            self.janela_recuperar_senha.geometry('690x550+300+10')
            self.janela_recuperar_senha['bg'] = '#F5F5F5'
            self.janela_recuperar_senha.resizable(width=False, height=False)
            
            self.label_superior = tk.Label(self.janela_recuperar_senha, bg='#004AAD')
            self.label_superior.place(relx=0, relwidth=1, relheight=0.08, rely=0)
            
            self.senac_logo = tk.PhotoImage(file=r'..\ProjetoFinal\logo_simbolo.png')
            self.label_senac_logo = tk.Label(self.janela_recuperar_senha, image=self.senac_logo, bg='#F5F5F5')
            self.label_senac_logo.place(relx=0.02, rely=0.09)
            
            self.label_Cadastro_usuario = tk.Label(self.janela_recuperar_senha, text='Recuperar Senha',
                                                   bg='#F5F5F5',
                                                   font='Inter 24 bold')
            self.label_Cadastro_usuario.place(relx=0.15, relwidth=0.40, rely=0.08, relheight=0.15)
            
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

