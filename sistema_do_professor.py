# Importando o arquivo de funções de texto
import funcoes_arquivo as fA
# Importando as funções do sistema
import funcoes_gestao as sis

# Consulta se o arquivo para cadastro existe, caso não exista, cria um novo.
arquivo = 'cadastros_alunos.txt' # Atribui o arquivo a variável
if not fA.existeArquivo(arquivo):
    fA.criaArquivo(arquivo)
    
# Consulta se o arquivo para aprovações existe, caso não exista, cria um novo.
arquivo = 'alunos_aprovados.txt' # Atribui o arquivo a variável
if not fA.existeArquivo(arquivo):
    fA.criaArquivo(arquivo)


def mostrar_menu():
    """
    Mostra o menu principal do sistema e suas opções.
    
    Returns:
        None
    """
    print('-='*25)
    print(' '*10, 'SISTEMA DO PROFESSOR', ' '*10)
    print('-='*25)
    print('|1| Cadastrar novas notas\n'
          '|2| Consultar aluno\n'
          '|3| Consultar notas da turma\n'
          '|4| Sair'
    )
    print('-='*30)

# Sistema do menu principal
while True:
   mostrar_menu()
   opcao = int(input('Escolha a opção desejada: '))

   if opcao == 1:
      print(' ')
      print('-'*42)
      print('-'*12, 'CADASTRO DE NOTAS', '-'*12)
      print('-'*42)
      print(' ')
      sis.cadastrar()

   elif opcao == 2:
      print(' ')
      print('-'*42)
      print('-'*12, 'CONSULTA DE ALUNO', '-'*12)
      print('-'*42)
      print(' ')
      sis.pesquisa_aluno()

   elif opcao == 3:
      print(' ')
      print('-'*42)
      print('-'*12, 'CONSULTA DE TURMA', '-'*12)
      print('-'*42)
      print(' ')
      sis.pesquisa_turma()

   elif opcao == 4:
      print('Saindo do programa, até a próxima.')
      break   
   
   else:
      print('Opção inválida, tente novamente.')
      continue

   
