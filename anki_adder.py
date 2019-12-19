import json
import requests

'''
Universal sentence encoder: https://tfhub.dev/google/universal-sentence-encoder-multilingual/2
Word similarity: https://stackabuse.com/levenshtein-distance-and-text-similarity-in-python/
'''


front = []
back = []

# Put your csv file in the same directory as this file, then just enter the name like below
with open("it_es_words.csv") as stream:
    for line in stream:
        f, b = line.strip().split(",")
        if f == b:
            continue
        front.append(f) # This says front card is the first column, switch this line and the following for the reverse
        back.append(b)



for i in range(len(front)): #
    print(i)
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "Test", # Edit your deck name as you want
                "modelName": "Basic ", # (and reversed card) Currently doesnt work
                "fields": {
                    "Front": front[i],
                    "Back": back[i]
                },
                "options": {
                    "allowDuplicate": False
                },
                "tags": [
                    ""
                ]
            }
        }
    }

    response = requests.post("http://localhost:8765", data=json.dumps(payload))
    print(response)
    print(response.content)

print("Done")


#Run set on list of both and subtracting them
