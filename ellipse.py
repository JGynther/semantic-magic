from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np


def ellipse(cards, dim_red_embeds):
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(13, 9))

    types = [
        "Creature",
        "Instant",
        "Sorcery",
        "Artifact",
        "Land",
        "Enchantment",
        "Planeswalker",
    ]

    categories = [[] for _ in types]

    for i, card in enumerate(cards):
        for j, ctype in enumerate(types):
            if ctype in card["type_line"]:
                categories[j].append(dim_red_embeds[i])
                break

    cmap = plt.get_cmap("Set3")

    for i, category in enumerate(categories):
        category = np.array(category)
        centroid = np.average(category, axis=0)

        ellipse = Ellipse(
            xy=centroid,
            width=2 * np.std(category[:, 0]),
            height=2 * np.std(category[:, 1]),
            alpha=0.8,
            color=cmap(i),
        )

        ax.add_patch(ellipse)
        ax.scatter(
            category[:, 0],
            category[:, 1],
            label=types[i],
            color=cmap(i),
            s=5,
            alpha=0.3,
        )

    legend = plt.legend()

    for handle in legend.legendHandles:
        handle.set_sizes([100])
        handle.set_alpha(1)

    plt.show()
