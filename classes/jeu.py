# jeu.py
from pokemon import Pokemon
from combat import Combat

# Classe pour gérer le jeu
class Jeu:
    def __init__(self):
        self.notre_pokemon = self.choose_starter() # Initialisation du Pokémon du joueur

    # Méthode pour choisir le Pokémon de départ
    @staticmethod
    def choose_starter():
        print("Choisissez votre Pokémon:") # Affichage du message de choix
        print("1. Bulbizarre (Plante)") # Affichage des choix
        print("2. Carapuce (Eau)") # Affichage des choix
        print("3. Salamèche (Feu)") # Affichage des choix

        while True: # Boucle pour la saisie du choix
            choix = input("Saisissez le numéro correspondant à votre choix: ") # Saisie du choix

            if choix == "1": # Si le choix est 1
                return Pokemon(1, "Bulbizarre", "plante", 0, 200, 60, 20, 0, 200,) # Retour du Pokémon Bulbizarre
            elif choix == "2": # Si le choix est 2
                return Pokemon(4, "Carapuce", "eau", 0, 200, 60, 20, 0, 200) # Retour du Pokémon Carapuce
            elif choix == "3": # Si le choix est 3
                return Pokemon(7, "Salamèche", "feu", 0, 200, 60, 20, 0, 200) # Retour du Pokémon Salamèche
            else:
                print("Choix invalide. Veuillez choisir à nouveau.") # Affichage du message d'erreur

    def play(self):
        print(f"Vous avez choisi {self.notre_pokemon.name}!") # Affichage du Pokémon choisi

        while True: # Boucle pour le jeu
            adversary = Combat.choose_opponent() # Choix d'un adversaire aléatoire
            combat = Combat(self.notre_pokemon, adversary) # Initialisation du combat
            combat.do_combat() # Lancement du combat

            if input("Voulez-vous continuer à jouer? (o/n): ").lower() != "o": # Vérification de la continuité du jeu
                break # Sortie de la boucle si la réponse est différente de "o"

if __name__ == "__main__":
    game = Jeu()
    game.play()