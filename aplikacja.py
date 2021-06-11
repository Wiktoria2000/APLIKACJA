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