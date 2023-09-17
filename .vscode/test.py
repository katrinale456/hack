import json
import os
import webbrowser


data = {}
input = input("what is your mood today? default, happy, sad, or calm? \n")

if input == "happy":
    
    data = {
        "liveServer.settings.port": 5501,
        "workbench.colorCustomizations": {
            "editor.background": "#191b1b",

        },
        
        "background.fullscreen": {
            "images": ["https://avante.biz/wp-content/uploads/Happy-Desktop-Backgrounds/Happy-Desktop-Backgrounds-041.jpg"], 
            "opacity": 0.91, 
            "size": "cover", 
            "position": "center", 
            "interval": 0 
        },
         "workbench.colorCustomizations": {
        "editor.foreground": "#000"
    },
    }

    webbrowser.open('../happy.mp3')

elif input == "sad":

        data = {
        "liveServer.settings.port": 5501,
        "workbench.colorCustomizations": {
            "editor.background": "#191b1b",
            "editor.fontFamily": "Menlo, Monaco, 'Courier New', monospace",
            "editor.fontColor": "white",
        },
        "background.fullscreen": {
            "images": ["https://wallpapercave.com/wp/wp4696794.jpg"], 
            "opacity": 0.91, 
            "size": "cover", 
            "position": "center", 
            "interval": 0 
        },
        "workbench.colorCustomizations": {
        "editor.foreground": "#777"
    },
    }
        webbrowser.open('C:/Users/aahme/OneDrive/Desktop/hackmitstuffs/hack/.vscode/sad.mp3')

        
elif input == "calm":
         


        data = {
        "liveServer.settings.port": 5501,
        "workbench.colorCustomizations": {
            "editor.background": "#191b1b"
        },
        "background.fullscreen": {
            "images": ["https://wallpaperset.com/w/full/2/5/f/38669.jpg"], 
            "opacity": 0.91, 
            "size": "cover", 
            "position": "center", 
            "interval": 0 
        },
        "workbench.colorCustomizations": {
        "editor.foreground": "#453"
    }
    }
    
        webbrowser.open('C:/Users/aahme/OneDrive/Desktop/hackmitstuffs/hack/.vscode/calm.mp3')

elif input == "default":  

        data = {
        "liveServer.settings.port": 5501,
        "workbench.colorCustomizations": {
            "editor.background": "#191b1b"
        },
        "background.fullscreen": {
            "images": [], 
            "opacity": 0.91, 
            "size": "cover", 
            "position": "center", 
            "interval": 0 
        },
        "workbench.colorCustomizations": {
        "editor.foreground": "#000"
    }
    }
    



# Specify the file name where you want to store the JSON data
file_name = "C:/Users/aahme/OneDrive/Desktop/hackmitstuffs/.vscode/settings.json"

# Method 1: Using json.dump() to write data to a JSON file
with open(file_name, "w") as json_file:
    json.dump(data, json_file)

# Method 2: Using json.dumps() to convert data to a JSON-formatted string
json_string = json.dumps(data)

# You can also write the JSON string to a file if needed
with open("data_string.json", "w") as json_string_file:
    json_string_file.write(json_string)
