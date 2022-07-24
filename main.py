import json
from difflib import get_close_matches

data = json.load(open("definition.json"))


def get_meaning(_word):
    _word = _word.lower()
    matches = get_close_matches(_word, data.keys(), 1)
    if _word in data:
        return data[_word]
    elif matches:
        error_confirmation = input("Did you mean {}? Y/N.".format(matches[0]))
        error_confirmation = error_confirmation.lower()
        if error_confirmation == "y":
            return data[matches[0]]
        elif error_confirmation != "n":
            print("I didn't get your answer")



def format_definition(defi):
    if defi is not None:
        n = 1
        for _ in defi:
            print(f"{n}. {defi[n - 1]}")
            n += 1
    else:
        print("The word does not exist. Please check")


w = ""
while w != "Q":
    w: str = input("Enter a word: ")
    definition = get_meaning(w)
    format_definition(definition)
    input("Press Enter for a new search... or Q to Quit")
    print('\n'*10)
