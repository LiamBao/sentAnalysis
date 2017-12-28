# -*- coding: utf-8 -*-
#author="liam_bao@163.com"


import jieba
from gensim import corpora
from collections import defaultdict
from helper import getExcel
class Analysis(object):

    def __init__(self, posdict='./dict/emotion_dict/pos_all_dict.txt',
                       negdict='./dict/emotion_dict/neg_all_dict.txt',
                       mostdict='./dict/degree_dict/most.txt',
                       verydict='./dict/degree_dict/very.txt',
                       moredict='./dict/degree_dict/more.txt',
                       ishdict='./dict/degree_dict/ish.txt',
                       insufficientdict='./dict/degree_dict/insufficiently.txt',
                       inversedict='./dict/degree_dict/inverse.txt'):
        # 情感词典
        self.posdict=posdict
        self.negdict=negdict
        # 程度副词词典
        self.mostdict=mostdict   # 权值为2
        self.verydict=verydict   # 权值为1.5
        self.moredict=moredict # 权值为1.25
        self.ishdict=ishdict   # 权值为0.5
        self.insufficientdict=insufficientdict  # 权值为0.25
        self.inversedict=inversedict  # 权值为-1

        #用户词典
        self.userdict= './dict/userdict.txt'
        self.stopwords='./dict/stopwords.txt'

    def preteat_clause(self, phase):
        #分句
        cut_list=list('。！~？!?…')
        reslist,i,start=[],0,0
        for word in phase:
            if word in cut_list:
                reslist.append(phase[start:i])
                start = i+1
                i += 1
            else:
                i += 1

        if start < len(phase):
            reslist.append(phase[start:])

        return reslist

    def cutwords_jieba(self, sentence):
        stropw = []
        userdict=self.userdict
        stopwords=self.stopwords
        if userdict:
            jieba.load_userdict(userdict)
            stropw = [line.strip() for line in open(stopwords,'r',encoding='utf-8').readlines()]

        frequency = defaultdict(int)
        l = list(jieba.cut(sentence))
        for t in l:
            frequency[t] += 1

        texts = [token for token in frequency if frequency[token] > 0]

        rtexts = list(set(texts)-set(stropw))
        return rtexts

    def deal_wrap(self,filedict):
        temp = []
        for x in open(filedict,'r',encoding='utf-8').readlines():
            temp.append(x.strip())
        return temp

    def cal_score(self,word, sentence_score):
        if word in self.mostdict:
            sentence_score *= 2.0
        elif word in self.verydict:
            sentence_score *= 1.75
        elif word in self.moredict:
            sentence_score *= 1.5
        elif word in self.ishdict:
            sentence_score *= 1.2
        elif word in self.insufficientdict:
            sentence_score *= 0.5
        elif word in self.inversedict:
            sentence_score *= -1
        return sentence_score

    def sentiment(self, sentence):
        i,s,posscore,negscore=0, 0, 0, 0
        for word in sentence:
            if word in self.posdict:
                posscore += 1 
                for w in sentence[s:i]:
                    posscore = self.cal_score(w, posscore)
                s = i + 1 

            elif word in self.negdict: 
                negscore += 1
                for w in sentence[s:i]:
                    negscore = self.cal_score(w, negscore)
                s = i + 1
            i+=1

        return posscore,negscore


if __name__ == "__main__":

    print("plz Make sure the data files *(dict/source)* is placed correctly")
    try:
        app = Analysis()
        total_pscore,total_nscore, item= 0, 0, []

        for tempstr in app.deal_wrap('./source/data.txt'):
            sentence_pscore, sentence_nscore = 0, 0
            for x in app.preteat_clause(tempstr):
                c = app.cutwords_jieba(sentence=x)
                posscore, negscore = app.sentiment(c)
                sentence_pscore += posscore
                sentence_nscore += negscore

            total_pscore += sentence_pscore
            total_nscore += sentence_nscore
            print('单句：{}得分：Positive score:{};Nagtive score:{};totalscore:{}'.
                    format(''.join(list(tempstr)[0:25])+'....',
                           sentence_pscore,
                           sentence_nscore,
                           sentence_pscore-sentence_nscore))
            item.append([(tempstr), sentence_pscore, sentence_nscore, sentence_pscore-sentence_nscore])
        item.append(['', '', '', ''])
        item.append(["whole article", "Positive score", "Nagtive score", "total score"])
        item.append(['', total_pscore, total_nscore, total_pscore-total_nscore])
        title=["sentence", "Positive score", "Nagtive score", "total score"]
        getExcel('data', title, item)
    except Exception as err:
        print(err)
    finally:
        input("Press any key to exit")
