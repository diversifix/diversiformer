import random


def read_wiki_sents(colab_path=None, n=100):
    with open(
        f"{colab_path or '../'}data/deu_wikipedia_2021_{n}K/deu_wikipedia_2021_{n}K-sentences.txt",
        "r",
    ) as f:
        lines = f.read().split("\n")[:-1]
        sents = [l.split("\t")[1] for l in lines]
        random.seed(45394)
        random.shuffle(sents)
    return sents


def chunks(l, n):
    """
    Yield successive n-sized chunks from l.
    from https://stackoverflow.com/q/312443/10190810
    """
    for i in range(0, len(l), n):
        yield l[i : i + n]
