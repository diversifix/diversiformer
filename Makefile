all:

wiki_folder = data/deu_wikipedia_2021_100K
wiki = $(wiki_folder)/deu_wikipedia_2021_100K-sentences.txt
lt = lib/LanguageTool-5.7/languagetool-server.jar

$(wiki):
	python src/download_wiki.py

wiki: $(wiki)

$(lt):
	wget -P lib https://languagetool.org/download/LanguageTool-stable.zip
	unzip -d lib lib/LanguageTool-stable.zip

lib/de:
	wget -P lib https://languagetool.org/download/ngram-data/ngrams-de-20150819.zip
	unzip -d lib lib/ngrams-de-20150819.zip

lt_server: $(lt) lib/de
	java -cp $(lt) org.languagetool.server.HTTPServer --port 8081 --languageModel=lib

data/training_data_general.json: wiki
	jupyter execute src/synthesize_training_data_general.ipynb

data/training_data_gender.json: wiki $(lt)
	jupyter execute src/synthesize_training_data_gender.ipynb

data/training_data_gender_highlighted.json: data/training_data_gender.json
	python src/annotate/highlight.py

clean:
	rm -rf $(wiki_folder)
	rm -rf lib/*
	rm -rf data/training_data_gender_highlighted.json
	rm -rf **/__pycache__
	rm -rf **/.cache
	rm -rf **/.ipynb_checkpoints
