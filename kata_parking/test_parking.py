from parking import calculer_prix


def test_un_stationnement_de_30_minutes_est_gratuit():
    assert calculer_prix(30) == 0
