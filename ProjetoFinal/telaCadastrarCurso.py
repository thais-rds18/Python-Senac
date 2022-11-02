from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
import sqlite3
from sqlite3 import Error
from tkinter import messagebox


class Cadastrar_Curso:

    def __init__(self, janela, conexao):
        # Base da janela
        self.conexao = conexao
        self.janela08 = janela
        self.janela08.title('Editar Salas')  # Trocar o título da janela
        #self.janela08.iconbitmap('icone.ico')  # Verificar se tem o ícone no seu arquivo
        self.janela08.geometry('890x650+300+10')
        self.janela08['bg'] = '#F5F5F5'
        self.janela08.resizable(width=False, height=False)

        self.label_superior = tk.Label(self.janela08, bg='#004AAD')
        self.label_superior.place(relx=0, relwidth=1, relheight=0.08, rely=0)

        # Logo do senac
        # self.senac_logo = tk.PhotoImage(file='logosenac.png')
        # self.label_senac_logo = tk.Label(self.janela, image=self.senac_logo, bg='#F5F5F5')
        # self.label_senac_logo.place(relx=0.4, rely=0.08)

        self.label_Cadastro_Professor = tk.Label(self.janela08, text='Cadastro Curso', bg='#F5F5F5',
                                                 font='Inter 28 bold')
        self.label_Cadastro_Professor.place(relx=0.15, relwidth=0.40, rely=0.10, relheight=0.15)

        # Entradas
        self.label_nome = tk.Label(self.janela08, bg='#F5F5F5', text='Nome:', font='Inter 17 bold', anchor='w')
        self.label_nome.place(relx=0.05, relwidth=0.08, rely=0.25, relheight=0.05)
        self.entrada_nome = tk.Entry(self.janela08, bg='#D9D9D9', font='Inter 17')
        self.entrada_nome.place(relx=0.15, relwidth=0.40, rely=0.25, relheight=0.045)


        self.label_Hora_Total = tk.Label(self.janela08, text='Carga Horária Total:',bg='#F5F5F5', font='Inter 17 bold', anchor='w')
        self.label_Hora_Total.place(relx=0.05, relwidth=0.30, rely=0.35, relheight=0.05)
        self.entrada_Hora_Total = tk.Entry(self.janela08,bg='#D9D9D9', font='Inter 17')
        self.entrada_Hora_Total.place(relx=0.37, relwidth=0.17, rely=0.35, relheight=0.045)

        self.label_Hora_Diaria = tk.Label(self.janela08, text='Carga Horária Diária:', bg='#F5F5F5', font='Inter 17 bold', anchor='w')
        self.label_Hora_Diaria.place(relx=0.05, relwidth=0.30, rely=0.45, relheight=0.05)
        self.entrada_Hora_Diaria = tk.Entry(self.janela08,bg='#D9D9D9', font='Inter 17' )
        self.entrada_Hora_Diaria.place(relx=0.37, relwidth=0.17, rely=0.45, relheight=0.045)


        self.label_Turno = tk.Label(self.janela08, bg='#F5F5F5', text='Turno:', font='Inter 17 bold', anchor='w')
        self.label_Turno.place(relx=0.56, relwidth=0.09, rely=0.25, relheight=0.05)
        self.entrada_Turno = ttk.Combobox(self.janela08, values=[" ", "Manhã", "Tarde", "Noite"], font='Inter 17')
        self.entrada_Turno.current(0)
        self.entrada_Turno.bind("<<ComboboxSelected>>")
        self.entrada_Turno.place(relx=0.66, relwidth=0.29, rely=0.25, relheight=0.045)

        self.label_inicio = tk.Label(self.janela08, bg='#F5F5F5', text='Início:', font='Inter 17 bold', anchor='w')
        self.label_inicio.place(relx=0.56, relwidth=0.09, rely=0.35, relheight=0.05)
        self.entrada_inicio = DateEntry(self.janela08,locale='pt_BR', dateformat='DD/MM/YYYY', font='Inter 17')
        self.entrada_inicio.place(relx=0.66, relwidth=0.28, rely=0.35, relheight=0.045)

        self.label_fim = tk.Label(self.janela08, bg='#F5F5F5', text='Fim:', font='Inter 17 bold', anchor='w')
        self.label_fim.place(relx=0.56, relwidth=0.08, rely=0.45, relheight=0.05)
        self.entrada_fim = DateEntry(self.janela08,locale='pt_BR', dateformat='DD/MM/YYYY', font='Inter 17')
        self.entrada_fim.place(relx=0.66, relwidth=0.28, rely=0.45, relheight=0.045)

        self.label_CPF_professor = tk.Label(self.janela08, bg='#F5F5F5', text='CPF do Professor:',
                                    font='Inter 16 bold', anchor='w')
        self.label_CPF_professor.place(relx=0.05, relwidth=0.21, rely=0.55, relheight=0.035)
        self.entrada_CPF_professor = tk.Entry(self.janela08, bg='#D9D9D9', font='Inter 17')
        self.entrada_CPF_professor.place(relx=0.28, relwidth=0.25, rely=0.55, relheight=0.045)

        self.label_Sala = tk.Label(self.janela08, bg='#F5F5F5', text='Nome Sala:',
                                    font='Inter 16 bold', anchor='w')
        self.label_Sala.place(relx=0.56, relwidth=0.21, rely=0.55, relheight=0.035)
        self.entrada_Sala = tk.Entry(self.janela08, bg='#D9D9D9', font='Inter 17')
        self.entrada_Sala.place(relx=0.70, relwidth=0.25, rely=0.55, relheight=0.045)

        self.label_polo = tk.Label(self.janela08, bg='#F5F5F5', text='Polo:',
                                    font='Inter 16 bold', anchor='w')
        self.label_polo.place(relx=0.05, relwidth=0.21, rely=0.65, relheight=0.035)
        self.entrada_polo = ttk.Combobox(self.janela08, values=[" ", "Faculdade Senac", "Edíficio João Barros"], font='Inter 17')
        self.entrada_polo.current(0)
        self.entrada_polo.bind("<<ComboboxSelected>>")
        self.entrada_polo.place(relx=0.15, relwidth=0.39, rely=0.65, relheight=0.045)

        self.label_andar = tk.Label(self.janela08, bg='#F5F5F5', text='Andar:',
                                    font='Inter 16 bold', anchor='w')
        self.label_andar.place(relx=0.56, relwidth=0.21, rely=0.65, relheight=0.035)
        self.entrada_andar = ttk.Combobox(self.janela08, values=[" ","1","2","3","4","5","6","7"], font='Inter 17')
        self.entrada_andar.current(0)
        self.entrada_andar.bind('<<ComboboxSelected>>')
        self.entrada_andar.place(relx=0.66, relwidth=0.25, rely=0.65, relheight=0.045)


        self.botao_cadastrar_cadastrar_curso = tk.Button(self.janela08, text='Cadastrar', fg='white', bg='#004AAD',
                                                             font='Inter 17 bold',
                                                             relief=FLAT, command=lambda: self.cadastrarCurso())
        self.botao_cadastrar_cadastrar_curso.place(relx=0.42, relwidth=0.15, rely=0.79, relheight=0.07)

        self.label_inferior = tk.Label(self.janela08, bg='#004AAD')
        self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)

    def cadastrarCurso(self):
            try:
                if self.entrada_nome.get() and self.entrada_Hora_Total.get() == '' and self.entrada_Hora_Diaria.get() == '' and self.entrada_inicio.get() == '' and self.entrada_fim.get() == '' and self.entrada_CPF_professor.get() == '' and self.entrada_Sala.get() == '' and self.entrada_polo.get() == '' and self.entrada_andar.get() == '':
                    messagebox.showerror('Atenção!', 'Preencha todos os campos!')
                else:
                    c = self.conexao.cursor()
                    sql = "INSERT INTO curso (nome, hora_total, hora_diaria, entrada_inicio, entrada_fim, CPF_professor, nomeSala, polo, andar) VALUES ( '" + self.entrada_nome.get() + "', '" + self.entrada_Hora_Total.get() + "','" + self.entrada_Hora_Diaria.get()+ "', '" + self.entrada_inicio.get() + "', '" + self.entrada_fim.get() + "', '" + self.entrada_CPF_professor.get() + "' , '" + self.entrada_Sala.get() + "', '" + self.entrada_polo.get() + "', '" + self.entrada_andar.get() + "')"
                    c.execute(sql)
                    self.conexao.commit()
                    messagebox.showinfo('Caixa de Mensagem', 'Dados Inseridos com sucesso!')
            except Error as ex:
                print('Não inseriu', ex)


#------------------ Fora da Classe ------------------

def conexaoBanco():
    caminho = 'C:\\projeto\\banco\\integração\\banco.db'
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
        print('Conexao aceita')
    except Error as ex:
        print('Erro de conexão:', ex)
    return conexao

janela = tk.Tk()
conexao = conexaoBanco()
objeto = Cadastrar_Curso(janela, conexao)
janela.mainloop()
conexao.close()