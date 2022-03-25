import src.modal as m
import PySimpleGUI as sg


def verificarConexao():
    verificador = m.conectarBanco("localhost", 'root', '', 'bd_filmes')
    font = ("Helvica, 16")
    if verificador.conectar() != 0:
        sg.popup('Conexão Estabelecida!\nClique abaixo para continuar!', title='Sucesso', font=font, )
    else:
        sg.popup('Servidor Offline!\nInicie o servidor e tente novamente!', title='Erro', font=font, )
        quit()
        
def validarInput(valor):
    apoio = valor['-LANCAMENTO_FILME-'].split('/'); apoio = ''.join(apoio)
    if valor['-NOME_FILME-'].strip() == '' or valor['-CATEGORIA_FILME-'] == 'Selecionar Categoria':
        sg.popup('Preencha os dados marcados com "*" para prosseguir', title='Campos Incompletos')
    elif not apoio.isdigit() or not len(valor['-LANCAMENTO_FILME-']) == 10:
        sg.popup('Preencha a data corretamente \nPreencha da seguinte forma: Dia/Mês/Ano')
    else:
        m.InserirDados.InserirFilme(valor['-NOME_FILME-'], valor['-SINOPSE-'], valor['-LANCAMENTO_FILME-'], valor['-CATEGORIA_FILME-'])
        
        
def filmesNaoAssistidos():
    dados = m.recuperarDadosnaoAssistidos()
    return dados

def marcarComoVisto(id_filme, janela):
    m.marcarFilmeComoVisto(id_filme, janela)
    
def recuperarFilmesCadastrados():
    dados = m.recuperarFilmesCadastradosAcao()
    return dados

def recuperarFilmesCID():
    dados = m.recuperarFilmesCadastradosCIDAcao()
    return dados

def excluirFilmeSelecionadoController(id_filme):
    m.excluirFilmeSelecionadoAcao(id_filme)
    
def PreencherCamposIDSelecionadoController(id_filme):
    dados = m.preencherCamposIDSelecionadoAcao(id_filme)
    return dados
    