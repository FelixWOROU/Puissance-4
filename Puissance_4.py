import tkinter.messagebox
from tkinter import *
import tkinter.colorchooser
"""import ttkbootstrap as tb
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog"""

lignes = 6
colonnes = 7
cercle_diam = 80
largeur_fenetre = colonnes * 80
hauteur_fenetre = lignes * 80
decalage_pions = 10
vitesse = 200


class Puissance4Game(Tk):
    First_clic = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.descente_en_cours = False
        self.resizable(False, False)
        self.Tour = StringVar()
        self.observation = StringVar()
        self.couleur_joueur1 = StringVar()
        self.couleur_joueur1.set("red")
        self.couleur_joueur2 = StringVar()
        self.couleur_joueur2.set("blue")
        self.observation.set("welcome 🎮")
        self.after(2000, self.reset_obs)
        self.Tour.set("Tour du joueur 1")
        Label(self, text="Joueur 1", font=('Arial Black', 8), bg='#ABABAB').place(x=2, y=10)
        Label(self, text="Joueur 2", font=('Arial Black', 8), bg='#ABABAB').place(x=70, y=10)
        self.actu_color = self.couleur_joueur1.get()
        self.j1_frame = Frame(self, width=30, height=30, bg=self.couleur_joueur1.get())
        self.j1_frame.place(x=15, y=35)
        self.j2_frame = Frame(self, width=30, height=30, bg=self.couleur_joueur2.get())
        self.j2_frame.place(x=85, y=35)
        self.joueur_actuel = Frame(self, width=30, height=30, bg=self.actu_color)
        self.joueur_actuel.place(x=largeur_fenetre + 210, y=40)
        Label(self, text="Félix's Game🎮", font=('Blackadder ITC', 15), bg='#ABABAB').place(x=15, y=100)
        Label(self, textvariable=self.Tour, font=('Arial Black', 10)).place(x=largeur_fenetre + 168, y=10)
        Label(self, text="Observations", bg='black', font=('Algerian', 13), borderwidth=5, relief=RAISED,
              fg='white').place(
            x=largeur_fenetre + 162, y=100)
        self.obs_label = Label(self, textvariable=self.observation, width=15, font=('Arial Black', 10), height=3,
                               justify=CENTER)
        self.obs_label.place(x=largeur_fenetre + 159, y=135)
        self.title("Puissance 4")
        self.config(bg='#ABABAB')
        self.geometry(str(largeur_fenetre + 300) + "x" + str(hauteur_fenetre + 2 * decalage_pions) + "+300+50")
        self.cnv = Canvas(self, width=largeur_fenetre + decalage_pions, height=hauteur_fenetre + decalage_pions,
                          bg='lavender')
        self.cnv.pack()
        self.pions_id = []
        for i in range(lignes):
            for j in range(colonnes):
                pion = self.cnv.create_oval(j * cercle_diam + decalage_pions, i * cercle_diam + decalage_pions,
                                            j * cercle_diam + decalage_pions + cercle_diam,
                                            i * cercle_diam + decalage_pions + cercle_diam, outline='black')
                self.pions_id.append(pion)
        for i in range(lignes):
            for j in range(colonnes):
                self.cnv.create_rectangle(j * cercle_diam + decalage_pions, i * cercle_diam + decalage_pions,
                                          j * cercle_diam + decalage_pions + cercle_diam,
                                          i * cercle_diam + decalage_pions + cercle_diam, outline='black')
        self.after(1, self.choix_couleur)  # choix_couleur
        self.cnv.bind('<Button-1>', self.clic)

    def joueur_color(self, fen, joueur):
        # my_color.show()
        # colors = my_color.result()
        if joueur == 1:
            my_color = tkinter.colorchooser.askcolor(title="Sélectionnez une couleur")
            if my_color[1]:
                Frame(fen, width=30, height=30, bg=str(my_color[1])).place(x=30, y=80)
                self.couleur_joueur1.set(str(my_color[1]))  # colors.hex
        elif joueur == 2:
            my_color = tkinter.colorchooser.askcolor(title="Sélectionnez une couleur")
            if my_color[1]:
                Frame(fen, width=30, height=30, bg=str(my_color[1])).place(x=210, y=80)
                self.couleur_joueur2.set(str(my_color[1]))  # colors.hex
        elif joueur == 0:
            fen.destroy()

    def choix_couleur(self):
        askcolors = Toplevel(self)
        askcolors.config(bg='ivory')
        askcolors.geometry("300x300+300+50")
        askcolors.focus_set()
        askcolors.grab_set()
        askcolors.title("Choix de couleurs")
        Label(askcolors, text="Choix des couleurs", justify=CENTER, font=('Arial Black', 15), bg='ivory').place(x=20,
                                                                                                                y=10)
        Button(askcolors, text="Joueur 1", command=lambda joueur=1: self.joueur_color(askcolors, joueur)).place(x=20,
                                                                                                                y=50)
        Button(askcolors, text="Joueur 2", command=lambda joueur=2: self.joueur_color(askcolors, joueur)).place(x=200,
                                                                                                                y=50)
        Button(askcolors, text="Valider", bg='green',
               command=lambda joueur=0: self.joueur_color(askcolors, joueur)).place(
            x=120, y=50)
        askcolors.mainloop()

    def clic(self, event):
        if Puissance4Game.First_clic == 0:
            self.actu_color = self.couleur_joueur1.get()
            self.joueur_actuel.config(bg=self.actu_color)
            self.j1_frame.config(bg=self.couleur_joueur1.get())
            self.j2_frame.config(bg=self.couleur_joueur2.get())
            Puissance4Game.First_clic += 1
        if not self.descente_en_cours:
            x, y = event.x, event.y
            select = self.cnv.find_closest(x, y)
            org = select[0] % colonnes
            if org == 0:
                if select[0] > colonnes - 1:
                    org = colonnes
                else:
                    org = select[0]
            if self.cnv.itemcget(org, 'fill') == '':
                self.cnv.itemconfig(org, fill=self.actu_color)
                self.after(vitesse // 2, self.descente, org, self.actu_color)
                if self.Tour.get()[-1] == '1':
                    self.Tour.set("Tour du joueur 2")
                    self.actu_color = self.couleur_joueur2.get()
                    self.joueur_actuel.config(bg=self.actu_color)
                else:
                    self.Tour.set("Tour du joueur 1")
                    self.actu_color = self.couleur_joueur1.get()
                    self.joueur_actuel.config(bg=self.actu_color)
            else:
                self.observation.set("Colonne pleine !!")
                self.after(1000, self.reset_obs)

    def descente(self, origine, color):
        if origine + colonnes in self.pions_id:
            if self.cnv.itemcget(origine + colonnes, 'fill') == '':
                self.cnv.itemconfig(origine + colonnes, fill=color)
                self.cnv.itemconfig(origine, fill='')
                self.descente_en_cours = True
                self.after(vitesse, self.descente, origine + colonnes, color)
            else:
                self.verify_winner(color)
        else:
            self.verify_winner(color)

    def verify_winner(self, color):
        def vertical_verify(cercle):
            # color = self.cnv.itemcget(cercle, 'fill')
            if cercle > (lignes * colonnes) // 2:
                win = True
                for i in range(4):
                    if self.cnv.itemcget(cercle - colonnes * i, 'fill') != color:
                        win = False
                return win
            else:
                win = True
                for i in range(4):
                    if self.cnv.itemcget(cercle + colonnes * i, 'fill') != color:
                        win = False
                return win

        def horizontal_verify(cercle):
            # color = self.cnv.itemcget(cercle, 'fill')
            win = True
            cercle_column = cercle % colonnes
            if cercle_column == 0:
                if cercle > colonnes - 1:
                    cercle_column = colonnes
                else:
                    cercle_column = cercle
            if cercle_column > lignes // 2:
                for i in range(4):
                    if self.cnv.itemcget(cercle - i, 'fill') != color:
                        win = False
                return win
            else:
                for i in range(4):
                    if self.cnv.itemcget(cercle + i, 'fill') != color:
                        win = False
                return win

        def diagonal_verify(cercle):
            win = True
            milieu = []
            cercle_column = cercle % colonnes
            if cercle_column == 0:
                if cercle > colonnes - 1:
                    cercle_column = colonnes
                else:
                    cercle_column = cercle
            if cercle % colonnes == 0:
                cercle_ligne = cercle // colonnes
            else:
                cercle_ligne = cercle // colonnes + 1
            if cercle_ligne > lignes // 2:  # verification de la diagonal montante
                if cercle_ligne >= cercle_column:  # diagonal de droite
                    for i in range(4):
                        if self.cnv.itemcget(cercle - i * colonnes + i, 'fill') != color:
                            win = False
                    if cercle_ligne != cercle_column:
                        """if win:
                            print("cercle: lg=", cercle_ligne, " co=", cercle_column)"""
                        return win
                    else:
                        milieu.append(win)
                        win = True
                if cercle_ligne <= cercle_column:  # diagonal de gauche
                    for i in range(4):
                        if self.cnv.itemcget(cercle - i * colonnes - i, 'fill') != color:
                            win = False
                    if cercle_ligne != cercle_column:
                        """if win:
                            print("cercle: lg=", cercle_ligne, " co=", cercle_column)"""
                        return win
                    else:
                        milieu.append(win)
                if cercle_ligne == cercle_column:
                    if True in milieu:
                        return True
                    else:
                        return False
            else:  # verification de la diagonal descendante
                if cercle_ligne >= cercle_column - 1:  # diagonal de droite
                    for i in range(4):
                        if self.cnv.itemcget(cercle + i * colonnes + i, 'fill') != color:
                            win = False
                    if cercle_ligne != cercle_column:
                        """if win:
                            print("cercle: lg=", cercle_ligne, " co=", cercle_column)"""
                        return win
                    else:
                        milieu.append(win)
                        win = True
                if cercle_ligne <= cercle_column - 1:  # diagonal de gauche
                    for i in range(4):
                        if self.cnv.itemcget(cercle + i * colonnes - i, 'fill') != color:
                            win = False
                    if cercle_ligne != cercle_column:
                        if win:
                            print("cercle: lg=", cercle_ligne, " co=", cercle_column)
                        return win
                    else:
                        milieu.append(win)
                if cercle_ligne == cercle_column:
                    if True in milieu:
                        return True
                    else:
                        return False

        end = False
        for pion in self.pions_id:
            if self.cnv.itemcget(pion, 'fill') == color:
                verify_liste = [vertical_verify(pion), horizontal_verify(pion), diagonal_verify(pion)]
                if True in verify_liste:
                    if color == self.couleur_joueur1.get():
                        self.obs_label.config(bg=self.couleur_joueur1.get())
                        self.observation.set("Gagnant !! :\nJOUEUR 1")
                    else:
                        self.obs_label.config(bg=self.couleur_joueur2.get())
                        self.observation.set("Gagnant !! :\nJOUEUR 2")
                    end = True
                    break
        if end:
            self.descente_en_cours = True
            self.after(2000, self.if_play_aigain)
        else:
            self.if_egalite()
            self.descente_en_cours = False

    def reset_obs(self):
        self.observation.set("")

    def if_play_aigain(self):

        if tkinter.messagebox.askyesno("Rejouer", "Voulez-vous recommencer ?"):
            self.play_aigain()
        else:
            self.destroy()

    def play_aigain(self):
        self.descente_en_cours = False
        Puissance4Game.First_clic = 0
        for pion in self.pions_id:
            self.cnv.itemconfig(pion, fill='')
            self.Tour.set("Tour du joueur 1")
            self.obs_label.config(bg='white')
            self.observation.set("welcome 🎮")
            self.after(1000, self.reset_obs)
            self.actu_color = self.couleur_joueur1.get()

    def if_egalite(self):
        egalite = True
        for pion in self.pions_id:
            if self.cnv.itemcget(pion, 'fill') == '':
                egalite = False
                break
        if egalite:
            self.obs_label.config(bg='#C6CEC0')
            self.observation.set("EGALITE")
            self.after(1000, self.if_play_aigain)


if __name__ == "__main__":
    root = Puissance4Game()
    root.mainloop()
