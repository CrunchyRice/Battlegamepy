"""
Bataille
Auteurs: Dylan Seevathian, William Laguette, Nôa Beya
Date: 25 février 2021
Jeu de bataille entre un joueur et un ordinateur,
on leur distribue à chacun 8 cartes via un paquet de 52 cartes mélangé,
ensuite sur 10 manches ils jouent chacun la première carte de leurs mains,
la carte avec la plus grande valeur gagne et le joueur qui la joué met a la fin de sa main les 2 cartes qui sont sur la table, si les deux cartes ont la même valeurs, peronne ne les prend,
celui qui a le plus de cartes à la fin des 10 manches l'emporte.
"""


#On importe la bibliothèque random
import random
#On importe le fichier "classes"
from classes import*
#On importe la bibliothèque tkinter
from tkinter import*
#De la bibliothèque PIL, on prend les modules Image et ImageTk
from PIL import Image, ImageTk
#On importe la bibliothèque tkinter.messagebox
from tkinter.messagebox import*



#On crée la fenêtre du jeu et on lui donne ça couleur d'arrière plan
window = Tk()
window.title("Jeu de bataille")
window.configure(bg= '#696969')
#On met la fenêtre en pleine écran
window.attributes("-fullscreen", True)



#On crée les widgets qui vont servir d'affichage des informations de la partie
carteOrdi = Label()
carteJoueur = Label()
popup = Label()
manche = Label()
ordi= LabelFrame()
table= Canvas()
joueur= LabelFrame()
profileJoueur= Label()
profileOrdi= Label()
paquetOrdi= Label()
paquetJoueur= Label()

#Boucle qui va nous permettre de rejouer jusqu'a que le joueuer décide d'arrêter
while True:

    #On enlève toute les informations de la partie d'avan
    ordi.pack_forget()
    table.pack_forget()
    joueur.pack_forget()
    profileJoueur.pack_forget()
    profileOrdi.pack_forget()
    paquetOrdi.pack_forget()
    paquetJoueur.pack_forget()

    #On crée le cadre qui va représenter l'ordinateur
    ordi = LabelFrame(window , text = "Ordinateur", padx= 10 , pady = 10, relief = FLAT, bg = 'red')
    ordi.pack(side = TOP)

    #On crée le canvas sur lequel s'afficheront les cartes
    table = Canvas(window,bg = '#DCDCDC')
    table.pack(expand = Y, fill = BOTH, padx = 200, pady = 10)


    #On crée le cadre qui va représenter le joueur
    joueur = LabelFrame(window, text = "Vous", padx = 10, pady = 10, relief = FLAT, bg = 'blue')
    joueur.pack(side = BOTTOM)

    #Création de images permettants de représenter le joueur et l'ordinateur et leurs donnant la bonne taille
    img = Image.open("image/ordi.png")
    img = img.resize((70,70), Image.ANTIALIAS)
    ordiPic = ImageTk.PhotoImage(img)
    profileOrdi = Label(ordi, image = ordiPic)
    profileOrdi.pack(side = LEFT)
    img2 = Image.open("image/joueur.png")
    img2 = img2.resize((70,70), Image.ANTIALIAS)
    joueurPic = ImageTk.PhotoImage(img2)
    profileJoueur = Label(joueur, image = joueurPic)
    profileJoueur.pack(side = LEFT)

    #On affiche le nombre de carte que l'ordinateur et le joueur ont au départ
    paquetOrdi = Label(ordi, text = "Cartes restantes: 8")
    paquetOrdi.pack()
    paquetJoueur = Label(joueur, text = "Cartes restantes: 8" )
    paquetJoueur.pack()



    #Création du jeu de 52 cartes :
    jeu = Paquet([])
    motifs=['coeur','carreau','pique','trèfle']
    for i in range(2,15):
        for j in motifs:
            jeu.ajoute_carte(Carte(i,j))

    #On mélange le jeu de carte, pour cela on utilise la méthode suffle de la bibliothèque Random
    random.shuffle(jeu.deck)

    #On distribue 8 cartes du jeu de carte qui vient d'être créé à chaque joueur
    p_joueur = Paquet([])
    p_ordi = Paquet([])
    for i in range(8):
        p_joueur.ajoute_carte(jeu.deck[0])
        jeu.enleve_carte(jeu.deck[0])
        p_ordi.ajoute_carte(jeu.deck[0])
        jeu.enleve_carte(jeu.deck[0])



    #Début des 10 combat de la bataille
    for combat in range(1,11) :  
        #Si la main du joueur ou de l'ordinateur est vide, la partie s'arrête
        if len(p_joueur.deck)==0 or len(p_ordi.deck)==0:
            break
        #On donne la possibilité d'arrêter le jeu avant chaque combat
        if not askyesno("Bataille", "Prochaine manche?") :
            break
        else :
            
            

            #On enlève toute les informations de la manche précédante
            carteOrdi.pack_forget()
            carteJoueur.pack_forget()
            popup.pack_forget()
            paquetOrdi.pack_forget()
            paquetJoueur.pack_forget()
            manche.pack_forget()


            #On assigne les cartes joué à l'image qui les correspondent et on ajuste leurs tailles
            img3 = Image.open("image/carte/"+str(p_ordi.deck[0])+".png")
            img3 = img3.resize((125,175), Image.ANTIALIAS)
            ordiCarteImage = ImageTk.PhotoImage(img3)
            carteOrdi = Label(table, image = ordiCarteImage)
            img4 = Image.open("image/carte/"+str(p_joueur.deck[0])+".png")
            img4 = img4.resize((125,175), Image.ANTIALIAS)
            joueurCarteImage = ImageTk.PhotoImage(img4)
            carteJoueur = Label(table, image = joueurCarteImage)
            carteOrdi.pack()
            carteJoueur.pack(side = BOTTOM)

            
            #Si la première carte de l'ordinateur est plus grande que celle du joueur, la carte du joueur est enlever de sa main pour aller dans celle du joueur et on repositionne la première carte à la fin de la main à l'aide de la méthode de la classe Paquet
            if p_joueur.deck[0] < p_ordi.deck[0] :
                popup = Label(table, text = "L'ORDINATEUR GAGNE CETTE MANCHE!",fg = "red",font = 'Didot 30' ,bg= "#DCDCDC")
                popup.pack(expand = Y)
                p_ordi.ajoute_carte(p_joueur.enleve_carte(p_joueur.deck[0]))
                p_ordi.repositionne_carte()
                
            
            #Si la premiere carte du joueur est plus grande que celle de l'ordi, la carte de l'ordi est enlever de sa main pour aller dans celle du joueur et on repositionne la première carte à la fin de la main à l'aide de la méthode de la classe Paquet
            elif p_ordi.deck[0] < p_joueur.deck[0] :
                popup = Label(table, text = "VOUS GAGNEZ CETTE MANCHE!",fg = "blue",font = 'Didot 30', bg = "#DCDCDC")
                popup.pack(expand = Y)
                p_joueur.ajoute_carte(p_ordi.enleve_carte(p_ordi.deck[0]))
                p_joueur.repositionne_carte()
                

            #Si les deux cartes sont égales, elles sont enlevées de la main de l'ordi et du joueur à l'aide de la méthode de la classe Paquet
            else:
                popup = Label(table, text = "ÉGALITÉ" , font = 'Didot 30',bg = "#DCDCDC")
                popup.pack(expand = Y)
                p_joueur.enleve_carte(p_joueur.deck[0])
                p_ordi.enleve_carte(p_ordi.deck[0])
                        
            #Affichage du numero de la manche
            manche = Label(table, text = "Manche: " + str(combat)+ "/10",font = 'Didot 24 ' ,bg = '#DCDCDC')
            manche.pack(side = LEFT)

            #affichage du nombre de cartes restantes dans chaque paquet au terme d'un combat            
            paquetOrdi = Label(ordi, text = "Cartes restantes: " + str(len(p_ordi.deck)))
            paquetOrdi.pack()
            paquetJoueur = Label(joueur, text = "Cartes restantes: " + str(len(p_joueur.deck)))
            paquetJoueur.pack()


    #Désignation du vainqueur et on donne la possibilité au joueur de rejouer
    if len(p_joueur.deck) > len(p_ordi.deck) :
        showinfo("Victoire","Bravo, tu as gagné!")
        if askyesno("Bataille", "Rejouer?"):
            pass
        else:
            quit()
    elif len(p_joueur.deck) < len(p_ordi.deck) :
        showinfo("Défaite","Dêsolé, tu as perdu!")
        if askyesno("Bataille", "Rejouer?"):
            pass
        else:
            quit()
    else :
        showinfo("Match Nul","Égalité!")
        if askyesno("Bataille", "Rejouer?"):
            pass
        else:
            quit()



window.mainloop()