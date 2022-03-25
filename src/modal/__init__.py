from mimetypes import init
import mysql.connector
import PySimpleGUI as sg
import src.view as v

class conectarBanco:
    def __init__(self, host, user, password, banco_dados=None):
        self.host = host
        self.user = user
        self.password = password
        self.banco_dados = banco_dados

    def conectar(self):
        try:
            banco = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.banco_dados,
            )
            return banco
        except mysql.connector.errors.InterfaceError:
            font = ("Helvica, 16")
            return 0
        
class Operacoes: 
    try:
        conexao = conectarBanco('localhost', 'root', '', 'bd_filmes')
        banco = conexao.conectar()
        cursor = banco.cursor()
    except Exception as error:
        pass

class InserirDados:
    def InserirFilme(nome_filme, sinopse, data_lancamento, categoria):
        try:
            Operacoes.cursor.execute(f"INSERT INTO filmes (id_filme, nome_filme, sinopse, data_lancamento, genero, assistido) VALUES(null, '{nome_filme}', '{sinopse}', '{data_lancamento}', '{categoria}', 0)")
            Operacoes.banco.commit()
            sg.popup('Filme adicionado a lista com sucesso!', title='Sucesso')
            
        except Exception as Error:
            sg.popup(f'Erro inesperado\n{Error}', title='Erro')
        
            
            
def recuperarDadosnaoAssistidos():
    try:
        Operacoes.cursor.execute(f'SELECT id_filme, nome_filme, data_lancamento FROM filmes WHERE assistido = 0')
        dados = Operacoes.cursor.fetchall()
    except Exception as Error:
        sg.popup(f'Erro inesperado\n{Error}', title='Erro')
    else:
            return dados
  
        
def marcarFilmeComoVisto(id_filme, janela):
    try:
        Operacoes.cursor.execute(f'SELECT assistido FROM filmes WHERE id_filme = {id_filme}')
        assistido = Operacoes.cursor.fetchone()
        Operacoes.cursor.execute(f'SELECT id_filme FROM filmes')
        ids = Operacoes.cursor.fetchall()
        if assistido[0] == 1:
            sg.popup('o ID indicado já está marcado como assistido!\nTente um novo ID', title='Erro')
        elif id_filme not in ids:
            Operacoes.cursor.execute(f"UPDATE filmes SET assistido = 1 WHERE id_filme = '{id_filme}'")
            Operacoes.banco.commit()
            sg.popup('Filme marcado como assistido com sucesso!', title='Sucesso')
        else:
            sg.popup('ID não encontrado!\nTente novamente!', title='Erro')
        v.atualizarTabelaFilmesNaoVistos(janela)
    except Exception as Error:
        sg.popup(f'Erro inesperado\n{Error}', title='Erro')
        
        
def recuperarFilmesCadastradosAcao():
    try:
        Operacoes.cursor.execute('SELECT nome_filme, sinopse, data_lancamento, CASE assistido WHEN "0" THEN "Não" WHEN "1" THEN "Sim" END AS assistido FROM filmes')
        dados = Operacoes.cursor.fetchall()
        return dados
    except Exception as Error:
        sg.popup(f'Erro inesperado\n{Error}', title='Erro')
        
def recuperarFilmesCadastradosCIDAcao():
    try:
        Operacoes.cursor.execute('SELECT id_filme, nome_filme, sinopse, data_lancamento, CASE assistido WHEN "0" THEN "Não" WHEN "1" THEN "Sim" END AS assistido FROM filmes')
        dados = Operacoes.cursor.fetchall()
        return dados
    except Exception as Error:
        sg.popup(f'Erro inesperado\n{Error}', title='Erro')
        
        
def excluirFilmeSelecionadoAcao(id_filme):
    try:
        Operacoes.cursor.execute(f'DELETE FROM filmes WHERE id_filme = "{id_filme}"')
        Operacoes.banco.commit()
    except Exception as Error:
        sg.popup(f'Erro inesperado\n{Error}', title='Erro')
    else:
        sg.popup('Filme Excluido com Sucesso!', title='Sucesso')
    pass

def preencherCamposIDSelecionadoAcao(id_filme):
    try:
        Operacoes.cursor.execute(f'SELECT nome_filme, sinopse, data_lancamento, genero FROM filmes WHERE id_filme = "{id_filme}"')
        dados = Operacoes.cursor.fetchall()
    except Exception as Error:
        sg.popup(f'Erro inesperado\n{Error}', title='Erro')
    else:
        return dados