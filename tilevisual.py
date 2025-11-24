from copy import deepcopy

from tile_data import TILE_DATA, TILE_HEIGHT, TILE_WIDTH

type TileCharDisplay = list[list[str]]
type ComponentData = dict[str, list[str]]


def construct_components(data: ComponentData) -> dict[str, TileCharDisplay]:
    components: dict[str, TileCharDisplay] = {}
    for component in data:
        line_list: TileCharDisplay = []
        for line in data[component]:
            char_list: list[str] = []
            for char in line:
                char_list.append(char)
            line_list.append(char_list)
        components[component] = line_list
    return components


TILE_COMPONENTS: dict[str, TileCharDisplay] = construct_components(TILE_DATA)


class TileVisual:
    def __init__(self, components: list[str]) -> None:
        # list of components must be ordered walls, features, roads
        self.components: list[TileCharDisplay] = []
        for component in components:
            self.components.append(TILE_COMPONENTS[component])

    def compose_tile(self) -> TileCharDisplay:
        """Assemble the tile components into a complete tile."""
        char_display: TileCharDisplay = deepcopy(TILE_COMPONENTS["frame"])
        for component in self.components:
            for i in range(TILE_HEIGHT):
                for j in range(TILE_WIDTH):
                    if component[i][j] != "◦":
                        char_display[i][j] = component[i][j]
        return char_display

    def draw_tile(self) -> None:
        # print("TileVisual.draw_tile() is for testing only")
        for line in self.compose_tile():
            string = ""
            for char in line:
                string += char
            print(string)
