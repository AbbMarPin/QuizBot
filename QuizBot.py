#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
import json
import random


class QuizBot:
    def __init__(self, randomize_awnsers=False, frågor="", verbose=True):
        self.frågor = frågor
        self.verbose = verbose
        self.randomize = randomize_awnsers
        self.index = 0
        self.score = 0
        self.streak = 0
        self.beststreak = 0
        self.numofquestions = 0

    def loadConfig(self, input, file=False):
        if file == True:
            with open(input, encoding='utf-8') as json_file:
                self.frågor = json.loads(json_file.read())

        elif type(input) == str:
            self.frågor = json.loads(input)

        elif type(input) == list:
            self.frågor = input

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
            print("| Inga frågor laddade!")
            return [False]

        if index == -1:
            if randomize:
                questions = []
                for x in range(len(self.frågor)):
                    questions.append(x)
                # print(questions)
                new_questions = random.sample(questions, len(questions))
                if len(questions) != 1:  # gör inte om det är en
                    while new_questions == questions:  # se till att det blir random
                        new_questions = random.sample(
                            questions, len(questions))
                # print(new_questions)
                n = 0
                for i in new_questions:
                    n += 1
                    # print(i)
                    if self.fråga(i) == "exit":
                        return [False]

            else:
                for i in range(len(self.frågor)):
                    self.fråga(i)
            return
        elif index == 1:
            print("| Control-C för att skippa")
            print("| 'Exit' för att avsluta")
            print("=" * 35)
        fråga = self.frågor[index]
        if self.randomize:
            fråga = self.randomorder(fråga)

        self.numofquestions += 1
        print("="*25)
        print("|", str(self.numofquestions)+"/"+str(len(self.frågor)),
              "(" + str(round(self.numofquestions/len(self.frågor) * 100, 2)) + "%)")
        print("| Fråga:", fråga["fråga"])
        print("| svarsalternativ:")
        for n, x in zip(range(1, len(fråga["svar"]) + 1), fråga["svar"]):
            print("|", n, "|", x)

        while True:
            try:
                svar = input("| val > ")
                if svar.upper() == "EXIT":
                    return "exit"
                svar = int(svar)
                if svar < 1 or svar > len(fråga["svar"]):
                    raise ValueError
                break
            except ValueError:
                print("| Ett tal mellan 1 och",
                      len(fråga["svar"]), "tack!")
                print("| 'Exit' för att avsluta")
            except KeyboardInterrupt:
                print("\n| Skippar...")
                return [False]
            except EOFError:
                print("\n| Avslutar...")
                exit()

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
        p = 5 - len(str(self.score))  # padding
        p2 = 8 - len(str(self.streak))
        print("┏━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃    Du fick          ┃")
        print("┃      ", self.score, "poäng!", " " * p,  "┃")
        print("┃ och din bästa streak┃")
        print("┃      var", str(self.beststreak) + "!", " " * p2, "┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━┛")
        return {
            "score": self.score,
            "best_streak": self.score
        }


def opentdbparser(url):
    import requests
    import html

    print("| Laddar Ned...", end="\r")

    try:
        res = requests.get(url).text
        res = json.loads(res)["results"]
    except:
        print("something went wrong when downloading, please try again")
        exit()
    print("               ", end="\r")

    frågor = []

    for fråga in res:

        for svar in range(len(fråga["incorrect_answers"])-1):  # fixa html encodeing
            fråga["incorrect_answers"][svar] = html.unescape(
                fråga["incorrect_answers"][svar])
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
        elif fråga["type"] == "boolean":

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
