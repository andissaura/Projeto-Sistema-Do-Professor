# Importando o arquivo de funções de texto
import funcoes_arquivo as fH
# Importando as funções do sistema
import funcoes_gestao as sis


def mostrar_menu():
    """
    Mostra o menu principal do sistema e suas opções.
    
    Returns:
        None
    """
    print('-='*30)
    print(''*7, 'SISTEMA DO PROFESSOR', ''*7)
    print('-='*30)
    print('|1| Cadastrar novas notas\n'
          '|2| Consultar aluno\n'
          '|3| Consultar notas da turma\n'
          '|4| Sair\n'
    )
    print('-='*30)

    # Consulta se o arquivo para cadastro existe, caso não exista, cria um novo.
    arquivo = 'cadastros_alunos.txt' # Atribui o arquivo a variável
    if fH.existeArquivo(arquivo):
        print('Arquivo localizado no sistema.')
    else:
        print('Arquivo não localizado no sistema.')
        fH.criaArquivo(arquivo)
    
    # Consulta se o arquivo para aprovações existe, caso não exista, cria um novo.
    arquivo = 'alunos_aprovados.txt' # Atribui o arquivo a variável
    if fH.existeArquivo(arquivo):
      print('Arquivo localizado no sistema.')
    else:
      print('Arquivo não localizado no sistema.')
      fH.criaArquivo(arquivo)


while True:
   mostrar_menu()
   opcao = int(input('Escolha a opção desejada: '))

   if opcao == 1:
      print('Insira os dados do aluno: ')
      sis.cadastrar()
   #elif opcao == 2:

   #elif opcao == 3:

   elif opcao == 4:
      print('Saindo do programa, até a próxima.')
      break   
   else:
      print('Opção inválida, tente novamente.')
      continue

   
