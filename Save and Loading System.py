import json
import os

class Player :
    def __init__(self,name,stage=1,score=0):
        self.name = name
        self.stage = stage
        self.score = score

    def to_dict(self):
        return{ "name":self.name, "stage":self.stage, "score":self.score }

    def saving_profile(self):
        filename= f"{self.name}_saved.json"
        with open(filename,"w") as f:
            json.dump(self.to_dict(),f, indent=4)
        print(f"Game save for {self.name}!")

    @classmethod
    def loading_profile(cls,name):
        filename = f"{name}_save.json"
        if os.path.exists(filename):
            with open(filename,"r") as f:
                data = json.load(f)
        else:
            print("Save does not exist!")
            return cls(name)

