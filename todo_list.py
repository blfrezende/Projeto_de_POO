import csv

class Tarefa:
    def __init__(self, titulo, data, status_tarefa):
        self.titulo = titulo
        self.data = data
        self.status_tarefa = status_tarefa
    
    def __repr__(self):
        return f'{[self.titulo, self.data, self.status_tarefa]}'

    def adicionar_tarefa(self):
        with open('tarefas.csv', 'a') as tarefas:
            note = csv.writer(tarefas, delimiter=';' , lineterminator = '\n')
            note.writerow([self.titulo, self.data, self.status_tarefa])