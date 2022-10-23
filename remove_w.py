import os
PATH = 'ses-1'
N_TO_DELETE = 100

deleted =0
base_path = os.path.join(PATH)
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
    if txt=="'w'\n": 
        deleted +=1
        jpgname = fn[:len(fn)-3]+'jpg'
        os.remove(os.path.join(base_path,fn))
        os.remove(os.path.join(base_path,jpgname))
    
    if deleted == N_TO_DELETE:
        break

file_list = []
print('\npost-augmentation')
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
print('deleted: ',deleted)
print(counter)