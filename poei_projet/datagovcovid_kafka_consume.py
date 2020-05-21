#!/usr/bin/env python
# coding: utf-8

from confluent_kafka import Consumer
from elasticsearch import Elasticsearch
import json
import requests
from time import sleep

running = True


def consumer_stop():
    running = False


# Création d'index
def es_create_index(es, index):
    request_body = {
        "settings": {
            "number_of_shards": 3,
            "number_of_replicas": 2
        }
    }
    print("creation de l'index...")
    es.indices.create(index=index, body=request_body)


# source du code : https://docs.confluent.io/current/clients/python.html
# func : fonction lambda appliquée à chaque messages
def consume_loop(consumer, topics, func):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0) # poll methode qui récupère les messages
            if msg is None: continue

            if msg.error():
                print(msg.error())
            else:
                data = msg.value().decode("utf-8")  # Convert bytes to a string
                func(data)
    finally:
       print("les données du topic : " + topics + " ont été envoyées avec succès")


def get_es_client(es_host):
    # Attendre que Elasticsearch soit bien disponible
    esUrl = 'http://' + str(es_host['host']) + ':' + str(es_host['port'])

    is_es_running = False
    while not is_es_running:
        try:
            if requests.get(esUrl, timeout=1).status_code is 200:
                is_es_running = True
                break
        except:
            pass
        print("Elasticsearch n'est pas encore disponible (" + str(esUrl) + ")...")
        sleep(5)

    print("Elasticsearch est maintenant disponible: " + str(esUrl))


    return Elasticsearch(hosts=[es_host])


def write_data_covid(es, index, message):
    data = json.loads(message)
    _id = str(data['departement']) + str(data['sexe']) + str(data['jour'])
    print(message)
    es.index(index=index, id=_id, body=message)


def write_date_echeance(es, index, message):
    print(message)
    es.index(index=index,  body=message)


def run_covid():
    # Index pour données covid
    es_index_covid = 'datagouvcovid'
    # Connection instance elasticsearch
    es_host = {'host': "elasticsearch", 'port': 9200}
    # Creation client elasticsearch
    es = get_es_client(es_host)
    # Supprimer l'index portant le même nom
    # es.indices.delete(index=es_index_covid, ignore=[400, 404])
    es_create_index(es, es_index_covid)
    # Configuration Kafka consumer
    conf = {'bootstrap.servers': "kafka:29092",
            'group.id': "covid",
            'auto.offset.reset': 'earliest'}
    # creation consumer
    consumer = Consumer(conf)
    # consomme et index les messages
    try:
        consume_loop(consumer, ["DataGouvCovid"], lambda message: write_data_covid(es, es_index_covid, message))
    finally:
        consumer.close()


def run_echeance():
    # Index pour données covid
    es_index_echeance = 'datagouvecheance'
    # Connection instance elasticsearch
    es_host = {'host': "elasticsearch", 'port': 9200}
    # Creation client elasticsearch
    es = get_es_client(es_host)
    # Supprimer l'index portant le même nom
    es.indices.delete(index=es_index_echeance, ignore=[400, 404])
    es_create_index(es, es_index_echeance)
    # Configuration Kafka consumer
    conf = {'bootstrap.servers': "kafka:29092",
            'group.id': "covid",
            'auto.offset.reset': 'earliest'}
    # creation client consumer
    consumer = Consumer(conf)
    # consomme et index les messages
    try:
        consume_loop(consumer, ["DataReportEcheanceCotisation"], lambda message: write_date_echeance(es, es_index_echeance, message))
    finally:
        consumer.close()


if __name__ == "__main":
    run_covid()
    run_echeance()
