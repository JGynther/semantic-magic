from sentence_transformers import SentenceTransformer
from utils import construct_embedding_string
import torch
import orjson

model_id = "llmrails/ember-v1"
model = SentenceTransformer(model_id, device="mps")

with open("oracle-cards.json") as file:
    data = orjson.loads(file.read())

cards = [construct_embedding_string(card) for card in data]

embeddings = model.encode(cards, normalize_embeddings=True, show_progress_bar=True)
torch.save(embeddings, "embeddings.pt")
