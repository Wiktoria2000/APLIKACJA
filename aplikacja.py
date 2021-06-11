# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 20:45:07 2021

@author: Wiktoria
"""

from math import atan, tan, cos, sin, sqrt, pi
import pandas as pd
import numpy as np 

dane = pd.read_excel('DANEE.xlsx')
#dane = pd.read_excel('C:\Users\DELL\Desktop\infa')


dane.index = dane['MIASTO'] #zamiana ineskow 1,2,3 na nazwy miast 
a = input('Miejsce wylotu linii Lufthansa: ')
#b = str(input('Miejsce lądowania  '))

#przyporządkowanie do konkretnej komórki 
h_fi = dane.loc[a,'H_(FI)']
m_fi = dane.loc[a,'M_(FI)']
s_fi = dane.loc[a,'S_(FI)']
h_l = dane.loc[a,'H_(L)']
m_l = dane.loc[a,'M_(L)']
s_l = dane.loc[a,'S_(L)']
H_m = dane.loc[a,' H']
lA = np.deg2rad(h_l + m_l/60 + s_l/3600)
fA = np.deg2rad(h_fi + m_fi/60 + s_fi/3600)
a = 6378137
e2 = 0.0066943800
#kartezjańskie dla miejsca odlotu
N=a/sqrt((1-e2*(sin(fA))**2));


x = (N+H_m)*cos(fA)*cos(lA);

y = (N+H_m)*cos(fA)*sin(lA);

z = (N*(1-e2)+H_m)*sin(fA);
print("współrzędne kartezjanskie dla miejsca wylotu:")
print("x:", round(x,3))
print("y:", round(y,3))
print("z:", round(z,3))

b = str(input('Miejsce lądowania  '))
h_fi2 = dane.loc[b,'H_(FI)']
m_fi2 = dane.loc[b,'M_(FI)']
s_fi2 = dane.loc[b,'S_(FI)']
h_l2 = dane.loc[b,'H_(L)']
m_l2 = dane.loc[b,'M_(L)']
s_l2 = dane.loc[b,'S_(L)']
H_m2 = dane.loc[b,' H']

lB = np.deg2rad(h_l2 + m_l2/60 + s_l2/3600)
#lA = np.deg2rad(h_l + m_l/60 + s_l/3600)
#fA = np.deg2rad(h_fi + m_fi/60 + s_fi/3600)
fB = np.deg2rad(h_fi2 + m_fi2/60 + s_fi2/3600)

#kartezjańskie dla miejsca przylotu 

N2=a/sqrt((1-e2*(sin(fB))**2));


x2 = (N2+H_m2)*cos(fB)*cos(lB);

y2 = (N2+H_m2)*cos(fB)*sin(lB);

z2 = (N2*(1-e2)+H_m2)*sin(fB);
print("współrzędne kartezjanskie dla miejsca lądowania:")
print("x:", round(x2,3))
print("y:", round(y2,3))
print("z:", round(z2,3))
