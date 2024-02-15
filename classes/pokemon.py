# pokemon.py
import pygame
import sys
from pokedex import Pokedex
import json


class Pokemon:
    def __init__(self, pokemon_num, name, pokemon_type, evo_lvl, hp, attack_pt, defense, xp_points, base_hp, image_path):
        self.pokemon_num = pokemon_num
        self.name = name
        self.poke_type = pokemon_type
        self.evo_lvl = evo_lvl
        self.hp = hp
        self.attack_pt = attack_pt
        self.defense = defense
        self.xp_points = xp_points
        self.base_hp = base_hp
        self.image = pygame.image.load(image_path)

    # Méthode pour convertir les données en dictionnaire
    def to_dict(self):
        return {
            "pokemon_num": self.pokemon_num,
            "name": self.name,
            "poke_type": self.poke_type,
            "evo_lvl": self.evo_lvl,
            "hp": self.hp,
            "attack_pt": self.attack_pt,
            "defense": self.defense,
            "xp_points": self.xp_points,
            "base_hp": self.base_hp
        }
    
    # Méthode pour convertir les données depuis un dictionnaire
    def from_dict(self, data):
        self.pokemon_num = data.get("pokemon_num", 0)
        self.name = data.get("name", "")
        self.poke_type = data.get("poke_type", "")
        self.evo_lvl = data.get("evo_lvl", 0)
        self.hp = data.get("hp", 0)
        self.attack_pt = data.get("attack_pt", 0)
        self.defense = data.get("defense", 0)
        self.xp_points = data.get("xp_points", 0)
        self.base_hp = data.get("base_hp", 0)

    # Méthode pour vérifier si l'évolution est possible
    def evo_ok (self):
        if self.evo_lvl == 0 and self.xp_points >= 1: # Si le niveau d'évolution est 0 et les points d'expérience sont supérieurs ou égaux à 1
            print(f"{self.name} peut évoluer au prochain stade.")
            return True # Retourne True
        elif self.evo_lvl == 1 and self.xp_points >= 3: # Si le niveau d'évolution est 1 et les points d'expérience sont supérieurs ou égaux à 3
            print(f"{self.name} lui reste une évolution possible.") 
            return True # Retourne True
        else: # Sinon
            print(f"{self.name} n'a plus d'évolution possible.")
            return False # Retourne False
    
    def gain_xp(self, points):
        self.xp_points += points
        print(f"{self.name} a gagné {points} points d'XP, vous avez maintenant {self.xp_points} points d'expérience et votre evo_lvl est {self.evo_lvl}.") # Affichage du message de gain d'expérience
            
    # Méthode pour évoluer le Pokémon
    def evolve_to(self, evolved_pokemon):
        print(f"{self.name} évolue en {evolved_pokemon.name}")
        self.pokemon_num = evolved_pokemon.pokemon_num
        self.name = evolved_pokemon.name
        self.poke_type = evolved_pokemon.poke_type
        self.evo_lvl = evolved_pokemon.evo_lvl
        self.hp = evolved_pokemon.hp
        self.attack_pt = evolved_pokemon.attack_pt
        self.defense = evolved_pokemon.defense
        self.xp_points = evolved_pokemon.xp_points
        self.base_hp = evolved_pokemon.base_hp

        print(f"Votre pokémon évolu en {self.name}, hp: {self.hp}, attaque: {self.attack_pt}")

    # Méthode pour faire évoluer le Pokémon
    def evolve(self):
        if self.evo_ok(): # Si l'évolution est possible
            if self.name == "Bulbizarre":
                evolved_pokemon = Pokemon(2, "Herbizarre", "plante", 1, 300, 80, 30, 0, 300, "classes/assets/Pokemon/Sprite_2.png")
                self.evolve_to(evolved_pokemon)
            elif self.name == "Herbizarre":
                evolved_pokemon = Pokemon(3, "Florizarre", "plante", 2, 400, 100, 40, 0, 400, "classes/assets/Pokemon/Sprite_3.png" )
                self.evolve_to(evolved_pokemon)
            elif self.name == "Carapuce":
                evolved_pokemon = Pokemon(5, "Carabaffe", "eau", 1, 300, 80, 30, 0, 300,"classes/assets/Pokemon/Sprite_5.png    ")
                self.evolve_to(evolved_pokemon)
            elif self.name == "Carabaffe":
                evolved_pokemon = Pokemon(6, "Tortank", "eau", 2, 400, 100, 40, 0, 400, "classes/assets/Pokemon/Sprite_6.png")
                self.evolve_to(evolved_pokemon)
            elif self.name == "Salamèche":
                evolved_pokemon = Pokemon(8, "Reptincel", "feu", 1, 300, 80, 30, 0, 300, "classes/assets/Pokemon/Sprite_8.png")
                self.evolve_to(evolved_pokemon)
            elif self.name == "Reptincel":
                evolved_pokemon = Pokemon(9, "Dracofeu", "feu", 2, 400, 100, 40, 0, 400, "classes/assets/Pokemon/Sprite_9.png")
                self.evolve_to(evolved_pokemon)
            elif self.name == "Roucool":
                evolved_pokemon = Pokemon(11, "Roucoups", "normal", 1, 300, 80, 30, 0, 300, "classes/assets/Pokemon/Sprite_11.png")
                self.evolve_to(evolved_pokemon)
            elif self.name == "Roucoups":
                evolved_pokemon = Pokemon(12, "Roucarnage", "normal", 2, 400, 100, 40, 0, 400, "classes/assets/Pokemon/Sprite_12.png")
                self.evolve_to(evolved_pokemon)
            elif self.name == "Tentacool":
                evolved_pokemon = Pokemon(14, "Tentacruel", "eau", 2, 350, 70, 65, 0, 350, "classes/assets/Pokemon/Sprite_14.png")
                self.evolve_to(evolved_pokemon)
            elif self.name == "Ramoloss":
                evolved_pokemon = Pokemon(16, "Flagadoss", "eau", 2, 350, 80, 70, 0, 350, "classes/assets/Pokemon/Sprite_16.png")
                self.evolve_to(evolved_pokemon)
            elif self.name == "Doduo":
                evolved_pokemon = Pokemon(18, "Dodrio", "normal", 2, 350, 85, 55, 0, 350, "classes/assets/Pokemon/Sprite_18.png")
                self.evolve_to(evolved_pokemon)
            elif self.name == "Otaria":
                evolved_pokemon = Pokemon(20, "Lamantine", "eau", 2, 350, 90, 60, 0, 350, "classes/assets/Pokemon/Sprite_20.png")
                self.evolve_to(evolved_pokemon)
            elif self.name == "Goupix":
                evolved_pokemon = Pokemon(22, "Feunard", "feu", 2, 350, 85, 55, 0, 350, "classes/assets/Pokemon/Sprite_22.png")
                self.evolve_to(evolved_pokemon)
            elif self.name == "Miaouss":
                evolved_pokemon = Pokemon(24, "Persian", "normal", 2, 350, 70, 60, 0, 350, "classes/assets/Pokemon/Sprite_24.png")
                self.evolve_to(evolved_pokemon)
            else:
                print(f"{self.name} ne peut pas évoluer.")  
                pass

    def heal(self):
        self.hp = self.base_hp
    
    def __str__(self):    
        return f"{self.name} est de type {self.poke_type}, a {self.hp} points de vie, {self.attack_pt} points d'attaque et {self.defense} points de défense."

# Liste des Pokémon
POKEMON_LIST = [
    Pokemon(1, "Bulbizarre", "plante", 0, 200, 60, 20, 0, 200, "classes/assets/Pokemon/Sprite_1.png"),
    Pokemon(2, "Herbizarre", "plante", 1, 300, 80, 30, 0, 300, "classes/assets/Pokemon/Sprite_2.png"),
    Pokemon(3, "Florizarre", "plante", 2, 400, 100, 40, 0, 400, "classes/assets/Pokemon/Sprite_3.png"),
    Pokemon(4, "Carapuce", "eau", 0, 200, 60, 20, 0, 200, "classes/assets/Pokemon/Sprite_4.png"),
    Pokemon(5, "Carabaffe", "eau", 1, 300, 80, 30, 0, 300, "classes/assets/Pokemon/Sprite_5.png"),
    Pokemon(6, "Tortank", "eau", 2, 400, 100, 40, 0, 400, "classes/assets/Pokemon/Sprite_6.png"),
    Pokemon(7, "Salamèche", "feu", 0, 200, 60, 20, 0, 200, "classes/assets/Pokemon/Sprite_7.png"),
    Pokemon(8, "Reptincel", "feu", 1, 300, 80, 30, 0, 300, "classes/assets/Pokemon/Sprite_8.png"),
    Pokemon(9, "Dracofeu", "feu", 2, 400, 100, 40, 0, 400, "classes/assets/Pokemon/Sprite_9.png"),
    Pokemon(10, "Roucool", "normal", 0, 200, 60, 20, 0, 200, "classes/assets/Pokemon/Sprite_10.png"),
    Pokemon(11, "Roucoups", "normal", 1, 300, 80, 30, 0, 300, "classes/assets/Pokemon/Sprite_11.png"),
    Pokemon(12, "Roucarnage", "normal", 2, 400, 100, 40, 0, 400, "classes/assets/Pokemon/Sprite_12.png"),
    Pokemon(13, "Tentacool", "eau", 1, 250, 40, 35, 0, 250, "classes/assets/Pokemon/Sprite_13.png"),
    Pokemon(14, "Tentacruel", "eau", 2, 350, 70, 55, 0, 350, "classes/assets/Pokemon/Sprite_14.png"),
    Pokemon(15, "Ramoloss", "eau", 1, 250, 60, 45, 0, 250, "classes/assets/Pokemon/Sprite_15.png"),
    Pokemon(16, "Flagadoss", "eau", 2, 350, 80, 55, 0, 350, "classes/assets/Pokemon/Sprite_16.png"),
    Pokemon(17, "Doduo", "normal", 1, 250, 65, 35, 0, 250, "classes/assets/Pokemon/Sprite_17.png"),
    Pokemon(18, "Dodrio", "normal", 2, 350, 85, 55, 0, 350, "classes/assets/Pokemon/Sprite_18.png"),
    Pokemon(19, "Otaria", "eau", 1, 250, 70, 40, 0, 250, "classes/assets/Pokemon/Sprite_19.png"),
    Pokemon(20, "Lamantine", "eau", 2, 350, 90, 55, 0, 350, "classes/assets/Pokemon/Sprite_20.png"),
    Pokemon(21, "Goupix", "feu", 1, 250, 65, 35, 0, 250, "classes/assets/Pokemon/Sprite_21.png"),
    Pokemon(22, "Feunard", "feu", 2, 350, 85, 55, 0, 350, "classes/assets/Pokemon/Sprite_22.png"),
    Pokemon(23, "Miaouss", "normal", 1, 250, 45, 35, 0, 250, "classes/assets/Pokemon/Sprite_23.png"),
    Pokemon(24, "Persian", "normal", 2, 350, 70, 55, 0, 350, "classes/assets/Pokemon/Sprite_24.png"),
]

