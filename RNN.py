import string
import numpy as np
import pandas as pd
import random
import nltk
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import Model
from keras.layers import LSTM, Input, TimeDistributed, Dense, Activation, RepeatVector, Embedding
from keras.optimizers import Adam
from keras.losses import sparse_categorical_crossentropy
from sklearn.model_selection import train_test_split
from nltk.translate.bleu_score import sentence_bleu
import pickle
import tensorflow as tf

class API_RNN:
    def __init__(self):
        self.enc_dec_model = tf.keras.models.load_model("deployment.h5")
        

    def logits_to_sentence(self, logits, tokenizer):
        index_to_words =  {idx: word for word, idx in tokenizer.word_index.items()}
        my_dict = index_to_words
        index_to_words[0] = '' 
        return ' '.join([index_to_words[prediction] for prediction in np.argmax(logits, 1)])
        
        
    def tokenize(self, df):
        text_tokenizer = Tokenizer()
        text_tokenizer.fit_on_texts(df)
        return text_tokenizer.texts_to_sequences(df), text_tokenizer
    
    
    def call(self, df):
        
        with open('target_text_tokenizer_rnn.pkl', 'rb') as file:
            target_text_tokenizer = pickle.load(file)
            
        for i in df:
            source_text_tokenized, source_text_tokenizer = self.tokenize(df[i])
            source_pad_sentence = pad_sequences(source_text_tokenized, 12, padding = "post")
            source_pad_sentence = source_pad_sentence.reshape(*source_pad_sentence.shape, 1)
            print("The input sentence is: {}".format(df[i][0]))
            print('The predicted sentence is :')
            rst = self.logits_to_sentence(self.enc_dec_model.predict(source_pad_sentence[i:i+1])[0], target_text_tokenizer)
            print(rst)
            return rst
            # print(self.logits_to_sentence(self.enc_dec_model.predict(source_pad_sentence[i:i+1])[0], target_text_tokenizer))
            # return self.logits_to_sentence(self.enc_dec_model.predict(source_pad_sentence[i:i+1])[0], target_text_tokenizer)