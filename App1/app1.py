import json
from difflib import get_close_matches
data=json.load(open("data.json"))
out=''
def translate(w):
    if w.lower() in data:
        return data[w]
    elif w.capitalize() in data:
        return data[w.capitalize()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w.lower(),data.keys()))>0:
        while True:
            print("Did you mean %s instead? (y/n)" % get_close_matches(w.lower(), data.keys())[0])
            a=input()
            if a.lower()=='y':
                return data[get_close_matches(w.lower(), data.keys())[0]]
                break
            elif a.lower()=='n':
                break
            else:
                print('\n Invalid input, try again!')

word=input("Enter Word to Search:")
out=translate(word)
if out==None:
    print(f"\n Word {word} not found in the dictionary!")
elif len(out)>1:
    for a in out:
        print(a)
elif len(out)==1:
    print(out[0])
