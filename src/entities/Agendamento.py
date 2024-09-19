from datetime import datetime
from uuid import uuid4

class Agendamento: 
    def __init__(self, documento, telefone, turno, especialista, data_retorno = "", data = datetime.now()):
        if datetime.now().weekday() >= 5:
            raise ValueError("Não é possível criar um agendamento no sábado ou domingo.")
        
        self.id = str(uuid4())
        self.documento = documento
        self.telefone = telefone
        self.turno = turno
        self.especialista = especialista
        self.data_retorno = data_retorno
        self.data = str(data)
        
    def marcar_retorno(self, data_retorno):
        self.data_retorno = data_retorno
        
    def to_object(self):
        return {
            "id": str(self.id), 
            "documento": str(self.documento), 
            "telefone": str(self.telefone),
            "turno": str(self.turno),
            "especialista": str(self.especialista),
            "data_retorno": str(self.data_retorno),
            "data": str(self.data)
        }