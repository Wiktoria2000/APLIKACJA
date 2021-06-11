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


#VINCENT (ODLEGLOSC MIEDZY LOTNISKAMI)
a = 6378137
e2 = 0.0066943800

b=a*(1-e2)**0.5;
f=1-(b/a);
L=lB-lA;
U1 = atan((1-f)*tan(fA));
U2 = atan((1-f)*tan(fB));

i=0;
La=L;
while 1:
    i=i+1;
    sd=sqrt(((cos(U2))*(sin(La)))**2+((cos(U1))*(sin(U2))-(sin(U1))*(cos(U2))*(cos(La)))**2);
    cd=(sin(U1))*(sin(U2))+(cos(U1))*(cos(U2))*(cos(La));
    d=atan(sd/cd);
    sa=(cos(U1))*(cos(U2))*(sin(La))/sd;
    c2dm=cd-2*(sin(U1))*(sin(U2))/(1-sa**2);
    
    C=(f/16)*(1-sa**2)*(4+f*(4-3*(1-sa**2)));
    Ls=La;
    La=L+(1-C)*f*sa*(d+C*sd*(c2dm+C*cd*(-1+2*c2dm**2)));
    
    if abs(La-Ls)<(0.000001/206265):
        break
    


u2=(((a**2)-(b**2))/(b**2))*(1-(sa)**2);
A=1+((u2)/16384)*(4096+(u2)*(-768+(u2)*(320-175*(u2))));
B=((u2)/1024)*(256+(u2)*(-128+(u2)*(74-47*(u2))));
dd=B*(sd)*((c2dm)+(0.25)*B*((cd)*(-1+2*(c2dm)**2)-(1/6)*B*(c2dm)*(-3+4*(sd)**2)*(-3+4*(c2dm)**2)));

s=b*A*(d-dd);
AAB=atan(((cos(U2))*(sin(Ls)))/((cos(U1))*(sin(U2))-(sin(U1))*(cos(U2))*(cos(Ls))));
ABA=atan(((cos(U1))*(sin(Ls)))/(((-sin(U1)))*(cos(U2))+(cos(U1))*(sin(U2))*(cos(Ls))))+pi;


if AAB<0:
    AAB=AAB+pi;
    ABA=ABA+pi;
print('\n DLUGOSC LOTU MIĘDZY LOTNISKAMI:',round(s,3),'m')
s = round(s,3)/1000
c = 4.52
p = 320000
spalanie = (1800*s)/100
cena = c*spalanie
print(round(cena,2),'zł')
cena_na_osobe = cena/544
print(round(cena_na_osobe,2),'zł')

#waga bagazu

k = input('Podaj klasę lotu:\n -klasa ekonomiczna\n -pierwsza klasa\n -biznes klasa\n  ')

w_podreczna = int(input('Podaj wagę twojego bagażu podręcznego: '))
w_dodatkowa = int(input('Podaj wagę twojego bagażu dodatkowego: '))

if k == 'biznes klasa':
    podstawa = 300
    if w_dodatkowa > 32:
        print('Twój bagaż dodatkowy przekracza dopuszcalną wagę (max 32kg)! Zmniejsz wagę bagażu. ')
    if w_dodatkowa <= 32:
        print('Waga bagażu dodatkowego dopuszczalna!')
    if w_podreczna <= 8:
        cena_biletu = cena_na_osobe + podstawa
    if w_podreczna > 8:
        cena_biletu = cena_na_osobe + 360 + podstawa
        print('Twój bagaż podręczny przekracza 8kg! Cena biletu wzrosła do',round(cena_biletu,2),'zł')
        
if k == 'klasa ekonomiczna':
    podstawa = 100
    if w_dodatkowa > 23:
        print('Twój bagaż dodatkowy przekracza dopuszcalną wagę (max 23kg)! Zmniejsz wagę bagażu. ')
    if w_dodatkowa <= 23:
        print('Waga bagażu dodatkowego dopuszczalna!')
    if w_podreczna <= 8:
        cena_biletu = cena_na_osobe + podstawa
    if w_podreczna > 8:
        cena_biletu = cena_na_osobe + 360 + podstawa
        print('Twój bagaż podręczny przekracza 8kg! Cena biletu wzrosła do',round(cena_biletu,2),'zł')
        
if k == 'pierwsza klasa':
    podstawa = 200
    if w_dodatkowa > 32:
        print('Twój bagaż dodatkowy przekracza dopuszcalną wagę (max 32kg)! Zmniejsz wagę bagażu. ')
    if w_dodatkowa <= 32:
        print('Waga bagażu dodatkowego dopuszczalna!')
    if w_podreczna <= 8:
        cena_biletu = cena_na_osobe + podstawa
    if w_podreczna > 8:
        cena_biletu = cena_na_osobe + 360 + podstawa
        print('Twój bagaż podręczny przekracza 8kg! Cena biletu wzrosła do',round(cena_biletu,2),'zł')
        
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap        

mapa = input('Wybierz rodzaj mapy: \n MAPA SATELITARNA wpisz MS \n MAPA POLITYCZNA wpisz MP \n')

if mapa == 'MP':

    lb = np.rad2deg(lB)
    la = np.rad2deg(lA)
    fa = np.rad2deg(fA)
    fb = np.rad2deg(fB)

    plt.figure(figsize = (20,20))
    h = 1000.
    m = Basemap(projection='nsper',lon_0=(la+lb)/2,lat_0=(fa+fb)/2,
        satellite_height=h*1000.,resolution='l')
    #m = Basemap(projection='merc',llcrnrlon=-15,llcrnrlat=35,urcrnrlon=69,
    #urcrnrlat=72, lat_ts=0, resolution='l')
    m.drawmapboundary(fill_color='#B5DAFE') #oceany
    m.fillcontinents(color='#77C4A8',lake_color='#B5DAFE')
    m.drawcountries(color='black',linewidth=1)
    m.drawstates(linewidth = 0.2)
    m.drawcoastlines()
    #m.bluemarble() wygląd podobny do satelity ale bez granic państw
    Points = {a:(fa,la),b:(fb,lb)}
    Lon = [Points[key][0] for key in Points]
    Lat = [Points[key][1] for key in Points]
    X, Y = m(Lat,Lon)
    m.scatter(X,Y,zorder=5,s=200,color="red",marker="^")
    x, y = m.gcpoints(Lat[0],Lon[0],Lat[1],Lon[1],500)
    plt.plot(x,y,color="#E59D59",linewidth=5)
    plt.show()
if mapa == 'MS': 
    lb = np.rad2deg(lB)
    la = np.rad2deg(lA)
    fa = np.rad2deg(fA)
    fb = np.rad2deg(fB)       
    plt.figure(figsize = (20,20))
    h = 1000.
    m = Basemap(projection='nsper',lon_0=(la+lb)/2,lat_0=(fa+fb)/2,
        satellite_height=h*1000.,resolution='l')
#m = Basemap(projection='merc',llcrnrlon=-15,llcrnrlat=35,urcrnrlon=69,
            #urcrnrlat=72, lat_ts=0, resolution='l')
#m.drawmapboundary(fill_color='#B5DAFE') #oceany
#m.fillcontinents(color='#77C4A8',lake_color='#B5DAFE')
#m.drawcountries(color='black',linewidth=1)
#m.drawstates(linewidth = 0.2)
#m.drawcoastlines()
    m.bluemarble() #wygląd podobny do satelity ale bez granic państw
    Points = {a:(fa,la),b:(fb,lb)}
    Lon = [Points[key][0] for key in Points]
    Lat = [Points[key][1] for key in Points]
    X, Y = m(Lat,Lon)
    m.scatter(X,Y,zorder=5,s=200,color="red",marker="^")
    x, y = m.gcpoints(Lat[0],Lon[0],Lat[1],Lon[1],500)
    plt.plot(x,y,color="#E59D59",linewidth=5)
    plt.show()   
