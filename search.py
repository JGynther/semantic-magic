from utils import find_card
import faiss
import numpy as np
import torch
import orjson

K = 5

with open("oracle-cards.json") as file:
    cards = orjson.loads(file.read())

embeddings = torch.load("embeddings.pt")
embeddings = np.array(embeddings)

dimensions = embeddings[0].shape[0]
index = faiss.IndexFlatIP(dimensions)
index.add(embeddings)

card = find_card("Dark Ritual", cards)
vector = np.array([embeddings[card]])

distances, indexes = index.search(vector, K)

for i in range(K):
    card = cards[indexes[0][i]]
    print(card["name"], distances[0][i], card["oracle_text"])
