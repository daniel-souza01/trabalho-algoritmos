from datetime import datetime
from uuid import uuid4
from entities.Turno import Turno

class Agendamento: 
    def __init__(self, documento, telefone, turno, especialista, data_retorno = "", data_criacao = datetime.now()):
        if datetime.now().weekday() >= 5:
            raise ValueError("Não é possível criar um agendamento no sábado ou domingo.")
        
        self.id = str(uuid4())
        self.documento = documento
        self.telefone = telefone
        self.turno = Turno[turno].value
        self.especialista = especialista
        self.data_retorno = data_retorno
        self.data_criacao = str(data_criacao)
        
    def marcar_retorno(self, data_retorno):
        self.data_retorno = data_retorno