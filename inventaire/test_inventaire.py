from inventaire import (
    val,
    alerte,
    mouv,
    cout,
    classer,
    rot,
    par_cat,
    rapport,
    maj_prix,
    export_json,
)


def test_val_comportement_actuel():

    articles = [
        {"q": 10, "pu": 5.50},
        {"q": 2, "pu": 12.00},
        {"q": 0, "pu": 20.00},
        {"q": -3, "pu": 15.00},
    ]

    assert val(articles) == 34


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
    article = {"ref": "ART-01", "q": 1, "seuil": 2, "pu": 10}

    assert cout(article) == 50


def test_classer_stock():

    article = [
        {"ref": "A1", "q": 2, "pu": 5},
        {
            "ref": "A2",
            "q": 5,
            "pu": 5,
        },
        {"ref": "A3", "q": 10, "pu": 5},
    ]

    resultat = classer(article)

    assert resultat[0]["ref"] == "A3"


def test_rot():
    article = {
        "ref": "ART-01",
        "q": 2,
    }

    assert rot(article, 30) == 2


def test_par_cat():
    articles = [
        {"ref": "ART-01", "cat": "outil", "q": 2, "pu": 3},
        {"ref": "ART-02", "cat": "piece", "q": 4, "pu": 5},
        {"ref": "ART-03", "cat": "consommable", "q": 10, "pu": 2},
    ]

    resultat = par_cat(articles)

    assert resultat["outil"] == 6
    assert resultat["piece"] == 20

    assert resultat["consommable"] == 20


def test_rapport():
    articles = [
        {"ref": "A1", "cat": "outil", "q": 2, "seuil": 5, "pu": 10},
        {"ref": "A2", "cat": "piece", "q": 10, "seuil": 3, "pu": 5},
    ]
    res = rapport(articles, verbose=False)
    assert res["valeur"] == 70.0
    assert res["nb"] == 2
    assert "A1" in res["alertes"]


def test_maj_prix():
    assert maj_prix("A1", 15) is None


def test_export_json(tmp_path):

    d = tmp_path / "inv.json"
    res = {"valeur": 70.0, "nb": 2}

    hist = export_json(res, chemin=str(d))
    assert len(hist) == 1
    assert hist[0]["valeur"] == 70.0
