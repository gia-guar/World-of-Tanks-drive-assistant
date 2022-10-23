# DS BALANCER
import os
import numpy as np


PATH = 'ses-1'
DELETE_EMPTY = True

def get_files(path, verbose=True, return_counter=False):
    # 1.1 target .txt files
    file_list = []
    for fn in os.listdir(os.path.join(PATH)):
        if fn.endswith('txt'):
            file_list.append(fn)

    # 1.2 examinate 
    counter = [0,0,0,0]
    for fn in file_list:
        txt = open(os.path.join(PATH,fn),'r').read()
        if 'w' in txt: counter[0]+=1
        if 'a' in txt: counter[1]+=1
        if 'd' in txt: counter[2]+=1
        if len(txt)==0: counter[3]+=1
    
    # print out results
    if verbose:
        print(counter)

    if return_counter:
        return (file_list,counter)
    else:
        return file_list

if __name__=='__main__':
    # 1.EVALUATE and get file list
    print('original keys collected: ', end='')
    f_list = get_files(PATH,verbose=True)

    # 2. delete extra:
    eliminated = 0

    # 2.1 delete Key.esc and ctrl
    for fn in f_list:
            txt = open(os.path.join(PATH,fn),'r').read()

            if 'Key.esc' in txt or 'Key.ctrl_l' in txt: 
                eliminated+=1
                os.remove(os.path.join(PATH,fn))
                os.remove(os.path.join(PATH,fn[:len(fn)-3]+'jpg'))

    # update list files
    f_list = get_files(PATH, verbose=False)

    # 2.2 delete empty files
    if DELETE_EMPTY:
        # remove 1
        for fn in f_list:
            txt = open(os.path.join(PATH,fn),'r').read()

            if len(txt)==0:
                jpgname = fn[:len(fn)-3]+'jpg'
                # print(jpgname)
                os.remove(os.path.join(PATH,fn))
                os.remove(os.path.join(PATH,jpgname))
                eliminated+=1

        # update list files
        print('   final keys collected: ', end='')
        labels = get_files(PATH,verbose=True)

    print(f'\nnumber of (frame,label) pairs deleded {eliminated}\n')