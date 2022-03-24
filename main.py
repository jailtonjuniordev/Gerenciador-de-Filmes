import src.view as view
import PySimpleGUI as sg


tela1 = view.tela1()


while True:
    janela, evento, valor = sg.read_all_windows()

    if evento == sg.WIN_CLOSED:
        if sg.popup('Deseja mesmo fechar o app ?', title='Confirmação', custom_text=('Sim', 'Não'), font=("Helvica, 14")) == 'Sim':  
            break
        else:
            pass
    
    elif evento == '-ADICIONAR_FILME-':
        view.mostrar_tela_adc_filmes(janela)
    
    elif evento == '-ADICIONAR_FILMES_ASSISTIDOS-':
        view.mostrar_tela_adc_filme_assistido(janela)
     
    elif evento == '-LISTAR_FILMES-':
        view.mostrar_tela_listar_filmes(janela)
        
    elif evento == '-OUTROS-':
        view.mostrar_tela_outros(janela)
                                        
    elif evento == '-SALVAR_DADOS_FILME-':
        view.inserirNovoFilme(valor)
        
    elif evento == '-MARCAR_COMO_VISTO-':
        view.marcarVistoAcao(valor['-ID_DESEJADO-'], janela)
    
    elif evento == '-ATUALIZAR_LISTA_FILMES_NAO_VISTOS-' or evento == '-ATUALIZAR_LISTA_FILMES_TOTAIS-':
        if evento == '-ATUALIZAR_LISTA_FILMES_NAO_VISTOS-':
            view.atualizarTabelaFilmesNaoVistos(janela)
        elif evento == '-ATUALIZAR_LISTA_FILMES_TOTAIS-':
            view.atualizarTabelaFilmesTotais(janela)
    
    
   