import json
import os
from pynput import keyboard

from src.core.screen import Screen
from src.components.player import AirPlane

class GameProfile:
    screen: Screen
    mainPlayer: AirPlane
    listener: keyboard.Listener

def __init__(self):
        self.save_folder = "./save_data"

def get_save_path(self, player_name: str):
    if not os.path.exists(self.save_folder):
        os.makedirs(self.save_folder)
    return os.path.join(self.save_folder, f"{player_name}.json")

def save_profile(self, player_name: str, current_wave: int, current_life: int, 
                kill_count: int, difficulty: int):
    save_data = {
        "player_name": player_name,
        "current_wave": current_wave,
        "current_life": current_life,
        "kill_count": kill_count,
        "difficulty": difficulty
    }
    
    save_path = self.get_save_path(player_name)
    
    try:
        with open(save_path, "w") as f:
            json.dump(save_data, f, indent=4)
        print(f"\n✓ Game saved for {player_name}!")
        return True
    except Exception as e:
        print(f"\n✗ Error saving game: {e}")
        return False

def load_profile(self, player_name: str):
    save_path = self.get_save_path(player_name)
    
    if not os.path.exists(save_path):
        return None
    
    try:
        with open(save_path, "r") as f:
            save_data = json.load(f)
        return save_data
    except Exception as e:
        print(f"\n✗ Error loading game: {e}")
        return None

def has_existing_profile(self, player_name: str):
    save_path = self.get_save_path(player_name)
    return os.path.exists(save_path)

def delete_profile(self, player_name: str):
    save_path = self.get_save_path(player_name)
    if os.path.exists(save_path):
        try:
            os.remove(save_path)
            print(f"\n✓ Profile deleted for {player_name}")
            return True
        except Exception as e:
            print(f"\n✗ Error deleting profile: {e}")
            return False
    return False
