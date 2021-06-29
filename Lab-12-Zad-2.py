import math

def pole_kuli(r):
   p = 4 * math.pi * r * r
   return p

def objetosc_kuli(r):
   o = (4 * math.pi * r * r * r)/3
   return o

def pole_stozka(r):
   p = math.pi * r * r
   return p

def objetosc_stozka(r, l):
   o = math.pi * r * l
   return o

def pole_szescianu(a):
   p = 6 * a * a
   return p

def objetosc_szescianu(a):
   o = a * a * a
   return o