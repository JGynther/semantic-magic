def construct_embedding_string(card: dict[str, str]):
    type_line = card["type_line"]
    # These might not exist
    mana_cost = card.get("mana_cost", "")
    oracle_text = card.get("oracle_text", "")
    power = card.get("power", "")
    toughness = card.get("toughness", "")

    string = f"{type_line} {mana_cost} {power} {toughness} {oracle_text}"

    return string.replace("\n", "")
