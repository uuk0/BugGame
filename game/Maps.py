import typing
import weakref


class ActiveWorld:
    def prepare_map(self, name: str):
        pass

    def switch_map(self, to: str, entry_point=None):
        pass


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
        self.sectors = []
        self.loaded_sectors: weakref.WeakSet["Map.MapSector"] = weakref.WeakSet()

    def from_data(self, data: dict):
        pass

