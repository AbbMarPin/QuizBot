from time import sleep
import json
frågor = []

class ui:
    def __init__(self):
        pass

    def title(self):
        print("""
    ┏━━━━━━━━━━━━━━━━━━━━━┓
    │  ultimate quiz      │
    │      of destiny!!!  │
    │                     │
    ┗━━━━━━━━━━━━━━━━━━━━━┛
        """)

    def line(self):
        print("="*25)


    def echo(self, text):
        print("|", text)


    def prompt(self, prompt_text):

        return input("| " + prompt_text + " > ")


    def exit_(self, text):
        print("\n|", text)
        exit()

ui = ui()

def info():
    ui.echo("1. starta quiz")
    ui.echo("2. gör nytt quiz")
    ui.echo("3. avsluta")
    option = ui.prompt("Val")
    return option

class FrågeBot:
    def __init__(self, frågor=""):
        self.frågor = frågor
        self.i = 0
        self.

    def loadConfig(self, file):
        with open(file, encoding='utf-8') as json_file:
            self.frågor = json.loads(json_file.read())
    
    def fråga(self, index):
        if self.frågor == "": # Inga frågor finns
            ui.echo("Inga frågor laddade!")
            return [False]
        fråga = self.frågor[index]
        ui.line()
        print("| Fråga:", fråga["fråga"])
        ui.echo("svarsalternativ:")
        for n, x in zip(range(1, len(fråga["svar"]) + 1), fråga["svar"]):
            ui.echo(str(n) + " | " + x)
        
        while True:
            try:
                svar = int(ui.prompt("val"))
                break
            except ValueError:
                ui.echo("Ett tal tack")
            except KeyboardInterrupt:
                print("\n| Skippar...")
                return [False]

        if svar == fråga["rätt"]:
            return [True]
        else:
            return [False]

    def fråga_nästa(self):
        self.fråga(self.i)
        self.i += 1

Frågebot = FrågeBot()


Frågebot.loadConfig("frågor.json")


for x in range(2):
    Frågebot.fråga_nästa()

# Frågebot.fråga(1)

# def main():
#     title()
#     svar = info()
#     if svar == "1":
#         # stata quiz
#         for x in frågor:
#             fråga(x)
#     elif svar == "2":
#         echo("ny quiz")
#     elif svar == "3":
#         exit_("Avlsutar...")
#     else:
#         pass

# if __name__ == "__main__":
#     while 1:
#         try:
#             main()
#         except Exception:
#             exit_("oväntat fel")
#         except KeyboardInterrupt:
#             exit_("Användaren avslutate")
