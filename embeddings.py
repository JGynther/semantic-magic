from transformers import AutoTokenizer, AutoModel
from utils import construct_embedding_string
import torch
import orjson


model_id = "BAAI/bge-small-en-v1.5"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModel.from_pretrained(model_id)


with open("oracle-cards.json") as file:
    data = orjson.loads(file.read())


cards = [construct_embedding_string(card) for card in data]
del data


with open("embeddings.txt", "a") as file:
    with torch.no_grad():
        for card in cards:
            inputs = tokenizer(card, padding=True, truncation=True, return_tensors="pt")
            output = model(**inputs)
            embedding = output[0][:, 0]
            embedding = torch.nn.functional.normalize(embedding, p=2, dim=1)
            embedding = embedding.squeeze().tolist()
            file.write(f"{embedding}\n")
