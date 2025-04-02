# Importando as funções de arquivo
import funcoes_arquivo as fA

def cadastrar():
    """
    Cadastra um aluno e suas notas no sistema.
    """
    prova = input('Digite a prova de referência: ').lower()
    nome = input('Digite o nome do aluno: ').lower()
    nota = float(input('Digite a nota do aluno: '))

    # Salva os dados no arquivo de cadastros
    fA.inserirCadastro('cadastros_alunos.txt', prova, nome, nota)
    # Salva notas da turma para tirar a média
    fA.inserirCadastro('notas_gerais.txt', prova, nome, nota)
    # Salva notas no arquivo do aluno
    fA.inserirCadastro('notas_por_aluno.txt', prova, nome, nota)

    print(f'Cadastro do aluno {nome.capitalize()} realizado com sucesso!')
    print(' ')

def pesquisa_aluno():
    """
    Pesquisa um aluno e todas as suas notas.
    """
    nome_aluno = input('Digite o nome do aluno: ').lower()
    print(' ')

    # Lista para armazenar as informações do aluno
    notas_encontradas = []

    # Abre o arquivo notas_por_aluno.txt
    try:
        arquivo = open('notas_por_aluno.txt', 'r')
        for linha in arquivo:
            # Divide as linhas em partes
            partes = linha.strip().split(';')
            if partes[1] == nome_aluno:
                # Adiciona as notas do aluno à lista
                prova = partes[0]
                nota = float(partes[2])
                notas_encontradas.append((prova, nota))
        arquivo.close()
    except FileNotFoundError:
        print('Arquivo de notas não encontrado.')
        return 
    
    # Calcula a média do aluno e exibe as notas
    if notas_encontradas:
        print(f'Notas do aluno {nome_aluno.capitalize()}:')
        soma_notas = 0
        for prova, nota in notas_encontradas: # Exibe as notas pra cada prova
            print(f'Prova: {prova.capitalize()}, Nota: {nota}')
            soma_notas += nota

        media = soma_notas / len(notas_encontradas) # Calcula a média
        status = 'APROVADO' if media >= 7 else 'REPROVADO' # Define o status baseado na média

        print(f'Média: {media:.2f} - {status}')
        print(' ')
    else:
        print(f'Nenhuma nota encontrada para o aluno {nome_aluno.capitalize()}.')

def pesquisa_turma():
    """
    Exibe todos os alunos da turma, e um resumo contendo a maior,
    a menor nota da turma e também a média.
    """
    try:
        arquivo = open('notas_gerais.txt', 'r')
        alunos = []
        notas = []
        
        for linha in arquivo: # Lê cada linha do arquivo de notas gerais
            partes = linha.strip().split(';') # Divide as linhas em partes 
            nome_aluno = partes[1] 
            nota = float(partes[2]) # Conversão da nota para float
            alunos.append(nome_aluno) # Adiciona na lita de alunos
            notas.append(nota) # Adiciona na lista de notas
        
        # Exibe os alunos cadastrados
        print('Alunos cadastrados:')
        for aluno in alunos:
            print(aluno.capitalize())
        
        # Calcula maior, menor nota e a média
        if notas: # Verifica se a lista não está vazia
            maior_nota = max(notas)
            menor_nota = min(notas)
            media_nota = sum(notas) / len(notas)

            # Exibe os resultados
            print(f'\nResumo da turma:')
            print(f'Maior nota: {maior_nota:.2f}')
            print(f'Menor nota: {menor_nota:.2f}')
            print(f'Média da turma: {media_nota:.2f}')
            print(' ')
        else:
            print('Nenhuma nota encontrada na turma.')
        
        arquivo.close()
    
    except FileNotFoundError:
        print('O arquivo de notas não foi encontrado.')
