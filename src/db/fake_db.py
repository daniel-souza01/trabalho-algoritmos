import json

class FakeDatabase:
    file_name =  "src/db/db.json"
    
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
        
    def select_by_turn_and_specialty(self, turno, especialista):
        return [a for a in self.agendamentos if a["turno"] == turno and a["especialista"] == especialista]
