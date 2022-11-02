import sqlite3
from sqlite3 import Error

def conexaoBanco():
    # caminho = 'Modelo Banco de dados\\bancoDedados.sql'
    caminho = 'Modelo Banco de dados\\bancoDedados.db'
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
        print('Conexao aceita')
    except Error as ex:
        print('Erro de conexão:', ex)
    return conexao

conexao = conexaoBanco()

def comandosSQL(sql):
    conexao = conexaoBanco()
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    conexao.close()
    return resultado


def testesalas():
    sql = 'SELECT * FROM salas order by nome'
    linhas = comandosSQL(sql)
    dicionario_salas = {}
    for i in linhas:
        dicionario_salas[i[0]] = i

    c = conexao.cursor()
    # c.execute("SELECT * FROM tb_login WHERE usuario = ? AND senha = ?", (self.campo1.get(), self.campo2.get()))
    c.execute(sql)
    c.close()
    return dicionario_salas