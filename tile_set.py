TILESET: list[tuple[dict[str, bool | list[list[str]]], int]] = [
    (
        {
            "roads": [],
            "cities": [],
            "monastery": True,
            "bonus": False,
        },
        4,
    ),
    (
        {
            "roads": [["bottom"]],
            "cities": [],
            "monastery": True,
            "bonus": False,
        },
        2,
    ),
    (
        {
            "roads": [],
            "cities": [["top", "bottom", "right", "left"]],
            "monastery": False,
            "bonus": True,
        },
        1,
    ),
    (
        {
            "roads": [],
            "cities": [["top", "right", "left"]],
            "monastery": False,
            "bonus": False,
        },
        3,
    ),
    (
        {
            "roads": [],
            "cities": [["top", "right", "left"]],
            "monastery": False,
            "bonus": True,
        },
        1,
    ),
    (
        {
            "roads": [["bottom"]],
            "cities": [["top", "right", "left"]],
            "monastery": False,
            "bonus": False,
        },
        1,
    ),
    (
        {
            "roads": [["bottom"]],
            "cities": [["top", "right", "left"]],
            "monastery": False,
            "bonus": True,
        },
        2,
    ),
    (
        {
            "roads": [],
            "cities": [["top", "left"]],
            "monastery": False,
            "bonus": False,
        },
        3,
    ),
    (
        {
            "roads": [],
            "cities": [["top", "left"]],
            "monastery": False,
            "bonus": True,
        },
        2,
    ),
    (
        {
            "roads": [["bottom", "right"]],
            "cities": [["top", "left"]],
            "monastery": False,
            "bonus": False,
        },
        3,
    ),
    (
        {
            "roads": [["bottom", "right"]],
            "cities": [["top", "left"]],
            "monastery": False,
            "bonus": True,
        },
        2,
    ),
    (
        {
            "roads": [],
            "cities": [["right", "left"]],
            "monastery": False,
            "bonus": False,
        },
        1,
    ),
    (
        {
            "roads": [],
            "cities": [["right", "left"]],
            "monastery": False,
            "bonus": True,
        },
        2,
    ),
    (
        {
            "roads": [],
            "cities": [["top"], ["left"]],
            "monastery": False,
            "bonus": False,
        },
        2,
    ),
    (
        {
            "roads": [],
            "cities": [["top"], ["bottom"]],
            "monastery": False,
            "bonus": False,
        },
        3,
    ),
    (
        {
            "roads": [],
            "cities": [["top"]],
            "monastery": False,
            "bonus": False,
        },
        5,
    ),
    (
        {
            "roads": [["bottom", "left"]],
            "cities": [["top"]],
            "monastery": False,
            "bonus": False,
        },
        3,
    ),
    (
        {
            "roads": [["bottom", "right"]],
            "cities": [["top"]],
            "monastery": False,
            "bonus": False,
        },
        3,
    ),
    (
        {
            "roads": [["bottom"], ["right"], ["left"]],
            "cities": [["top"]],
            "monastery": False,
            "bonus": False,
        },
        3,
    ),
    (
        {
            "roads": [["right", "left"]],
            "cities": [["top"]],
            "monastery": False,
            "bonus": False,
        },
        3,
    ),
    (
        {
            "roads": [["top", "bottom"]],
            "cities": [],
            "monastery": False,
            "bonus": False,
        },
        8,
    ),
    (
        {
            "roads": [["bottom", "left"]],
            "cities": [],
            "monastery": False,
            "bonus": False,
        },
        9,
    ),
    (
        {
            "roads": [["bottom"], ["right"], ["left"]],
            "cities": [],
            "monastery": False,
            "bonus": False,
        },
        4,
    ),
    (
        {
            "roads": [["top"], ["bottom"], ["right"], ["left"]],
            "cities": [],
            "monastery": False,
            "bonus": False,
        },
        1,
    ),
]

STARTING_TILE: dict[str, bool | list[list[str]]] = {
    "roads": [["right", "left"]],
    "cities": [["top"]],
    "monastery": False,
    "bonus": False,
}
