def existeArquivo(nomeArquivo):
    """
    Verifica se o arquivo já existe no sistema.

    Args:
        nomeArquivo (str): Nome do arquivo a ser verificado.

    Returns:
        bool: True se o arquivo existir, False caso contrário.
    """
    try:
        file = open(nomeArquivo, 'r')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def abrirArquivoLeitura(nomeArquivo):
    """
    Abre o arquivo para leitura.

    Args:
        nomeArquivo (str): Nome do arquivo a ser aberto.

    Returns:
        file: Objeto de arquivo aberto para leitura.
        None: Caso ocorra um erro ao abrir o arquivo.
    """
    try:
        file = open(nomeArquivo, 'r')
    except FileNotFoundError:
        print(f'Erro: O arquivo {nomeArquivo} não foi encontrado.')
        return None
    except PermissionError:
        print(f'Erro: Permissão negada para ler o arquivo {nomeArquivo}.')
        return None
    except:
        print(f'Erro: Não foi possível abrir o arquivo {nomeArquivo}.')
        return None
    else:
        print(f'Arquivo {nomeArquivo} aberto com sucesso!')
        return file
        
def criaArquivo(nomeArquivo):
    """
    Cria um novo arquivo.
    
    Args:
        nomeArquivo(str): Nome do arquivo a ser criado.
    
    Returns:
        None
    """
    try:
        file = open(nomeArquivo, 'w+')
        file.close()
    except:
        print(f'Erro: Não foi possível criar o arquivo {nomeArquivo}.')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso!')	

def listarArquivo(nomeArquivo):
    """
    Abre o arquivo para leitura e retorna seu conteúdo.
    
    Args:
        nomeArquivo (str): Nome do arquivo a ser lido.
        
    Returns:
        list: Lista com o conteúdo do arquivo
    """
    try:
        file = open(nomeArquivo, 'r')
    except FileNotFoundError:
        print(f'Erro: O arquivo {nomeArquivo} não foi encontrado.')
        return None
    except PermissionError:
        print(f'Erro: Permissão negada para ler o arquivo {nomeArquivo}.')
        return None
    except:
        print(f'Erro: Não foi possível abrir o arquivo {nomeArquivo}.')
        return None
    else:
        dados = file.readlines()
    finally:
        file.close()
        return dados
    
def inserirCadastro(nomeArquivo, provaRef, nomeAluno, notaAluno):
    """
    Insere um novo cadastro no arquivo.
    
    Args:
        nomeArquivo (str): Nome do arquivo onde o cadastro será inserido.
        provaRef (str): Referência da prova.
        nomeAluno (str): Nome do aluno.
        notaAluno (float): Nota do aluno.
        
    Returns:
        None
    """
    try:
        file = open(nomeArquivo, 'a')
    except FileNotFoundError:
        print(f'Erro: O arquivo {nomeArquivo} não foi encontrado.')
        return None
    except PermissionError:
        print(f'Erro: Permissão negada para ler o arquivo {nomeArquivo}.')
        return None
    except:
        print(f'Erro: Não foi possível abrir o arquivo {nomeArquivo}.')
        return None
    else:
        file.write(f'{provaRef.capitalize()};{nomeAluno.capitalize()};{notaAluno}\n')
    finally:
        file.close()