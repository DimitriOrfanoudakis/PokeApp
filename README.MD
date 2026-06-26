# PokeApp

# 🇬🇧🇺🇸 EN 

## Description
A small desktop app that connects to the *PokéAPI* and displays some info on random or searched pokémon.
Please check the **Installation** section on how to run it on your pc.

## Installation
**IMPORTANT: The latest Python version should be installed on your system**
1. Clone the repository:
    - git clone https://github.com/DimitriOrfanoudakis/PokeApp
    - cd PokeApp
2. Create and activate a virtual environment:
    - python -m venv venv 
    - (if not working, try python3 -m venv venv)
    

    - Windows(Command Prompt): venv\Scripts\activate.bat
    - Windows(Powershell): venv\Scripts\Activate.ps1
    - MacOS/Linux: source venv/bin/activate
3. Install dependencies:
    - pip install -r requirements.txt
4. Run the app:
    - python app.py


## Development Process
This was created as a learning project to get to know a GUI library in Python.
Initially just a program that selected a random word from a list and displayed it, I remembered the *PokéAPI*,
which I had stumbled upon at some point and thought it would be cool to display random Pokémon instead.

After finding out how to request data from the API and parse the JSON response,
I looked into adding a sound/cry and image when each pokémon was displayed, similar to how the pokédex in the older games did it.
These sound and image files are also requested from the API.

Finally, a search function was implemented, to make it more like an actual pokémon lookup tool.

Libraries used and why:
- TkInter (initially), later switched to CustomTkInter for a nicer design and dark mode
- requests for HTTP methods    
- io/BytesIO for binary stream conversions
- Pillow (PIL) for image files
- pygame for sound files

Biggest challenge:
    After first implementation of the app, I thought it was running fine until I moved it to a second display and
    buttons and labels were overlapping and out of proportion. This taught me to consider differences in display size and the concept of scaling.



🇩🇪🇦🇹🇨🇭 DE

## Beschreibung
Eine kleine Desktop-App, die sich mit der *PokéAPI* verbindet und ein paar Infos über zufällige oder gesuchte Pokémon anzeigt.
Zum ausführen der App auf dem eigenen PC, bitte den Anweisungen unter **Installation** folgen.

## Installation
**WICHTIG: Die neueste Python-Version sollte auf dem System installiert sein.**
1. Repository klonen:
    - git clone https://github.com/DimitriOrfanoudakis/PokeApp
    - cd PokeApp
2. Virtual Environent erstellen und aktivieren:
    - python -m venv venv 
    - (falls der Befehl mit python nicht funktioniert, bitte "python3 -m venv venv" probieren)
    

    - Windows(Command Prompt): venv\Scripts\activate.bat
    - Windows(Powershell): venv\Scripts\Activate.ps1
    - MacOS/Linux: source venv/bin/activate
3. Dependencies installieren:
    - pip install -r requirements.txt
4. App ausführen:
    - python app.py

## Entwicklungsprozess
Die App begann als Lernprojekt um zum ersten Mal eine GUI in Python kennenzulernen.
Anfangs war es ein Programm, welches nach Knopfdruck ein zufälliges Wort aus einer Liste auswählte und anzeigte.

Anschließend erinnerte ich mich an die *PokéAPI*, welche ich zufällig mal entdeckt hatte und fand die Idee cool,
statt irgendwelcher Wörter zufällige Pokémon anzeigen zu lassen.

Nachdem ich herausgefunden hatte, wie man Daten von der API anfordert und die JSON-Rückgabe verarbeitet,
wollte ich neben ein paar Textinfos auch ein Bild des Pokémons anzeigen und einen Ton/Ruf abspielen,
ähnlich wie es im Pokédex der alten Spiele war.
Diese Daten werden ebenfalls von der API angefordert.

Zuletzt wurde neben der Zufälligen Anzeige auch eine Suche implementiert, um einem echten Nachschlagtool für Pokémon zu ähneln.

Verwendete Libaries:
- TkInter (anfangs), später auf CustomTkInter gewechselt für ein hübscheres Design und Dark-Mode-Optionen
- requests für HTTP Methoden
- io/BytesIO für binary stream conversions
- Pillow (PIL) für Bilddateien
- pygame für Sounddateien

Größte Herausforderung:

Nach der ersten Implementierung der App mit Suchfunktion sah alles gut aus, bis ich die App auf einen Zweitbildschirm gezogen habe.
Auf einmal waren Buttons und Labels verschoben und überlappten sich teilweise gegenseitig. Dadurch wurde ich auf das Konzept der Skalierung aufmerksam 
und auf die Notwendigkeit verschiedene Anzeigeoptionen zu bedenken.