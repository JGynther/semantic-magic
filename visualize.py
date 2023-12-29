from sklearn.manifold import TSNE
from ellipse import ellipse
import torch
import orjson
import numpy as np

with open("oracle-cards.json") as file:
    cards = orjson.loads(file.read())

cards = np.array(cards)

embeddings = torch.load("embeddings.pt")
embeddings = np.array(embeddings)

tsne = TSNE(n_components=2, random_state=1, metric="cosine")
dim_red_embeds = tsne.fit_transform(embeddings)

ellipse(cards, dim_red_embeds)
