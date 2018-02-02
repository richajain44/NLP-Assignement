#importing necessary libraries
import pandas as pd
import glob
from nltk.tokenize import word_tokenize
import itertools
import nltk
import re
from nltk.util import ngrams
from collections import Counter
from os import listdir
from os.path import isfile, join
from nltk.corpus import stopwords

#reading files from both positive and negative folder
filelist_pos=[]
filelist_neg=[]
stop_words= set(stopwords.words('english'))
print("Part 1 of the assignment to display the Word Count, Unique Word Count, Top 10 Bigrams and Trigrams\n")
pos_path = input("Enter the path for Positive folder: ")
pos_onlyfiles = [f for f in listdir(pos_path) if isfile(join(pos_path, f))]
neg_path = input("Enter the path for Negative folder: ")
neg_onlyfiles = [f for f in listdir(neg_path) if isfile(join(neg_path, f))]

pos=[]
neg=[]
#Reading each line, replacing tag with empty string, converting text to lowercase and removing punctuation
for i in pos_onlyfiles:
    filereader = open(pos_path+ "/"+ i,"rt")
    line = filereader.read()
    line = line.replace("<br />", " ")
    line  =re.sub("[^a-zA-Z]"," ",line)
    line = line.lower()
    pos.append(line)
for i in neg_onlyfiles:
    filereader =open(neg_path+"/"+i,"rt")
    line = filereader.read()
    line = line.replace("<br />", " ")
    line  =re.sub("[^a-zA-Z]"," ",line)
    line = line.lower()
    neg.append(line)
#Combining both the list
combined_list = pos + neg
#Creating word tokens for the entire dataset
word_token=[]
wt_without_stop=[]
for i in combined_list:
    word_token.extend(word_tokenize(i))
print("Number of word token including stopwords : " + str(len(word_token)))
for i in word_token:
	if i not in stop_words:
		wt_without_stop.append(i)
print("Number of word token excluding stopwords: " + str(len(wt_without_stop)))
#Vocabulary size, number of unique word in the dataset
print("Number of unique words including in data: " + str(len(list(set(word_token)))))
print("Number of unique words excluding in data: " +str(len(list(set(wt_without_stop)))))

#Bigrams
print("\n") 
print("Top 10 Bigrams including stopwords:")
bigrams = ngrams(word_token,2)
print(Counter(bigrams).most_common(10))

#Bigrams
print("\n") 
print("Top 10 Bigrams excluding stopwords:")
bigrams_without = ngrams(wt_without_stop,2)
print(Counter(bigrams_without).most_common(10))

#Trigrams 
print("\n")
print("Top 10 Trigrams including stopwords:")
trigrams= ngrams(word_token,3)
print(Counter(trigrams).most_common(10))

#Trigrams 
print("\n")
print("Top 10 Trigrams excluding stopwords:")
trigrams_without= ngrams(wt_without_stop,3)
print(Counter(trigrams_without).most_common(10))

print("\n")
print("Part 2 of the program to display the probability of the third word given two words\n")
print("The function excludes stopwords while calculating probability\n")
w1 = input("Enter the first word: ")
w2= input("Enter the second word: ")
w3=input("Enter the third word: ")

#Function for a given sequence of words, computes the probability of the third word
word_token_trigram = ngrams(wt_without_stop,3)
word_token_tri = dict(Counter(word_token_trigram))
word_token_bigram = ngrams(wt_without_stop,2)
word_token_bi = dict(Counter(word_token_bigram))
def sequence(w1,w2,w3):
    t =(w1,w2)
    t1 = (w1,w2,w3)
    if t1 in word_token_tri:
        x =word_token_tri[t1]
    else:
        x =1
        
    if t1 in word_token_tri:
    	y = word_token_bi[t]
    else:
        value = word_token_bi.get(t,0)
        y = len(word_token_bi) + value
    print(x)
    print(y)
    p =x / y        
     
    return p
prob = sequence(w1,w2,w3)
print("The probability of third word given two words is: " + str(round(prob,6)))