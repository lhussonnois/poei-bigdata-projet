#!/usr/bin/env python
# coding: utf-8

data = {"01": {"dep_label": "Ain", "region": "Auvergne-Rhône-Alpes"},
        "02": {"dep_label": "Aisne", "region": "Hauts-de-France"},
        "03": {"dep_label": "Allier", "region": "Auvergne-Rhône-Alpes"},
        "04": {"dep_label": "Alpes-de-Haute-Provence", "region": "Provence-Alpes-Côte d'Azur"},
        "05": {"dep_label": "Hautes-Alpes", "region": "Provence-Alpes-Côte d'Azur"},
        "06": {"dep_label": "Alpes-Maritimes", "region": "Provence-Alpes-Côte d'Azur"},
        "07": {"dep_label": "Ardèche", "region": "Auvergne-Rhône-Alpes"},
        "08": {"dep_label": "Ardennes", "region": "Grand Est"},
        "09": {"dep_label": "Ariège", "region": "Occitanie"},
        "10": {"dep_label": "Aube", "region": "Grand Est"},
        "11": {"dep_label": "Aude", "region": "Occitanie"},
        "12": {"dep_label": "Aveyron", "region": "Occitanie"},
        "13": {"dep_label": "Bouches-du-Rhône", "region": "Provence-Alpes-Côte d'Azur"},
        "14": {"dep_label": "Calvados", "region": "Normandie"},
        "15": {"dep_label": "Cantal", "region": "Auvergne-Rhône-Alpes"},
        "16": {"dep_label": "Charente", "region": "Nouvelle-Aquitaine"},
        "17": {"dep_label": "Charente-Maritime", "region": "Nouvelle-Aquitaine"},
        "18": {"dep_label": "Cher", "region": "Centre-Val de Loire"},
        "19": {"dep_label": "Corrèze", "region": "Nouvelle-Aquitaine"},
        "21": {"dep_label": "Côte-d'Or", "region": "Bourgogne-Franche-Comté"},
        "22": {"dep_label": "Côtes-d'Armor", "region": "Bretagne"},
        "23": {"dep_label": "Creuse", "region": "Nouvelle-Aquitaine"},
        "24": {"dep_label": "Dordogne", "region": "Nouvelle-Aquitaine"},
        "25": {"dep_label": "Doubs", "region": "Bourgogne-Franche-Comté"},
        "26": {"dep_label": "Drôme", "region": "Auvergne-Rhône-Alpes"},
        "27": {"dep_label": "Eure", "region": "Normandie"},
        "28": {"dep_label": "Eure-et-Loir", "region": "Centre-Val de Loire"},
        "29": {"dep_label": "Finistère", "region": "Bretagne"},
        "2A": {"dep_label": "Corse-du-Sud", "region": "Corse"},
        "2B": {"dep_label": "Haute-Corse", "region": "Corse"},
        "30": {"dep_label": "Gard", "region": "Occitanie"},
        "31": {"dep_label": "Haute-Garonne", "region": "Occitanie"},
        "32": {"dep_label": "Gers", "region": "Occitanie"},
        "33": {"dep_label": "Gironde", "region": "Nouvelle-Aquitaine"},
        "34": {"dep_label": "Hérault", "region": "Occitanie"},
        "35": {"dep_label": "Ille-et-Vilaine", "region": "Bretagne"},
        "36": {"dep_label": "Indre", "region": "Centre-Val de Loire"},
        "37": {"dep_label": "Indre-et-Loire", "region": "Centre-Val de Loire"},
        "38": {"dep_label": "Isère", "region": "Auvergne-Rhône-Alpes"},
        "39": {"dep_label": "Jura", "region": "Bourgogne-Franche-Comté"},
        "40": {"dep_label": "Landes", "region": "Nouvelle-Aquitaine"},
        "41": {"dep_label": "Loir-et-Cher", "region": "Centre-Val de Loire"},
        "42": {"dep_label": "Loire", "region": "Auvergne-Rhône-Alpes"},
        "43": {"dep_label": "Haute-Loire", "region": "Auvergne-Rhône-Alpes"},
        "44": {"dep_label": "Loire-Atlantique", "region": "Pays de la Loire"},
        "45": {"dep_label": "Loiret", "region": "Centre-Val de Loire"},
        "46": {"dep_label": "Lot", "region": "Occitanie"},
        "47": {"dep_label": "Lot-et-Garonne", "region": "Nouvelle-Aquitaine"},
        "48": {"dep_label": "Lozère", "region": "Occitanie"},
        "49": {"dep_label": "Maine-et-Loire", "region": "Pays de la Loire"},
        "50": {"dep_label": "Manche", "region": "Normandie"},
        "51": {"dep_label": "Marne", "region": "Grand Est"},
        "52": {"dep_label": "Haute-Marne", "region": "Grand Est"},
        "53": {"dep_label": "Mayenne", "region": "Pays de la Loire"},
        "54": {"dep_label": "Meurthe-et-Moselle", "region": "Grand Est"},
        "55": {"dep_label": "Meuse", "region": "Grand Est"},
        "56": {"dep_label": "Morbihan", "region": "Bretagne"},
        "57": {"dep_label": "Moselle", "region": "Grand Est"},
        "58": {"dep_label": "Nièvre", "region": "Bourgogne-Franche-Comté"},
        "59": {"dep_label": "Nord", "region": "Hauts-de-France"},
        "60": {"dep_label": "Oise", "region": "Hauts-de-France"},
        "61": {"dep_label": "Orne", "region": "Normandie"},
        "62": {"dep_label": "Pas-de-Calais", "region": "Hauts-de-France"},
        "63": {"dep_label": "Puy-de-Dôme", "region": "Auvergne-Rhône-Alpes"},
        "64": {"dep_label": "Pyrénées-Atlantiques", "region": "Nouvelle-Aquitaine"},
        "65": {"dep_label": "Hautes-Pyrénées", "region": "Occitanie"},
        "66": {"dep_label": "Pyrénées-Orientales", "region": "Occitanie"},
        "67": {"dep_label": "Bas-Rhin", "region": "Grand Est"},
        "68": {"dep_label": "Haut-Rhin", "region": "Grand Est"},
        "69": {"dep_label": "Rhône", "region": "Auvergne-Rhône-Alpes"},
        "70": {"dep_label": "Haute-Saône", "region": "Bourgogne-Franche-Comté"},
        "71": {"dep_label": "Saône-et-Loire", "region": "Bourgogne-Franche-Comté"},
        "72": {"dep_label": "Sarthe", "region": "Pays de la Loire"},
        "73": {"dep_label": "Savoie", "region": "Auvergne-Rhône-Alpes"},
        "74": {"dep_label": "Haute-Savoie", "region": "Auvergne-Rhône-Alpes"},
        "75": {"dep_label": "Paris", "region": "Île-de-France"},
        "76": {"dep_label": "Seine-Maritime", "region": "Normandie"},
        "77": {"dep_label": "Seine-et-Marne", "region": "Île-de-France"},
        "78": {"dep_label": "Yvelines", "region": "Île-de-France"},
        "79": {"dep_label": "Deux-Sèvres", "region": "Nouvelle-Aquitaine"},
        "80": {"dep_label": "Somme", "region": "Hauts-de-France"},
        "81": {"dep_label": "Tarn", "region": "Occitanie"},
        "82": {"dep_label": "Tarn-et-Garonne", "region": "Occitanie"},
        "83": {"dep_label": "Var", "region": "Provence-Alpes-Côte d'Azur"},
        "84": {"dep_label": "Vaucluse", "region": "Provence-Alpes-Côte d'Azur"},
        "85": {"dep_label": "Vendée", "region": "Pays de la Loire"},
        "86": {"dep_label": "Vienne", "region": "Nouvelle-Aquitaine"},
        "87": {"dep_label": "Haute-Vienne", "region": "Nouvelle-Aquitaine"},
        "88": {"dep_label": "Vosges", "region": "Grand Est"},
        "89": {"dep_label": "Yonne", "region": "Bourgogne-Franche-Comté"},
        "90": {"dep_label": "Territoire de Belfort", "region": "Bourgogne-Franche-Comté"},
        "91": {"dep_label": "Essonne", "region": "Île-de-France"},
        "92": {"dep_label": "Hauts-de-Seine", "region": "Île-de-France"},
        "93": {"dep_label": "Seine-Saint-Denis", "region": "Île-de-France"},
        "94": {"dep_label": "Val-de-Marne", "region": "Île-de-France"},
        "95": {"dep_label": "Val-d'Oise", "region": "Île-de-France"},
        "971": {"dep_label": "Guadeloupe", "region": "Guadeloupe"},
        "972": {"dep_label": "Martinique", "region": "Martinique"},
        "973": {"dep_label": "Guyane", "region": "Guyane"},
        "974": {"dep_label": "La Réunion", "region": "La Réunion"},
        "976": {"dep_label": "Mayotte", "region": "Mayotte"},
        "975": {"dep_label": "Saint-Pierre-et-Miquelon", "region": "Collectivités d'Outre-Mer"},
        "977": {"dep_label": "Saint-Barthélemy", "region": "Collectivités d'Outre-Mer"},
        "978": {"dep_label": "Saint-Martin", "region": "Collectivités d'Outre-Mer"},
        "984": {"dep_label": "Terres australes et antarctiques françaises", "region": "Collectivités d'Outre-Mer"},
        "986": {"dep_label": "Wallis et Futuna", "region": "Collectivités d'Outre-Mer"},
        "987": {"dep_label": "Polynésie française", "region": "Collectivités d'Outre-Mer"},
        "988": {"dep_label": "Nouvelle-Calédonie", "region": "Collectivités d'Outre-Mer"}}


def get_dep_label_and_region(code_dep):
    if code_dep in data:
        return data[code_dep]
    else:
        return {"dep_label": "NA", "region": "NA"}
