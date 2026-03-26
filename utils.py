import os

# Function to clear the console screen
def clear_console():
    if os.name == 'nt':  # for Windows
        os.system('cls')

def goto_xy(position):
    print(f"\x1B[{position[1]};{position[0]}f", end='')