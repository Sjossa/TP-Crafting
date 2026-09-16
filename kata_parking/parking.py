import math


def calculer_prix(minutes, abonnee=False, estElectrique=False):

    if minutes < 0:
        raise ValueError("Erreur durée negative")

    temps_gratuit = 30

    if estElectrique:
        temps_gratuit = 60
    if minutes <= temps_gratuit:
        return 0

    temps_depasse = minutes - temps_gratuit

    temps_suplementaire = temps_depasse / 30
    calcul_tranche_30_minutes_depasser = math.ceil(temps_suplementaire)

    calcul_ajout_facturation = calcul_tranche_30_minutes_depasser * 1.50

    calcul_nombre_de_jour = math.ceil(minutes / 1440)

    plafond_nombre_de_jour = calcul_nombre_de_jour * 18

    prix_final = min(calcul_ajout_facturation, plafond_nombre_de_jour)

    if abonnee:
        prix_final = prix_final * 0.60

    return round(prix_final, 2)
