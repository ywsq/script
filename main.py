import random
import argparse
import tkinter
from tkinter import messagebox


def verification_caracteres(mot_de_passe, majuscule, minuscule, chiffre, special, caracteres_speciaux):
    if len(mot_de_passe) < 4:
        return False
    else:
        if majuscule == "oui":
            if not any(c.isupper() for c in mot_de_passe):
                return True
        if minuscule == 'oui':
            if not any(c.islower() for c in mot_de_passe):
                return True
        if chiffre == 'oui':
            if not any(c.isnumeric() for c in mot_de_passe):
                return True
        if special == 'oui':
            if not any(c in caracteres_speciaux for c in mot_de_passe):
                return True
        return False


class MotDePasse:

    def __init__(self, longueur_min=5, longueur_max=15, majuscule='oui', minuscule='oui', chiffre='oui', special='oui'):
        """
        PRE : 'longueur_min' et 'longueur_max' doivent être des entiers positifs. 'majuscule', 'minuscule', 'chiffre',
        'special' doivent être des chaines de caractères égales à "oui" ou "non".
        POST : L'objet et les attributs sont initialisés avec les paramètres fournis.
        """
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
        """
        Getter pour les caractères spéciaux.
        PRE : /
        POST : Retourne les caractères spéciaux autorisés dans le mot de passe.
        """
        return self._caracteres_speciaux

    @caracteres_speciaux.setter
    def caracteres_speciaux(self, caracteres_special):
        """
        Setter pour les caractères spéciaux.
        PRE : La valeur passée en paramètre doit être une chaîne de caractères.
        POST : La propriété _caracteres_speciaux de l'objet est mise à jour avec la valeur passée en paramètre.
        """
        self._caracteres_speciaux = caracteres_special

    def generer_mot_de_passe(self):
        """
        PRE : 'longueur_min', 'longueur_max', 'majuscule', 'minuscule', 'chiffre', 'special' doivent être correctement
        initialisés.
        POST : Le résultat retrouné ('mot_de_passe') est une chaine de caractères dont la longueur est comprise entre
        'longueur_min' et 'longueur_max'. Le mot de passe contient les caractères ayant été spécifiés ('majuscule',
        'minuscule', 'chiffre', 'special')
        """
        self.__init__(self.longueur_min, self.longueur_max, self.majuscule, self.minuscule, self.chiffre, self.special)
        # Ajout des caractères utilisés
        if self.majuscule == "oui" or "oui" in self.majuscule:
            self.caracteres_utilises += self.caracteres_majuscules
        if self.minuscule == "oui" or "oui" in self.minuscule:
            self.caracteres_utilises += self.caracteres_minuscules
        if self.chiffre == "oui" or "oui" in self.chiffre:
            self.caracteres_utilises += self.caracteres_chiffre
        if self.special == "oui" or "oui" in self.special:
            self.caracteres_utilises += self.caracteres_speciaux
        # Génération du mot de passe
        for i in range(random.randint(self.longueur_min, self.longueur_max)):
            self.mot_de_passe += random.choice(self.caracteres_utilises)
        return self.mot_de_passe

    def __str__(self):
        """
        Représentation sous forme de chaîne de caractères.
        PRE : /
        POST: Retourne une chaîne de caractères représentant le mot de passe généré.
        """
        affichage_mot_de_passe = self.generer_mot_de_passe()
        return f"Mot de passe généré ({len(affichage_mot_de_passe)} caractères): {affichage_mot_de_passe}"


def pas_valide(longueur_min, longueur_max):
    while longueur_min < 0 or longueur_max < longueur_min:
        print("La longueur entrée n'est pas valide, Réessayez ...")
        return True


class MotDePassePersonalise(MotDePasse):

    def __init__(self, longueur_min, longueur_max, majuscule, minuscule, chiffre, special):
        """
        PRE : 'longueur_min', 'longueur_max', 'majuscule', 'minuscule', 'chiffre', 'special' doivent être conformes
        aux spécifications de la classe parente.
        POST : Une instance de MotDePassePersonnalise est créée avec les paramètres spécifiés, les propriétés de la
        classe MotDePasse sont initialisées.
        """
        super().__init__(longueur_min, longueur_max, majuscule, minuscule, chiffre, special)

    def definir_parametre(self):
        """
        Permet à l'utilisateur de définir les paramètres pour la génération du mot de passe.
        PRE : Les valeurs saisies par l'utilisateur doivent être conformes aux spécifications.
        POST : Les propriétés 'longueur_min', 'longueur_max', 'majuscule', 'minuscule', 'chiffre', 'special' sont mises
        à jour avec les valeurs saisies par l'utilisateur.
        """
        self.longueur_min = int(input("Le nombre minimum de caractères qu'aura votre mot de passe:"))
        self.longueur_max = int(input("Le nombre maximum de caractères qu'aura votre mot de passe:"))
        self.majuscule = input("Est-ce que votre mot de passe aura une majuscule ? (oui ou non):").lower()
        self.minuscule = input("Est-ce que votre mot de passe aura une minuscule ? (oui ou non):").lower()
        self.chiffre = input("Est-ce que votre mot de passe aura un chiffre ? (oui ou non):").lower()
        self.special = input("Est-ce que votre mot de passe aura un caractère spécial ? (oui ou non):").lower()

    def generer_mot_de_passe(self):
        """
        PRE : Les paramètres doivent être correctement définis à l'aide de la méthode 'definir_parametre'.
        POST : Le résultat retourné est une chaîne de caractères représentant un mot de passe personnalisé.
        """
        print("Veuillez compléter:")
        self.definir_parametre()
        while pas_valide(self.longueur_min, self.longueur_max):
            self.definir_parametre()
        mot_de_passe = super().generer_mot_de_passe()
        while verification_caracteres(mot_de_passe, self.majuscule, self.minuscule, self.chiffre,
                                      self.special, self.caracteres_speciaux):
            mot_de_passe = super().generer_mot_de_passe()
        return mot_de_passe

    def __str__(self):
        """
        Représentation sous forme de chaîne de caractères.
        PRE : /
        POST : Retourne une chaîne de caractères représentant le mot de passe généré.
        """
        affichage_mot_de_passe = self.generer_mot_de_passe()
        return f"Mot de passe personnalisé généré ({len(affichage_mot_de_passe)} caractères): {affichage_mot_de_passe}"


def is_robuste(mot_de_passe, caracteres_speciaux):
    """
    Vérification de la robustesse du mot de passe généré.
    PRE : 'mot_de_passe' doit être une chaine de caractères.
    POST : Le résultat retourné est un booléen indiquant si le mot de passe est robuste.
    """
    dico_mdp_nuls = {'password', 'usr', 'azerty', 'qwerty', 'guest', 'loulou', 'motdepasse'}
    # Variable qui va stocker la somme
    somme_chiffres = 0
    # Variable qui conservera le dernier chiffre de la chaine
    liste_chiffre = ""
    # Variable qui sera True si elle contient un élément de dico_mdp_nuls
    mdp_nul = False
    # Vérification de la vulnérabilité du mot de passe
    for mot in dico_mdp_nuls:
        if mot in mot_de_passe:
            mdp_nul = True
            break
    for caractere in mot_de_passe:
        # Faire la somme des chiffres et récupérer le dernier chiffre de la chaine
        if caractere.isnumeric():
            somme_chiffres += int(caractere)
            liste_chiffre += caractere
    caracteres_absents = verification_caracteres(mot_de_passe, "oui", "oui", "oui", "oui", caracteres_speciaux)
    # Vérification de la robustesse
    is_valid = not caracteres_absents and len(mot_de_passe) >= 15 and not mdp_nul and int(liste_chiffre[0]) * \
        len(liste_chiffre) != somme_chiffres
    return is_valid


class MotDePasseRobuste(MotDePasse):

    def __init__(self, longueur_min, longueur_max, majuscule, minuscule, chiffre, special):
        """
        PRE : longueur_min, longueur_max, majuscule, minuscule, chiffre, special doivent être conformes aux
        spécifications de la classe parente.
        POST : Une instance de MotDePasseRobuste est créée avec les paramètres spécifiés, les propriétés de la classe
        MotDePasse sont initialisées avec les valeurs fournies.
        La propriété caracteres_speciaux est définie avec la valeur "&@!?$%£_#".
        """
        super().__init__(longueur_min, longueur_max, majuscule, minuscule, chiffre, special)
        self.caracteres_speciaux = "&@!?$%£_#"

    def generer_mot_de_passe_robuste(self):
        """
        PRE : Les paramètres doivent être correctement définis à l'initialisation de la classe.
        POST : Le résultat retourné est une chaine de caractères représentant un mot de passe robuste.
        """
        mot_de_passe = super().generer_mot_de_passe()
        while not is_robuste(mot_de_passe, self.caracteres_speciaux):
            mot_de_passe = super().generer_mot_de_passe()
        return mot_de_passe

    def __str__(self):
        """
        Représentation sous forme de chaîne de caractères.
        PRE : /
        POST : Retourne une chaîne de caractères représentant le mot de passe robuste généré.
        """
        affichage_mot_de_passe = self.generer_mot_de_passe_robuste()
        return f"Mot de passe robuste généré ({len(affichage_mot_de_passe)} caractères): {affichage_mot_de_passe}"


class InterfaceGraphique:
    def __init__(self, fenetre=tkinter.Tk()):
        """
        Initialisation de l'interface graphique
        PRE : /
        POST : Initialise l'interface graphique avec une fenêtre tkinter et les champs nécessaires.
        """
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
        """
        PRE : /
        POST : Génère un mot de passe en utilisant la classe MotDePasse et affiche une fenêtre avec le mot de passe
        généré.
        """
        mot_de_passe = MotDePasse()
        messagebox.showinfo("Mot de passe généré", f"Mot de passe généré : {mot_de_passe}")

    def generer_mdp_robuste(self):
        """
        PRE : /
        POST : Génère un mot de passe en utilisant la classe MotDePasseRobuste et affiche une fenêtre avec le mot de
        passe généré.
        """
        mot_de_passe = MotDePasseRobuste(15, 30, 'oui', 'oui', 'oui', 'oui')
        messagebox.showinfo("Mot de passe généré", f"Mot de passe généré : {mot_de_passe}")

    def generer_mdp_custom(self):
        """
        PRE : Les champs de longueur doivent être remplis, les longueurs saisies doivent être positives, la longueur
        maximale doit être supérieure ou égale à la longueur minimale et au moins un type de caractères est choisi.
        POST : Une fenêtre affiche le mot de passe généré, une information ou un message d'erreur en cas de saisie
        invalide.
        RAISE : - ValueError → les champs de longueurs ne peuvent pas être vides ou négatives. La longueur maximale doit
                être supérieure à la longueur minimale.
                - IndexError → Le mot de passe doit comporter au moins un type de caractères. Si aucun caractère n'est
                choisi, la boucle ne peut pas itérer une chaine vide pour générer le mot de passe
        """
        try:
            # Préconditions
            if self.champ_longueur_min.get() == "" or self.champ_longueur_max.get() == "":
                raise ValueError("Les champs * sont obligatoires")
            if not self.champ_longueur_min.get().isnumeric() or not self.champ_longueur_max.get().isnumeric():
                raise ValueError("La longueur doit être un nombre exemple: 12")
            if int(self.champ_longueur_max.get()) < 0 or int(self.champ_longueur_min.get()) < 0:
                raise ValueError("La valeur négative est invalide")
            if int(self.champ_longueur_max.get()) < int(self.champ_longueur_min.get()):
                raise ValueError("La longueur max. est plus petite que la longueur min.")
            # Récupérer les valeurs des champs
            longueur_min = int(self.champ_longueur_min.get())
            longueur_max = int(self.champ_longueur_max.get())
            majuscule = self.champ_majuscule.get().lower()
            minuscule = self.champ_minuscule.get().lower()
            chiffre = self.champ_chiffre.get().lower()
            special = self.champ_special.get().lower()
            # Génération du mot de passe sur base des valeurs des champs
            mot_de_passe_instance = MotDePasse(longueur_min, longueur_max, majuscule, minuscule, chiffre, special)
            mot_de_passe = mot_de_passe_instance.generer_mot_de_passe()

            while verification_caracteres(mot_de_passe, majuscule, minuscule, chiffre, special,
                                          mot_de_passe_instance.caracteres_speciaux):
                mot_de_passe = mot_de_passe_instance.generer_mot_de_passe()
            messagebox.showinfo("Mot de passe généré", f"Mot de passe généré : {mot_de_passe}")
        # Exceptions
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))
        except IndexError:
            messagebox.showinfo("info", "Veuillez entrer 'oui' dans au moins un champ de caractère, Réessayez ...")

    def init(self):
        """
        Initialise l'interface graphique avec des boutons et des champs de saisie.
        - Boutons : "Normal", "Robuste", "Custom" pour générer différents types de mots de passe.
        - Champs de saisie : Longueur minimale, longueur maximale, Majuscule, Minuscule, Chiffre, Caractère spécial.
        Les boutons sont associés aux méthodes correspondantes pour générer les mots de passe.
        Les champs de saisie permettent à l'utilisateur de personnaliser les paramètres des mots de passe.
        """
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


def cli():
    """
    Utilisation en ligne de commande.
    PRE : /
    POST : D'après les arguments passés en ligne de commande, génère un mot de passe en utilisant la classe appropriée,
    puis l'affiche.
    """
    parser = argparse.ArgumentParser(description="Générateur de mot de passe.")
    parser.add_argument("--custom", action="store_true", help="Générer un mot de passe personnalisé.")
    parser.add_argument("--robuste", action="store_true", help="Générer un mot de passe robuste.")
    args = parser.parse_args()
    # Génération selon l'argument
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
    cli()
    interface = InterfaceGraphique()
    interface.fenetre.mainloop()
