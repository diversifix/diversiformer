all: data/training_data_general.json

wiki = "data/deu_wikipedia_2021_10K/deu_wikipedia_2021_10K-sentences.txt"

wiki:
	python src/download_wiki.py

data/training_data_general.json: wiki
	jupyter execute src/synthesize_training_data_general.ipynb
