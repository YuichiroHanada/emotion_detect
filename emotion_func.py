import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
import glob
import os
import cv2
import time
import IPython.display as ipd 

import wave     #wavファイルを扱うためのライブラリ
import pyaudio
import librosa 
import librosa.display

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import *
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import backend as K

import efficientnet.tfkeras as efn

# from keras.models import load_model
label_decoder = {0:"angry", 1:"happy", 2:"normal"}

def predict_emotion(model, wav_path):

    signal, sr = librosa.load(wav_path)
       

    x1 = librosa.feature.melspectrogram(y=signal, sr=22050)   
    x2 = librosa.power_to_db(x1, ref=np.max)

    IMG_SIZE = (128,194)

    X = np.zeros(shape=(1, IMG_SIZE[0], IMG_SIZE[1], 3))

    resized = cv2.resize(x2, (IMG_SIZE[1], IMG_SIZE[0]))

    for j in range(3):
        X[0,:,:,j] = resized

    y_test = model.predict(X)
    return label_decoder[np.argmax(y_test)]


def record(FileName, Record_Seconds = 5, save = True):
    """
    録音して、波形表示
    """
    chunk = 1024
    FORMAT = pyaudio.paInt16
    
    CHANNELS = 1 #モノラル
    RATE = 44100 #サンプルレート（録音の音質）
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)
    
    #レコード開始
    print("Recording start...")
    all = []
    for i in range(0, int(RATE / chunk * Record_Seconds)):
        data = stream.read(chunk) #音声を読み取って、
        all.append(data) #データを追加
    
    #レコード終了
    print("Finished Recording.")
    
    stream.close()
    p.terminate()
    
    if(save): #保存するか？
        wavFile = wave.open(FileName, 'wb')
        wavFile.setnchannels(CHANNELS)
        wavFile.setsampwidth(p.get_sample_size(FORMAT))
        wavFile.setframerate(RATE)
        # wavFile.writeframes(b''.join(all)) #Python2 用
        wavFile.writeframes(b"".join(all)) #Python3用
        wavFile.close()
    
def emotion_out(model):
    print("Recording startになったら4秒くらい話してみて！")
    now_time = time.time()
    wav_path = "wav/" + str(now_time) + ".wav"
    record(wav_path)
    emotion = predict_emotion(model, wav_path)

    return emotion

def load_emotionModel():
    model=load_model('audio_emotion_v01.h5')

    return model
    
        
