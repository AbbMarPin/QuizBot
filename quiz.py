#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        import json
        import random
        self.frågor = frågor
        self.index = 0
        self.score = 0
        self.streak = 0
        self.beststreak = 0

    def loadConfig(self, input, file=False):
        if file == True:
            with open(input, encoding='utf-8') as json_file:
                self.frågor = json.loads(json_file.read())
        
        elif type(input) == dict:
            self.frågor = input
        
        elif type(input) == str:
            self.frågor = json.loads(input)

    def randomorder(self, fråga):
        pass
    
    
    def fråga(self, index=-1):
        if self.frågor == "": # Inga frågor finns
            ui.echo("Inga frågor laddade!")
            return [False]

        if index == -1:
            for i in range(len(self.frågor)-1):
                self.fråga(i)
        
        fråga = self.frågor[index]
        ui.line()
        print("| Fråga:", fråga["fråga"])
        ui.echo("svarsalternativ:")
        for n, x in zip(range(1, len(fråga["svar"]) + 1), fråga["svar"]):
            ui.echo(str(n) + " | " + x)
        
        while True:
            try:
                svar = int(ui.prompt("val"))
                if svar < 1 or svar > len(fråga["svar"]):
                    raise ValueError
                break
            except ValueError:
                ui.echo("Ett tal mellan 1 och " + str(len(fråga["svar"])) + " tack!")
            except KeyboardInterrupt:
                print("\n| Skippar...")
                return [False]

        if svar == fråga["rätt"]:
            self.score += 1
            self.streak += 1
            if self.streak > self.beststreak:
                self.beststreak = self.streak
            return [True]
        else:
            self.streak = 0
            return [False]

    def fråga_nästa(self):
        self.fråga(self.index)
        self.index += 1

    def finalscore(self):
        p = 5 - len(str(self.score))
        p2 = 8 - len(str(self.streak))
        print("┏━━━━━━━━━━━━━━━━━━━━━┓")
        print("│    Du fick          │")
        print("│      ", self.score, "poäng!", " " * p,  "│")
        print("│ och din bästa streak│")
        print("│      var", str(self.beststreak) + "!", " " * p2, "│")
        print("┗━━━━━━━━━━━━━━━━━━━━━┛")

Frågebot = FrågeBot()


Frågebot.loadConfig("frågor.json", file=True)

Frågebot.fråga()

Frågebot.finalscore()

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
