#asset_manager.py


#this disctionary maps a name to file path, so we can load the file when needed
class AssetManager:
    def __init__(self):
        self.assets = {
            "enemy1": "animations/enemy01.txt",
            "enemy2": "animations/enemy02.txt",
            "enemy3": "animations/enemy03.txt",
            "miniboss": "animations/miniboss.txt"
        }
