import cv2
import numpy as np
import os, os.path
import inspect
from os.path import isfile, join
from os import listdir

from Multi_Traffic_Scene_Perception.settings import BASE_DIR
from user.models import Upload_Model


def is_similar(image1, image2):
    return image1.shape == image2.shape and not(np.bitwise_xor(image1,image2).any())

def comp(test):
    id=0
    '''path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/currencies'
    num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
    for i in range(1,num_files+1):
        print(i)
    onlyfiles = os.listdir('currencies')'''
    for o in Upload_Model.objects.all():
        '''print(o)
        img = cv2.imread('currencies/'+o)
        cv2.imshow('ImageWindow', img)
        cv2.waitKey()'''
        pat=os.path.join(BASE_DIR, 'assets'+o.images.url)
        if is_similar(cv2.imread(test),cv2.imread(pat)):
            #img = cv2.imread(o.imagesCurrency.url)
            #cv2.imshow('ImageWindow', img)
            #cv2.waitKey()
            id=o.id
            break
    return id

#print(is_similar(cv2.imread('dd.png'),cv2.imread('dd1.png')))