import numpy as np
import pandas as pd
import pickle
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from sklearn.preprocessing import LabelEncoder




class API_RNN:
    def __init__(self):
        self.enc_dec_model = tf.keras.models.load_model("promising.h5")
        

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
        data = pd.read_csv('Regional analysis new.csv')
        blacklisted_names = data['Blacklisted Name'].values
        results=[]
        label_encoder = LabelEncoder()
        label_encoder.fit_transform(blacklisted_names)
        with open('target_text_tokenizer_rnn.pkl', 'rb') as file:
            target_text_tokenizer = pickle.load(file)
            
        for i in df:

            source_text_tokenized, source_text_tokenizer = self.tokenize(df[i])
            source_pad_sentence = pad_sequences(source_text_tokenized, maxlen=68)
            # source_pad_sentence = source_pad_sentence.reshape(*source_pad_sentence.shape, 1)
            print("The input sentence is: {}".format(df[i][0]))
            print('The predicted sentence is :')
            predictions = self.enc_dec_model.predict(source_pad_sentence)
            predicted_labels = label_encoder.inverse_transform(predictions.argmax(axis=1))

            for sequence, predicted_label in zip(source_text_tokenized, predicted_labels):
                results.append(predicted_label)

            print(results)
            return results
