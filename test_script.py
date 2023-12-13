from unittest import TestCase
from main import MotDePasse
from main import MotDePasseRobuste
from main import is_robuste


class TestMotDePasse(TestCase):
    # méthode appelée avant chaque test
    def setUp(self):
        self.mot_de_passe = MotDePasse()

    def test_generer_mot_de_passe_length(self):    # teste si la méthode generer_mot_de_passe fonctionne correctement
        mot_de_passe_genere = self.mot_de_passe.generer_mot_de_passe()
        self.assertGreaterEqual(len(mot_de_passe_genere), self.mot_de_passe.longueur_min)
        self.assertLessEqual(len(mot_de_passe_genere), self.mot_de_passe.longueur_max)


class TestMotDePasseRobuste(TestCase):
    # méthode appelée avant chaque test
    def setUp(self):
        self.mot_de_passe_robuste = MotDePasseRobuste(15, 30, 'oui', 'oui', 'oui', 'oui')

    # teste si la méthode is_robuste fonctionne
    def test_is_robuste(self):
        mdp_fictif = "Aesfdesef5432#&f"
        self.assertTrue(is_robuste(mdp_fictif))

    # teste si la méthode str de MotDePasseRobuste fonctionne
    def test_generer_mot_de_passe_robuste_length(self):
        mot_de_passe_genere = self.mot_de_passe_robuste.generer_mot_de_passe_robuste()
        self.assertGreaterEqual(len(mot_de_passe_genere), self.mot_de_passe_robuste.longueur_min)
        self.assertLessEqual(len(mot_de_passe_genere), self.mot_de_passe_robuste.longueur_max)
