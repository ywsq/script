import random
import argparse
import tkinter
from tkinter import messagebox


class MotDePasse:
    def __init__(self, longueur_min=5, longueur_max=15, majuscule='oui', minuscule='oui', chiffre='oui', special='oui'):
        self.longueur_min = longueur_min
        self.longueur_max = longueur_max
        self.majuscule = majuscule
        self.minuscule = minuscule
        self.chiffre = chiffre
        self.special = special
        self.caracteres_chiffre = "0123456789"
        self._caracteres_speciaux = "&@!?$%"
        self.caracteres_minuscules = "abcdefghijklmnopqrstuvwxyz"
        self.caracteres_majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.caracteres_utilises = ""
        self.mot_de_passe = ""

    @property
    def caracteres_speciaux(self):
        return self._caracteres_speciaux

    @caracteres_speciaux.setter
    def caracteres_speciaux(self, caracteres_special):
        self._caracteres_speciaux = caracteres_special

    def generer_mot_de_passe(self):
        self.__init__(self.longueur_min, self.longueur_max, self.majuscule, self.minuscule, self.chiffre, self.special)
        # Ajout des caractères utilisés
        if self.majuscule == "oui":
            self.caracteres_utilises += self.caracteres_majuscules
        if self.minuscule == "oui":
            self.caracteres_utilises += self.caracteres_minuscules
        if self.chiffre == "oui":
            self.caracteres_utilises += self.caracteres_chiffre
        if self.special == "oui":
            self.caracteres_utilises += self.caracteres_speciaux
        # Génération du mot de passe
        for i in range(random.randint(self.longueur_min, self.longueur_max)):
            self.mot_de_passe += random.choice(self.caracteres_utilises)
        return self.mot_de_passe

    def __str__(self):
        affichage_mot_de_passe = self.generer_mot_de_passe()
        return f"Mot de passe généré ({len(affichage_mot_de_passe)} caractères): {affichage_mot_de_passe}"


class MotDePassePersonalise(MotDePasse):
    def __init__(self, longueur_min, longueur_max, majuscule, minuscule, chiffre, special):
        super().__init__(longueur_min, longueur_max, majuscule, minuscule, chiffre, special)

    def definir_parametre(self):
        self.longueur_min = int(input("Le nombre minimum de caractères qu'aura votre mot de passe:"))
        self.longueur_max = int(input("Le nombre maximum de caractères qu'aura votre mot de passe:"))
        self.majuscule = input("Est-ce que votre mot de passe aura une majuscule ? (oui ou non):").lower()
        self.minuscule = input("Est-ce que votre mot de passe aura une minuscule ? (oui ou non):").lower()
        self.chiffre = input("Est-ce que votre mot de passe aura un chiffre ? (oui ou non):").lower()
        self.special = input("Est-ce que votre mot de passe aura un caractère spécial ? (oui ou non):").lower()

    def generer_mot_de_passe(self):
        return super().generer_mot_de_passe()

    def __str__(self):

        print("Veuillez compléter:")
        self.definir_parametre()
        affichage_mot_de_passe = self.generer_mot_de_passe()
        return f"Mot de passe personnalisé généré \
        ({len(affichage_mot_de_passe)} caractères): {affichage_mot_de_passe}"


class MotDePasseRobuste(MotDePasse):

    def __init__(self, longueur_min, longueur_max, majuscule, minuscule, chiffre, special):
        super().__init__(longueur_min, longueur_max, majuscule, minuscule, chiffre, special)
        self.caracteres_speciaux = "&@!?$%£_#"

    def generer_mot_de_passe_robuste(self):
        mot_de_passe = super().generer_mot_de_passe()
        while not self.is_robuste(mot_de_passe):
            mot_de_passe = super().generer_mot_de_passe()
        return mot_de_passe

    def is_robuste(self, mot_de_passe):
        dico_mdp_nuls = {'password', 'usr', 'azerty', 'qwerty', 'guest', 'loulou', 'motdepasse'}
        # Variable de la somme utilisée pour savoir si les chiffres sont répétitifs
        somme_caracteres = 0
        # Conservation du dernier chiffre de la chaine
        chiffre = ""
        mdp_nul = False

        # Vérification de la vulnérabilité du mot de passe
        for mot in dico_mdp_nuls:
            if mot in mot_de_passe:
                mdp_nul = True
                break

        for caractere in mot_de_passe:
            # Seulement accepter les nombres
            if caractere.isnumeric():
                somme_caracteres += int(caractere)
                chiffre = caractere

        # Vérification de la robustesse
        is_valid = len(mot_de_passe) >= 15 and not mdp_nul and chiffre * len(mot_de_passe) != somme_caracteres

        return is_valid

    def __str__(self):
        affichage_mot_de_passe = self.generer_mot_de_passe_robuste()
        return f"Mot de passe robuste généré ({len(affichage_mot_de_passe)} caractères): {affichage_mot_de_passe}"


class InterfaceGraphique:
    def __init__(self, fenetre=tkinter.Tk()):
        self.fenetre = fenetre
        self.fenetre.title("MotDePasse Generator")
        self.fenetre.geometry("500x350")
        self.champ_longueur_min = tkinter.Entry(self.fenetre, width=4)
        self.champ_longueur_max = tkinter.Entry(self.fenetre, width=4)
        self.champ_majuscule = tkinter.Entry(self.fenetre, width=7)
        self.champ_minuscule = tkinter.Entry(self.fenetre, width=7)
        self.champ_chiffre = tkinter.Entry(self.fenetre, width=7)
        self.champ_special = tkinter.Entry(self.fenetre, width=7)

        self.init()

    def generer_mdp(self):
        mot_de_passe = MotDePasse()
        messagebox.showinfo("Mot de passe généré", f"Mot de passe généré : {mot_de_passe}")

    def generer_mdp_robuste(self):
        mot_de_passe = MotDePasseRobuste(15, 30, 'oui', 'oui', 'oui', 'oui')
        messagebox.showinfo("Mot de passe généré", f"Mot de passe généré : {mot_de_passe}")

    def generer_mdp_custom(self):
        try:
            # Récupérer les valeurs des champs
            longueur_min = int(self.champ_longueur_min.get())
            longueur_max = int(self.champ_longueur_max.get())
            majuscule = self.champ_majuscule.get()
            minuscule = self.champ_minuscule.get()
            chiffre = self.champ_chiffre.get()
            special = self.champ_special.get()

            mot_de_passe = MotDePasse(longueur_min, longueur_max, majuscule, minuscule, chiffre, special)
            messagebox.showinfo("Mot de passe généré", f"Mot de passe généré : {mot_de_passe}")
        except ValueError:
            if len(self.champ_longueur_min.get()) == 0 or len(self.champ_longueur_max.get()) == 0:
                messagebox.showinfo("info", "Les champs avec * sont obligatoires. Réessayez ...")
            else:
                messagebox.showerror("Erreur", "La valeur entrée n'est pas valide, Réessayez ...")
        except TypeError:
            messagebox.showinfo("info", "Veuillez taper 'oui' dans au moins un champ de caractère. Réessayez ...")

    def init(self):
        # Initialisation des boutons
        label_bouton = tkinter.Label(self.fenetre, text="Clique sur le type de mot de passe à générer")
        bouton_normal = tkinter.Button(self.fenetre, text="Normal", width=20, command=self.generer_mdp)
        bouton_robuste = tkinter.Button(self.fenetre, text="Robuste", width=20, command=self.generer_mdp_robuste)
        bouton_custom = tkinter.Button(self.fenetre, text="Custom", width=20, command=self.generer_mdp_custom)
        # Initialisation des labels
        label_longueur_min = tkinter.Label(self.fenetre, text="* Longueur minimale :")
        label_longueur_max = tkinter.Label(self.fenetre, text="* Longueur maximale :")
        label_majuscule = tkinter.Label(self.fenetre, text="Majuscule (oui ou non) :")
        label_minuscule = tkinter.Label(self.fenetre, text="Minuscule (oui ou non) :")
        label_chiffre = tkinter.Label(self.fenetre, text="Chiffre (oui ou non) :")
        label_special = tkinter.Label(self.fenetre, text="Caractère spécial (oui ou non) :")
        # Insertion des boutons dans l'interface
        label_bouton.pack()
        bouton_normal.pack()
        bouton_robuste.pack()
        bouton_custom.pack()
        label_longueur_min.pack()
        self.champ_longueur_min.pack()
        label_longueur_max.pack()
        self.champ_longueur_max.pack()
        label_majuscule.pack()
        self.champ_majuscule.pack()
        label_minuscule.pack()
        self.champ_minuscule.pack()
        label_chiffre.pack()
        self.champ_chiffre.pack()
        label_special.pack()
        self.champ_special.pack()


def main():
    parser = argparse.ArgumentParser(description="Générateur de mot de passe.")
    parser.add_argument("--custom", action="store_true", help="Générer un mot de passe personnalisé.")
    parser.add_argument("--robuste", action="store_true", help="Générer un mot de passe robuste.")
    args = parser.parse_args()

    if args.custom:
        mdp_personnalise = MotDePassePersonalise(8, 12, "", "", "", "")
        print(mdp_personnalise)
    elif args.robuste:
        mdp_robuste = MotDePasseRobuste(15, 30, 'oui', 'oui', 'oui', 'oui')
        print(mdp_robuste)
    else:
        mot_de_passe = MotDePasse()
        print(mot_de_passe)


if __name__ == '__main__':
    main()
    interface = InterfaceGraphique()
    interface.fenetre.mainloop()
