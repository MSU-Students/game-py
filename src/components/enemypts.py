#pts per enemy

from src.core.screen import Screen
from src.components.player import AirPlane, EnemyPlayer
import src.modules.game_levels as game_levels

points_enemy01 = 100
points_enemy02 = 150
points_enemy03 = 200
points_Miniboss_kill = 500
points_Miniboss_hit = 10

class GamePoints:
    def get_base_points(self, enemy_type: str):
        points_map = {
            "enemy01": points_enemy01,
            "enemy02": points_enemy02,
            "enemy03": points_enemy03,
            "Miniboss": points_Miniboss_hit
        }
        return points_map.get(enemy_type, 50)

def calculate_final_score(self, enemy_type: str, current_level: int, is_kill: bool = True):
        base = self.get_base_points(enemy_type)
        
        if enemy_type == "Miniboss" and is_kill:
            base = points_Miniboss_kill
        multipliers = {
            game_levels.EASY: 1.0,
            game_levels.MODERATE: 1.5,
            game_levels.HARD: 2.0
        }
        
        multiplier = multipliers.get(current_level, 1.0)
        return int(base * multiplier)
