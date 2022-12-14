from tkinter import *
import tkinter as tk
from tkinter import ttk


def telaEditarSala():
    class TelaEditarSala:
        def __init__(self, janela_salas_edicao):
            self.editar_salas = janela_salas_edicao
            self.editar_salas.title('Cadastrar Salas')  # Trocar o título da janela
            self.editar_salas.iconbitmap('icone.ico')  # Verificar se tem o ícone no seu arquivo
            self.editar_salas.geometry('1440x750+50+10')
            self.editar_salas['bg'] = '#F5F5F5'
            self.editar_salas.resizable(width=False, height=False)

            self.label_superior = tk.Label(self.editar_salas, bg='#004AAD')
            self.label_superior.place(relx=0, relwidth=1, relheight=0.08, rely=0)

            self.senac_logo = tk.PhotoImage(file=r'..\ProjetoFinal\logo_simbolo.png')
            self.senac_tituloPag = tk.Label(self.editar_salas,text='Editar Salas', font='Inter 26 bold')
            self.label_senac_logo = tk.Label(self.editar_salas, image=self.senac_logo)
            self.label_senac_logo.place(relx=0.1, rely=0.13)
            self.senac_tituloPag.place(relx=0.19, rely=0.15)

            # Entradas
            self.label_polo = tk.Label(self.editar_salas, bg='#F5F5F5', text='Polo:', font='Inter 17 bold',
                                       anchor='w')
            self.label_polo.place(relx=0.513, relwidth=0.08, rely=0.23, relheight=0.035)
            self.entrada_polo = ttk.Combobox(self.editar_salas, width=12,
                                             values=['Faculdade Senac', 'Recife Sede', 'Aprendizagem'])
            self.entrada_polo.current()
            self.entrada_polo.place(relx=0.57, relwidth=0.213, rely=0.23, relheight=0.035)

            self.label_nome_sala = tk.Label(self.editar_salas, bg='#F5F5F5', text='Nome:', font='Inter 17 bold',
                                            anchor='w')
            self.label_nome_sala.place(relx=0.16, relwidth=0.08, rely=0.33, relheight=0.035)
            self.entrada_nome_sala = tk.Entry(self.editar_salas, bg='#D9D9D9')
            self.entrada_nome_sala.place(relx=0.247, relwidth=0.213, rely=0.33, relheight=0.035)

            self.label_cadeiras = tk.Label(self.editar_salas, bg='#F5F5F5', text='Cadeiras:', font='Inter 17 bold',
                                           anchor='w')
            self.label_cadeiras.place(relx=0.16, relwidth=0.075, rely=0.4, relheight=0.035)
            self.entrada_cadeiras = tk.Entry(self.editar_salas, bg='#D9D9D9')
            self.entrada_cadeiras.place(relx=0.242, relwidth=0.218, rely=0.4, relheight=0.035)

            self.label_computadores = tk.Label(self.editar_salas, bg='#F5F5F5', text='Computadores:',
                                               font='Inter 17 bold',
                                               anchor='w')
            self.label_computadores.place(relx=0.16, relwidth=0.12, rely=0.47, relheight=0.035)
            self.entrada_computadores = tk.Entry(self.editar_salas, bg='#D9D9D9')
            self.entrada_computadores.place(relx=0.286, relwidth=0.174, rely=0.47, relheight=0.035)

            self.label_televisores = tk.Label(self.editar_salas, bg='#F5F5F5', text='Televisores:',
                                              font='Inter 17 bold',
                                              anchor='w')
            self.label_televisores.place(relx=0.16, relwidth=0.096, rely=0.54, relheight=0.035)
            self.entrada_televisores = tk.Entry(self.editar_salas, bg='#D9D9D9')
            self.entrada_televisores.place(relx=0.263, relwidth=0.197, rely=0.54, relheight=0.035)

            self.label_Tela_retratil = tk.Label(self.editar_salas, bg='#F5F5F5', text='Tela retrátil:',
                                                font='Inter 17 bold',
                                                anchor='w')
            self.label_Tela_retratil.place(relx=0.16, relwidth=0.096, rely=0.61, relheight=0.035)
            self.entrada_Tela_retratil = tk.Entry(self.editar_salas, bg='#D9D9D9')
            self.entrada_Tela_retratil.place(relx=0.263, relwidth=0.197, rely=0.61, relheight=0.035)

            self.label_andar = tk.Label(self.editar_salas, bg='#F5F5F5', text='Andar:', font='Inter 17 bold',
                                        anchor='w')
            self.label_andar.place(relx=0.515, relwidth=0.0443, rely=0.33, relheight=0.035)
            self.entrada_andar = tk.Entry(self.editar_salas, bg='#D9D9D9')
            self.entrada_andar.place(relx=0.5633, relwidth=0.2517, rely=0.33, relheight=0.035)

            self.label_mesas = tk.Label(self.editar_salas, bg='#F5F5F5', text='Mesas:', font='Inter 17 bold',
                                        anchor='w')
            self.label_mesas.place(relx=0.515, relwidth=0.057, rely=0.4, relheight=0.035)
            self.entrada_mesas = tk.Entry(self.editar_salas, bg='#D9D9D9')
            self.entrada_mesas.place(relx=0.576, relwidth=0.239, rely=0.4, relheight=0.035)

            self.label_projetores = tk.Label(self.editar_salas, bg='#F5F5F5', text='Projetores:',
                                             font='Inter 17 bold', anchor='w')
            self.label_projetores.place(relx=0.515, relwidth=0.09, rely=0.47, relheight=0.039)
            self.entrada_projetores = tk.Entry(self.editar_salas, bg='#D9D9D9')
            self.entrada_projetores.place(relx=0.609, relwidth=0.206, rely=0.47, relheight=0.035)

            self.label_quadros = tk.Label(self.editar_salas, bg='#F5F5F5', text='Quadros:', font='Inter 17 bold',
                                          anchor='w')
            self.label_quadros.place(relx=0.515, relwidth=0.075, rely=0.54, relheight=0.035)
            self.entrada_quadros = tk.Entry(self.editar_salas, bg='#D9D9D9')
            self.entrada_quadros.place(relx=0.594, relwidth=0.221, rely=0.54, relheight=0.035)

            self.label_ar_condicionado = tk.Label(self.editar_salas, bg='#F5F5F5', text='Ar-condicionado:',
                                                  font='Inter 17 bold',
                                                  anchor='w')
            self.label_ar_condicionado.place(relx=0.515, relwidth=0.14, rely=0.61, relheight=0.035)
            self.entrada_ar_condicionado = tk.Entry(self.editar_salas, bg='#D9D9D9')
            self.entrada_ar_condicionado.place(relx=0.659, relwidth=0.157, rely=0.61, relheight=0.035)

            self.botao_cadastrar_cadastrar_sala = tk.Button(self.editar_salas, text='Editar', fg='white',
                                                            bg='#004AAD',
                                                            font='Inter 17 bold',
                                                            relief=FLAT)
            self.botao_cadastrar_cadastrar_sala.place(relx=0.3, relwidth=0.12, rely=0.75, relheight=0.07)
            self.botao_cadastrar_cadastrar_sala.bind('<Any-Button>')

            self.botao_pesquisar_sala = tk.Button(self.editar_salas, text='Pesquisar', fg='white',
                                                  bg='orange',
                                                  font='Inter 17 bold',
                                                  relief=FLAT)
            self.botao_pesquisar_sala.place(relx=0.6, relwidth=0.12, rely=0.75, relheight=0.07)
            self.botao_pesquisar_sala.bind('<Any-Button>')

            self.label_inferior = tk.Label(self.editar_salas, bg='#004AAD')
            self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)

    janela_salas_geral = tk.Toplevel()
    objetoSalasGeral = TelaEditarSala(janela_salas_geral)
    janela_salas_geral.mainloop()
