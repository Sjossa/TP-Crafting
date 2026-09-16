from inventaire import val, alerte


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
