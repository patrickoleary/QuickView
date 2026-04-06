TYPE_COLORS = [
    "red",
    "yellow",
    "purple",
    "cyan",
    "brown",
    "indigo",
    "gray",
    "orange",
    "green",
    "orange",
    "lime",
    "deep-purple",
]


def get_type_color(index: int) -> str:
    return TYPE_COLORS[index % len(TYPE_COLORS)]
