from typing import Tuple

import numpy as np  # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if this tile can be walked over.
        ("transparent", np.bool),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when this tile is not in FOV.
        ("light", graphic_dt),
    ]
)


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

#TODO We'll need to get this so that a function just fills it out, from a dict

# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), (222, 238, 214), (20, 12, 28)), dtype=graphic_dt)

floor = new_tile(
    walkable=True, 
    transparent=True, 
    dark=(ord("·"), (48, 52, 109), (20, 12, 28)),
    light=(ord("·"), (133, 149, 161), (20, 12, 28)),
)
wall = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("#"), (222, 238, 214), (20, 12, 28)),
    light=(ord("#"), (222, 238, 214), (20, 12, 28)),
)
stairs_up = new_tile(
    walkable=True, 
    transparent=True, 
    dark=(ord(">"), (222, 238, 214), (20, 12, 28)),
    light=(ord(">"), (210, 125, 44), (20, 12, 28)),
)
stairs_down = new_tile(
    walkable=True, 
    transparent=True,
    dark=(ord("<"), (222, 238, 214), (20, 12, 28)),
    light=(ord("<"), (210, 125, 44), (20, 12, 28)),
)
wall_ul_corner = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("╔"), (222, 238, 214),(20, 12, 28)),
    light=(ord("╔"), (210, 125, 44),(20, 12, 28)),
)
wall_horizontal = new_tile(
    walkable=False, 
    transparent=False,
    dark=(ord("═"), (222, 238, 214),(20, 12, 28)),
    light=(ord("═"), (210, 125, 44),(20, 12, 28)),
)
wall_ur_corner = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("╗"), (222, 238, 214),(20, 12, 28)),
    light=(ord("╗"), (210, 125, 44),(20, 12, 28)),
)

wall_vertical = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("║"), (222, 238, 214),(20, 12, 28)),
    light=(ord("║"), (210, 125, 44),(20, 12, 28)),
)

wall_lr_corner = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("╝"), (222, 238, 214),(20, 12, 28)),
    light=(ord("╝"), (210, 125, 44),(20, 12, 28)),
)

wall_ll_corner = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("╚"), (222, 238, 214),(20, 12, 28)),
    light=(ord("╚"), (210, 125, 44),(20, 12, 28)),
)
#TODO this doesn't really fit the categories
door = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("+"), (222, 238, 214),(20, 12, 28)),
    light=(ord("+"), (222, 238, 214),(20, 12, 28)),
)

left_t = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("╠"), (222, 238, 214),(20, 12, 28)),
    light=(ord("╠"), (210, 125, 44),(20, 12, 28))
)

right_t = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("╣"), (222, 238, 214),(20, 12, 28)),
    light=(ord("╣"), (210, 125, 44),(20, 12, 28)),
)
bottom_t = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("╩"), (222, 238, 214),(20, 12, 28)),
    light=(ord("╩"), (210, 125, 44),(20, 12, 28)),
)
top_t = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("╦"), (222, 238, 214),(20, 12, 28)),
    light=(ord("╦"), (210, 125, 44),(20, 12, 28)),
)
carpet = new_tile(
    walkable=True, 
    transparent=True, 
    dark=(ord("░"), (222, 238, 214),(20, 12, 28)),
    light=(ord("░"), (208, 70, 72),(68, 36, 52)),
)
vase = new_tile(
    walkable=False, 
    transparent=True, 
    dark=(ord("Φ"), (222, 238, 214),(20, 12, 28)),
    light=(ord("Φ"), (218, 212, 94),(20, 12, 28)),
)
pillar = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("■"), (222, 238, 214),(20, 12, 28)),
    light=(ord("■"), (20, 12, 28),(210, 125, 44)),
)
water = new_tile(
    walkable=False, 
    transparent=True, 
    dark=(ord("≈"), (222, 238, 214),(20, 12, 28)),
    light=(ord("≈"), (109, 194, 202),(89, 125, 206)),
)
pyramid = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord("▲"), (222, 238, 214),(20, 12, 28)),
    light=(ord("▲"), (222, 238, 214),(20, 12, 28)),
)
altar = new_tile(
    walkable=True, 
    transparent=True, 
    dark=(ord("╥"), (222, 238, 214),(20, 12, 28)),
    light=(ord("╥"), (208, 70, 72),(20, 12, 28)),
)
herb = new_tile(
    walkable=False, 
    transparent=True, 
    dark=(ord("♣"), (222, 238, 214),(20, 12, 28)),
    light=(ord("♣"), (52, 101, 36),(20, 12, 28)),
)
flower = new_tile(
    walkable=False, 
    transparent=True, 
    dark=(ord("☼"), (222, 238, 214),(20, 12, 28)),
    light=(ord("☼"), (218, 212, 94),(20, 12, 28)),
)
low_wall_ll = new_tile(
    walkable=False, 
    transparent=True, 
    dark=(ord("└"), (222, 238, 214),(20, 12, 28)),
    light=(ord("└"), (210, 125, 44),(20, 12, 28)),
)
low_wall_lr = new_tile(
    walkable=False, 
    transparent=True, 
    dark=(ord("┘"), (222, 238, 214),(20, 12, 28)),
    light=(ord("┘"), (210, 125, 44),(20, 12, 28)),
)
low_wall_vert = new_tile(
    walkable=False, 
    transparent=True, 
    dark=(ord("│"), (222, 238, 214),(20, 12, 28)),
    light=(ord("│"), (210, 125, 44),(20, 12, 28)),
)
low_wall_horiz = new_tile(
    walkable=False, 
    transparent=True, 
    dark=(ord("─"), (222, 238, 214),(20, 12, 28)),
    light=(ord("─"), (210, 125, 44),(20, 12, 28)),
)
low_wall_ul = new_tile(
    walkable=False, 
    transparent=True, 
    dark=(ord("┌"), (222, 238, 214),(20, 12, 28)),
    light=(ord("┌"), (210, 125, 44),(20, 12, 28)),
)
low_wall_ur = new_tile(
    walkable=False, 
    transparent=True, 
    dark=(ord("┐"), (222, 238, 214),(20, 12, 28)),
    light=(ord("┐"), (210, 125, 44),(20, 12, 28)),
)

