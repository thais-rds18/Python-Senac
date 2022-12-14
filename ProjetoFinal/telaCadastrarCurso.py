from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
import sqlite3
from sqlite3 import Error
from tkinter import messagebox

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
            self.label_nome = tk.Label(self.janela_cadastrar_curso, bg='#F5F5F5', text='Nome:', font='Inter 17 bold', anchor='w')
            self.label_nome.place(relx=0.05, relwidth=0.08, rely=0.25, relheight=0.05)
            self.entrada_nome = tk.Entry(self.janela_cadastrar_curso, bg='#D9D9D9', font='Inter 17')
            self.entrada_nome.place(relx=0.15, relwidth=0.40, rely=0.25, relheight=0.045)

            self.label_Hora_Total = tk.Label(self.janela_cadastrar_curso, text='Carga Horária Total:', bg='#F5F5F5', font='Inter 17 bold',
                                             anchor='w')
            self.label_Hora_Total.place(relx=0.05, relwidth=0.30, rely=0.35, relheight=0.05)
            self.entrada_Hora_Total = tk.Entry(self.janela_cadastrar_curso, bg='#D9D9D9', font='Inter 17')
            self.entrada_Hora_Total.place(relx=0.37, relwidth=0.17, rely=0.35, relheight=0.045)

            self.label_Hora_Diaria = tk.Label(self.janela_cadastrar_curso, text='Carga Horária Diária:', bg='#F5F5F5',
                                          font='Inter 17 bold', anchor='w')
            self.label_Hora_Diaria.place(relx=0.05, relwidth=0.30, rely=0.45, relheight=0.05)
            self.entrada_Hora_Diaria = tk.Entry(self.janela_cadastrar_curso, bg='#D9D9D9', font='Inter 17')
            self.entrada_Hora_Diaria.place(relx=0.37, relwidth=0.17, rely=0.45, relheight=0.045)

            self.label_Turno = tk.Label(self.janela_cadastrar_curso, bg='#F5F5F5', text='Turno:', font='Inter 17 bold', anchor='w')
            self.label_Turno.place(relx=0.56, relwidth=0.09, rely=0.25, relheight=0.05)
            self.entrada_Turno = ttk.Combobox(self.janela_cadastrar_curso, values=[" ", "Manhã", "Tarde", "Noite"], font='Inter 17')
            self.entrada_Turno.current(0)
            self.entrada_Turno.bind("<<ComboboxSelected>>")
            self.entrada_Turno.place(relx=0.66, relwidth=0.29, rely=0.25, relheight=0.045)

            self.label_inicio = tk.Label(self.janela_cadastrar_curso, bg='#F5F5F5', text='Início:', font='Inter 17 bold', anchor='w')
            self.label_inicio.place(relx=0.56, relwidth=0.09, rely=0.35, relheight=0.05)
            self.entrada_inicio = DateEntry(self.janela_cadastrar_curso, locale='pt_BR', dateformat='DD/MM/YYYY', font='Inter 17')
            self.entrada_inicio.place(relx=0.66, relwidth=0.28, rely=0.35, relheight=0.045)

            self.label_fim = tk.Label(self.janela_cadastrar_curso, bg='#F5F5F5', text='Fim:', font='Inter 17 bold', anchor='w')
            self.label_fim.place(relx=0.56, relwidth=0.08, rely=0.45, relheight=0.05)
            self.entrada_fim = DateEntry(self.janela_cadastrar_curso, locale='pt_BR', dateformat='DD/MM/YYYY', font='Inter 17')
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
            self.entrada_polo = ttk.Combobox(self.janela_cadastrar_curso, values=[" ", "Faculdade Senac", "Recife Sede", "Aprendizagem"],
                                         font='Inter 17')
            self.entrada_polo.current(0)
            self.entrada_polo.bind("<<ComboboxSelected>>")
            self.entrada_polo.place(relx=0.15, relwidth=0.39, rely=0.65, relheight=0.045)

            self.label_andar = tk.Label(self.janela_cadastrar_curso, bg='#F5F5F5', text='Andar:',
                                    font='Inter 16 bold', anchor='w')
            self.label_andar.place(relx=0.56, relwidth=0.21, rely=0.65, relheight=0.035)
            self.entrada_andar = ttk.Combobox(self.janela_cadastrar_curso, values=[" ", "1", "2", "3", "4", "5", "6", "7"],
                                          font='Inter 17')
            self.entrada_andar.current(0)
            self.entrada_andar.bind('<<ComboboxSelected>>')
            self.entrada_andar.place(relx=0.66, relwidth=0.25, rely=0.65, relheight=0.045)

            self.botao_cadastrar_cadastrar_curso = tk.Button(self.janela_cadastrar_curso, text='Cadastrar', fg='white', bg='#004AAD',
                                                         font='Inter 17 bold',
                                                         relief=FLAT, command=lambda: self.cadastrarCurso())
            self.botao_cadastrar_cadastrar_curso.place(relx=0.42, relwidth=0.15, rely=0.79, relheight=0.07)

            self.label_inferior = tk.Label(self.janela_cadastrar_curso, bg='#004AAD')
            self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)

        def cadastrarCurso(self):
            try:
                self.validar_cadastro_curso = list()
                self.validar_cadastro_curso = [self.entrada_nome.get(), self.entrada_Hora_Total.get(),
                                               self.entrada_Hora_Diaria.get(), self.entrada_Turno.get(),
                                               self.entrada_inicio.get(), self.entrada_fim.get(),
                                               self.entrada_CPF_professor.get(), self.entrada_Sala.get(),
                                               self.entrada_polo.get(), self.entrada_andar.get()]

                for cadaResposta in self.validar_cadastro_curso:
                    analise = bool(cadaResposta)
                    if analise == False or cadaResposta.isspace() == True:
                        messagebox.showinfo('Alerta', 'Preencha corretamente todos os campos')
                        break

                self.validar_numeros_cadastro_cruso = list()
                self.validar_numeros_cadastro_cruso = [self.entrada_Hora_Total.get(), self.entrada_Hora_Diaria.get(),
                                                       self.entrada_CPF_professor.get()]

                for cadaItem in self.validar_numeros_cadastro_cruso:
                    if cadaItem.isnumeric() == False:
                        messagebox.showerror('Erro de Entrada', 'Os campos:\n- Carga Horária Total \n- Carga Horária Diária \n- CPF do Professor'
                                                                '\naceitam somente números!')
                        break
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
                turno = "UPDATE salas SET ocupado_manha = True WHERE nome = '" + self.entrada_Sala.get() + "' AND polo = '"+self.entrada_polo.get()+"' AND andar = '" + self.entrada_andar.get() +"';"

            if self.entrada_Turno.get() == 'Tarde':
                turno = f"UPDATE salas SET ocupado_tarde = True WHERE nome = '" + self.entrada_Sala.get() + "' AND polo = '"+self.entrada_polo.get()+"' AND andar = '" + self.entrada_andar.get() +"';"

            if self.entrada_Turno.get() == 'Noite':
                turno = f"UPDATE salas SET ocupado_noite = True WHERE nome = '" + self.entrada_Sala.get() + "' AND polo = '"+self.entrada_polo.get()+"' AND andar = '" + self.entrada_andar.get() +"';"

            return turno
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


    janela_cadastrar_curso = tk.Toplevel()
    conexao = conexaoBanco()
    objetoCadastrarCurso = Cadastrar_Curso(janela_cadastrar_curso, conexao)
    janela_cadastrar_curso.mainloop()
    conexao.close()

