# -*- coding: utf-8 -*-
# This code is used to classify whether a email is spam or not

import os
from collections import Counter
import numpy as np
from sklearn.metrics import confusion_matrix

from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC

import matplotlib.pyplot as plt

def make_Dictionary(train_dir):
    emails=[os.path.join(train_dir,textFileName) for textFileName in os.listdir(train_dir)]
    all_words=[]
    for mail in emails:
        with open(mail) as m: # opening the file 
            for i,line in enumerate(m):
                if i==2: #Body of email is only 3rd line of text file
                    words=line.split()
                    all_words+=words
    
    print(all_words)
    dictionary=Counter(all_words) # Counter is used to calculate occurences of a list item
    print(dictionary)
    
    # dictionary keys contain the word and value contain the occurences of a list item
    # Removing the non-word from all_words array means which are not useful
#    list_to_remove=dictionary.keys()
    print(dictionary.copy())
    for item in dictionary.copy():
        if item.isalpha()==False: # checking whether string contain alphabet value or not
#            print("hi")
            del dictionary[item]
        elif len(item)==1:
#            print("hello")
            del dictionary[item]
    dictionary=dictionary.most_common(3000) # putting 3000 most common words
    print(dictionary)
    return dictionary

# The below python code will generate a feature vector matrix whose rows 
# denote 702 files of training set and columns denote 3000 words of dictionary. 

def extract_features(mail_dir):
    files=[os.path.join(mail_dir,txtfilename) for txtfilename in os.listdir(mail_dir)]
    feature_matrix=np.zeros((len(files),3000)) # vectore matrix of size len(files)*3000
    doc_id=0;
    for file in files:
        with open(file) as f:
            for i,line in enumerate(f):
                if i==2:
                    words=line.split()
                    for word in words:
                        word_id=0
                        for i,d in enumerate(dictionary):
                            if d[0]==word:
                                word_id=i
                                feature_matrix[doc_id,word_id]=words.count(word) # occurences of word in words array
        doc_id+=1
    
    return feature_matrix


train_dir="SpamMailDataset/train-mails"

#creating a dictionary of word with its frequency
dictionary=make_Dictionary(train_dir)

#preparing feature vector per training mail and its labels
train_feature_matrix=extract_features(train_dir)
print(train_feature_matrix)


# Training using SVM and Naive classifier
train_labels=np.zeros(702)
train_labels[351:702]=1 # Since we know that last 350 files are spam files so we put 1 there else put 0. 

model1=MultinomialNB()
model2=LinearSVC()
model1.fit(train_feature_matrix,train_labels)
model2.fit(train_feature_matrix,train_labels)


# Test the unseen mails for spam
test_dir="SpamMailDataset/test-mails"
test_feature_matrix=extract_features(test_dir)
test_labels=np.zeros(260)
test_labels[130:260]=1 # Since we know that last 130 files are spam files so we put 1 there else put 0
result1=model1.predict(test_feature_matrix)
result2=model2.predict(test_feature_matrix)
#plt.plot(test_feature_matrix,test_labels)
print(confusion_matrix(test_labels,result1))
print(confusion_matrix(test_labels,result2))
