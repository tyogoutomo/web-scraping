import sys, os, json, time, argparse, cv2, imutils
import tensorflow as tf
from mtcnn.mtcnn import MTCNN
from tqdm import tqdm
from datetime import datetime

detector = MTCNN(min_face_size=100)

def mtcnnCropper(
    keyword_path, filename,
    margin=60, rmv_srcimg=True):
    # print("cropping in folder", keyword_path)
    
    image_path = os.path.join(keyword_path, filename)
    
    try:
        image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        if rmv_srcimg:
            os.remove(image_path)
    except:
        print('[Warning!]:{} image reading process not successful!'.format(image_path))
        return
    
    results = detector.detect_faces(image)
    
    iterator = 1
    for result in results:
        bbox = result['box']
        up = bbox[0]-margin if bbox[0]-margin>0 else 0
        down = bbox[0]+bbox[2]+margin if bbox[0]+bbox[2]+margin<image.shape[1] else image.shape[1]
        left = bbox[1]-margin if bbox[1]-margin>0 else 0
        right = bbox[1]+bbox[3]+margin if bbox[1]+bbox[3]+margin<image.shape[0] else image.shape[0]

        img_width = right - left
        img_height = down - up

        try:
            cropped_img = image[left:right, up:down]
        except:
            print('[Warning!]:{} crop process not successful!'.format(image_path))
            continue

        if (img_width < 300) or (img_height < 300):
            cropped_img = imutils.resize(cropped_img,width=512)

        now = datetime.now()
        timestamp = datetime.timestamp(now)

        img_name = os.path.join(keyword_path, filename[:-4] + '_' + str(timestamp) + '.jpg')
        iterator += 1

        try:
            cv2.imwrite(img_name, cv2.cvtColor(cropped_img, cv2.COLOR_RGB2BGR))
        except:
            print()
            print('[Warning!]:{} save process not successful!'.format(img_name))
            continue