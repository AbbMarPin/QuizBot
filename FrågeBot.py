#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
import json
import random
from ui import ui

ui = ui()

class FrågeBot:
    def __init__(self, randomize=False, frågor="", verbose=True):
        import json
        import random
        self.frågor = frågor
        self.verbose = verbose
        self.randomize = randomize
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
        # TODO Random stuff
        # vet vilken räät svar är
        # lista med 1 till antal svar med random nummer som sätts och scrambelar
        # svaren och sätter rätt svar på rätt
        rättsvar = fråga["svar"][fråga["rätt"]-1]

        randlista = random.sample(fråga["svar"], len(fråga["svar"]))

        for n, svar in zip(range(1, len(randlista)+1), randlista):
            if svar == rättsvar:
                rättrandsvar = n

        return {
            "fråga": fråga["fråga"],
            "svar": randlista,
            "rätt": rättrandsvar
        }

    def fråga(self, index=-1):
        if self.frågor == "":  # Inga frågor finns
            ui.echo("Inga frågor laddade!")
            return [False]

        if index == -1:
            for i in range(len(self.frågor)-1):
                self.fråga(i)

        fråga = self.frågor[index]
        if self.randomize:
            fråga = self.randomorder(fråga)

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
                ui.echo("Ett tal mellan 1 och " +
                        str(len(fråga["svar"])) + " tack!")
            except KeyboardInterrupt:
                print("\n| Skippar...")
                return [False]

        if svar == fråga["rätt"]:
            self.score += 1
            self.streak += 1
            if self.streak > self.beststreak:
                self.beststreak = self.streak
            if self.verbose:
                print("| Rätt!!")
                print("| Poäng:", self.score)
                print("| Streak:", self.streak)
            return [True]
        else:
            self.streak = 0
            if self.verbose:
                print("| Fel!!")
                print("| Poäng:", self.score)
                print("| Streak:", self.streak)
            return [False]

    def fråga_nästa(self):
        self.fråga(self.index)
        self.index += 1

    def finalscore(self):
        p = 5 - len(str(self.score))
        p2 = 8 - len(str(self.streak))
        print("┏━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃    Du fick          ┃")
        print("┃      ", self.score, "poäng!", " " * p,  "┃")
        print("┃ och din bästa streak┃")
        print("┃      var", str(self.beststreak) + "!", " " * p2, "┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━┛")

