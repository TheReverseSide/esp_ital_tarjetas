import json
import requests

'''
Universal sentence encoder: https://tfhub.dev/google/universal-sentence-encoder-multilingual/2
Word similarity: https://stackabuse.com/levenshtein-distance-and-text-similarity-in-python/
'''


front = []
back = []
with open("it_es_words.csv") as stream:
    for line in stream:
        f, b = line.strip().split(",")
        if f == b:
            continue
        front.append(f)
        back.append(b)



for i in range(len(front)): #
    print(i)
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": "Test",
                "modelName": "Basic ", # (and reversed card) #! Currently doesnt work
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
