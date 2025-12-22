from enum import Enum
import math
from typing import Any, Optional, Tuple

# TODO: Add comments. Add type hints.

# Keywords:
#   +, -, *, /, //, %, **,
#   ==, !=, <=, >=, <, >,
#   not, and, or,
#   True, False, None,
#   str()，list(), dict(), set(),
#   .append(), .add(), .remove(), .pop(), .insert(),
#   len(), range(),
#   import, from,
#   def, pass, return,
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
    Dinosaur = 'dinosaur'
    Grass = 'grass'
    Hedge = 'hedge'
    Dead_Pumpkin = 'dead_pumpkin'
    Pumpkin = 'pumpkin'
    Sunflower = 'sunflower'
    Tree = 'tree'
    Treasure = 'treasure'

class Grounds(Enum):
    Grassland = 'grassland'
    Soil = 'soil'

class Hats(Enum):
    Brown_Hat = 'brown_hat'
    Cactus_Hat = 'cactus_hat'
    Carrot_Hat = 'carrot_hat'
    Dinosaur_Hat = 'dinosaur_hat'
    Gold_Hat = 'gold_hat'
    Gray_Hat = 'gray_hat'
    Green_Hat = 'green_hat'
    Pumpkin_Hat = 'pumpkin_hat'
    Purple_Hat = 'purple_hat'
    Straw_Hat = 'straw_hat'
    Sunflower_Hat = 'sunflower_hat'
    Traffic_Cone = 'traffic_cone'
    Tree_Hat = 'tree_hat'
    Wizard_Hat = 'wizard_hat'


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


def abs(number: int | float) -> int | float:
    """
    @category: `builtin_funcions`.
    @description: Computes the absolute value of a `number`.
    @parameter number: The number.
    @returns: `number` if number is positive, `-number` otherwise.
    @ticks: 1.
    """
    return math.abs(number)

def can_harvest() -> bool:
    """
    @category: `builtin_funcions`.
    @description: Used to find out if plants are fully grown.
    @returns: `True` if there is an entity under the drone is ready to be harvested.
              `False` otherwise.
    @ticks: 1.
    @see_also: `Unlocks.Speed`
    """
    pass

def can_move(direction: Direction) -> bool:
    pass

def change_hat(hat: Hats) -> None:
    pass

def clear() -> None:
    pass

def do_a_flip() -> None:
    pass

def get_companion() -> Tuple[
    (Entities.Bush | Entities.Grass | Entities.Tree | Entities.Carrot),
    Tuple[int, int]
]:
    pass

def get_cost(q: Entities | Unlocks, level: Optional[int] = None) -> dict[Items, int]:
    pass

def get_entity_type() -> Optional[Entities]:
    pass

def get_ground_type() -> Grounds:
    pass

def get_pos_x() -> int:
    pass

def get_pos_y() -> int:
    pass

def get_tick_count() -> 

def get_water() -> float:
    pass

def get_world_size() -> int:
    pass

def harvest() -> None:
    pass

def has_finished(drone_handler: DroneHandler) -> bool:
    pass

def max_drones() -> int:
    pass
    
def measure(direction: Direction) -> int:
    pass

def move(direction: Direction) -> bool:
    pass

def num_drones() -> int:
    pass
    
def num_items(item: Items) -> int:
    pass

def num_unlocked(_unlock: Unlocks) -> int:
    pass
    
def pet_the_piggy() -> None:
    pass

def plant(entity: Entities) -> None:
    pass

def print(_obj: Any) -> None:
    pass

def quick_print(_obj: Any) -> None:
    pass

def spawn_drone() -> False | DroneHandler:
    pass

def swap(direction: Direction) -> None:
    pass

def till() -> None:
    pass

def unlock(_unlock: Unlocks) -> None:
    pass

def use_item(item: Items, n: int) -> None:
    pass

def wait_for(drone_handler: DroneHandler) -> None:
    pass
