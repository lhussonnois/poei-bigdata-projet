# Projet BigData POEI

## Pré-requis

* Docker, Docker-compose
* Python 3

## Données

* https://www.data.gouv.fr/en/datasets/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/
* https://www.data.gouv.fr/fr/datasets/mesures-exceptionnelles-covid-19-reports-de-cotisations-urssaf-employeurs-par-departement-x-grand-secteur/

## Utiliser le projet

### Cloner

```bash
git clone https://github.com/lhussonnois/poei-bigdata-projet.git
```

### Builder image docker

```bash
docker-compose build
```

### Démarrer

```bash
docker-compose up -d
```

### Elasticsearch / Kibana

* Elasticsearch : [http://localhost:9200](http://localhost:9200)
* Kibana : [http://localhost:5601](http://localhost:5601)