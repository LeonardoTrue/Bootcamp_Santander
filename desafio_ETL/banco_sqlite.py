import sqlite3
from pathlib import Path
# PEGANDO LOCAL DA PASTA
LOCAL = Path(__file__).parent
NOME_BD = "usuario.db"
ABSOLUTO = LOCAL / NOME_BD
# ABRINDO CONEXAO
con = sqlite3.connect(ABSOLUTO)
cursor = con.cursor()


# CRIAR TABELA siMPLES PARA ARMAZENAR INFORMAÇOES DOS USUARIOS
def criando_tabela():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INT UNIQUE NOT NULL,
        nome VARCHAR(20) NOT NULL,
        mensagem TEXT 
        )
        """)
    con.commit()


# INSERINDO VALORES TRANSFORMADOS NA BASE DE DADOS
def adicionando_no_banco_de_dados(_id,nome,msg):
    cursor.execute(
        '''
        INSERT OR IGNORE INTO usuarios (id_usuario,nome,mensagem) 
        VALUES(?,?,?)''',(_id,nome,msg,))
    con.commit()






# CRIANDO TABELA

