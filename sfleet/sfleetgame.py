import resources
from game.game import Game
from vessel import Vessel


class SfleetGame(Game):
    def __init__(self, fullscreen=True):
        super(SfleetGame, self).__init__(fullscreen=fullscreen, name="S Fleet")

        self.player_fleet = self.load_player_fleet()
        self.enemy_fleet = self.load_enemy_fleet()

        self.game_objects += self.player_fleet + self.enemy_fleet

    def load_player_fleet(self, batch=None):
        if batch is None:
            batch = self.main_batch

        ship_spec = {
            'speed': 10,
            'hull': 100,
            'armour': 50,
            'armour_threshold': 10,
            'shield': 50,
            'shield_recharge': 10,
            'weapon_range': 30,
            'weapon_damage': 20
        }

        player_ship = Vessel(name="ASF Brantd",
                             x=self.window.width / 2.0,
                             y=200.0,
                             rotation=0,
                             hull_image=resources.arkadian_cruiser_image,
                             spec=ship_spec,
                             batch=batch)

        self.window.push_handlers(player_ship)
        return [player_ship]

    def load_enemy_fleet(self, batch=None):
        if batch is None:
            batch = self.main_batch

        ship_spec = {
            'speed': 10,
            'hull': 100,
            'armour': 50,
            'armour_threshold': 10,
            'shield': 50,
            'shield_recharge': 10,
            'weapon_range': 30,
            'weapon_damage': 20
        }

        enemy_ship = Vessel(name="ITV Vladimir",
                            x=self.window.width / 2.0,
                            y=self.window.height - 200.0,
                            rotation=180.0,
                            hull_image=resources.terran_cruiser_image,
                            spec=ship_spec,
                            batch=batch)

        self.window.push_handlers(enemy_ship)
        return [enemy_ship]
