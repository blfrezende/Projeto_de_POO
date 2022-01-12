import csv
from datetime import datetime, date
import inquirer

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

    def alterar_status(self):
        with open('tarefas.csv') as tarefas:
            tabela_tarefas = csv.reader(tarefas, delimiter=';', lineterminator='\n')
            conteudo_tabela = list(tabela_tarefas)
            
        for linha in conteudo_tabela:
            if linha[0] == self.titulo:
                if linha[3] == 'Pendente':
                    linha[3] = 'Concluida'
                else:
                  linha[3] = 'Pendente'
                
        with open('tarefas.csv', 'w') as tarefas:
            altera = csv.writer(tarefas, delimiter=';', lineterminator='\n')
            altera.writerows(conteudo_tabela)

    def remover_tarefa(self):
        with open('tarefas.csv') as tarefas:
            tabela_tarefas = csv.reader(tarefas, delimiter=';', lineterminator = '\n')
            conteudo_tabela = list(tabela_tarefas)
            lista_tarefa = [self.titulo,self.data,self.categoria,self.status_tarefa]
            
            indice = conteudo_tabela.index(lista_tarefa)
            conteudo_tabela.pop(indice)

        
        with open('tarefas.csv','w') as tarefas:
            remove = csv.writer(tarefas, delimiter=';', lineterminator='\n')
            remove.writerows(conteudo_tabela)

    def vizualizar_tarefas():
        with open('tarefinha.csv') as tarefas:
            tabela_tarefas = csv.reader(tarefas, delimiter=';', lineterminator='\n')
            conteudo_tabela = list(tabela_tarefas)
        print('TAREFAS:')
        print('[Título, Data, Categoria, Status]')
        for tarefa in conteudo_tabela:
            print(tarefa)    

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

    with open('tarefas.csv') as tarefas:
      tabela_tarefas = csv.reader(tarefas, delimiter=';', lineterminator='\n')
      conteudo_tabela = list(tabela_tarefas)

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
    questions3 = [
      inquirer.Text('titulo', message = 'Qual o título da tarefa que deseja alterar o status?')
    ]
    answers3 = inquirer.prompt(questions3)

    with open('tarefas.csv') as tarefas:
      tabela_tarefas = csv.reader(tarefas, delimiter=';', lineterminator='\n')
      conteudo_tabela = list(tabela_tarefas)

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


  # elif answers['option'] == 'Remover tarefa':
  #   questions4 = [
  #     inquirer.Text('titulo', message = 'Qual o título da tarefa que deseja remover?')
  #   ]
  #   answers4 = inquirer.prompt(questions4)
  #   remover_tarefa(answers4['titulo'])

  # elif answers['option'] == 'Vizualizar tarefas':
  #  vizualizar_tarefas()

  else:
    break
#tarefa1 = Lista_de_tarefas(titulo='pescar', data = '09/02/22', categoria= 'lazer')
#tarefa1.adicionar_tarefa()
# tarefa1.alterar_status()
#tarefa1.remover_tarefa()
#Lista_de_tarefas.vizualizar_tarefas()


# data = datetime.now()
# datetime.strftime(data.now(), '%d/%m/%Y')
