from datetime import datetime

from parking import calculer_prix


import pytest


def test_un_stationnement_de_30_minutes_est_gratuit():
    assert calculer_prix(30) == 0


def test_facturation_au_dela_de_30_minutes():

    assert calculer_prix(31) == 1.50


def test_facturation_pour_chaque_24h():
    assert calculer_prix(480) == 18
    assert calculer_prix(1440) == 18


def test_facturation_camion_perte_60_pourcent():
    assert calculer_prix(31, True) == 0.90


def test_facturation_camion_electrique_abonne():
    assert calculer_prix(60, True, True) == 0


def test_exemple_erreur():

    with pytest.raises(ValueError, match="Erreur durée negative"):
        calculer_prix(-5)


def test_consequence_72H_vehicule():
    assert calculer_prix(4320) == 250


def test_facturation_avec_dates_actuelles():
    heure_entree = datetime(2035, 1, 1, 10, 0)
    heure_actuelle = datetime(2035, 1, 1, 11, 30)

    assert calculer_prix(heure_entree, heure_actuelle=heure_actuelle) == 3.0
