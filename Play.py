from gameplay_class import *
from tensorflow.keras.models import load_model
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
from pynput.keyboard import Key, Controller

def get_image_from_filepath(file_path):
    byte_img = tf.io.read_file(file_path)
    img = tf.io.decode_jpeg(byte_img)
    img = tf.image.rgb_to_grayscale(img)
    img = img/255
    img = img[80:][:]
    img = tf.image.resize(img, (235,256))
    return img

def test(model):
    fp = "a06cf698-52b3-11ed-87ac-64bc580216eb.jpg"
    img = get_image_from_filepath(fp)
    plt.figure()
    plt.imshow(img)
    plt.show()
    img = tf.expand_dims(img,0)
    out = round_pred(model(img)[0],0.1)
    command = get_command_from_output(out)
    print(command)
    print(np.array(model(img)[0],dtype='float'))
    quit()



def preprocess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = tf.image.rgb_to_grayscale(img)
    img = img/255
    img = img[80:][:]
    img = tf.image.resize(img, (235,256))
    return img

def round_pred(y, thresh):
    y = np.array(y,dtype='float')
    y[np.where(y>thresh)] = 1
    y = np.array(y, dtype='int')
    return y

def get_command_from_output(y):
    pos = np.array(np.where(y==1))
    command = ''
    for i in pos[0]:
        if pos.size==0: return command
        command += keymap[i]
    return command

keymap = {0:'a',1:'w',2:'d'}

if __name__ == '__main__':
    folder = 'ses-1'
    delay = 5
    model = load_model("E:\Data\documenti\PROGRAMMAZIONE\Game-AI\WOT_drive_assistant.h5")

    # test(model) 
    
    time.sleep(delay)
    print()
    game = GamePlay()
    
    while game.is_active():
        game = GamePlay()

        print("_ _ _")
        frame = game.get_frame()

        fname = os.path.join(folder,str(uuid.uuid1()))
        cv2.imwrite(f'{fname}.jpg',np.array(frame))

        frame = preprocess(frame)
        frame = tf.expand_dims(frame,0)
        out = round_pred(model(frame)[0],0.05)
        
        command = get_command_from_output(out)
        print('pred = ',np.array(model(frame)[0],dtype='float'), end=' ')
        print(command)
        print('\n')

        keyboard = Controller()
        for c in command:
            keyboard.press(c)
        time.sleep(0.5)

        for c in command:
            keyboard.release(c)

        