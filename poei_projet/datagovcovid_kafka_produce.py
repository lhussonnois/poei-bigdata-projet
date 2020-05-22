#!/usr/bin/env python
# coding: utf-8

import csv
import requests
import json
from .data_dept import get_dep_label_and_region
from confluent_kafka import Producer


def produce_json(producer, topic, data):
	json_dump = json.dumps(data).encode('utf-8')
	producer.produce(topic, json_dump)
	print("Produced into topic '" + topic + "' : " + str(json_dump))


def collect_csv_to_kafka(producer, topic, url):
	with requests.get(url, stream=True) as response: # récupère le csv via la librairie requests
		lines = (line.decode('utf-8') for line in response.iter_lines()) #  récupère chaque ligne du csv que l'on décode
		rows = csv.reader(lines, delimiter=';')
		next(rows)  # permet de skip le header
		for r in rows:
			if len(r) == 7:
				data = {
					'departement': r[0],
					'sexe': r[1],
					'jour': r[2],
					'hospitalisation': int(r[3]),
					'reanimation': int(r[4]),
					'retour_au_domicile': int(r[5]),
					'deces': int(r[6])
				}
				region = get_dep_label_and_region(data['departement']) # ajoute les régions pour l'analyse des données
				data.update(region)
				produce_json(producer, topic, data)
			else:
				print("Invalid line : " + str(r))


def run():
	producer = Producer({'bootstrap.servers': 'kafka:29092'})

	CSV_URL = 'https://www.data.gouv.fr/en/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7'
	collect_csv_to_kafka(producer, "DataGouvCovid", CSV_URL)
	producer.flush()

	JSON_URL = 'https://www.data.gouv.fr/fr/datasets/r/46be802e-e802-4931-87d9-6a649452c9fd'
	r = requests.get(JSON_URL)
	for record in r.json(): # itère sur chaque objet, ici on modifie un peu le document json pour avoir tout au même niveau
		data = record['fields']
		data['datasetid'] = record['datasetid']
		data['recordid'] = record['recordid']
		produce_json(producer, "DataReportEcheanceCotisation", data)
	producer.flush()


if __name__ == "__main__":
	run()



