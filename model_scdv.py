#必要なモジュールをインポート
import re
import os
import numpy as np
import MeCab
import collections
from gensim.models.word2vec import Word2Vec
from sklearn.mixture import GaussianMixture

def DeleteNewline(strings):
    strings = strings.replace('&nbsp', '')
    strings = strings.replace('\n','')
    strings = strings.replace('\t','')
    strings = strings.replace('\r','')
    px = re.compile(r"<[^>]*?>")
    strings = px.sub("",strings)
    return strings

def CalcSim(target, params):
    similarity = []
    for i in params:
        param = i
        s = np.dot(target, param)/(np.linalg.norm(target)*np.linalg.norm(param))
        similarity.append(s)

    return similarity

def Preprocess_Mecab(number, data):
    number_list = []
    data_flat = []
    for n,d in zip(number,data):
        for i in range(len(d)):
            number_list.append(n)
        data_flat.extend(d)

    docs = []
    m = MeCab.Tagger ("-Owakati")
    for d in data_flat:
        tagged = DeleteNewline(m.parse(d))
        docs.append(tagged.split(' '))

    words = []
    for i in docs:
        words.extend(i)
    counts = collections.Counter(words)
    words = [i for i in list(counts.keys()) if counts[i] >= 5]

    return(docs, number_list, words)

def Postprocess_SCDV(word_vectors, docs, words):

    words = np.array(words)
    word_idf = np.zeros_like(words, dtype=np.uint32)

    for doc in docs:
        lim = len(doc)
        for w in doc:
            if(lim == 0):
                break
            else:
                idx = np.where(w == words)
                word_idf[idx] += 1
                lim -= 1
                
    word_idf = 1 + np.log(len(docs) / (word_idf))

    num_clusters = 60
    clf =  GaussianMixture(n_components=num_clusters,covariance_type="full")
    z_gmm = clf.fit(word_vectors)
    idx = clf.predict(word_vectors)
    idx_proba = clf.predict_proba(word_vectors)

    gmm_word_vectors = np.empty((word_vectors.shape[0], word_vectors.shape[1] * num_clusters))
    n = 0
    for vector,proba,idf in zip(word_vectors,idx_proba,word_idf):
        for m,p in enumerate(proba):
            if(m == 0):
                cluster_vector = vector * p
            else:
                cluster_vector = np.hstack((cluster_vector,vector * p))
        gmm_word_vectors[n] = idf * cluster_vector
        n += 1

    doc_vectors = []
    min_ = 0
    max_ = 0

    for doc in docs:
        
        vector = np.zeros_like(gmm_word_vectors[0])

        for word in doc:
            try:
                idx = np.where(word == words)[0][0]
                vector += gmm_word_vectors[idx]
            except:
                pass

        vector = vector/(np.linalg.norm(vector)+1e-9)
        min_ += np.min(vector)
        max_ += np.max(vector)
        doc_vectors.append(vector)

    doc_vectors = np.array(doc_vectors)

    min_ = min_/doc_vectors.shape[0]
    max_ = max_/doc_vectors.shape[0]

    doc_vectors_sparse = []
    for vec in doc_vectors:
        t = (1/100) * (abs(min_)+abs(max_))/2
        vec_sparse = np.where(abs(vec) > t, vec, 0)
        doc_vectors_sparse.append(vec_sparse)
    doc_vectors_sparse = np.array(doc_vectors_sparse)

    return(doc_vectors_sparse)

def Calculate_Network(th, doc_vectors_sparse, number, number_list, docs, created, modified, author):

    sim_pairs = []
    network = []
    weight = np.zeros_like(number,dtype=np.float32)
    for i in range(doc_vectors_sparse.shape[0]):
        similarity = CalcSim(doc_vectors_sparse[i], doc_vectors_sparse)
        similarity = np.array(similarity)
        idx = np.where(similarity > float(th))
        sim_th = similarity[idx]
        num = np.array(number_list)[idx]
        for s,n,d in zip(sim_th,num,idx[0]):
            if(number.index(number_list[i]) != number.index(n)):
                network.append([number.index(number_list[i]),number.index(n)])
                sim_pairs.append([str(number_list[i]),''.join(docs[int(i)]), str(number_list[d]),''.join(docs[int(d)]), s])
                weight[number.index(number_list[i])] += 1 * s
    
    network = np.array(network)
    hoge = np.array(sim_pairs)[:,4].astype(np.float32)
    idx_sim = np.argsort(hoge)[-1::-1]
    sim_pairs_sort = np.array(sim_pairs)[idx_sim]
    network_csv = []
    dic_json = {'elements': {'nodes': [], 'edges': []}}

    for n,w in zip(number, weight):
        dic_json['elements']['nodes'].append({'data': {'id': str(number.index(n)), 'id_num': n, 'author': author[int(number.index(n))], \
            'created': created[int(number.index(n))],'last_modified': modified[int(number.index(n))],'weight': float(w)}})

    for n, (i,g) in enumerate(zip(sim_pairs_sort, network[idx_sim])):
        if(n%2 == 0):
            network_csv.append(list(i))
            dic_json['elements']['edges'].append({'data': {'source': str(g[0]),'source_num': number[g[0]], 'source_txt': i[1].replace('\u3099',''),\
                'target': str(g[1]), 'target_num': number[g[1]],'target_txt': i[3].replace('\u3099',''),'value': float(i[4])}})
        # dic_json['links'].append({'data': {'source': number[g[0]],'target': number[g[1]],'value': float(i[4])}})
    
    return(network_csv, dic_json)