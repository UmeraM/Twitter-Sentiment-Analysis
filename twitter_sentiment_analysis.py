# -*- coding: utf-8 -*-
"""Twitter_Sentiment_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sySccbIxwdbSXMXWyOd0OqbYaXgEnsT3
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme='monokai', context='notebook', ticks=True , grid=False)

!pip install jupyterthemes

tweets_df=pd.read_csv("/content/train.csv.zip")

tweets_df

tweets_df.info()

tweets_df.describe()

tweets_df['tweet']

tweets_df=tweets_df.drop(['id'], axis=1)

tweets_df

sns.heatmap(tweets_df.isnull(), yticklabels= False, cbar= False,cmap='Blues')

tweets_df.hist(bins=30, figsize=(13,5),color='r')

sns.countplot(tweets_df['label'], label='count')

tweets_df['Length']=tweets_df['tweet'].apply(len)

tweets_df

tweets_df['Length'].plot(bins=100,kind='hist')

tweets_df.describe()

tweets_df[tweets_df['Length']==11]['tweet'].iloc[0]

positive=tweets_df[tweets_df['label']==0]

positive

negative=tweets_df[tweets_df['label']==1]

negative

sentences=tweets_df['tweet'].tolist()

sentences

len(sentences)

sentences_as_one_string=" ".join(sentences)

!pip install wordcloud
from wordcloud import WordCloud

plt.figure(figsize=(20,20))
plt.imshow(WordCloud().generate(sentences_as_one_string))

negative_list=negative['tweet'].tolist()
negative_sentences_as_one_string=" ".join(negative_list)

plt.figure(figsize=(20,20))
plt.imshow(WordCloud().generate(negative_sentences_as_one_string))

import string
string.punctuation

Test='good morning beautiful people :).....I am having fun learning Machine learning and AI!!'

Test_punc_removed=[  char for char in Test if char not in string.punctuation]

Test_punc_removed

Test_punc_removed_join=' '.join(Test_punc_removed)
Test_punc_removed_join

Test_punc_removed=[]
for char in Test:
  if char not in string.punctuation:
    Test_punc_removed.append(char)

Test_punc_removed_join=' '.join(Test_punc_removed)
Test_punc_removed_join

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stopwords.words('english')

Test_punc_removed_join_clean= [ word for word in Test_punc_removed_join.split() if word.lower() not in stopwords.words('english')]

Test_punc_removed_join_clean

Test_punc_removed_join=''.join(Test_punc_removed)
Test_punc_removed_join

mini_challenge='Here is a mini challenge, that will teach you how to remove stopwords and punctations!'

challenge = [char for char in mini_challenge if char not in string.punctuation]
challenge= ''.join(challenge)
challenge=[ word for word in challenge.split() if word.lower() not in stopwords.words('english')]

challenge

from sklearn.feature_extraction.text import CountVectorizer
sample_data=['This is the first paper.','This is the second paper.','This is the third one.','Is this the first paper?']
vectorizer= CountVectorizer()
x= vectorizer.fit_transform(sample_data)

print(vectorizer.get_feature_names())

print(x.toarray())

def message_cleaning(message):
  Test_punc_removed= [char for char in message if char not in string.punctuation]
  Test_punc_removed_join=''.join(Test_punc_removed)
  Test_punc_removed_join_clean=[word for word in Test_punc_removed_join.split() if word.lower() not in stopwords.words('english')]
  return Test_punc_removed_join_clean

tweets_df_clean = tweets_df['tweet'].apply(message_cleaning)

print(tweets_df_clean[5])

print(tweets_df['tweet'][5])

from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer(analyzer=message_cleaning)
tweets_countvectorizer= vectorizer.fit_transform(tweets_df['tweet'])

tweets_countvectorizer.shape

x= tweets_countvectorizer

x.shape

y= tweets_df['label']

from sklearn.model_selection import train_test_split
x_train, x_test ,y_train, y_test = train_test_split(x,y,test_size=0.2 )

from sklearn.naive_bayes import MultinomialNB
NB_classifier = MultinomialNB()
NB_classifier.fit(x_train,y_train)

from sklearn.metrics import classification_report,confusion_matrix

y_predict_test=NB_classifier.predict(x_test)
cm=confusion_matrix(y_test,y_predict_test)
sns.heatmap(cm,annot=True)

print(classification_report(y_test,y_predict_test))

!pip install jupyterthemes

