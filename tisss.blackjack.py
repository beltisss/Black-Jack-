import random


class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def points(self):
        """Renvoie la valeur brute de la carte pour le calcul du score."""
        if self.valeur == 1:
            return 11
        if 2 <= self.valeur <= 10:
            return self.valeur
        return 10

    def __str__(self):
        if self.valeur == 1:
            nom = "As"
        elif 2 <= self.valeur <= 10:
            nom = str(self.valeur)
        elif self.valeur == 11:
            nom = "Valet"
        elif self.valeur == 12:
            nom = "Dame"
        else:
            nom = "Roi"

        if self.couleur == 0:
            couleur = "pique"
        elif self.couleur == 1:
            couleur = "coeur"
        elif self.couleur == 2:
            couleur = "carreau"
        else:
            couleur = "trèfle"

        return f"{nom} de {couleur}"


class Paquet:
    def __init__(self):
        self.cartes = [Carte(valeur, couleur) for valeur in range(1, 14) for couleur in range(4)]
        self.melanger()

    def melanger(self):
        """Mélange le paquet de cartes."""
        random.shuffle(self.cartes)

    def distribuer(self):
        """Retire et renvoie la première carte du paquet."""
        if not self.cartes:
            raise ValueError("Le paquet est vide.")
        return self.cartes.pop(0)


class Main:
    def __init__(self, nom):
        self.nom = nom
        self.cartes = []

    def ajouter_carte(self, carte):
        """Ajoute une carte à la main."""
        self.cartes.append(carte)

    def score(self):
        """Calcule le score en gérant correctement les As."""
        total = 0
        nb_as = 0

        for carte in self.cartes:
            total += carte.points()
            if carte.valeur == 1:
                nb_as += 1

        while total > 21 and nb_as > 0:
            total -= 10
            nb_as -= 1

        return total

    def est_buste(self):
        return self.score() > 21

    def afficher(self, cacher_premiere=False):
        """Affiche la main. Option pour cacher la première carte de la banque."""
        print(f"\n{self.nom} :")
        for i, carte in enumerate(self.cartes):
            if cacher_premiere and i == 0:
                print("- [Carte cachée]")
            else:
                print(f"- {carte}")

        if cacher_premiere:
            print("Score visible : ?")
        else:
            print(f"Score : {self.score()}")


class BlackJack:
    def __init__(self):
        self.paquet = Paquet()
        self.joueur = Main("Joueur")
        self.banquier = Main("Banquier")

    def distribuer_depart(self):
        for _ in range(2):
            self.joueur.ajouter_carte(self.paquet.distribuer())
            self.banquier.ajouter_carte(self.paquet.distribuer())

    def tour_joueur(self):
        while True:
            self.joueur.afficher()
            self.banquier.afficher(cacher_premiere=True)

            if self.joueur.est_buste():
                print("\nTu dépasses 21. Tu as perdu.")
                return False

            choix = input("\nVeux-tu une nouvelle carte ? (o/n) : ").strip().lower()
            while choix not in {"o", "n"}:
                choix = input("Réponds par 'o' pour oui ou 'n' pour non : ").strip().lower()

            if choix == "o":
                nouvelle = self.paquet.distribuer()
                self.joueur.ajouter_carte(nouvelle)
                print(f"\nTu pioches : {nouvelle}")
            else:
                return True

    def tour_banquier(self):
        print("\nTour du banquier...")
        self.banquier.afficher()

        while self.banquier.score() < 17:
            carte = self.paquet.distribuer()
            self.banquier.ajouter_carte(carte)
            print(f"Le banquier pioche : {carte}")

        self.banquier.afficher()

    def afficher_resultat(self):
        score_joueur = self.joueur.score()
        score_banquier = self.banquier.score()

        print("\n===== Résultat =====")
        self.joueur.afficher()
        self.banquier.afficher()

        if self.banquier.est_buste():
            print("\nLe banquier dépasse 21. Tu gagnes !")
        elif score_joueur > score_banquier:
            print("\nTu gagnes !")
        elif score_joueur < score_banquier:
            print("\nLe banquier gagne.")
        else:
            print("\nÉgalité.")

    def jouer(self):
        print("===== BLACKJACK =====")
        self.distribuer_depart()

        if not self.tour_joueur():
            return

        self.tour_banquier()
        self.afficher_resultat()


if __name__ == "__main__":
    jeu = BlackJack()
    jeu.jouer()
