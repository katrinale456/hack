import json
import os

possibleThemes = {"happy": "https://wallpapercave.com/wp/3klnmq2.jpg", 
                "sad": "https://wallpapercave.com/wp/wp4696793.jpg", 
                "calm": "https://cdn.wallpapersafari.com/63/53/43JAMq.jpg"}
theme = ""

def changeBackground():
    while True:
        i = input("What mood are you feeling today? (happy, sad, calm)\n")

        if i in possibleThemes.keys():
            break

    return possibleThemes[i]

print(changeBackground())
filename = 'settings.json'

with open(filename, "r") as json_file:
    data = json.load(json_file)

print(data)
