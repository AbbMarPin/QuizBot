#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
import json
import random
from ui import ui


ui = ui()


class FrågeBot:
    def __init__(self, randomize_awnsers=False, frågor="", verbose=True):
        import json
        import random
        self.frågor = frågor
        self.verbose = verbose
        self.randomize = randomize_awnsers
        self.index = 0
        self.score = 0
        self.streak = 0
        self.beststreak = 0

    def loadConfig(self, input, file=False):
        if file == True:
            with open(input, encoding='utf-8') as json_file:
                self.frågor = json.loads(json_file.read())

        elif type(input) == list:
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

    def fråga(self, index=-1, randomize=False):
        if self.frågor == "":  # Inga frågor finns
            ui.echo("Inga frågor laddade!")
            return [False]

        if index == -1:
            if randomize:
                questions = []
                for x in range(len(self.frågor)):
                    questions.append(x)
                # print(questions)
                new_questions = random.sample(questions, len(questions))
                while new_questions == questions:  # se till att det blir random
                    new_questions = random.sample(questions, len(questions))
                # print(new_questions)
                n = 0
                for i in new_questions:
                    n += 1
                    # print(i)
                    self.fråga(i)

            else:
                for i in range(len(self.frågor)):
                    self.fråga(i)
            return

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
            self.streak += 1
            self.score += 10 * self.streak/10
            if self.streak > self.beststreak:
                self.beststreak = self.streak
            if self.verbose:
                print("| Rätt!!")
                print("| Poäng:", self.score)
                print("| Streak:", self.streak)
                sleep(.5)
            return [True]
        else:
            self.streak = 0
            if self.verbose:
                print("| Fel!!")
                print("| Rätt Svar:", fråga["svar"][fråga["rätt"]-1])
                print("| Poäng:", self.score)
                print("| Streak:", self.streak)
                sleep(1)
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


def opentdbparser(url):
    import requests
    import html

    try:
        res = requests.get(url).text
        res = json.loads(res)["results"]
    except:
        print("something went wrong when downloading, please try again")
        exit()

    frågor = []

    for fråga in res:

        for svar in range(len(fråga["incorrect_answers"])-1): # fixa html encodeing
            fråga["incorrect_answers"][svar] = html.unescape(fråga["incorrect_answers"][svar])
        fråga["correct_answer"] = html.unescape(fråga["correct_answer"])
        fråga["question"] = html.unescape(fråga["question"])
            

        if fråga["type"] == "multiple":
            svar = []
            for x in fråga["incorrect_answers"]:
                svar.append(x)

            svar.append(fråga["correct_answer"])

            rättsvar = svar[-1:][0]

            randlista = random.sample(svar, len(svar))

            for n, svar in zip(range(1, len(randlista)+1), randlista):
                # print(svar, rättsvar)
                if svar == rättsvar:
                    rättrandsvar = n


            frågor.append({
                "fråga": fråga["question"],
                "svar": randlista,
                "rätt": rättrandsvar
            })
        elif fråga["type"] == "multiple":

            if fråga["correct_answer"] == "True":
                rättsvar = 1
            else:
                rättsvar = 2

            frågor.append({
                "fråga": fråga["question"],
                "svar": ["Sant", "Falskt"],
                "rätt": rättsvar
            })

    return frågor
