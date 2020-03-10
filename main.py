from FrågeBot import FrågeBot
from ui import ui

ui = ui()

def info():
    ui.echo("1. starta quiz")
    ui.echo("2. gör nytt quiz")
    ui.echo("3. avsluta")
    option = ui.prompt("Val")
    return option


Frågebot = FrågeBot(randomize=False, verbose=True)

Frågebot.loadConfig("frågor.json", file=True)

Frågebot.fråga()

Frågebot.finalscore()
