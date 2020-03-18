import QuizBot
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

if info
QB = QuizBot.QuizBot(randomize_awnsers=True, verbose=True)

quiz = QuizBot.opentdbparser("https://opentdb.com/api.php?amount=100")

QB.loadConfig(quiz)

# Frågebot.loadConfig("frågor.json", file=True)

QB.fråga(randomize=True)

QB.finalscore()
