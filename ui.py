
class ui:
    def __init__(self):
        pass

    def title(self):
        print("""
    ┏━━━━━━━━━━━━━━━━━━━━━┓
    ┃  ultimate quiz      ┃
    ┃      of destiny!!!  ┃
    ┃                     ┃
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

