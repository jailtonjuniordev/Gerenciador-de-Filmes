import PySimpleGUI as sg
import src.controller as c


def mostrar_tela_adc_filmes(janela):
    janela['-TELA_ADC_FILME_ASSISTIDO-'].update(visible=False)
    janela['-TELA_LISTAR_FILME-'].update(visible=False)
    janela['-TELA_ADC_FILME-'].update(visible=True)
    janela['-TELA_OUTROS-'].update(visible=False)
    janela['-TITULO-'].update(visible=False)
    janela['-TELA_OUTROS_EDITAR-'].update(visible=False)
    janela['-TELA_OUTROS_DELETAR-'].update(visible=False)

def mostrar_tela_adc_filme_assistido(janela):
    janela['-TELA_ADC_FILME_ASSISTIDO-'].update(visible=True)
    janela['-TELA_LISTAR_FILME-'].update(visible=False)
    janela['-TELA_ADC_FILME-'].update(visible=False)
    janela['-TELA_OUTROS-'].update(visible=False)
    janela['-TELA_OUTROS_EDITAR-'].update(visible=False)
    janela['-TELA_OUTROS_DELETAR-'].update(visible=False)
    janela['-TITULO-'].update(visible=False)

def mostrar_tela_listar_filmes(janela):
    janela['-TELA_ADC_FILME_ASSISTIDO-'].update(visible=False)
    janela['-TELA_LISTAR_FILME-'].update(visible=True)
    janela['-TELA_ADC_FILME-'].update(visible=False)
    janela['-TELA_OUTROS-'].update(visible=False)
    janela['-TITULO-'].update(visible=False)
    janela['-TELA_OUTROS_EDITAR-'].update(visible=False)
    janela['-TELA_OUTROS_DELETAR-'].update(visible=False)

def mostrar_tela_outros(janela):
    janela['-TELA_ADC_FILME_ASSISTIDO-'].update(visible=False)
    janela['-TELA_LISTAR_FILME-'].update(visible=False)
    janela['-TELA_ADC_FILME-'].update(visible=False)
    janela['-TELA_OUTROS-'].update(visible=True)
    janela['-TITULO-'].update(visible=False)
    janela['-TELA_OUTROS_EDITAR-'].update(visible=False)
    janela['-TELA_OUTROS_DELETAR-'].update(visible=False)

def mostrar_tela_outros_editar(janela):
    janela['-TELA_ADC_FILME_ASSISTIDO-'].update(visible=False)
    janela['-TELA_LISTAR_FILME-'].update(visible=False)
    janela['-TELA_ADC_FILME-'].update(visible=False)
    janela['-TELA_OUTROS-'].update(visible=False)
    janela['-TITULO-'].update(visible=False)
    janela['-TELA_OUTROS_EDITAR-'].update(visible=True)
    janela['-TELA_OUTROS_DELETAR-'].update(visible=False)

def mostrar_tela_outros_deletar(janela):
    janela['-TELA_ADC_FILME_ASSISTIDO-'].update(visible=False)
    janela['-TELA_LISTAR_FILME-'].update(visible=False)
    janela['-TELA_ADC_FILME-'].update(visible=False)
    janela['-TELA_OUTROS-'].update(visible=False)
    janela['-TITULO-'].update(visible=False)
    janela['-TELA_OUTROS_EDITAR-'].update(visible=False)
    janela['-TELA_OUTROS_DELETAR-'].update(visible=True)



def tela1(valor):
    c.verificarConexao()
    btn_adc = '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'
    btn_assistir = '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'
    btn_listar_filmes = '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'
    btn_outros = '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'
    menu = [
        [sg.Text(' '*32),
         sg.Button(image_data=btn_adc, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()), tooltip="Adicionar novo Filme", key='-ADICIONAR_FILME-'),
         sg.Text('   '),
         sg.Button(image_data=btn_assistir, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()), tooltip="Marcar filmes como assistidos", key='-ADICIONAR_FILMES_ASSISTIDOS-'),
         sg.Text('   '),
         sg.Button(image_data=btn_listar_filmes, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()), tooltip="Listar Filmes", key='-LISTAR_FILMES-'),
         sg.Text('   '),
         sg.Button(image_data=btn_outros, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()), tooltip="Outras Opções", key='-OUTROS-')
         ],
        
    ]
    
    categorias = ["Ação", "Anime", "Brasileiros", "Clássicos", "Comédia", "Comédia stand-up", "Documentários", "Drama", "Esportes", "Estrangeiros", "Fantasia", "Fé e espiritualidade",
                  "Ficção cientifica", "Músicais", "Para a familia toda", "Policial", "Romance", "Suspense", "Terror"]
    frame_adc_filme = [
        [sg.Text('Adicionar novo filme', size=(680,0), justification='center', font=("Futura, 16"))],
        [sg.Text('Nome do Filme *', size=(15,0)), sg.Input(size=(680,5), border_width=0, key='-NOME_FILME-',do_not_clear=False)],
        [sg.Text('Sinopse', size=(15,0)), sg.Multiline(size=(680,5), key='-SINOPSE-', do_not_clear=False)],
        [sg.Text('Data de Lançamento *', size=(15,0)), sg.Input(size=(680,5), border_width=0, key='-LANCAMENTO_FILME-', do_not_clear=False)],
        [sg.Text('Categoria *', size=(15,0)), sg.Combo(values=categorias, default_value='Selecionar Categoria', size=(680,5), readonly=True, key='-CATEGORIA_FILME-',  )],
        [sg.Text()],
        [sg.Text(' '*30),
        sg.Button('Salvar Novo Filme', border_width=0, size=(30,2), font=("Neuton, 16"), key='-SALVAR_DADOS_FILME-')]
            
    ]
    adc_filme = [
        [sg.Frame(layout=frame_adc_filme, title='', border_width=0)],
        
    ]

    cabeca = ["ID", "Nome do Filme", "Lançamento"]
    
    frame_filme_assistido = [
        [sg.Text('Adicionar filme a lista de assistidos', size=(680,0), justification='center', font=("Futura, 16"))],
    ]
    adc_filme_assistido = [
        [sg.Frame(layout=frame_filme_assistido, title='', border_width=0)],
        [sg.Text('ID do filme: '), sg.Input(size=(30,2), key='-ID_DESEJADO-', do_not_clear=False), sg.Button('Marcar como Assistido', key='-MARCAR_COMO_VISTO-')],
        [sg.Table(values=recuperarFilmesNaoAssistidos(), headings=cabeca, auto_size_columns=False,
                  col_widths=[5,30,20],
                  justification='center',
                  key='-FILMES_NAO_VISTOS-')],
        [sg.Button('Atualizar Lista', key='-ATUALIZAR_LISTA_FILMES_NAO_VISTOS-')]
        
    ]
    
    cabeca_todos = ['Nome do Filme', 'Sinopse', 'Data de Lançamento', "Assistido"]
    
    frame_listar_filme = [
         [sg.Text('Filmes cadastrados', size=(680,0), justification='center', font=("Futura, 16"))],
    ]
    listar_filme = [
        [sg.Frame(layout=frame_listar_filme, title='', border_width=0)],
        [sg.Button('Atualizar Lista', key='-ATUALIZAR_LISTA_FILMES_TOTAIS-')],
        [sg.Table(values=recuperarTodosFilmesCadastrados(), headings=cabeca_todos,
                   auto_size_columns=False, 
                   col_widths=[13,25,15,15],
                   row_height=45,
                   justification='center',
                   key='-TODOS_FILMES_CADASTRADOS-'
                   )],
         
    ]
    
    frame_outros = [
        [sg.Text('Outras Opções', size=(680,0), justification='center', font=("Futura, 16"))]
    ]
    
    btn_edit = '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'
    btn_del = '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'
    
    outros = [
        [sg.Frame(layout=frame_outros, title='', border_width=0)],
        [sg.Button(image_data=btn_edit, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()), tooltip="Editar Filme Cadastrado", key='-EDITAR_FILME-'),
        sg.Text('   '),
        sg.Button(image_data=btn_del, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()), tooltip="Excluir Filme Cadastrado", key='-EXCLUIR_FILME-'),],
    ]
    
    
    
    
    
    nome_filme = ''; sinopse = ''; data_lancamento = ''; categoria = '';
    
    frame_outros_editar = [
        [sg.Text('Editar Filme', size=(680,0), justification='center', font=("Futura, 16"))],
        [sg.Text('ID do Filme', size=(15,0)), sg.Input(border_width=0, key='-ID_FILME_SELECIONADO-'), sg.Button('Pesquisar Filme', border_width=0, key='-PESQUISAR_FILME_INDICADO-', size=(320,0))],
        [sg.Text('Nome do Filme *', size=(15,0)), sg.Input(f'{nome_filme}',size=(680,5), border_width=0, key='-NOME_FILME_EDITO-',do_not_clear=False)],
        [sg.Text('Sinopse', size=(15,0)), sg.Multiline(f'{sinopse}', size=(680,5), key='-SINOPSE_EDITADO-', do_not_clear=False)],
        [sg.Text('Data de Lançamento *', size=(15,0)), sg.Input(f'{data_lancamento}', size=(680,5), border_width=0, key='-LANCAMENTO_FILME_EDITADO-', do_not_clear=False)],
        [sg.Text('Categoria *', size=(15,0)), sg.Combo(values=categorias, default_value=f'{categoria}', size=(680,5), readonly=True, key='-CATEGORIA_FILME_EDITADO-',  )],
        [sg.Text()],
        [sg.Text(' '*30),
        sg.Button('Alterar Filme', border_width=0, size=(30,2), font=("Neuton, 16"), key='-SALVAR_DADOS_FILME_EDITADO-')]
    ]
    
    outros_editar = [
        [sg.Frame(layout=frame_outros_editar, title='', border_width=0)],
    ]
    
    frame_outros_deletar = [
        [sg.Text('Deletar Filme', size=(680,0), justification='center', font=("Futura, 16"))],
        
    ]
    
    cabeca_todos = ['ID', 'Nome do Filme', 'Sinopse', 'Data de Lançamento', "Assistido"]
    
    outros_deletar = [
        [sg.Frame(layout=frame_outros_deletar, title='', border_width=0)],
        [sg.Text('ID do filme: '), sg.Input(size=(30,2), key='-ID_DESEJADO_EXCLUIR-', do_not_clear=False), sg.Button('Excluir Filme', key='-EXCLUIR_FILME_SELECIONADO-')],
        [sg.Button('Atualizar Lista', key='-ATUALIZAR_LISTA_FILMES_PARA_EXCLUIR-')],
        [sg.Table(values=c.recuperarFilmesCID(), headings=cabeca_todos,
                   auto_size_columns=False, 
                   col_widths=[5,13,25,15,15],
                   row_height=45,
                   justification='center',
                   key='-TODOS_FILMES_CADASTRADOS_EXCLUIR-'
                   )],
    ]
    
    
    layout = [
        [sg.Column(menu, element_justification='center', key='-MENU_PRINCIPAL-')],
        [sg.HSeparator()],
        [sg.Text("Selecione algum menu acima!", size=(680,0), justification='center', font=("Futura, 30"), key='-TITULO-'),
         sg.Column(adc_filme, element_justification='center', visible=False, key='-TELA_ADC_FILME-'),
         sg.Column(adc_filme_assistido, element_justification='center', visible=False, key='-TELA_ADC_FILME_ASSISTIDO-'),
         sg.Column(listar_filme, element_justification='center', visible=False, key='-TELA_LISTAR_FILME-'),
         sg.Column(outros, element_justification='center', visible=False, key='-TELA_OUTROS-'),
         sg.Column(outros_editar, element_justification='center', visible=False, key='-TELA_OUTROS_EDITAR-'),
         sg.Column(outros_deletar, element_justification='center', visible=False, key='-TELA_OUTROS_DELETAR-'),
         ]
    ]

    return sg.Window("Gerenciador de Filmes", layout=layout, finalize=True, size=(680,480), grab_anywhere_using_control=False)


def inserirNovoFilme(valor):
    c.validarInput(valor)
    
def recuperarFilmesNaoAssistidos():
    dados = c.filmesNaoAssistidos()
    return dados



def marcarVistoAcao(id_filme, janela):
    if id_filme.strip() != '':
        c.marcarComoVisto(id_filme, janela)
    else:
        sg.popup('O campo ID não pode estar vazio!', title='Erro')

def atualizarTabelaFilmesNaoVistos(janela):
    janela['-FILMES_NAO_VISTOS-'].update(recuperarFilmesNaoAssistidos())
  
def atualizarTabelaFilmesTotais(janela):
    janela['-TODOS_FILMES_CADASTRADOS-'].update(recuperarTodosFilmesCadastrados())
  
def recuperarTodosFilmesCadastrados():
    dados = c.recuperarFilmesCadastrados()
    return dados

def atualizarTabelaFilmesExcluir(janela):
    janela['-TODOS_FILMES_CADASTRADOS_EXCLUIR-'].update(c.recuperarFilmesCID())

def excluirFilmeSelecionado(id_filme):
    c.excluirFilmeSelecionadoController(id_filme)
    
def preencherCamposIDSelecionado(id_filme):
    dados = c.PreencherCamposIDSelecionadoController(id_filme)
    return dados