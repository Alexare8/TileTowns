import sys
from tile_data import TILE_WIDTH, TILE_HEIGHT, TILE_DATA


def construct_components(data):
    components = {}
    for component in data:
        line_list = []
        for line in data[component]:
            char_list = []
            for char in line:
                char_list.append(char)
            line_list.append(char_list)
        components[component] = line_list
    return components

TILE_COMPONENTS = construct_components(TILE_DATA)


class Tile:
    def __init__(self, components):
        # list of components must be ordered walls, roads, feature
        self.components = []
        for component in components:
            self.components.append(TILE_COMPONENTS[component])


    def compose_tile(self):
        """Assemble the tile components into a complete tile."""
        ascii = TILE_COMPONENTS["frame"]
        for component in self.components:
            for i in range(TILE_HEIGHT):
                for j in range(TILE_WIDTH):
                    if component[i][j] != "◦":
                        ascii[i][j] = component[i][j]

        return ascii


def main():
    args = sys.argv[1:]
    tile = Tile(args)
    output = tile.compose_tile()
    for line in output:
        string = ""
        for char in line:
            string += char
        print(string)


if __name__ == "__main__":
    main()
