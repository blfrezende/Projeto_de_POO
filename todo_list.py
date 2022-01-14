import csv
from datetime import datetime, date
import inquirer
import pandas as pd

class Lista_de_tarefas:
    def __init__(self, titulo, data, categoria):
        self.titulo = titulo
        self.data = data
        self.categoria = categoria
        self.status_tarefa = 'Pendente'
    
    def __repr__(self):
        return f'{[self.titulo, self.data, self.categoria, self.status_tarefa]}'

    def adicionar_tarefa(self):
        with open('tarefas.csv', 'a') as tarefas:
            note = csv.writer(tarefas, delimiter=';' , lineterminator = '\n')
            note.writerow([self.titulo, self.data, self.categoria, self.status_tarefa])

    def ler_e_criar_lista():
      with open('tarefas.csv') as tarefas:
            tabela_tarefas = csv.reader(tarefas, delimiter=';', lineterminator='\n')
            conteudo_tabela = list(tabela_tarefas)
      return conteudo_tabela

    def alterar_status(self):
        conteudo_tabela = Lista_de_tarefas.ler_e_criar_lista()
            
        for linha in conteudo_tabela:
            if linha[0] == self.titulo:
                if linha[3] == 'Pendente':
                    linha[3] = 'Concluida'
                    print('\n--------------------------------------------------------')
                    print(f' Status da tarefa \'{linha[0]}\' foi alterado para {linha[3]}. ')
                    print('--------------------------------------------------------\n')
                else:
                  linha[3] = 'Pendente'
                  print('\n--------------------------------------------------------')
                  print(f' Status da tarefa \'{linha[0]}\' foi alterado para {linha[3]}. ')
                  print('--------------------------------------------------------\n')

        with open('tarefas.csv', 'w') as tarefas:
            altera = csv.writer(tarefas, delimiter=';', lineterminator='\n')
            altera.writerows(conteudo_tabela)
            

    def remover_tarefa(self):
        conteudo_tabela = Lista_de_tarefas.ler_e_criar_lista()
        
        for linha in conteudo_tabela:
          if linha[0] == self.titulo:
            indice = conteudo_tabela.index(linha)
            conteudo_tabela.pop(indice)
            print('\n--------------------------------------------------------')
            print('     Tarefa ', linha[0] , ' removida com sucesso!!        ')
            print('--------------------------------------------------------\n')


        
        with open('tarefas.csv','w') as tarefas:
            remove = csv.writer(tarefas, delimiter=';', lineterminator='\n')
            remove.writerows(conteudo_tabela)

    def vizualizar_tarefas():
        conteudo_tabela = Lista_de_tarefas.ler_e_criar_lista()

        dict_tarefas = {}
        for tarefa in conteudo_tabela:
          dict_tarefas[tarefa[0]] = [tarefa[1],tarefa[2],tarefa[3]]

        df = pd.DataFrame(data=dict_tarefas.values(),index=dict_tarefas.keys(),columns = ['   Data','   Categoria','     Status'])
        df.rename_axis('Tarefa', axis = 'columns', inplace = True)
        print('\n---------------------------------------------------')
        print(df)
        print('---------------------------------------------------\n')

while True:
  questions = [
    inquirer.List('option',
      message = 'Escolha uma das opções abaixo',
      choices = [
            'Adicionar tarefa',
            'Alterar status da tarefa',
            'Remover tarefa',
            'Vizualizar tarefas',
            'Encerrar'
      ]         
    )
  ]
  answers = inquirer.prompt(questions)

  if answers['option'] == 'Adicionar tarefa':
    questions2 = [
      inquirer.Text('titulo', message = 'Qual o título da tarefa?'),
      inquirer.Text('data', message = 'Qual a data de realização da tarefa?'),
      inquirer.Text('categoria', message = 'Qual a categoria da tarefa?')
    ]
    answers2 = inquirer.prompt(questions2)

    conteudo_tabela = Lista_de_tarefas.ler_e_criar_lista()

    objeto_titulo = 0

    for objeto in conteudo_tabela:
      if answers2['titulo'] == objeto[0]:
        objeto_titulo += 1

    if objeto_titulo != 0: 
      print('\n--------------------------------------------------------')
      print(' Já existe uma tarefa com esse título. Tente novamente!!!')
      print('--------------------------------------------------------\n')
    else:
      tarefa = Lista_de_tarefas(answers2['titulo'], answers2['data'], answers2['categoria'])
      tarefa.adicionar_tarefa()

  elif answers['option'] == 'Alterar status da tarefa':
    conteudo_tabela = Lista_de_tarefas.ler_e_criar_lista()

    print('\n---------------------------------------------------')
    print('         Essas são as tarefas da lista :                  ')
    Lista_de_tarefas.vizualizar_tarefas()
    
    questions3 = [
      inquirer.Text('titulo', message = 'Qual o título da tarefa que deseja alterar o status?')
    ]
    answers3 = inquirer.prompt(questions3)

    contador = 0

    for objeto in conteudo_tabela:
        if answers3['titulo'] == objeto[0]:
          tarefa = Lista_de_tarefas(objeto[0], objeto[1], objeto[2])
          tarefa.alterar_status()
          contador += 1

    if contador == 0:
      print('\n--------------------------------------------------------')
      print(' Não existe tarefa com esse título. Tente novamente!!!')
      print('--------------------------------------------------------\n')


  elif answers['option'] == 'Remover tarefa':
    questions4 = [
      inquirer.Text('titulo', message = 'Qual o título da tarefa que deseja remover?')
    ]
    answers4 = inquirer.prompt(questions4)
    
    conteudo_tabela = Lista_de_tarefas.ler_e_criar_lista()

    contador = 0

    for objeto in conteudo_tabela:
        if answers4['titulo'] == objeto[0]:
          tarefa = Lista_de_tarefas(objeto[0], objeto[1], objeto[2])
          tarefa.remover_tarefa()
          contador += 1

    if contador == 0:
      print('\n--------------------------------------------------------')
      print(' Não existe tarefa com esse título. Tente novamente!!!')
      print('--------------------------------------------------------\n')

  elif answers['option'] == 'Vizualizar tarefas':
    Lista_de_tarefas.vizualizar_tarefas()

  else:
    break