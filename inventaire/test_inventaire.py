from inventaire import val


def test_val_comportement_actuel():

    articles = [
        {"q": 10, "pu": 5.50},
        {"q": 2, "pu": 12.00},
        {"q": 0, "pu": 20.00},
        {"q": -3, "pu": 15.00},
    ]

    assert val(articles) == 79.0
