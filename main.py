import random


class MotDePasse:
    def __init__(self, longueur, majuscule, minuscule, chiffre, special):
        self.longueur = longueur
        self.majuscule = majuscule
        self.minuscule = minuscule
        self.chiffre = chiffre
        self.special = special

    def generer_mot_de_passe(self):
        chiffre = "0123456789"
        caracteres_speciaux = "&@!?$%"
        caracteres_minuscules = "abcdefghijklmnopqrstuvwxyz"
        caracteres_majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        caracteres_utilises = ""
        mot_de_passe = ""
        if self.majuscule == "oui":
            caracteres_utilises += caracteres_majuscules
        if self.minuscule == "oui":
            caracteres_utilises += caracteres_minuscules
        if self.chiffre == "oui":
            caracteres_utilises += chiffre
        if self.special == "oui":
            caracteres_utilises += caracteres_speciaux
        for i in range(int(self.longueur)):
            mot_de_passe += random.choice(caracteres_utilises)
        return mot_de_passe

#       def __str__(self):


if __name__ == '__main__':
    try:
        print("veuillez compléter")
        longueur_mot_de_passe = input("Le nombre de caractères qu'aura votre mot de passe:")
        majuscule_mot_de_passe = input("Est ce que votre mot de passe aura une majuscule ? (oui ou non):").lower()
        minuscule_mot_de_passe = input("Est ce que votre mot de passe aura une minuscule ? (oui ou non):").lower()
        chiffre_mot_de_passe = input("Est ce que votre mot de passe aura un chiffre ? (oui ou non):").lower()
        special_mot_de_passe = input("Est ce que votre mot de passe aura un caractère spécial ? (oui ou non):").lower()

#       ajout de bool() car sinon la valeur est un string et non booléen

        user_mot_de_passe = MotDePasse(longueur_mot_de_passe, majuscule_mot_de_passe, minuscule_mot_de_passe, chiffre_mot_de_passe, special_mot_de_passe)
        mot_de_passe = user_mot_de_passe.generer_mot_de_passe()
        print(f"longueur du mot de passe : {len(mot_de_passe)} caractères")
        print(f"Mot de passe généré : {mot_de_passe}")

    except:
        print("Réessayez, il faut au moins un paramètre au mot de passe.")