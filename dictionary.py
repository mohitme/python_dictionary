import json
from difflib import get_close_matches
data = json.load(open("dictionary.json"))

def ret_def(word):
    if word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        res = input("Did you mean '%s' instead? [y or n]" % get_close_matches(word,data.keys())[0])
        if res == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif res == 'n':
            return "That word doesn't exist"
        else: return "Invalid Input"
        

out = ret_def(input("Enter a word: "))

if type(out) == list:
    for i in out:
        print("-",i)
else:
    print("-",out)


