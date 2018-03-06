#importing necessary files
import numpy as np
import pandas as pd

#declaring the necessary variables
obs = ['start','learning','changes','throughly','stop']
states = ['start','noun', 'verb','adverb','stop']
trans_p = {'start':{'start':1,'verb':0.3,'noun':0.2,'adverb':0,'stop':0},
           'noun':{'start':0,'noun':0.1,'verb':0.3,'adverb':0.1,'stop':0},
           'verb':{'start':0,'noun':0.4,'verb':0.1,'adverb':0.4,'stop':0},
           'adverb':{'start':0,'noun':0,'verb':0,'adverb':0,'stop':0.1},
           'stop':{'start':0,'noun':0,'verb':0,'adverb':0,'stop':1}}
emit_p = {'start':{'start':0,'learning':0,'changes':0,'throughly':0,'stop':0},
          'noun':{'start':0,'learning':0.001,'changes':0.003,'throughly':0,'stop':0},
          'verb':{'start':0,'learning':0.003,'changes':0.004,'throughly':0,'stop':0},
          'adverb':{'start':0,'learning':0,'changes':0,'throughly':0.002,'stop':0},
          'stop':{'start':0,'learning':0,'changes':0,'throughly':0,'stop':1}}


matrix = np.zeros((5,5),dtype=float)
l=0
t=0
tag={}
backtrack=np.empty((5,5), dtype=object)
np.set_printoptions(precision=15,suppress=True)

#code for calculating the Vertbi Matrix
for index_c,col in enumerate(obs):
    if index_c==0:
        for index_r,row in enumerate(states):
            matrix[index_r][index_c]= trans_p[row][col]
    else:
        for index_r,row in enumerate(states):
            t=0
            temp_index=0
            if index_r==0:
                matrix[index_r][index_c]=0    
            else:
                #print(matrix)
                for index_r1,row1 in enumerate(states):
                    l=emit_p[row][col]*trans_p[row1][row]*matrix[index_r1][index_c-1]
                    if l>t:
                        t=l
                        temp_index=row1
                backtrack[index_r][index_c]=temp_index
                matrix[index_r][index_c]=t
               
print("Viterbi Matrix")
print(matrix)

df = pd.DataFrame(data=matrix,columns=obs,index=states)
pd.set_option('precision',15)
print("Dataframe-Viterbi Matrix")
print(df)

print("BackTrack Matrix")
print(backtrack)
df1 = pd.DataFrame(data=backtrack,columns=obs)
print("Dataframe-BackTrack Matrix")
print(df1)