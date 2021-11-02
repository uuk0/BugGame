import os
import typing

root = os.path.dirname(os.path.dirname(__file__))
asset_dir = root+"/assets"
data_dir = root+"/data"
saves_dir = root+"/saves"


class StonePathBuilder:
    pass


class WallPlacer:
    pass


class GrassLayer:
    def decorate(self, position: typing.Tuple[int, int], group: str):
        pass


class FunctionalObjectPlacer:
    def place_stair(self, position: typing.Tuple[int, int]):
        pass

    def place_cube(self, position: typing.Tuple[int, int]):
        pass

    def place_chest(self, position: typing.Tuple[int, int], opened: bool):
        pass

    def place_door(self, position: typing.Tuple[int, int], opened: bool):
        pass

    def place_big_container(self, position: typing.Tuple[int, int]):
        pass

    def place_small_container(self, position: typing.Tuple[int, int]):
        pass

    def place_barrel(self, position: typing.Tuple[int, int]):
        pass

    def place_big_waystone(self, position: typing.Tuple[int, int]):
        pass

    def place_medium_waystone(self, position: typing.Tuple[int, int]):
        pass

    def place_small_waystone(self, position: typing.Tuple[int, int]):
        pass

    def place_bank(self, position: typing.Tuple[int, int], orientation: str = "front"):
        pass

    def place_tree(self, position: typing.Tuple[int, int], tree_type: str = None):
        pass

    def place_bush(self, position: typing.Tuple[int, int], bush_type: str = None):
        pass


class PlayerRenderer:
    def add_player(self, dynamic_position: typing.Callable[[], typing.Tuple[float, float]]):
        pass


class ItemRenderingRegistry:
    def register_item(self, name: str, texture_path: str, region: typing.Tuple[int, int, int, int] = None):
        pass

