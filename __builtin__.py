import builtins
from enum import Enum
import math
from typing import Any, Dict, Iterable, Optional, Tuple

from _fake_collection import fake_collection

# TODO: Complete comments.

# Keywords:
#   +, -, *, /, //, %, **,
#   ==, !=, <=, >=, <, >,
#   not, and, or,
#   True, False, None,
#   import, from,
#   def, ..., return,
#   global,
#   if, elif, else, while, for, continue, break,
#   __name__
#
# single-line string only:
#   'str' is ok.
#   """str""" is unsupported.

Direction = str
DroneHandler = int

South = 'south'
East = 'east'
North = 'north'
West = 'west'

class Entities(Enum):
    Apple = 'apple'
    Bush = 'bush'
    Cactus = 'cactus'
    Carrot = 'carrot'
    Dead_Pumpkin = 'dead_pumpkin'
    Dinosaur = 'dinosaur'
    Grass = 'grass'
    Hedge = 'hedge'
    Pumpkin = 'pumpkin'
    Sunflower = 'sunflower'
    Treasure = 'treasure'
    Tree = 'tree'

class Grounds(Enum):
    Grassland = 'grassland'
    Soil = 'soil'

class Hats(Enum):
    Brown_Hat = 'brown_hat'
    Cactus_Hat = 'cactus_hat'
    Carrot_Hat = 'carrot_hat'
    Dinosaur_Hat = 'dinosaur_hat'
    Gold_Hat = 'gold_hat'
    Gold_Trophy_Hat = 'gold_trophy_hat'
    Golden_Cactus_Hat = 'golden_cactus_hat'
    Golden_Carrot_Hat = 'golden_carrot_hat'
    Golden_Gold_Hat = 'golden_gold_hat'
    Golden_Pumpkin_Hat = 'golden_pumpkin_hat'
    Golden_Sunflower_Hat = 'golden_sunflower_hat'
    Golden_Tree_Hat = 'golden_tree_hat'
    Gray_Hat = 'gray_hat'
    Green_Hat = 'green_hat'
    Pumpkin_Hat = 'pumpkin_hat'
    Purple_Hat = 'purple_hat'
    Silver_Trophy_Hat = 'silver_trophy_hat'
    Straw_Hat = 'straw_hat'
    Sunflower_Hat = 'sunflower_hat'
    The_Farmers_Remains = 'the_farmers_remains'
    Top_Hat = 'top_hat'
    Traffic_Cone = 'traffic_cone'
    Traffic_Cone_Stack = 'traffic_cone_stack'
    Tree_Hat = 'tree_hat'
    Wizard_Hat = 'wizard_hat'
    Wood_Trophy_Hat = 'wood_trophy_hat'


class Items(Enum):
    Bone = 'bone'
    Cactus = 'cactus'
    Carrot = 'carrot'
    Fertilizer = 'fertilizer'
    Gold = 'gold'
    Hay = 'hay'
    Power = 'power'
    Pumpkin = 'pumpkin'
    Water = 'water'
    Weird_substance = 'weird_substance'
    Wood = 'wood'

class Leaderboards(Enum):
    Cactus = 'cactus'
    Cactus_Single = 'cactus_single'
    Carrots = 'carrots'
    Carrots_Single = 'carrots_single'
    Dinosaur = 'dinosaur'
    Fastest_Reset = 'fastest_reset'
    Hay = 'hay'
    Hay_Single = 'hay_single'
    Maze = 'maze'
    Maze_Single = 'maze_single'
    Pumpkins = 'pumpkins'
    Pumpkins_Single = 'pumpkins_single'
    Sunflowers = 'sunflowers'
    Sunflowers_Single = 'sunflowers_single'
    Wood = 'wood'
    Wood_Single = 'wood_single'

class Unlocks(Enum):
    Auto_Unlock = 'auto_unlock'
    Cactus = 'cactus'
    Carrots = 'carrots'
    Costs = 'costs'
    Debug = 'debug'
    Debug_2 = 'debug_2'
    Dictionaries = 'dictionaries'
    Dinosaurs = 'dinosaurs'
    Expand = 'expand'
    Fertilizer = 'fertilizer'
    Functions = 'functions'
    Grass = 'grass'
    Hats = 'hats'
    Import = 'import'
    Leaderboard = 'leaderboard'
    Lists = 'lists'
    Loops = 'loops'
    Mazes = 'mazes'
    Megafarm = 'megafarm'
    Operators = 'operators'
    Plant = 'plant'
    Polyculture = 'polyculture'
    Pumpkins = 'pumpkins'
    Senses = 'senses'
    Simulation = 'simulation'
    Speed = 'speed'
    Sunflowers = 'sunflowers'
    The_Farmers_Remains = 'the_farmers_remains'
    Timing = 'timing'
    Top_Hat = 'top_hat'
    Trees = 'trees'
    Utilities = 'utilities'
    Variables = 'variables'
    Watering = 'watering'


def can_harvest() -> bool:
    """
    @category: `builtin_funcions`.
    @description: Used to find out if plants are fully grown.
    @returns: `True` if there is an entity under the drone is ready to be harvested.
              `False` otherwise.
    @ticks: 1.
    @unlock: `Unlocks.?`
    @see_also: `Unlocks.Speed`
    """
    ...


def can_move(direction: Direction) -> bool:
    ...


def change_hat(hat: Hats) -> None:
    ...


def clear() -> None:
    ...


def do_a_flip() -> None:
    ...


def get_companion() -> Optional[Tuple[
    (Entities.Bush | Entities.Grass | Entities.Tree | Entities.Carrot),
    Tuple[int, int]
]]:
    ...


def get_cost(q: Entities | Unlocks, level: Optional[int] = None) -> Optional[dict[Items, int]]:
    ...


def get_entity_type() -> Optional[Entities]:
    ...


def get_ground_type() -> Grounds:
    ...


def get_pos_x() -> int:
    ...


def get_pos_y() -> int:
    ...


def get_tick_count() -> int:
    ...


def get_time() -> int:
    ...


def get_water() -> float:
    ...


def get_world_size() -> int:
    ...


def harvest() -> bool:
    ...


def has_finished(drone_handler: DroneHandler) -> bool:
    ...


def leaderboard_run(leaderboard: Leaderboards, file_name: str, speedup: float) -> None:
    ...


def max_drones() -> int:
    ...


# should use `float` instead of `int` for return type?
def measure(direction: Optional[Direction] = None) -> int | Tuple[int, int] | None:
    ...


def move(direction: Direction) -> bool:
    ...


def num_drones() -> int:
    ...


def num_items(item: Items) -> float:
    ...


def num_unlocked(_unlock: Unlocks | Entities | Grounds | Items | Hats) -> int:
    ...


def pet_the_piggy() -> None:
    ...


def plant(entity: Entities) -> None:
    ...


def print(*_obj: Any) -> None:
    ...


def quick_print(*_obj: Any) -> None:
    ...


def random() -> float:
    ...


def set_execution_speed(speed: float) -> None:
    ...


def set_world_size(size: float) -> None:
    ...


def simulate(
    filename: str,
    sim_unlocks: dict[Unlocks, int] | Iterable[Unlocks] | Unlocks,
    sim_items: dict[Items, float],
    sim_globals: dict[str, Any],
    seed: int,
    speedup: float
) -> float:
    ...


def spawn_drone() -> Optional[DroneHandler]:
    ...


def swap(direction: Direction) -> bool:
    ...


def till() -> None:
    ...


def unlock(_unlock: Unlocks) -> bool:
    ...


def use_item(item: Items, n: int = 1) -> None:
    ...


def wait_for(drone_handler: DroneHandler) -> Any:
    ...

"""
@category: `builtin_funcions`.
@description: Computes the absolute value of a `number`.
@parameter number: The number.
@returns: `number` if number is positive, `-number` otherwise.
@ticks: 1.
@unlock: `Unlocks.?`
"""
abs = builtins.abs
len = builtins.len
min = builtins.min
max = builtins.max

range = builtins.range
str = builtins.str
dict = fake_collection
list = fake_collection
set = fake_collection
