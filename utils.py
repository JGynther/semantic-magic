import re


def construct_embedding_string(card: dict[str, str]):
    type_line = card["type_line"]
    oracle_text = card.get("oracle_text", "")

    text = " ".join([type_line, oracle_text])

    text = text.lower()
    text = text.replace(card["name"].lower(), "this")  # Remove card name
    text = re.sub(r"\([^)]+\)", "", text)  # Remove reminder text between ()
    text = text.replace("\n", " ")  # Remove newlines

    return text


def find_card(name: str, cards: list[dict[str, str]]):
    name = name.lower()

    for i, card in enumerate(cards):
        if card["name"].lower() == name:
            return i

    raise ValueError(f"Card {name} not found")
