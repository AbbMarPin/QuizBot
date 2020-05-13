# QuizBot
A Python library for quizzing

# Såhär fungerar det

ui är en hjälpklass som kan fråga frågor, en lista med frågor och skriva saker på ett fint sätt

main är ett exempelprogram som kan hjälpa dig fråga frågor och till och med skapa nya

Quizbot är filen med klassen quizbot som kan fråga alla frågor och håller reda på poäng osv

Quizbot kan hämta frågor från 3 ställen, en sträng som har blivit exporterad av fråge generatorn, en JSON fil eller en opentdb url. De första två är lätta att fixa eftersom den laddar in ett JSON objekt. Opentdb har en annan funktion som tar in en url, laddar ned JSON objektet, html avkodar texten och till sist konverterar från deras format till et format som Quizbot kan förstå.

När Quizbot får frågorna som den ska fråga och ”fråga” funktionen körs kollar den först om ett index för en specifik fråga har angetts. 

Om det inte har det vill vi köra funktionen genom alla frågor på en gång. Vi kör funktionen igen med en slumpmässad frågeordning (om specificerat) med en specificerad index. 

Om det har det frågas den specifika frågan och om den ska slumpa frågealternativen gör den det med randomorder funktionen.

Randomorder funktionen tar in en fråga som argument och slumpar ordningen av svarsalternativen medan den håller koll på vilket svar som är rätt. Till sist returneras den nya frågan.

Headern för frågan skriv ut och ett procenttal för hur långt man har kommit visas.

Svarsalternativen skrivs ut i ordning och om man väljer ett alternativ som inte finns ställs frågan igen. Om användaren skriver ”exit” avslutas frågeställningen.

Om användaren har svarat rätt sparas 10 poäng multiplicerat med streaken delat med 10 till användarens poäng. Detta är för att ge användare med högre streak värde mer poäng.

När alla frågor är slut avslutas funktionen och ”finalscore” kan köras. Denna funktion skriver ut användarens poäng och bästa streak på ett fint sätt med padding för att alla väggar ska sitta där de ska.


# Usage
```pycon
>>> import QuizBot

>>> Frågebot = QuizBot.QuizBot(randomize=False, verbose=True) # Initiera frågebotten, randomisera svars alternativ
                                                       # Skriv också ut om det blir rätt eller fel
>>> Frågebot.loadConfig("frågor.json", file=True) # ladda frågor fån en fil (kan vara string eller dict också)

>>> Frågebot.fråga(randomize=True) # Fråga alla fråga i slumpmässig ordning

>>> Frågebot.finalscore() # visa slutresultat
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
    
# Quiz format

Detta är formatet för frågor som programet kan läsa, en "fråga", några "svar" och ett index (börjar på 1) på vilket svar som är rätt


    [
        {
            "fråga": "hur många magar har en ko?",
            "svar": [
                "tre stycken",
                "en stycken",
                "fyra stycken",
                "två stycken"
            ],
            "rätt": 3
        },
        {
            "fråga": "vilken är rätt???",
            "svar":[
                "rätt",
                "fel",
                "*fel*"
            ],
            "rätt": 1
        }
    ]
