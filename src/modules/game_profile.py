from pynput import keyboard

from src.core.screen import Screen
from src.components.player import AirPlane

class GameProfile:
    screen: Screen
    mainPlayer: AirPlane
    listener: keyboard.Listener

