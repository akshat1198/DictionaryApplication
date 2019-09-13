import json  
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    match = get_close_matches(word,data.keys())
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(match)>0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %match[0])
        if yn.upper() == "Y":
            return data[match[0]]
        elif yn.upper() =="N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "Word doesn't exist"

word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)