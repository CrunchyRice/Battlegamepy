
import random
from classes import*
from tkinter import*
from PIL import Image, ImageTk
from tkinter.messagebox import*




window = Tk()
window.title("Jeu de bataille")
window.configure(bg= '#696969')

window.attributes("-fullscreen", True)



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


while True:

    ordi.pack_forget()
    table.pack_forget()
    joueur.pack_forget()
    profileJoueur.pack_forget()
    profileOrdi.pack_forget()
    paquetOrdi.pack_forget()
    paquetJoueur.pack_forget()


    ordi = LabelFrame(window , text = "Ordinateur", padx= 10 , pady = 10, relief = FLAT, bg = 'red')
    ordi.pack(side = TOP)

    table = Canvas(window,bg = '#DCDCDC')
    table.pack(expand = Y, fill = BOTH, padx = 200, pady = 10)


    joueur = LabelFrame(window, text = "Vous", padx = 10, pady = 10, relief = FLAT, bg = 'blue')
    joueur.pack(side = BOTTOM)


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


    paquetOrdi = Label(ordi, text = "Cartes restantes: 8")
    paquetOrdi.pack()
    paquetJoueur = Label(joueur, text = "Cartes restantes: 8" )
    paquetJoueur.pack()



    jeu = Paquet([])
    motifs=['coeur','carreau','pique','trèfle']
    for i in range(2,15):
        for j in motifs:
            jeu.ajoute_carte(Carte(i,j))


    random.shuffle(jeu.deck)


    p_joueur = Paquet([])
    p_ordi = Paquet([])
    for i in range(8):
        p_joueur.ajoute_carte(jeu.deck[0])
        jeu.enleve_carte(jeu.deck[0])
        p_ordi.ajoute_carte(jeu.deck[0])
        jeu.enleve_carte(jeu.deck[0])




    for combat in range(1,11) :  

        if len(p_joueur.deck)==0 or len(p_ordi.deck)==0:
            break

        if not askyesno("Bataille", "Prochaine manche?") :
            break
        else :
            
            


            carteOrdi.pack_forget()
            carteJoueur.pack_forget()
            popup.pack_forget()
            paquetOrdi.pack_forget()
            paquetJoueur.pack_forget()
            manche.pack_forget()


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

            
           
            if p_joueur.deck[0] < p_ordi.deck[0] :
                popup = Label(table, text = "L'ORDINATEUR GAGNE CETTE MANCHE!",fg = "red",font = 'Didot 30' ,bg= "#DCDCDC")
                popup.pack(expand = Y)
                p_ordi.ajoute_carte(p_joueur.enleve_carte(p_joueur.deck[0]))
                p_ordi.repositionne_carte()
                
            
            
            elif p_ordi.deck[0] < p_joueur.deck[0] :
                popup = Label(table, text = "VOUS GAGNEZ CETTE MANCHE!",fg = "blue",font = 'Didot 30', bg = "#DCDCDC")
                popup.pack(expand = Y)
                p_joueur.ajoute_carte(p_ordi.enleve_carte(p_ordi.deck[0]))
                p_joueur.repositionne_carte()
                


            else:
                popup = Label(table, text = "ÉGALITÉ" , font = 'Didot 30',bg = "#DCDCDC")
                popup.pack(expand = Y)
                p_joueur.enleve_carte(p_joueur.deck[0])
                p_ordi.enleve_carte(p_ordi.deck[0])
                        

            manche = Label(table, text = "Manche: " + str(combat)+ "/10",font = 'Didot 24 ' ,bg = '#DCDCDC')
            manche.pack(side = LEFT)
       
            paquetOrdi = Label(ordi, text = "Cartes restantes: " + str(len(p_ordi.deck)))
            paquetOrdi.pack()
            paquetJoueur = Label(joueur, text = "Cartes restantes: " + str(len(p_joueur.deck)))
            paquetJoueur.pack()



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
