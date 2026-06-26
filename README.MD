# PokeApp

# 🇬🇧 EN 

## Description
A small desktop app that connects to the *PokéAPI* and displays some info on random or searched pokémon.
Please check the **Installation** section on how to run it on your pc.

## Installation

1. Clone the repository:
    git clone https://github.com/DimitriOrfanoudakis/PokeApp
    cd PokeApp
2. Create and activate a virtual environment:
    python -m venv venv (if not working, try python3 -m venv venv)
    
    Windows(Command Prompt): venv\Scripts\activate.bat
    Windows(Powershell): venv\Scripts\Activate.ps1
    MacOS/Linux: source venv/bin/activate
3. Install dependencies:
    pip install -r requirements.txt
4. Run the app:
    python app.py


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