import csv
from datetime import datetime, date

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
            # novo_conteudo = []
            lista_tarefa = [self.titulo,self.data,self.categoria,self.status_tarefa]
            
            indice = conteudo_tabela.index(lista_tarefa)
            conteudo_tabela.pop(indice)

        
        with open('tarefas.csv','w') as tarefas:
            remove = csv.writer(tarefas, delimiter=';', lineterminator='\n')
            remove.writerows(conteudo_tabela)

        




# tarefa1 = Lista_de_tarefas(titulo='pescar', categoria= 'lazer')
# tarefa1.adicionar_tarefa()
# tarefa1.alterar_status()
# tarefa1.remover_tarefa()


# data = datetime.now()
# datetime.strftime(data.now(), '%d/%m/%Y')
