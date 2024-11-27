from random import randint
class Carte:
    def __init__(self, _val, _coul):
        self.valeur = _val
        self.couleur = _coul
    def __str__(self):
        """
        renvoie la valeur et le couleur de la carte
        """
        if self.valeur == 1:
            nom = "As"
        elif self.valeur>=2 and self.valeur<=10:
            nom = str(self.valeur)
        elif self.valeur == 11 :
            nom = "valet"
        elif self.valeur == 12 :
            nom = "Dame"
        else :
            nom="Roi"

        if self.couleur == 0:
            couleur = "pique"
        elif self.couleur == 1:
            couleur = "coeur"
        elif self.couleur == 2:
            couleur = "carreau"
        else :
            couleur = "trefle"
        return nom + " de " +couleur

class Paquet:
    def __init__(self):
        self.cartes = []
        for i in range(1,14):
          for j in range(4):
            self.cartes.append(Carte(i,j))
    def echanger(tab,a,b):
        """
        echange les valeurs aux indices a et b dans le tableau tab et renvoie tab
        """
        tmp=tab[a]
        tab[a]=tab[b]
        tab[b]=tmp
        return tab
    def melanger(self, _nb_iterations):
        """
        échange nb_iterations fois 2 indices aléatoires dans cartes
        """
        for _ in range(nb_iterations):
            self.cartes = echanger(self.cartes,randint(0,len(self.cartes)-1),randint(0,len(self.cartes)-1))
    def distribuer(self):
        """
        renvoie la 1ère carte du paquet et la retire du paquet
        """
        c = self.cartes[0]
        self.cartes = [self.cartes[i]for i in range(1,len(self.cartes))]
        return c

class Main:
    def __init__(self):
        self.cartes = []
    def score(self):
        """
        renvoie le score de la main en entier
        """
        nb_As = 0
        score = 0
        for i in range(len(self.cartes)):
            if self.main[i].getValeur>=2 or self.main[i].getValeur<=10 : score = score +1
            elif self.main[i].getValeur>=11 or self.main[i].getValeur<=13 : score = score +1
            else: nb_As=nb_As+1
        for i in range (As):
            if score+11<=21: score = score + 11
            else: score = score + 1
            return score
    def getScore(self):
        return self.score
    def eliminier(self):
        if score>21: print("eliminé")
    def ajouterCarte(self, _carte):
        """
        ajoute carte dans le tableau self.cartes
        """
        self.cartes.append(carte)
    def afficher_banque(self):
        print (self.cartes[0], "?")
    def afficher_joueur(self):
        for i in range(len(self.cartes)):
            print(self.cartes[i])



class BlackJack:
    def __init__(self):
        self.banquier = main()
        self.joueurs = []
        self.Paquet = Paquet()
    def jeu(self):
        for i in range(len(self.joueurs)):
            while self.joueurs[i].getScore <=21:
             self.joueurs.afficher_joueur
             self.joueurs.score
            demande = int(input("tu veux une nouvelle carte? Y/N"))
            if reply == Y :
             self.joueurs.distribuer()
            else: print("break")
        print("self.banquier.afficher_banque")
        print("self.banquier.score")
        for i in range(len(self.joueurs)):
            if self.joueurs[i].getScore<= 21 and self.joueurs[i].getScore>self.banquier.score:
                print("le joueur a gagné")
            else: self.joueurs[i].eliminer()























