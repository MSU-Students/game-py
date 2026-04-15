from utils import sleep, goto_xy
from screen import Screen
from player import AirPlane
from pynput import keyboard
class GameAnimation:
    screen: Screen
    mainPlayer: AirPlane
    listener: keyboard.Listener

    