from datetime import datetime
from uuid import uuid4

class Agendamento: 
    """
    Classe que representa um agendamento de consulta.

    @param {str} documento - Documento de identificação do paciente.
    @param {str} telefone - Número de telefone de contato do paciente.
    @param {str} turno - Turno de preferência para o agendamento ("MANHÃ", "TARDE", "NOITE").
    @param {str} especialista - Especialista para o qual o agendamento é feito ("MÉDICO", "DENTISTA").
    @param {str} [data_retorno=""] - Data do retorno, opcional, em formato de string.
    @param {datetime} [data=datetime.now()] - Data do agendamento, padrão para o momento atual.
    @throws {ValueError} - Lançado se a data atual for um sábado ou domingo.
    """
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
        """
        Método para marcar a data de retorno do agendamento.

        @param {str} data_retorno - Data do retorno em formato de string.
        """
        self.data_retorno = data_retorno
        
    
    def to_object(self):
        """
        Converte os dados do agendamento para um formato de objeto (dicionário).

        @returns {Object} - Dicionário com os dados do agendamento, incluindo id, documento, telefone, turno, especialista, 
        data de retorno e data de agendamento.
        """
        return {
            "id": str(self.id), 
            "documento": str(self.documento), 
            "telefone": str(self.telefone),
            "turno": str(self.turno),
            "especialista": str(self.especialista),
            "data_retorno": str(self.data_retorno),
            "data": str(self.data)
        }