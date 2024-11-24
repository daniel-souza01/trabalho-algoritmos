import json

class FakeDatabase:
    """
    Classe que simula um banco de dados em arquivo JSON.

    A classe FakeDatabase permite persistir, consultar e inserir agendamentos em um arquivo JSON.
    Os dados são carregados e salvos no arquivo especificado por `file_name`.

    @param {str} file_name - Caminho para o arquivo JSON onde os dados serão armazenados.
    """
    file_name =  "src/db/db.json"
    
    def __init__(self):
        self.agendamentos = self.select()
        
    def persist(self):
        """
        Este método grava os dados de agendamentos no arquivo especificado pela variável `file_name`.
        """
        with open(self.file_name, 'w') as file:
            json.dump(self.agendamentos, file)

    def select(self):
        """
        Tenta abrir o arquivo JSON e carregar os agendamentos armazenados. Caso o arquivo não exista, retorna uma lista vazia.
        """
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    
    def insert(self, agendamento):
        """
        Insere um novo agendamento na lista e persiste as alterações no arquivo JSON.

        @param {dict} agendamento - Agendamento a ser inserido. Deve ser um dicionário contendo as informações do agendamento.
        """
        self.agendamentos.append(agendamento)
        self.persist()
        
    def select_by_turn_and_specialty(self, turno, especialista):
        """
        Filtra os agendamentos existentes para retornar apenas aqueles que correspondem ao turno e especialista fornecidos.

        @param {str} turno - Turno de busca.
        @param {str} especialista - Especialista de busca.
        @returns {list} - Lista de agendamentos que atendem ao filtro.
        """
        return [a for a in self.agendamentos if a["turno"] == turno and a["especialista"] == especialista]
