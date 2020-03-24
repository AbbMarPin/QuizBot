
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
        print("="*35)

    def echo(self, text):
        print("|", text)

    def prompt(self, prompt_text):
        return input("| " + prompt_text + " > ")

    def prompt_list(self, list, text):
        for x, n in zip(list, range(1, len(list) + 1)):
            print("|", n, "|", x)
        return input("| " + text + " > ")

    def exit_(self, text):
        print("\n|", text)
        exit()

