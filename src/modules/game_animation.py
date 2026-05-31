from src.utils import sleep, goto_xy
from src.core.screen import Screen
from src.components.player import AirPlane
from pynput import keyboard
from src.components.explosion import Explosion
class GameAnimation:
    screen: Screen
    mainPlayer: AirPlane
    listener: keyboard.Listener

    Explosion = []

    