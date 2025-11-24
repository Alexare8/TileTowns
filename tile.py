from enum import Enum
from socket import EAI_SYSTEM
from subprocess import STD_OUTPUT_HANDLE

from tile_set import STARTING_TILE, TILESET
from tilevisual import TileVisual


class Tile:
    def __init__(
        self,
        roads: list[list[str]] = [],
        cities: list[list[str]] = [],
        monastery: bool = False,
        bonus: bool = False,
    ) -> None:
        # Roads as lists of connected road pieces ie: ["top", "bottom"], ["right"]
        # Cities as lists of connected edges ie: ["left", "top"] or ["bottom"]
        # Top must come first, then bottom, then right, then left
        if cities and monastery:
            raise ValueError("Tile cannot have both city and monastery")
        for road in roads:
            if len(road) < 1 or len(road) > 2:
                raise ValueError("A road must have exactly one or two ends on a tile.")
        self.roads = roads
        self.cities = cities
        self.monastery = monastery
        self.bonus = bonus
        self.visual = self.get_visual()

    def __repr__(self) -> str:
        output = []

        roads = []
        for road in self.roads:
            roads.append(", ".join(road))
        output.append(f"Roads: {roads}")

        cities = []
        for city in self.cities:
            cities.append(", ".join(city))
        output.append(f"Cities: {cities}")

        output.append(f"Monastery: {self.monastery}")
        output.append(f"Bonus: {self.bonus}")

        return "\n".join(output)

    def get_visual(self) -> TileVisual:
        """Create tile visual from list of visual components in order walls, roads, features"""
        components = []
        for city in self.cities:
            if len(city) == 1:
                components.append(f"wall {city[0]}")
            if len(city) == 2:
                match city[0], city[1]:
                    case "top", "right":
                        components.append("wall top-left bottom-right")
                    case "bottom", "left":
                        components.append("wall top-left bottom-right")

                    case "top", "left":
                        components.append("wall buttom-left top-right")
                    case "bottom", "right":
                        components.append("wall buttom-left top-right")
            if len(city) == 3:
                for side in ["top", "bottom", "right", "left"]:
                    if side not in city:
                        components.append(f"wall {side}")
            if len(city) == 4:
                components.append("city center")

        if self.monastery:
            components.append("monastery")

        for road in self.roads:
            if len(road) == 1:
                components.append(f"road {road[0]}")
            if len(road) == 2:
                components.append(f"road {road[0]} {road[1]}")

        return TileVisual(components)


def show_tiles() -> None:
    print("Starting Tile:")
    starting_tile = Tile(**STARTING_TILE)
    starting_tile.visual.draw_tile()
    print("Tile Pool")
    tiles = []
    for tile, quantity in TILESET:
        tiles.append((Tile(**tile), quantity))
    for tile, quantity in tiles:
        print(f"{quantity} of:")
        tile.visual.draw_tile()


def main():
    show_tiles()


if __name__ == "__main__":
    main()
