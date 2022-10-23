import cv2
import numpy as np
import os
from PIL import Image
import uuid
import cv2

"""
augment 'a' and 'd' keys by flipping the pictures. The script also generates new labels 
which reflects the rotation
WANT_TO_AUGMENT = True --> performs augmentation
DELETE EMPTY = True --> delete empty labels if needed

"""
# edit the path to a folder
PATH = 'ses-1'

# flip a frame, mirror the label and save both with a new unique ID
def flip(filename):
    
    txt = open(os.path.join(base_path,fn),'r').read()
    pic = Image.open(os.path.join(base_path, filename[:len(filename)-3]+'jpg'))
    
    # augment pic
    new_fn = os.path.join(base_path, f'{uuid.uuid1()}')
    augmented_pic = pic.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

    # augment text
    if 'a' in txt:
        augmented_lbl = txt.replace('a','d')
    elif 'd' in txt:
        augmented_lbl = txt.replace('d','a')
    else:
        return 

    # save
    augmented_pic.save(f'{new_fn}.jpg')
    new_txt = open(f'{new_fn}.txt', 'w').write(augmented_lbl)

if __name__ == '__main__':
    WANT_TO_AUGMENT = True
    DELETE_EMPTY = False
    
    base_path = os.path.join(PATH)

    if WANT_TO_AUGMENT:
        augmented =0
        file_list = []
        print('pre-augmentation')
        for fn in os.listdir(base_path):
            if fn.endswith('txt'):
                file_list.append(fn)

        # examinate 
        counter = [0,0,0,0]
        for fn in file_list:
            txt = open(os.path.join(base_path,fn),'r').read()
            if 'w' in txt: counter[0]+=1
            if 'a' in txt: counter[1]+=1
            if 'd' in txt: counter[2]+=1
            if len(txt)==0: counter[3]+=1
        print(counter)

        # augment
        for fn in file_list:
            txt = open(os.path.join(base_path,fn),'r').read()
            if 'd' or 'a' in txt:
                augmented +=1
                flip(fn)

        print('post-augmentation')
        file_list = []
        for fn in os.listdir(base_path):
            if fn.endswith('txt'):
                file_list.append(fn)

        # examinate 
        counter = [0,0,0,0]
        for fn in file_list:
            txt = open(os.path.join(base_path,fn),'r').read()
            if 'w' in txt: counter[0]+=1
            if 'a' in txt: counter[1]+=1
            if 'd' in txt: counter[2]+=1
            if len(txt)==0: counter[3]+=1
        print(counter)

    if DELETE_EMPTY:
        deleted =0
        file_list = []
        print('pre-augmentation')
        for fn in os.listdir(base_path):
            if fn.endswith('txt'):
                file_list.append(fn)

        # examinate 
        counter = [0,0,0,0]
        for fn in file_list:
            txt = open(os.path.join(base_path,fn),'r').read()
            if 'w' in txt: counter[0]+=1
            if 'a' in txt: counter[1]+=1
            if 'd' in txt: counter[2]+=1
            if len(txt)==0: counter[3]+=1
        print(counter)

        # delete 
        for fn in file_list:
            txt = open(os.path.join(base_path,fn),'r').read()
            if len(txt)==0: 
                deleted +=1
                jpgname = fn[:len(fn)-3]+'jpg'
                os.remove(os.path.join(base_path,fn))
                os.remove(os.path.join(base_path,jpgname))
        
        file_list = []
        print('post-augmentation')
        for fn in os.listdir(base_path):
            if fn.endswith('txt'):
                file_list.append(fn)

        # examinate again
        counter = [0,0,0,0]
        for fn in file_list:
            txt = open(os.path.join(base_path,fn),'r').read()
            if 'w' in txt: counter[0]+=1
            if 'a' in txt: counter[1]+=1
            if 'd' in txt: counter[2]+=1
            if len(txt)==0: counter[3]+=1
        print('deleted: ',deleted)
        print(counter)