import typer
import json
from db.fake_db import FakeDatabase
from entities.Agendamento import Agendamento
from uuid import uuid4
from datetime import datetime
from rich import print
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

db = FakeDatabase()

@app.command()
def criar(documento: str, telefone: int, turno: str, especialista: str):    
    try:
        agendamento = Agendamento(documento, telefone, turno, especialista)
        agendamento_object = {
            "id": str(agendamento.id), 
            "documento": str(agendamento.documento), 
            "telefone": str(agendamento.telefone),
            "turno": str(agendamento.turno),
            "especialista": str(agendamento.especialista),
            "data_retorno": str(agendamento.data_retorno),
            "data_criacao": str(agendamento.data_criacao)
        }
        db.insert(agendamento_object)
        
        print("[bold green]Agendamento criado[/bold green] com sucesso! :white_check_mark:")
        
        table = Table("Id", "Documento", "Telephone", "Turno", "Especialista", "Data de retorno", "Data de criação")
        table.add_row(
            str(agendamento.id), 
            str(agendamento.documento), 
            str(agendamento.telefone),
            str(agendamento.turno),
            str(agendamento.especialista),
            str(agendamento.data_retorno),
            str(agendamento.data_criacao))
        console.print(table)
    except Exception as e:
        print(f":boom: [bold red]{e}[/bold red] :boom:")
        
@app.command()
def todos():    
    try:
        todos = db.select()

        print("[bold blue]A lista de todos os agendamentos cadastrados:[/bold blue] :file_folder:")
        
        table = Table("Id", "Documento", "Telephone", "Turno", "Especialista", "Data de retorno", "Data de criação")
        for item in todos:            
            table.add_row(
            str(item["id"]), 
            str(item["documento"]), 
            str(item["telefone"]),
            str(item["turno"]),
            str(item["especialista"]),
            str(item["data_retorno"]),
            str(item["data_criacao"]))
        
        
        console.print(table)
    except Exception as e:
        print(f":boom: [bold red]{e}[/bold red] :boom:")


if __name__ == "__main__":
    app()