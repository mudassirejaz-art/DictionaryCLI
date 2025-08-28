import json
from rich.console import Console
from rich.table import Table

console = Console()

def display_word(data):
    if not data:
        console.print("[red]Word not found![/red]")
        return

    word = data[0]['word']
    console.print(f"[bold green]{word}[/bold green]")

    for meaning in data[0].get('meanings', []):
        part = meaning.get('partOfSpeech', '')
        definitions = meaning.get('definitions', [])
        table = Table(title=f"{part.capitalize()} Definitions")
        table.add_column("Definition", style="cyan")
        table.add_column("Example", style="magenta")
        for d in definitions:
            table.add_row(d.get('definition',''), d.get('example',''))
        console.print(table)

def export_word(data, filename="word.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)