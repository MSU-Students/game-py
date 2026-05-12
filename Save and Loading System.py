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

    def complete_stage(self, points_earned):
        self.score += points_earned
        self.stage += 1
        print(f"Level Up! {self.name} is now on Stage {self.stage}")
        self.saving_profile()

    @staticmethod
    def select_profile():
        files = [f for f in os.listdir() if f.endswith("_saved.json")]
        if not files:
            print("No profiles found. Create a new one!")
            return None
        print("\n--- Select Your Profile ---")
        for i, filename in enumerate(files):
            display_name = filename.replace("_saved.json", "")
            print(f"{i + 1}. {display_name}")
        
        choice = int(input("Enter number: ")) - 1
        selected_name = files[choice].replace("_saved.json", "")
        return Player.loading_profile(selected_name)
    
    @classmethod
    def loading_profile(cls,name):
        filename = f"{name}_save.json"
        if os.path.exists(filename):
            with open(filename,"r") as f:
                data = json.load(f)
        else:
            print("Save does not exist!")
            return cls(name)

