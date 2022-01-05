#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.utils.extmath import softmax
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestCentroid
from sklearn.metrics import f1_score, make_scorer
import sklearn
from sklearn import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


columns = ['ID', 'Age', 'Gender', 'Education', 'Country', 'Ethnicity', 'Neuroticism', 'Extraversion', 'Openness', 'Agreeableness', 'Conscientiousness', 'Impulsiveness', 'Sensation_seeking', 'Alcohol', 'Amphetamine', 'Amyl_nitrite', 'Benzodiazepine', 'Caffeine', 'Cannabis', 'Chocolate', 'Cocaine', 'Crack', 'Ecstasy', 'Heroin', 'Ketamine', 'Legal_highs', 'LSD', 'Methadone', 'Mushrooms', 'Nicotine', 'Semeron', 'VSA']

df = pd.read_csv("drug_consumption.data",names=columns)

data_brut = df.copy()

def split_in_parts(c, intervs, vals):
    for j in range(len(vals)):
        if intervs[j] <= c <= intervs[j+1]:
            return j
    print(intervs)

n_split = 10

for col in data_brut.iloc[:,6:13]:
    column = data_brut[col]
    intervs = np.linspace(min(column), max(column), n_split+1)
    vals = list(range(1, n_split+1))
    data_brut[col] = column.map(lambda x: split_in_parts(x, intervs, vals))

data_brut.set_index('ID', inplace = True)

def frequence(a):
    return 1 if ((a == 'CL6') or (a == 'CL5') or (a == 'CL4')) else 0

for col in data_brut.iloc[:,-19:]:
    data_brut[col] = data_brut[col].map(frequence)

data_brut['heroinPl'] = data_brut.apply(lambda x: int((x['Cocaine'] + x['Crack'] + x['Heroin'] + x['Methadone'])>0), axis = 1)

data_brut['ecstasyPl'] = data_brut.apply(lambda x: int((x['Amphetamine']  + x['Cannabis'] + x['Cocaine']  + x['Ecstasy'] + x['Ketamine'] + x['LSD'] + x['Methadone'] + x['Mushrooms'] )>0), axis = 1)

data_brut['benzoPl'] = data_brut.apply(lambda x: int((x['Amphetamine'] + x['Cocaine'] + x['Methadone'])>0), axis = 1)

data_brut.drop(['Caffeine','Chocolate','Nicotine','Legal_highs','Alcohol','Amphetamine','Amyl_nitrite','Benzodiazepine', 'Cannabis', 'Cocaine', 'Crack', 'Ecstasy', 'Heroin', 'Ketamine', 'LSD', 'Methadone', 'Mushrooms', 'Semeron', 'VSA'], axis = 1, inplace = True)

def toFixed(x):
    x = float('{:.5f}'.format(x))
    return x

for i in data_brut.iloc[:,:-3]:
    data_brut[i] = data_brut[i].map(toFixed)

def changeAge(x):
    if (x == -0.95197):
        x = 0
    elif (x == -0.07854):
        x = 1
    elif (x == 0.49788):
        x = 2
    elif (x == 1.09449):
        x = 3
    elif (x == 1.82213):
        x = 4
    elif (x == 2.59171):
        x = 5
    return x

data_brut['Age'] = data_brut['Age'].map(changeAge)
def changeGender(x):
    if (x == 0.48246 ):
        x = 0
    elif (x == -0.48246 ):
        x = 1
    return x

data_brut['Gender'] = data_brut['Gender'].map(changeGender)

def changeEducation(x):
    if (x == -2.43591):
        x = 0
    elif (x == -1.73790):
        x = 1
    elif (x == -1.43719):
        x = 2
    elif (x == -1.22751):
        x = 3
    elif (x == -0.61113):
        x = 4
    elif (x == -0.05921):
        x = 5
    elif (x == 0.45468):
        x = 6
    elif (x == 1.16365):
        x = 7
    elif (x == 1.98437):
        x = 8
    return x

data_brut['Education'] = data_brut['Education'].map(changeEducation)

def changeCountry(x):
    if (x == -0.09765):
        x = 0
    elif (x == 0.24923):
        x = 1
    elif (x == -0.46841):
        x = 2
    elif (x == -0.28519):
        x = 3
    elif (x == 0.21128):
        x = 4
    elif (x == 0.96082):
        x = 5
    elif (x == -0.57009):
        x = 6
    return x

data_brut['Country'] = data_brut['Country'].map(changeCountry)

def changeEthnicity(x):
    if (x == -0.50212):
        x = 0
    elif (x == -1.10702):
        x = 1
    elif (x == 1.90725):
        x = 2
    elif (x == 0.12600):
        x = 3
    elif (x == -0.22166):
        x = 4
    elif (x == 0.11440):
        x = 5
    elif (x == -0.31685):
        x = 6
    return x

data_brut['Ethnicity'] = data_brut['Ethnicity'].map(changeEthnicity)

data_heroin = data_brut.drop(['ecstasyPl', 'benzoPl'], axis=1)
data_ecstasy= data_brut.drop(['heroinPl', 'benzoPl'], axis=1)
data_benzo= data_brut.drop(['heroinPl', 'ecstasyPl'], axis=1)

y1 = data_heroin['heroinPl']

X1 = data_heroin.drop(['heroinPl','Country','Ethnicity','Extraversion'], axis=1)

X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size = 0.2, random_state = 42, stratify=y1)

scaler = StandardScaler()
scaler.fit(X1_train)                 # Il ne faut fiter que sur les data d'entrainement
X1_train = scaler.transform(X1_train)
X1_test  = scaler.transform(X1_test)  # apply same transformation to test data

y2 = data_ecstasy['ecstasyPl']
X2 = data_ecstasy.drop(['ecstasyPl','Country','Ethnicity','Extraversion'], axis=1)

X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size = 0.2, random_state = 42, stratify=y2)

scaler = StandardScaler()
scaler.fit(X2_train)                 # Il ne faut fiter que sur les data d'entrainement
X2_train = scaler.transform(X2_train)
X2_test  = scaler.transform(X2_test)

y3 = data_benzo['benzoPl']
X3 = data_benzo.drop(['benzoPl','Country','Ethnicity','Extraversion'], axis=1)


X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size = 0.2, random_state = 42, stratify=y3)

scaler = StandardScaler()
scaler.fit(X3_train)                 # Il ne faut fiter que sur les data d'entrainement
X3_train = scaler.transform(X3_train)
X3_test  = scaler.transform(X3_test)

ft1_nc=NearestCentroid().fit(X1_train, y1_train)
y1_nc_pred=ft1_nc.predict(X1_test)

ft2h_rl=LogisticRegression(C=0.1, class_weight='balanced', solver='liblinear')

ft2h_rl.fit(X2_train, y2_train)

ft3_nc=NearestCentroid(shrink_threshold=0.0).fit(X3_train, y3_train)
y3_nc_pred=ft3_nc.predict(X3_test)

def predict_proba(self, X):
    distances = pairwise_distances(X, self.centroids_, metric=self.metric)
    probs = softmax(distances)  
    return probs

def prediction(values):
    Age,Gender,Education,Neuroticism,Openness,Agreeableness,Conscientiousness,Impulsiveness,Sensation_seeking = values['Age'],values['Gender'],values['Education'],values['Neuroticism'],values['Openness'],values['Agreeableness'],values['Conscientiousness'],values['Impulsiveness'],values['Sensation_seeking']
    a = round(predict_proba(ft1_nc,[[Age,Gender,Education,Neuroticism,Openness,Agreeableness,Conscientiousness,Impulsiveness,Sensation_seeking]])[0][0]*100)
    b = round(ft2h_rl.predict_proba([[Age,Gender,Education,Neuroticism,Openness,Agreeableness,Conscientiousness,Impulsiveness,Sensation_seeking]])[0][1]*100)
    c = round(predict_proba(ft3_nc,[[Age,Gender,Education,Neuroticism,Openness,Agreeableness,Conscientiousness,Impulsiveness,Sensation_seeking]])[0][0]*100)
    return [a, b, c]
