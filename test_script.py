from unittest import TestCase

from main import MotDePassePersonalise
from main import MotDePasse
from main import MotDePasseRobuste
from main import is_robuste
from main import verification_caracteres
from main import pas_valide


class TestFunctions(TestCase):
    def test_verification_caracteres(self):
        # Test lorsque le mot de passe est vide
        self.assertFalse(verification_caracteres("", "oui", "oui", "oui", "oui", "&@!?$%"),
                         "Le mot de passe vide ne doit pas être accepté")
        self.assertFalse(verification_caracteres("", "non", "non", "non", "non", "&@!?$%"),
                         "Le mot de passe vide ne doit pas être accepté")

        # Test lorsque la longueur du mot de passe est inférieure à 4
        self.assertFalse(verification_caracteres("abc", "oui", "oui", "oui", "oui", "&@!?$%"),
                         "Si la longueur est inférieure à 4, pas de vérification et return False")
        self.assertFalse(verification_caracteres("4ab", "oui", "oui", "oui", "oui", "&@!?$%"),
                         "Si la longueur est inférieure à 4, pas de vérification et return False")

        # Test lorsque la longueur du mot de passe est égale à 4
        self.assertTrue(verification_caracteres("abcd", "oui", "oui", "oui", "oui", "&@!?$%"),
                        "Le mot de passe qui ne contient pas les caracteres specifiés retourne True")
        self.assertTrue(verification_caracteres("ABCD", "oui", "oui", "oui", "oui", "&@!?$%"),
                        "Le mot de passe qui ne contient pas les caracteres specifiés retourne True")
        self.assertTrue(verification_caracteres("1234", "oui", "oui", "oui", "oui", "&@!?$%"),
                        "Le mot de passe qui ne contient pas les caracteres specifiés retourne True")
        self.assertTrue(verification_caracteres("%$@&", "oui", "oui", "oui", "oui", "&@!?$%"),
                        "Le mot de passe qui ne contient pas les caracteres specifiés retourne True")
        self.assertFalse(verification_caracteres("ABCD", "oui", "non", "non", "non", "&@!?$%"),
                         "Le mot de passe qui contient les caracteres specifiés retourne False")
        self.assertFalse(verification_caracteres("abcd", "non", "oui", "non", "non", "&@!?$%"),
                         "Le mot de passe qui contient les caracteres specifiés retourne False")
        self.assertFalse(verification_caracteres("1234", "non", "non", "oui", "non", "&@!?$%"),
                         "Le mot de passe qui contient les caracteres specifiés retourne False")
        self.assertFalse(verification_caracteres("%$@&", "non", "non", "non", "oui", "&@!?$%"),
                         "Le mot de passe qui contient les caracteres specifiés retourne False")
        self.assertFalse(verification_caracteres("a85%", "non", "oui", "oui", "oui", "&@!?$%"),
                         "Le mot de passe qui contient les caracteres specifiés retourne False")
        self.assertFalse(verification_caracteres("A85%", "oui", "non", "oui", "oui", "&@!?$%"),
                         "Le mot de passe qui contient les caracteres specifiés retourne False")
        self.assertFalse(verification_caracteres("aB@%", "oui", "oui", "non", "oui", "&@!?$%"),
                         "Le mot de passe qui contient les caracteres specifiés retourne False")
        self.assertFalse(verification_caracteres("aB85", "oui", "oui", "oui", "non", "&@!?$%"),
                         "Le mot de passe qui contient les caracteres specifiés retourne False")

        # Test lorsque le mot de passe contient des caractères majuscules
        self.assertFalse(verification_caracteres("ABCD", "oui", "non", "non", "non", "&@!?$%"),
                         "Le mot de passe contient des majuscules et retourne False")
        self.assertFalse(verification_caracteres("AbCd", "oui", "oui", "non", "non", "&@!?$%"),
                         "Le mot de passe contient au moins une majuscule et retourne False")
        self.assertTrue(verification_caracteres("abcd", "oui", "non", "non", "non", "&@!?$%"),
                        "Le mot de passe ne contient aucune majuscule et retourne True")
        self.assertTrue(verification_caracteres("ab7%", "oui", "oui", "oui", "oui", "&@!?$%"),
                        "Le mot de passe ne contient aucune majuscule et retourne True")

        # Test lorsque le mot de passe contient des caractères minuscules
        self.assertFalse(verification_caracteres("aBCD", "oui", "oui", "non", "non", "&@!?$%"),
                         "Le mot de passe contient au moins une minuscule et retourne False")
        self.assertFalse(verification_caracteres("abcd", "non", "oui", "non", "non", "&@!?$%"),
                         "Le mot de passe contient des minuscules et retourne False")
        self.assertTrue(verification_caracteres("ABCD", "non", "oui", "non", "non", "&@!?$%"),
                        "Le mot de passe ne contient aucune minuscule et retourne True")
        self.assertTrue(verification_caracteres("AB7%", "oui", "oui", "oui", "oui", "&@!?$%"),
                        "Le mot de passe ne contient aucune minuscule et retourne True")

        # Test lorsque le mot de passe contient des chiffres
        self.assertFalse(verification_caracteres("1234", "non", "non", "oui", "non", "&@!?$%"),
                         "Le mot de passe est composé de chiffre et retourne False")
        self.assertFalse(verification_caracteres("Ab4%", "oui", "oui", "oui", "oui", "&@!?$%"),
                         "Le mot de passe contient au moins un chiffre et retourne False")
        self.assertTrue(verification_caracteres("AbC%", "oui", "oui", "oui", "oui", "&@!?$%"),
                        "Le mot de passe contient aucun chiffre et retourne True")

        # Test lorsque le mot de passe contient des caractères spéciaux
        self.assertFalse(verification_caracteres("!@#$", "non", "non", "non", "oui", "&@!?$%"),
                         "Le mot de passe contient des caractères spéciaux")
        self.assertFalse(verification_caracteres("2ab&C", "oui", "oui", "oui", "oui", "&@!?$%"),
                         "Le mot de passe contient au moins un caractère spécial")
        self.assertTrue(verification_caracteres("Ab85", "oui", "oui", "oui", "oui", "&@!?$%"),
                        "Le mot de passe contient aucun caractère spécial et retourne True")

        # Test lorsque tous les types de caractères sont requis
        self.assertFalse(verification_caracteres("Ab1!", "oui", "oui", "oui", "oui", "&@!?$%"))
        self.assertTrue(verification_caracteres("abcd", "oui", "oui", "oui", "oui", "&@!?$%"))

        # Test lorsque tous les types de caractères ne sont pas requis
        self.assertFalse(verification_caracteres("abcd", "non", "non", "non", "non", "&@!?$%"))
        self.assertTrue(verification_caracteres("abcd", "non", "non", "non", "oui", "&@!?$%"))

    def test_is_robuste(self):
        # Test lorsque le mot de passe est vide
        self.assertFalse(is_robuste("", "&@!?$%"), "Le mot de passe avec aucun caractère n'est pas robuste")

        # Test si la longueur est inférieure à 15
        self.assertFalse(is_robuste("Ab1!", "&@!?$%"), "Le mot de passe de moins de 15 caractères n'est pas robuste")
        self.assertFalse(is_robuste("r@op!eZp5zYH4", "&@!?$%"), "Le mot de passe de 14 caractères n'est pas robuste")

        # Test

        # Test si le mot de passe contient un nombre répétitif
        self.assertFalse(is_robuste("444444444444444444", "&@!?$%"), "Le mot de passe qui ne contient que des chiffres,\
                                                                     n'est pas robuste")
        self.assertFalse(is_robuste("r4444@op!eZp444444", "&@!?$%"), "Le mot de passe qui contient un seul chiffre\
                                                                     répétitif, n'est pas robuste")
        self.assertTrue(is_robuste("r4454@op!eZp544445", "&@!?$%"), "Le mot de passe qui contient des chiffres\
                                                                    différents, est robuste")

        # Test lorsque le mot de passe est présent dans la liste des mots de passe nuls
        self.assertFalse(is_robuste("aC4K$password%?Y", "&@!?$%"), "Invalide le mot de passe qui contient 'password'")
        self.assertFalse(is_robuste("aC4K$azerty%y087", "&@!?$%"), "Invalide le mot de passe qui contient 'azerty'")
        self.assertFalse(is_robuste("aC4K$qwerty%y087", "&@!?$%"), "Invalide le mot de passe qui contient 'qwerty'")
        self.assertFalse(is_robuste("aC4K$guest%y087O", "&@!?$%"), "Invalide le mot de passe qui contient 'guest'")
        self.assertFalse(is_robuste("aC4K$motdepasse%", "&@!?$%"), "Invalide le mot de passe qui contient 'motdepasse'")
        self.assertFalse(is_robuste("aC4K$loulou%y087", "&@!?$%"), "Invalide le mot de passe qui contient 'loulou'")
        self.assertFalse(is_robuste("aC4K$usr%y087AbM", "&@!?$%"), "Invalide le mot de passe qui contient 'usr'")

        # Test lorsque le mot de passe est robuste
        self.assertTrue(is_robuste("Abc123!xyz$1RMhz", "&@!?$%"))


class TestMotDePasse(TestCase):
    def test___init__(self):
        # Test avec des paramètres par défaut
        mot_de_passe = MotDePasse()
        self.assertEqual(mot_de_passe.longueur_min, 5, "test longueur_min par défaut")
        self.assertEqual(mot_de_passe.longueur_max, 15, "test longueur_max par défaut")
        self.assertEqual(mot_de_passe.majuscule, 'oui', "test majuscule par défaut")

    def test_generer_mot_de_passe(self):
        mot_de_passe = MotDePasse()
        mdp_genere = mot_de_passe.generer_mot_de_passe()
        self.assertTrue(len(mdp_genere) >= mot_de_passe.longueur_min, "Test longueur minimale")
        self.assertTrue(len(mdp_genere) <= mot_de_passe.longueur_max, "Test longueur maximale")

    def test_caracteres_speciaux(self):
        mot_de_passe = MotDePasse()
        mot_de_passe.caracteres_speciaux = "!@#$%"
        self.assertEqual(mot_de_passe.caracteres_speciaux, "!@#$%", "Test setter et getter caracteres_speciaux")


class TestMotDePasseRobuste(TestCase):
    def test_generer_mot_de_passe_robuste(self):
        mot_de_passe_robuste = MotDePasseRobuste(15, 30, 'oui', 'oui', 'oui', 'oui')
        mdp_genere = mot_de_passe_robuste.generer_mot_de_passe_robuste()

        # Vérifie que le mot de passe généré est robuste
        self.assertTrue(is_robuste(mdp_genere, mot_de_passe_robuste.caracteres_speciaux),
                        "Test de robustesse du mot de passe généré")
        self.assertTrue(mot_de_passe_robuste.longueur_min <= len(mdp_genere) <= mot_de_passe_robuste.longueur_max,
                        "Test longueur du mot de passe généré")

    def test_caracteres_speciaux_personalises(self):
        mot_de_passe_robuste = MotDePasseRobuste(5, 30, 'oui', 'oui', 'oui', 'oui')
        mot_de_passe_robuste.caracteres_speciaux = "!@#$%"

        # Vérifie que les caractères spéciaux sont correctement pris en compte
        mdp_genere = mot_de_passe_robuste.generer_mot_de_passe_robuste()
        self.assertTrue(any(caractere in mot_de_passe_robuste.caracteres_speciaux for caractere in mdp_genere),
                        "True si les caractères spécifiés sont utilisés dans le mot de passe")
        mot_de_passe_robuste.caracteres_speciaux = "@"
        # Vérifie que les caractères spéciaux sont correctement pris en compte
        mdp_genere = mot_de_passe_robuste.generer_mot_de_passe_robuste()
        self.assertTrue(any(caractere in mot_de_passe_robuste.caracteres_speciaux for caractere in mdp_genere),
                        "True si les caractères spécifiés sont utilisés dans le mot de passe")


class TestMotDePassePersonalise(TestCase):
    def test_definir_parametre(self):
        mot_de_passe_personnalise = MotDePassePersonalise(5, 30, 'oui', 'oui', 'oui', 'oui')
        print("test conformité de la valeur des paramètres")
        mot_de_passe_personnalise.definir_parametre()
        self.assertFalse(pas_valide(mot_de_passe_personnalise.longueur_min, mot_de_passe_personnalise.longueur_max),
                        "Test si la longueur est positive et si la longueur maximale est plus grande que la\
                        longueur minimale")
        self.assertIn(mot_de_passe_personnalise.majuscule, ['oui', 'non'], "Test de majuscule")
        self.assertIn(mot_de_passe_personnalise.minuscule, ['oui', 'non'], "Test de minuscule")
        self.assertIn(mot_de_passe_personnalise.chiffre, ['oui', 'non'], "Test de chiffre")
        self.assertIn(mot_de_passe_personnalise.special, ['oui', 'non'], "Test de caractère spécial")

    def test_generer_mot_de_passe_personnalise(self):
        mot_de_passe_personnalise = MotDePassePersonalise(5, 30, 'oui', 'oui', 'oui', 'oui')
        print("test conformité du mot de passe généré sur base des paramètres")
        # Vérifie que le mot de passe généré respecte les paramètres définis
        mot_de_passe_genere = mot_de_passe_personnalise.generer_mot_de_passe()
        self.assertGreaterEqual(len(mot_de_passe_genere), mot_de_passe_personnalise.longueur_min,
                                "Test de longueur minimale du mot de passe généré")
        self.assertLessEqual(len(mot_de_passe_genere), mot_de_passe_personnalise.longueur_max,
                             "Test de longueur maximale du mot de passe généré")
        if mot_de_passe_personnalise.majuscule == 'oui':
            self.assertTrue(any(c.isupper() for c in mot_de_passe_genere),
                            "Test de majuscule dans le mot de passe généré")
        if mot_de_passe_personnalise.minuscule == 'oui':
            self.assertTrue(any(c.islower() for c in mot_de_passe_genere),
                            "Test de minuscule dans le mot de passe généré")
        if mot_de_passe_personnalise.chiffre == 'oui':
            self.assertTrue(any(c.isdigit() for c in mot_de_passe_genere),
                            "Test de chiffre dans le mot de passe généré")
        if mot_de_passe_personnalise.special == 'oui':
            caractere_special = set("!@#$%^&*()_-+=<>?")
            self.assertTrue(any(c in caractere_special for c in mot_de_passe_genere),
                            "Test de caractère spécial dans le mot de passe généré")
