import resources
from hero import Hero
from settings import WINDOW_HORIZONTAL_CENTER, WINDOW_VERTICAL_CENTER


def player_hero(batch=None):
    player_hero = Hero(name="Player Hero", body_image=resources.player_image,
                       x=WINDOW_HORIZONTAL_CENTER, y=WINDOW_VERTICAL_CENTER,
                       batch=batch)
    return player_hero
