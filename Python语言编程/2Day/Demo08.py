import jieba,wordcloud
text="我去清华图书馆看书"
wordA=jieba.lcut(text,cut_all=True)
wordB=jieba.lcut(text)
print(wordA,"\n",wordB)

