# QuizBot
A Python library for quizzing


# Usage
```pycon
>>> from FrågeBot import FrågeBot

>>> Frågebot = FrågeBot(randomize=False, verbose=True)

>>> Frågebot.loadConfig("frågor.json", file=True)

>>> Frågebot.fråga(randomize=True)

>>> Frågebot.finalscore()
```

## Output

    =========================
    | Fråga: hur många magar har en ko?
    | svarsalternativ:
    | 1 | tre stycken
    | 2 | en stycken
    | 3 | fyra stycken
    | 4 | två stycken
    | val > 3
    | Rätt!!   
    | Poäng: 1 
    | Streak: 1
    =========================
    | Fråga: jadu godnatt
    | svarsalternativ:
    | 1 | zzzz
    | 2 | ZzzZzz
    | 3 | *snark*
    | val > 1
    | Rätt!!
    | Poäng: 2
    | Streak: 2
    ┏━━━━━━━━━━━━━━━━━━━━━┓
    ┃    Du fick          ┃
    ┃       2 poäng!      ┃
    ┃ och din bästa streak┃
    ┃      var 2!         ┃
    ┗━━━━━━━━━━━━━━━━━━━━━┛
