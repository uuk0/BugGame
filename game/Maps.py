import json
import typing
import weakref

import pyglet

from game.Resources import resource_path


class ActiveWorld:
    def __init__(self):
        self.maps: typing.Dict[str, "Map"] = {}

        self.current_map: typing.Optional["Map"] = None

    def prepare_map(self, name: str):
        if name not in self.maps:
            m = Map()

            with open(resource_path("data/maps/"+name+".json")) as f:
                data = json.load(f)

            m.from_data(data)
            self.maps[name] = m

    def switch_map(self, to: str, entry_point=None):
        if to not in self.maps:
            raise ValueError(to)

        m = self.maps[to]

        if entry_point is not None:
            m.last_player_position = entry_point

        self.current_map = m
        m.join()

    def draw(self):
        if self.current_map is not None:
            self.current_map.draw()


class Map:
    class MapSector:
        def __init__(self, parent_map: "Map"):
            self.parent = parent_map
            self.neighbor_sectors: weakref.WeakSet["Map.MapSector"] = weakref.WeakSet()

        def ensure_neighbor_sectors(self):
            self.parent.loaded_sectors.add(self)
            self.parent.loaded_sectors.update(self.neighbor_sectors)

        def from_data(self, data: dict):
            pass

    def __init__(self):
        self.name = None

        self.sectors = []
        self.loaded_sectors: weakref.WeakSet["Map.MapSector"] = weakref.WeakSet()

        self.rendering_batch = pyglet.graphics.Batch()

        self.last_player_position = None
        self.spawn_position = (0, 0)

    def from_data(self, data: dict):
        self.name = data.setdefault("name", None)
        self.spawn_position = tuple(data.setdefault("spawn_position", (0, 0)))

        for sector_data in data.setdefault("sectors", []):
            sector = Map.MapSector(self)
            self.sectors.append(sector)
            sector.from_data(sector_data)

    def join(self):
        pass

    def draw(self):
        pass

