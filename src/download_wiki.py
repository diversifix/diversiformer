import tarfile
import urllib.request

import snakemake

url = "http://pcai056.informatik.uni-leipzig.de/downloads/corpora/deu_wikipedia_2021_100K.tar.gz"
with urllib.request.urlopen(url) as f:
    stream = urllib.request.urlopen(url)
    f = tarfile.open(fileobj=stream, mode="r|gz")
    f.extractall(path="data")
