from tilevisual import TileVisual, draw_single_tile


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

        for road in self.roads:
            if len(road) == 1:
                components.append(f"road {road[0]}")
            if len(road) == 2:
                components.append(f"road {road[0]} {road[1]}")

        if self.monastery:
            components.append("monastery")

        return TileVisual(components)


def main() -> None:
    roads = []
    cities = [["left", "right"]]
    monastary = False
    tile: Tile = Tile(roads, cities, monastary)
    draw_single_tile(tile.visual.compose_tile())


if __name__ == "__main__":
    main()
