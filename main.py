import QuizBot
from ui import ui
import json

ui = ui()


def info():
    ui.line()
    ui.echo("Huvudmeny")
    ui.line()
    option = ui.prompt_list(["ladda quiz", "gör nytt quiz", "avsluta"], "Val")
    if option == "3":
        return False
    return option


QB = QuizBot.QuizBot(randomize_awnsers=True, verbose=True)

while True:

    try:
        val = info()
    except KeyboardInterrupt:
        ui.exit_("Avslutar")

    if val == False:
        break

    elif val == "1":
        ui.line()
        try:
            ui.echo("Vad har du för sorts quiz?")

            val = ui.prompt_list(
                ["Fil", "opentdb Url", "sträng"], "Val").upper()
            data = ui.prompt("")

            if val == "1":
                QB.loadConfig(data, file=True)
            elif val == "2":
                # https://opentdb.com/api.php?amount=100
                QB.loadConfig(QuizBot.opentdbparser(data))
            elif val == "3":
                QB.loadConfig(data)

            QB.fråga(randomize=True)

            QB.finalscore()
        except KeyboardInterrupt:
            ui.echo("\n")
            ui.line()

    elif val == "2":
        ui.line()
        ui.echo("Välkommen till denna fråge generator!")
        ui.echo("")
        ui.echo("Frågor fungerar såhär:")
        ui.echo("En fråga")
        ui.echo("2-oändigt många svar")
        frågor = []

        while True:
            ui.line()
            antal_frågor = len(frågor) + 1
            fråga = {}
            try:
                ui.echo("Fråga " + str(antal_frågor))
                header = ui.prompt("Fråga, 'exit' för att avsluta")
            except KeyboardInterrupt:
                break
            if header.upper() == "EXIT":
                break
            fråga["fråga"] = header

            svar = []
            exit = False
            while exit == False:
                try:
                    a = ui.prompt("Svar")
                except KeyboardInterrupt:
                    exit = True
                if a.upper() == "EXIT":
                    exit = True
                else:
                    if a in svar:
                        ui.echo("Inga dubletter tack")
                    elif a == "":
                        exit = True
                    else:
                        svar.append(a)

            fråga["svar"] = svar
            ui.line()
            exit = False
            while exit == False:
                try:
                    rätt = int(ui.prompt_list(svar, "Vilken är rätt?"))
                    if rätt < 1 or rätt > len(fråga["svar"]):
                        raise ValueError
                    rätt = int(rätt)
                    fråga["rätt"] = rätt
                    exit = True
                except ValueError:
                    print("| Ett tal mellan 1 och",
                          len(fråga["svar"]), "tack!")
                    ui.line()
                except KeyboardInterrupt:
                    print()
                    ui.line()
            frågor.append(fråga)

        print()
        ui.line()
        ui.echo("Hur vill du exportera?")
        try:
            a = ui.prompt_list(["sträng (printa)", "fil"], "val")
        except:
            print("\n", json.dumps(frågor))

        if a == "1":
            print("\n", json.dumps(frågor))
        elif a == "2":
            print()
            try:
                fil_namn = ui.prompt("Vad ska filen heta?")
            except KeyboardInterrupt:
                print("\n", json.dumps(frågor))
                break
            
            
            with open(fil_namn, "w+", encoding='utf-8') as json_file:
                json.dump(frågor, json_file)

# QB.loadConfig(quiz)

# Frågebot.loadConfig("frågor.json", file=True)

# QB.fråga(randomize=True)
