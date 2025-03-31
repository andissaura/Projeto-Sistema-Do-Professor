# Importando as funções de arquivo
import funcoes_arquivo as fH

def cadastrar():
    """
    Cadastra um aluno e suas notas no sistema.
    """
    prova = input('Digite a prova de referência: ')
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota do aluno: '))

    # Salva os dados no arquivo de cadastros
    fH.inserir_cadastro('cadastros_alunos.txt', prova, nome, nota)
    # Salva notas da turma para tirar a média
    fH.inserir_cadastro('notas_gerais.txt', prova, nome, nota)
    # Salva notas no arquivo do aluno
    fH.inserir_cadastro('notas_por_aluno.txt', nome, nota)

#def pesquisa_aluno():

#def pesquisa_turma():
