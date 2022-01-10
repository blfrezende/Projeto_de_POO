class Tarefa:
    def __init__(self, titulo, data, status_tarefa):
        self.titulo = titulo
        self.data = data
        self.status_tarefa = status_tarefa
    
    def __repr__(self):
        return f'{[self.titulo, self.data, self.status_tarefa]}'

tarefa1 = Tarefa('tarefa1', '01/01/22', 'pendente')
print(tarefa1)

