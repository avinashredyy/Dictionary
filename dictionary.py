import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    if usr_input in data.keys():
        return data[word]
    else:
        s = get_close_matches(usr_input, data.keys(), n=1)[0]
        print("Did you mean? ", s, ". If Yes press Y If No press N")
        ans = input().lower()
        if ans == "y":
            return data[s]
        else:
            return "No word found"

usr_input = input("Enter a word: ").lower()
print(meaning(usr_input))
