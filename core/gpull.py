import os
from time import sleep

def gpull():
    os.system("git pull")
    sleep(3)
    print("Pull done!")
    
def start_setup():
    os.system("python3 setup.py")
    
if __name__ == "__main__":
    gpull()
    start_setup() 
