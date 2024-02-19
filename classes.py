"""
Classes pour le jeu de bataille
Auteurs: Dylan Seevathian, William Laguette, Nôa Beya
Date: 25 février 2021
Les classes qui vont permettrent de faire fonctinner un jeu de bataille.
"""

class Carte :
    """ Classe pour gérer des cartes, et dont l'attribut est un chiffre et un motif """
    def __init__(self,chiffre,motif):
        """ Constructeur de la classe """
        self.motif=motif
        self.chiffre=chiffre

    def __str__(self):
        """ Méthode qui permet d'afficher une carte en chaine de caractères grace à son chiffre et à son motif, par exemple: str(Carte(11,'pique')) affichera : 'valet de pique'"""
        valeur=self.chiffre
        if valeur==11:
            valeur="valet"
        if valeur==12:
            valeur="dame"
        if valeur==13:
            valeur="roi"
        if valeur==14:
            valeur="as"

        return str(valeur) + " de " + str(self.motif)


    def __lt__(self,other):
        """ Méthode qui permet de vérifier quelle carte a la plus grande valeur entre deux cartes """
        return self.chiffre<other.chiffre

    def __eq__(self,other):
        """ Méthode qui permet de vérifier l'égaliter entre deux cartes """
        return self.chiffre==other.chiffre


class Paquet :
    """ Classe pour gérer des paquets de cartes dont l'attribut est une liste de cartes """
    def __init__(self,deck):
        """ Constructeur de la classe"""
        self.deck = deck

    def __str__(self):
        """ Méthode qui permet de d'afficher la liste de cartes son forme de chaine de caractères, par exemples: str(Paquet([Carte(2,'pique'),Carte(3,'pique')])) affichera: '2 de pique ; 3 de pique ;'"""
        resultat= ""
        for i in range(len(self.deck)):
            resultat+=str(self.deck[i]) + ' ; '
        return resultat

    def ajoute_carte(self,carte):
        """ Méthode qui permet d'ajouter une carte pris en paramettre dans la liste de carte """
        return self.deck.append(carte)

    def enleve_carte(self,carte):
        """ Méthode qui permet d'enlever une carte pris en paramettre de la liste de carte """
        for i in range(len(self.deck)):
            if self.deck[i]==carte:
                return self.deck.pop(i)

    def repositionne_carte(self):
        """ Méthode qui permet de repositionner la premiere carte de la liste à la fin de la liste """
        self.ajoute_carte(self.deck[0])
        self.enleve_carte(self.deck[0])
        return self.deck
