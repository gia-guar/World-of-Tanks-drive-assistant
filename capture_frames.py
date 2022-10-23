from gameplay_class import *
import time

"""
*** CAPTURE_FRAMES.PY: ***

Collect screenshot in an area which is by default area=(1420, 500,500, 550) 
see gameplay_class 

gameplay_class.GamePlay.collect_gameplay(destination, flag):
destination: str, 
    explicit the folder to save the data into

flag: Boolean, allow control over 'w' and empty commands collection to avoid 
    overcollection of frequent classes;

- save the screenshots as .jpg to a destination folder with a unique ID name
- save the combo of keys pressed at the same time of the collected frame 
as .txt with to a destination folder with the same ID name of the folder

gameplay_class.GamePlay.report(): 
    print out the number N of frames collected (2*N = total files, txt+jpg)

gameplay_class.collected_item_so_far(folder):
    print out the number of 'w''a''s''empty' commands present in all .txt files in a folder

"""
if __name__ == '__main__':
    folder = 'ses-1'
    collect_all = True
    game = GamePlay()
    time.sleep(5)

    while game.is_active():
        time.sleep(0.5)
        print("_ _ _")
        game.collect_gameplay(folder,collect_all)
    
    # print out info
    game.Report()
    collected_item_so_far(folder)