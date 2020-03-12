import FrågeBot
from ui import ui

ui = ui()

def info():
    ui.echo("1. ladda quiz")
    ui.echo("2. gör nytt quiz")
    ui.echo("3. avsluta")
    option = ui.prompt("Val")
    if option == "3":
        exit()
    return option


Frågebot = FrågeBot.FrågeBot(randomize_awnsers=True, verbose=True)

Frågor = FrågeBot.opentdbparser("https://opentdb.com/api.php?amount=10")

Frågebot.loadConfig(Frågor)

# Frågebot.loadConfig("frågor.json", file=True)

Frågebot.fråga(randomize=True)

Frågebot.finalscore()
