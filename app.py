import customtkinter as ctk
from PIL import Image, ImageTk
from io import BytesIO
import random
import requests
import pygame

DEFAULT_WIDTH = 280
DEFAULT_HEIGHT = 360
POKEMON_LIMIT = 386 # Only pokemon from first 3 generations

class Pokemon:
    poke_cache = {} # Cache fetched pokemon data, so every name only fetches once from API
    def __init__(self, name):
        self.name = name
        self.data = None
        self.photo = None
        if not self.check_cache():
            self.fetch_data()
    
    def check_cache(self):
        """"Check Pokemon name before API request"""
        if self.poke_cache.get(self.name):
            self.data = self.poke_cache.get(self.name)            
            return True
        else:
            return None
    
    def fetch_data(self):
        """Fetch Pokemon data from API"""
        try:
            r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
            r.raise_for_status()
            self.data = r.json()
            self.poke_cache.update({self.name : self.data})            
        except requests.RequestException as e:
            print(f"Error fetching {self.name}: {e}")
            self.data = None
    
    def get_sprite(self):
        """Return sprite URL"""
        if self.data:
            return self.data['sprites']['front_default']
        return None

    def get_cry(self):
        """Return cry/sound url"""
        if self.data:
            return self.data['cries']['legacy']
        return None
    
    def get_height(self) -> float:
        """Height in decimetres (converted to m before returning)"""
        return (self.data['height'] /10) if self.data else None
    
    def get_weight(self) -> float:
        """Weight in hectograms (converted to kg before returning)"""
        return (self.data['weight'] /10) if self.data else None
    
    def get_id(self):
        """Return Pokedex ID"""
        return self.data['id'] if self.data else None
    
    def get_type(self):
        """Return type(Normal, Fire etc.)"""
        return self.data['types'][0]['type']['name']


# GUI setup
class PokedexApp:
    

    def __init__(self, root):
        self.root = root
        pygame.mixer.init()
        self.poke_names = self._load_pokemon_list()
        if not self.poke_names:
            print("ERROR: Could not load Pokemon data. Please check your internet connection.")
            return
        self.current_pokemon = None
        self._setup_ui()
        self.load_random_pokemon()
                
    
    def _load_pokemon_list(self):
        """Fetch list of Pokemon names from API"""
        try:
            r = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={POKEMON_LIMIT}', timeout=5) 
            r.raise_for_status()
            r_dict = r.json()
            return [poke['name'] for poke in r_dict.get('results', [])]
        except requests.RequestException as e:
            print(f"Failed to load Pokemon list: {e}")
            return []
    
    def _setup_ui(self):
        """Create GUI elements"""
        frm = ctk.CTkFrame(self.root)
        frm.grid(sticky="nsew")
        
        # Configure root grid weights so frame expands
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Configure frame grid weights for centering
        frm.columnconfigure(0, weight=1)
        frm.columnconfigure(1, weight=1)
        frm.rowconfigure(0, weight=1)
        frm.rowconfigure(1, weight=1)
        frm.rowconfigure(2, weight=1)
        frm.rowconfigure(3, weight=1)

        # Name label
        self.name_label = ctk.CTkLabel(frm, text="", font=("Arial", 16, "bold"), anchor="center")
        self.name_label.grid(column=0, row=0, columnspan=2, pady=10, sticky="ew")
        
        # Image label
        self.image_label = ctk.CTkLabel(frm, text="")
        self.image_label.grid(column=0, row=1, columnspan=2, pady=10)
        
        # Info label
        self.info_label = ctk.CTkLabel(frm, text="")
        self.info_label.grid(column=0, row=2, columnspan=2, pady=10)
        
        # Buttons
        ctk.CTkButton(frm, text="Search", command=self.search_poke).grid(column=0, row=3, padx=5)
        ctk.CTkButton(frm, text="Random Pokémon", command=self.load_random_pokemon).grid(column=1, row=3, padx=5)
    
    def load_random_pokemon(self):
        """Load a random Pokemon"""
        name = random.choice(self.poke_names)
        self.display_pokemon(name)
    
    def display_error(self):
        """Display an error if name not found """
        self.name_label.configure(text="ERROR")
        # Open the local image file using PIL
        local_image = Image.open("error.png")            
        # Resize it to match the standard sprite dimensions (200x200)
        local_image = local_image.resize((200, 200), Image.Resampling.LANCZOS)            
        # Wrap it in a CustomTkinter image container
        error_photo = ctk.CTkImage(light_image=local_image, dark_image=local_image, size=(200, 200))            
        # Apply it to the label and save a reference to prevent garbage collection
        self.image_label.configure(image=error_photo)
        self.image_label.image = error_photo
        self.info_label.configure(text="There is no pokemon with that name.\nPlease try again!")


    def display_pokemon(self, name):
        """Display requested or random pokemon"""
        self.current_pokemon = Pokemon(name)
        self.name_label.configure(text=self.current_pokemon.name.capitalize())
        self.display_sprite()
        self.show_info()
        self.play_sound()

    def search_poke(self):
        """Get user input and search for that name"""
        dialog = ctk.CTkInputDialog(text="Type a name (up to 3rd gen pokemon):", title="Pokésearch")
        # need to delay the call .iconbitmap() at least 200ms or ctk overwrites with default icon
        dialog.after(250, lambda: dialog.iconbitmap("pokemon.ico"))
        searched_name = dialog.get_input()
        if searched_name != None:
            if searched_name.lower() in self.poke_names:
                self.display_pokemon(searched_name.lower())            
            else:
                self.display_error()
        else:
            return 

    def display_sprite(self):
        """Load and display the Pokemon sprite"""
        spr_w = 200 # Sprite width
        spr_h = 200 # Sprite height
        try:
            sprite_url = self.current_pokemon.get_sprite()
            if sprite_url:
                response = requests.get(sprite_url)
                image_data = (Image.open(BytesIO(response.content))).resize((spr_w, spr_h), Image.Resampling.LANCZOS)
                photo = ctk.CTkImage(light_image=image_data, dark_image=image_data, size=(spr_w, spr_h))
                self.image_label.configure(image=photo)
                self.image_label.image = photo  # Keep a reference to prevent gargabe collection
        except Exception as e:
            print(f'Could not load image sprite: {e}')
    
    def play_sound(self):
        """Load and play the Pokemon cry/sound"""
        try:                    
            cry_url = self.current_pokemon.get_cry()
            if cry_url:            
                response = requests.get(cry_url)
                sound_data = BytesIO(response.content)
                sound = pygame.mixer.Sound(sound_data)
                sound.play()
        except Exception as e:
            print(f'Could not play sound: {e}')
    
    def show_info(self):
        """Display Pokemon info"""
        if self.current_pokemon and self.current_pokemon.data:
            height = self.current_pokemon.get_height()
            weight = self.current_pokemon.get_weight()
            pokedex_id = self.current_pokemon.get_id()
            poke_type = self.current_pokemon.get_type()
            info = f"Pokedex ID: {pokedex_id}\nType: {poke_type.capitalize()}\nHeight: {height}m | Weight: {weight}kg" 
            self.info_label.configure(text=info)

def setup_window(root):
    """Sets up and configures the window so it has the same proportions on any screen"""
    # Add title and icon    
    root.title("Pokéfan")
    root.iconbitmap('pokemon.ico')

    # Rescaling
    # Get the DPI scaling factor
    dpi_scale = root.winfo_fpixels('1i') / 96  # 96 is standard DPI    
    # Adjust geometry based on DPI
    width = int(DEFAULT_WIDTH * dpi_scale)
    height = int(DEFAULT_HEIGHT * dpi_scale)
    root.geometry(f"{width}x{height}")

    root.resizable(False, False) 



if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    root = ctk.CTk()
    setup_window(root)

    app = PokedexApp(root)
    root.mainloop()
