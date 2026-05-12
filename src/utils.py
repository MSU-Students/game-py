import os
import time

# Function to clear the console screen
def clear_console():
    if os.name == 'nt':  # for Windows
        os.system('cls')

def goto_xy(position):
    print(f"\x1B[{position[1]};{position[0]}f", end='')

def sleep(delay = 1):
    time.sleep(delay)


class TimeClass:
    beginningTime = time.time()
    startTime: float
    currentTIme: float
    targetTime: float
    startTimerCalling: bool = False
    def __init__(self):
        self.beginningTime = time.time() # The starting time
        self.startTime: float # Is the time when the startTimer() is called
        self.currentTime: float # The current time
        self.targetTime: float # Is the time when the startTimer() is called plus the cooldown time
        self.startTimerCalling: bool = False # Only set to true if the startTimer() isn't done yet

    # Returns how long the program is currently running
    def timeCheck(self):
        self.currentTime = time.time() - self.beginningTime
        return self.currentTime
    
    # Starts timer until it reaches the cooldown time
    def startTimer(self, cooldown: float): 
        if self.startTimerCalling==False:
            self.startTime = self.currentTime
            self.targetTime = self.startTime + cooldown
            self.startTimerCalling = True
    
    # Returns true if the targetTime less than the currentTime
    def timerFinished(self):
        if self.currentTime >= self.targetTime:
            self.startTimerCalling = False
            return True
        else:
            return False
        



