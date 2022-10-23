from mss import mss
import cv2
import numpy as np
import uuid
import os
from pynput.keyboard import Key, Listener, KeyCode

def get_values(list, indeces):
    temp =[]
    for i in indeces: 
        temp.append(list[i])
    return temp

def collected_item_so_far(PATH):
    # COUNT 'W''A''S' and Empty commands 
    labels = []
    for fn in os.listdir(os.path.join(PATH)):
        if fn.endswith('txt'):
            labels.append(fn)

    counter = [0,0,0,0]
    for fn in labels:
        txt = open(os.path.join(PATH,fn),'r').read()
        if 'w' in txt: counter[0]+=1
        if 'a' in txt: counter[1]+=1
        if 'd' in txt: counter[2]+=1
        if len(txt)==0: counter[3]+=1
    
    print('w keys: ',counter[0])
    print("a keys: ",counter[1])
    print("d keys: ",counter[2])
    print("empty: ", counter[3])

class GamePlay():
    #set up game area
    def __init__(self, area=(1920-500, 500,500, 550) ):
        self.game_area = {"left":area[0], "top":area[1], "width":area[2], "height":area[3]}
        self.capture =  mss()
        self.current_keys = None
        self.status = True
        self.Nframes = 0
        self.current_command = {'Key.space':False}

    # return frames only
    def get_frame(self):
        gamecap = np.array(self.capture.grab(self.game_area))
        listener = Listener(on_press=self.on_keypress, on_release = self.on_keyrelease)
        listener.start()
        
        return gamecap
    
    # return keys being pressed
    def log(self):
        # print( self.current_command)
        labels = list(self.current_command.keys())
        vals = np.array(list(self.current_command.values()))     
        idx = np.where(vals == 1)[0]
        key_frames= get_values(labels,idx)
        print(key_frames)
        return key_frames

    def is_active(self):
        return self.status

    # print out number of collected frames
    def Report(self):
        print('frames collected: ',self.Nframes)
    
    # Listener method - on_keypress
    def on_keypress(self, key):
        self.current_command[key] = True
        
        if self.current_keys == key:
            #print(self.current_keys)
            return self.current_keys
        else:
            #print(self.current_keys)
            self.current_keys = key
            return self.current_keys
    
    # Listener method - on_keyrelease
    def on_keyrelease(self,key):
        if key == Key.esc:
            self.status = False
            return False
        self.current_command[key] = False
        self.current_keys = None

    # collect and save typed keys and associated frame
    def collect_gameplay(self,folder,collect_all=False):
        # make folder if not existing
        if not os.path.isdir(folder):
            os.mkdir(folder)
        
        # collect frame
        fname = os.path.join(folder,str(uuid.uuid1()))
        gamecap = np.array(self.capture.grab(self.game_area))

        # collect keystrokes
        listener = Listener(on_press=self.on_keypress, on_release = self.on_keyrelease)
        listener.start() 

        # save
        # collect_all = False: not saving 'w' key to have balance between keys, unless some ohter key is pressed too; 
        if collect_all:
            self.Nframes = self.Nframes+1
            cv2.imwrite(f'{fname}.jpg',gamecap)
            np.savetxt(f'{fname}.txt',np.array(self.log()), fmt = '%s')
        else:
            try:
                if len(np.array(self.log()))>=2:
                    self.Nframes = self.Nframes+1
                    cv2.imwrite(f'{fname}.jpg',gamecap)
                    np.savetxt(f'{fname}.txt',np.array(self.log()), fmt = '%s')
                elif len(np.array(self.log()))==0:
                    pass
                elif not np.array(self.log())[0]==KeyCode.from_char('w'):
                    self.Nframes = self.Nframes+1
                    cv2.imwrite(f'{fname}.jpg',gamecap)
                    np.savetxt(f'{fname}.txt',np.array(self.log()), fmt = '%s')
            except:
                self.Nframes = self.Nframes+1
                cv2.imwrite(f'{fname}.jpg',gamecap)
                np.savetxt(f'{fname}.txt',np.array(self.log()), fmt = '%s')
