#必要なモジュールをインポート
import re
import os
import time
import sys
import numpy as np
from gensim.models.word2vec import Word2Vec
import json,codecs
import datetime
import pandas as pd
import docx
import glob
import model_scdv

def Date2Str(date):
    date_str = ['/'.join([str(i.month),str(i.day)])+' '+':'.join([str(i.hour),str(i.minute).zfill(2)]) for i in date]
    return date_str

if __name__ == '__main__':
    
    args = sys.argv
    dir_name = args[1]
    th = args[2]
    
    path = glob.glob('./'+dir_name+'/*.docx')
    number = [i.strip('./'+dir_name+'\\') for i in path]
    number = ['0'+i.strip('.docx') for i in number]

    #ストップワードリストをstopwords.txtから参照
    if(os.path.exists('stopwords.txt')):
        stopwords = np.loadtxt('stopwords.txt',dtype=np.str)
        print('Detect stopwords.txt')
    else:
        stopwords = []
        print('stopwords.txt not found')

    print('Loading .docx documents ...')
    data = []
    modified = []
    created = []
    author = []
    for p,n in zip(path,number):
        
        txt = []
        doc = docx.Document(p)
        meta = doc.core_properties
        modified.append(meta.modified)
        created.append(meta.created)
        author.append(str(meta.author))

        # ワードから文書を取得
        for par in doc.paragraphs:
            t = par.text
            t = t.replace('\u3000','')
            for s in stopwords:
                t = t.replace(s,'')
            t = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,t)
            t = t.split('。')
            txt.extend(t)
            
        txt = [i for i in txt if len(i) >= 20]
        data.append(txt)
    
    modified_str = Date2Str(modified)
    created_str = Date2Str(created)

    #文章番号(number_list)とそれぞれの文(docs), 語彙(word)のリストの作製
    print('Preprocessing ...')
    docs, number_list, words = model_scdv.Preprocess_Mecab(number, data)

    #Word2Vecモデルの学習
    path = glob.glob('./model/*.model')
    if(len(path) == 0):

        path = glob.glob('./pretrained_model/*.model')
        print('Loading pre-trained W2V model ('+str(path[0])+')...')

        model = Word2Vec.load(path[0])
        print('Updating specified word vectors by Word2Vec...')
        model.train(sentences=docs,total_examples=len(docs),
                    total_words=len(words),
                    word_count= len(model.wv.index2word),
                    epochs=1000)

        model.save("./model/"+dir_name+"_model.model")

    else:
        path = glob.glob('./model/*.model')
        print('Loading W2V model ('+str(path[0])+')...')
        model = Word2Vec.load(path[0])

    #W2Vモデルから必要な単語ベクトルを取得
    word_vectors = [model.wv[i] for i in model.wv.vocab if i in words]
    word_vectors = np.array(word_vectors)

    #SCDVを用いてクラスタリング＋スパース化
    doc_vectors_sparse = model_scdv.Postprocess_SCDV(word_vectors, docs, words)

    #類似文章ネットワークの作製
    network_csv, dic_json = model_scdv.Calculate_Network(th, doc_vectors_sparse, number, number_list, docs, created_str, modified_str, author)

    #ネットワークを保存
    print('Save Network...')    
    df = pd.DataFrame(network_csv, columns=['Num','Target','Num','Text','Similarity'],index=None)
    df.to_csv('result_(sim='+str(th)+').csv',encoding='utf_8_sig')
    with codecs.open('./network_(sim='+str(th)+').json', 'w' , encoding='utf-8') as f:
        json.dump(dic_json, f, indent = 4, ensure_ascii=False)

    print('Complete!!!!')

