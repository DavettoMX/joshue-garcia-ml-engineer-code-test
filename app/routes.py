from flask import jsonify, request

from . import api

import spacy
nlp = spacy.load('es_core_news_sm')


@api.route('/api/v1/ner', methods=['POST'])
def extract_entities():
    """
    Extract named entities from a list of sentences using SpaCy.

    This function expects a JSON payload with a key 'oraciones' containing
    a list of sentences in Spanish. It processes each sentence using the SpaCy
    'es_core_news_sm' model to extract named entities and their labels.

    :return: A JSON object with a key 'resultado' containing a list of
    """
    try:
        data = request.get_json()  # Get the JSON payload from the request

        oraciones = data.get('oraciones', [])  # Get the list of sentences from the payload
        resultados = []

        for oracion in oraciones:
            doc = nlp(oracion) # Process the sentence using Spacy NLP pipeline
            entidades = {entidad.text: entidad.label_ for entidad in doc.ents}  # Extract entities from the sentence

            resultados.append({"oración": oracion, "entidades": entidades})

        return jsonify({"resultado": resultados})

    except Exception as e:
        return jsonify({"error": str(e)})


