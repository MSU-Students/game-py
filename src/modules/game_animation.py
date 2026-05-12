from src.utils import sleep, goto_xy
from src.core.screen import Screen
from src.components.player import AirPlane
from pynput import keyboard
class GameAnimation:
    screen: Screen
    mainPlayer: AirPlane
    listener: keyboard.Listener

    