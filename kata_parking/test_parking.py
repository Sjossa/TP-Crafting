import pytest

from parking import calculer_prix


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

    with pytest.raises(ValueError, match="Le message d'erreur que tu attends"):
        calculer_prix(-5)
