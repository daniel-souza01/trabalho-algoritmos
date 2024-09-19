import json

class FakeDatabase:
    file_name =  "db.json"
    
    def __init__(self):
        self.agendamentos = self.select()
        
    def persist(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.agendamentos, file)

    def select(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def insert(self, agendamento):
        self.agendamentos.append(agendamento)
        self.persist()
