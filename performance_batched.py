import faiss
import numpy as np
import torch
from time import time

embeddings = torch.load("embeddings.pt")
embeddings = np.array(embeddings)

dimensions = embeddings[0].shape[0]
index = faiss.IndexFlatIP(dimensions)
index.add(embeddings)

times = []
length = len(embeddings)

for _ in range(10):
    test_indexes = np.random.randint(0, length, size=10_000)

    vectors = []
    for i in test_indexes:
        vectors.append(embeddings[i])

    vectors = np.array(vectors)

    start = time()

    index.search(vectors, k=5)

    times.append(time() - start)

print("Unit: seconds")
print(f"10 x 10 000 kNN searches with k=5")
print(f"Total: {np.sum(times)}")
print(f"Comparisons per second: {100_000 / np.sum(times)}")
print(f"Mean: {np.mean(times)}")
print(f"Std: {np.std(times)}")
print(f"Min: {np.min(times)}")
print(f"Max: {np.max(times)}")
