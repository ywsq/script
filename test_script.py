from unittest import TestCase

from main import MotDePassePersonalise
from main import MotDePasse
from main import MotDePasseRobuste
from main import is_robuste


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
        self.assertTrue(is_robuste(mdp_genere), "Test de robustesse du mot de passe généré")
        self.assertTrue(mot_de_passe_robuste.longueur_min <= len(mdp_genere) <= mot_de_passe_robuste.longueur_max,
                        "Test longueur du mot de passe généré")

    def test_caracteres_speciaux_personalises(self):
        mot_de_passe_robuste = MotDePasseRobuste(15, 30, 'oui', 'oui', 'oui', 'oui')
        mot_de_passe_robuste.caracteres_speciaux = "!@#$%"

        # Vérifie que les caractères spéciaux sont correctement pris en compte
        mdp_genere = mot_de_passe_robuste.generer_mot_de_passe_robuste()
        for caractere in mdp_genere:
            self.assertTrue(caractere in mot_de_passe_robuste.caracteres_speciaux,
                            "Test de caractères spéciaux personnalisés")

    def test_str_mot_de_passe_robuste(self):
        mot_de_passe_robuste = MotDePasseRobuste(15, 30, 'oui', 'oui', 'oui', 'oui')
        chaine_mot_de_passe = str(mot_de_passe_robuste)

        # Vérifie que la représentation sous forme de chaîne contient la longueur du mot de passe généré
        self.assertIn(str(len(mot_de_passe_robuste.generer_mot_de_passe_robuste())), chaine_mot_de_passe,
                      "Test de la représentation sous forme de chaîne du mot de passe robuste")

    def test_is_robuste(self):
        # Vérifie la fonction de vérification de robustesse pour un mot de passe donné
        mot_de_passe_robuste = "Aesfdesef5432#&f"
        self.assertTrue(is_robuste(mot_de_passe_robuste), "Test de la robustesse du mot de passe")


class TestMotDePassePersonalise(TestCase):
    def test_definir_parametre(self):
        mot_de_passe_personnalise = MotDePassePersonalise(8, 12, 'oui', 'oui', 'oui', 'oui')

        # Vérifie que les paramètres sont correctement définis
        mot_de_passe_personnalise.definir_parametre()
        self.assertGreaterEqual(mot_de_passe_personnalise.longueur_min, 8, "Test de longueur minimale")
        self.assertGreaterEqual(mot_de_passe_personnalise.longueur_max, 12, "Test de longueur maximale")
        self.assertIn(mot_de_passe_personnalise.majuscule, ['oui', 'non'], "Test de majuscule")
        self.assertIn(mot_de_passe_personnalise.minuscule, ['oui', 'non'], "Test de minuscule")
        self.assertIn(mot_de_passe_personnalise.chiffre, ['oui', 'non'], "Test de chiffre")
        self.assertIn(mot_de_passe_personnalise.special, ['oui', 'non'], "Test de caractère spécial")

    def test_generer_mot_de_passe_personnalise(self):
        mot_de_passe_personnalise = MotDePassePersonalise(8, 12, 'oui', 'oui', 'oui', 'oui')

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

    def test_str_mot_de_passe_personnalise(self):
        mot_de_passe_personnalise = MotDePassePersonalise(8, 12, 'oui', 'oui', 'oui', 'oui')
        chaine_mot_de_passe = str(mot_de_passe_personnalise)

        # Vérifie que la représentation sous forme de chaîne contient la longueur du mot de passe généré
        self.assertIn(str(len(mot_de_passe_personnalise.generer_mot_de_passe())), chaine_mot_de_passe,
                      "Test de la représentation sous forme de chaîne du mot de passe personnalisé")
