"""
NO DESAFIO FOI PROPOSTO QUE BUSCASSEMOS EM UM ARQUIVO CSV IDS DE DETERMINADOS USUARIOS
COM ESSE IDS COMSUMIRIAMOS DA API "SANTANDER DEV WEEK" INFORMAÇOES QUE SERIA USADO EM UMA FICTICIA CAMPANHA
DE MARKETING BANCARIO, DA API DO CHAT GPT SERIA CONSUMIDO DO UMA MENSAGEM QUE MOSTRASSE AS VANTAGEMS DE
INVESTIR A CADA USUARIO

NAO FOI POSSIVEL USAR A API DO CHAT ENTAO ESTOU PROPONTO ESSA SOLUÇÃO COM DICIONARIOS
UTILIZANDO OS CONCEITOS DE ETL PASSADOS NA LAB

Extração
Transformação
Load(carregamento) -> que sera feito em um banco de dados sqlite3 para simular o envio de volta a api SANTANDER DEV WEEK
"""
# IMPORTANDO LIB NECESSARIA
import pandas as pd
from banco_sqlite import *

# EXTRAINDO DO ARQUIVO CSV OS IDS
retorno_do_arquivo = pd.read_csv(r"C:\Users\Usuario\Desktop\estud\Bootcamp_Santander\desafio_ETL\users.csv")
# RETORNADO OS IDs PRESENTE NO ARQUIVO EM FORMATO DE LISTA
id_usuario = retorno_do_arquivo["userID"].tolist()

# DICIONARIO COM INFORMAÇOES
# LISTA DE DICIONARIO COM INFORMAÇOES DOs USUARIOS
informacoes_users = [
    {"id": 1, "nome": "leonardo", "idade": 25},
    {"id": 2, "nome": "paula","idade": 30},
    {"id": 10, "nome": "pedro","idade": 12},
    {"id": 5, "nome": "joao","idade": 45},
    {"id": 100, "nome": "laura","idade": 50},
    {"id": 101, "nome": "jubileu","idade": 30} # id nao presente no arquivo
]

def filtrando_informacoes_do_usuario(info_user:list,id_user:list):
    # FILTRANDO INFORMAÇOES DO DICIONARIO COM BASE NOS IDs PRESENTE NO ARQUIVO
    for info_do_dic in info_user: # passando em cada dicionario na lista
        for user_id in id_user: # passando em cada id na lista
            _ids = user_id # ids resgatados da lista 
            if info_do_dic["id"] == _ids: # comparando id da lista com id nas informaçoes do usuario
                mensagem_para_usuarios(id_user=info_do_dic["id"],name=info_do_dic["nome"]) # CHAMANDO FUNÇÃO QUE MOSTRA A MENSAGEM DE INVESTIMENTOS

# FUNÇÃO QUE VAI CRIAR UMA MENSAGEM PERSONALISADA PARA OS USUARIOS
def mensagem_para_usuarios(id_user:int,name:str):
    mensagem = f"""
    Ola \033[32m{name}\033[m Transforme Seu Dinheiro em Conquistas com Nossos Investimentos Bancários!
    Você já imaginou ter seu dinheiro trabalhando para você, gerando renda e construindo um futuro sólido?
    Com os nossos produtos de investimento bancário, essa possibilidade está ao seu alcance!
    \033[32m{name}\033[m Ao investir, você permite que seu dinheiro cresça ao longo do tempo, superando a simples poupança.
    Colocamos à sua disposição uma variedade de opções para atender suas metas financeiras, seja a curto, médio ou longo prazo.\n\n
    """
    criando_tabela()
    adicionando_no_banco_de_dados(_id=id_user,nome=name,msg=mensagem)
    print(mensagem)

filtrando_informacoes_do_usuario(info_user=informacoes_users,id_user=id_usuario)