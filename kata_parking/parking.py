from datetime import datetime
import math


def _obtenir_minutes(minutes_ou_entree, heure_actuelle):
    """Convertit une date d'entrée en minutes ou retourne les minutes directes."""
    if isinstance(minutes_ou_entree, datetime):
        if heure_actuelle is None:
            heure_actuelle = datetime.now()
        difference = heure_actuelle - minutes_ou_entree
        return int(difference.total_seconds() / 60)
    return minutes_ou_entree


def _calculer_tarif_standard(minutes, estElectrique):
    """Calcule le tarif de base selon le temps gratuit et les plafonds journaliers."""
    temps_gratuit = 60 if estElectrique else 30
    if minutes <= temps_gratuit:
        return 0

    temps_depasse = minutes - temps_gratuit
    tranches = math.ceil(temps_depasse / 30)
    calcul_ajout = tranches * 1.50

    plafond_jour = math.ceil(minutes / 1440) * 18
    return min(calcul_ajout, plafond_jour)


def calculer_prix(
    minutes_ou_entree, abonnee=False, estElectrique=False, heure_actuelle=None
):
    """Fonction principale orchestrant le calcul du prix du parking."""
    minutes = _obtenir_minutes(minutes_ou_entree, heure_actuelle)

    if minutes < 0:
        raise ValueError("Erreur durée negative")

    if minutes >= 4320:
        return 250.0

    prix_final = _calculer_tarif_standard(minutes, estElectrique)

    if abonnee:
        prix_final = prix_final * 0.60

    return round(prix_final, 2)
