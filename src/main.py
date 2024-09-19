import typer
from db.fake_db import FakeDatabase
from entities.Agendamento import Agendamento
from rich import print
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()
db = FakeDatabase()
table = Table("Id", "Documento", "Telephone", "Turno", "Especialista", "Data de retorno", "Data de criação")

@app.command()
def criar(documento: str, telefone: int, turno: str, especialista: str):    
    try:
        ag = Agendamento(documento, telefone, turno, especialista).to_object()
        db.insert(ag)
        print("[bold green]Agendamento criado[/bold green] com sucesso! :white_check_mark:")
        table.add_row(ag["id"], ag["documento"],  ag["telefone"], ag["turno"], ag["especialista"], ag["data_retorno"], ag["data"])
        console.print(table)
    except Exception as e:
        print(f":boom: [bold red]{e}[/bold red] :boom:")
        
@app.command()
def todos():    
    try:
        todos = db.select()
        print("[bold blue]A lista de todos os agendamentos cadastrados:[/bold blue] :file_folder:")
        for ag in todos:
            table.add_row(ag["id"], ag["documento"],  ag["telefone"], ag["turno"], ag["especialista"], ag["data_retorno"], ag["data"])
        console.print(table)
    except Exception as e:
        print(f":boom: [bold red]{e}[/bold red] :boom:")


if __name__ == "__main__":
    app()