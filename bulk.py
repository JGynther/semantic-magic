import orjson
import torch
import numpy as np
import faiss

with open("oracle-cards.json") as file:
    cards = orjson.loads(file.read())

embeddings = torch.load("embeddings.pt")
embeddings = np.array(embeddings)

dimensions = embeddings[0].shape[0]
index = faiss.IndexFlatIP(dimensions)
index.add(embeddings)

distances, indexes = index.search(embeddings, k=11)

neighbours = []

for i in range(len(embeddings)):
    obj = {"id": cards[i]["id"], "neighbours": []}

    for j in range(1, 11):
        obj["neighbours"].append(cards[indexes[i][j]]["id"])

    neighbours.append(obj)

with open("neighbours.json", "w") as file:
    file.write(orjson.dumps(neighbours).decode("utf-8"))
