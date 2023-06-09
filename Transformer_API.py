#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
import logging
import time
import matplotlib.pyplot as plt
import math
import pathlib
import random
import string
import re
import numpy as np
import tensorflow as tf
import nltk
# import jiwer

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import pad_sequences
from tensorflow.keras.layers import Layer, Input, Embedding
from tensorflow import keras
from tensorflow.keras.models import Sequential, Model
from nltk.tokenize import RegexpTokenizer
from tensorflow.keras.layers import MultiHeadAttention, Dense, Dropout, LayerNormalization, GlobalAveragePooling1D
from tensorflow import keras
# from keras_nlp.layers import PositionEmbedding
from tensorflow.keras import layers
from tensorflow.keras.layers import TextVectorization
from sklearn import metrics
from nltk.translate import meteor_score
from nltk.translate.bleu_score import sentence_bleu
# from rouge import Rouge
from sklearn.metrics import f1_score
from tensorflow.keras.models import load_model


# In[2]:


#dataset = pd.read_csv('POC Detect Data Modified - Copy.csv', encoding = "utf_8")

#text_pairs = [] 
#for names in dataset['Combined Names ']:
#    source, target = names.split('\\t')
#    target = "[start] " + target + " [end]"
#    text_pairs.append((source, target))

#Clean sentences
#source = [pair[0] for pair in text_pairs]
#target = [pair[1] for pair in text_pairs]


# In[10]:


class API_Transformer:
    
    
    
    def __init__(self):
        self.transformer = tf.keras.models.load_model('Model')
        dataset = pd.read_csv('POC Detect Data Modified - Copy.csv', encoding = "utf_8")
        text_pairs = [] 
        for names in dataset['Combined Names ']:
            self.source, target = names.split('\\t')
            self.target = "[start] " + target + " [end]"
            text_pairs.append((self.source, self.target))

        #Clean sentences
        self.source = [pair[0] for pair in text_pairs]
        self.target = [pair[1] for pair in text_pairs]
        #self.transformer = tf.keras.models.load_weights("Weights.h5")
        
        
    def decode(self, input_name):
        translated = self.decode_sequence(input_name)
        return translated 
    
    def decode_sequence(self, input_sentence):
        
        ########################################################################################################
        
        #spa_index_lookup
        with open("output.txt", 'r') as file:
            target_index_lookup = file.read()
            
            
        #########################################################################################################
            
        from_disk = pickle.load(open("source_vectorization.pkl", "rb"))

        source_vectorization = TextVectorization(max_tokens=from_disk['config']['max_tokens'],
                                          output_mode='int',
                                          output_sequence_length=from_disk['config']['output_sequence_length'])

        source_vectorization.adapt(self.source)
        source_vectorization.set_weights(from_disk['weights'])
        
        ###########################################################################################################
        
        from_disk = pickle.load(open("target_vectorization.pkl", "rb"))

        target_vectorization = TextVectorization(max_tokens=from_disk['config']['max_tokens'],
                                          output_mode='int',
                                          output_sequence_length=from_disk['config']['output_sequence_length'])

        target_vectorization.adapt(self.target)
        target_vectorization.set_weights(from_disk['weights'])

        ############################################################################################################
            
        max_decoded_sentence_length = 22
        tokenized_input_sentence = source_vectorization([input_sentence])
        decoded_sentence = "start"
        for i in range(max_decoded_sentence_length):
            tokenized_target_sentence = target_vectorization([decoded_sentence])[:, :-1]
            predictions = self.transformer([tokenized_input_sentence, tokenized_target_sentence])
            #sampled_token_index = np.argmax(random.choices(predictions[0, i, :], k=20))
            sampled_token_index = np.argmax(predictions[0, i, :])
            if sampled_token_index !=0 or sampled_token_index !=1 or sampled_token_index !=2 or sampled_token_index !=3:  
                sampled_token = target_index_lookup[sampled_token_index]
                decoded_sentence += " " + sampled_token

            if sampled_token == "end":
                break
        return decoded_sentence


# In[ ]:




