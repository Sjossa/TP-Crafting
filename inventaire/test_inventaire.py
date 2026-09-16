from inventaire import val, alerte, mouv, cout


def test_val_comportement_actuel():

    articles = [
        {"q": 10, "pu": 5.50},
        {"q": 2, "pu": 12.00},
        {"q": 0, "pu": 20.00},
        {"q": -3, "pu": 15.00},
    ]

    assert val(articles) == 79.0


def test_alerte_comportement_actuel():
    articles = [
        {"ref": "A1", "q": 2, "seuil": 5},
        {
            "ref": "A2",
            "q": 5,
            "seuil": 5,
        },
        {"ref": "A3", "q": 10, "seuil": 5},
    ]

    assert alerte(articles) == ["A1"]


def test_mouv_stock_insuffisant_comportement_actuel():
    article = {"ref": "ART-01", "q": 5}

    resultat = mouv(article, q=10, t="out")

    assert resultat is False

    assert article["q"] == -5


def test_cout_stock():
    article = {"ref": "ART-01", "q": 2, "seuil": 2, "pu": 10}

    assert cout(article) == 50
