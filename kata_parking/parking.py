import math


def calculer_prix(minutes):
    if minutes <= 30:
        return 0

    temps_depasse = minutes - 30

    temp_suplementaire = temps_depasse / 30
    calcul_tranche_de_30_minutes_depasserr = math.ceil(temp_suplementaire)

    calcul_ajout_de_facturation = calcul_tranche_de_30_minutes_depasserr * 1.50

    calcul_nombre_de_jour = math.ceil(minutes / 1440)

    plafond_nombre_de_jour = calcul_nombre_de_jour * 18

    return min(calcul_ajout_de_facturation, plafond_nombre_de_jour)
