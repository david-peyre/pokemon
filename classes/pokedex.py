# pokedex.py
import json

class Pokedex:
    def __init__(self): 
        self.pokedex_file = "pokedex.json" # Initialisation du nom du fichier
        self.pokedex = {"Pokemons apercus": []} # Initialisation du Pokédex

    # Méthode pour charger les données depuis un fichier
    def _load_data_from_file(self):
        try:
            with open(self.pokedex_file, "r") as f: # Ouverture du fichier en lecture
                return json.load(f) # Chargement des données depuis le fichier
        except FileNotFoundError: # Gestion de l'erreur si le fichier n'existe pas
            return None # Retour de la valeur None
        except json.decoder.JSONDecodeError: # Gestion de l'erreur si le décodage JSON échoue
            print("Erreur de décodage JSON dans le fichier pokedex.json") # Affichage du message d'erreur
            return None

    # Méthode pour charger le Pokédex depuis un fichier
    def load_from_file(self):
        data = self._load_data_from_file() # Chargement des données depuis le fichier
        if data: # Si les données existent
            self.pokedex = data # Mise à jour du Pokédex

    # Méthode pour sauvegarder le Pokédex dans un fichier
    def save_to_file(self):
        with open(self.pokedex_file, "w") as f: # Ouverture du fichier en écriture
            json.dump(self.pokedex, f, indent=2) # Écriture des données dans le fichier

    def add_to_pokedex(self, pokemon_data):
        self.load_from_file()  # Chargez d'abord les données existantes
        self.pokedex["Pokemons apercus"].append(pokemon_data)  # Ajoutez le nouveau Pokémon
        self.save_to_file()  # Sauvegardez le Pokédex mis à jour

    
    # Méthode pour afficher tous les pokémons du Pokédex
    def display_all_pokemons(self):
        pokemons = self.pokedex.get("Pokemons apercus", []) # Récupération des pokémons
        if pokemons:
            for index, pokemon_data in enumerate(pokemons, start=1): # Parcours de la liste des pokémons
                print(f"{index}. {pokemon_data['name']}") # Affichage du nom du pokémon
        else:
            print("Aucun Pokémon dans le Pokédex.") # Affichage du message d'erreur

    # Méthode pour afficher les détails d'un pokémon
    def __str__(self):
        return f"Pokédex personnel : {self.pokedex.get('Pokemons apercus', [])}" # Retour de la chaîne de caractères
    

if __name__ == "__main__":
    pokedex_instance = Pokedex()
    pokedex_instance.load_from_file()
    print(pokedex_instance)
